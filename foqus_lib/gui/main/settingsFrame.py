'''
    settingsFrame.py

    John Eslick, Carnegie Mellon University, 2014

    This Material was produced under the DOE Carbon Capture Simulation
    Initiative (CCSI), and copyright is held by the software owners:
    ORISE, LANS, LLNS, LBL, PNNL, CMU, WVU, et al. The software owners
    and/or the U.S. Government retain ownership of all rights in the
    CCSI software and the copyright and patents subsisting therein. Any
    distribution or dissemination is governed under the terms and
    conditions of the CCSI Test and Evaluation License, CCSI Master
    Non-Disclosure Agreement, and the CCSI Intellectual Property
    Management Plan. No rights are granted except as expressly recited
    in one of the aforementioned agreements.
'''
from foqus_lib.gui.main.turbineConfig import *
from foqus_lib.framework.uq.LocalExecutionModule import *
from settingsFrame_UI import *
from PySide import QtGui, QtCore
import logging
import time
import re
import StringIO
import shutil
import pickle #not sure why this is here probably remove
from pprint import pprint
import subprocess
import xml.etree.ElementTree as ET
if os.name == 'nt':
    import win32process

class settingsFrame(QtGui.QFrame, Ui_settingsFrame):
    '''
        This class is a dialog box that allows you to view and change
        general FOQUS settings.  It's called log settings because it
        started out with only log settings.
    '''
    waiting = QtCore.Signal() # indicates a task is going take a while
    notwaiting = QtCore.Signal() # indicates a wait is over
    def __init__(self, dat, parent=None):
        '''
            Initialize FOQUS settings dialog
        '''
        QtGui.QFrame.__init__(self, parent)
        self.setupUi(self) # Create the widgets
        self.dat = dat
        # translate the slider value into a logging level
        self.lglev = [0]*6
        self.lglev[5] = logging.CRITICAL
        self.lglev[4] = logging.ERROR
        self.lglev[3] = logging.WARNING
        self.lglev[2] = logging.INFO
        self.lglev[1] = logging.DEBUG
        #connect turbine config edit button
        self.turbConfigEditButton.clicked.connect(
            self.editTurbineConfigFile)
        self.turbCConfigEditButton.clicked.connect(
            self.editTurbineCConfigFile)
        #connect browse buttons
        self.wdirBrowseButton.clicked.connect(self.browseWorkingDir)
        self.turbBrowseButton.clicked.connect(self.browseTurbineFile)
        self.turbCBrowseButton.clicked.connect(
            self.browseTurbineCFile)
        self.turbLiteBrowseButton.clicked.connect(self.browseTurbLite)
        self.psuadeBrowseButton.clicked.connect(self.browsePsuadeFile)
        self.simSinterBrowsButton.clicked.connect(self.browseSinterFile)
        self.javaHomeButton.clicked.connect(self.browseJavaDir)
        self.alamoPathButton.clicked.connect(self.browseALAMOPath)
        self.rScriptPathButton.clicked.connect(self.browseRScriptPath)
        #Connect okay/cancel singnals
        self.revertButton.clicked.connect(self.revert)
        #
        self.startLite.clicked.connect(self.startTurbineService)
        self.stopLite.clicked.connect(self.stopTurbineService)
        self.TestTurb.clicked.connect(self.turbineTest)
        self.testLite.clicked.connect(self.turbineLiteTest)
        self.changePort.clicked.connect(self.updateTurbineLitePort)

    def updateTurbineLitePort(self):
        """
        Enter a new port number for TurbineLite
        """
        # Set xml file location
        tcfg =  os.path.join(
            self.turbLiteHomeEdit.text(),
            "Services\webAPI\SelfManagedWebApplicationWindowsService.exe.config")
        #Get XML string
        try:
            with open(tcfg, 'rb') as f:
                xmls = f.read()
        except:
            logging.getLogger("foqus." + __name__).exception(
                "Failed to open TubbineLite config file")
            QtGui.QMessageBox.warning(self, "Error",
                "Could not read TurbineLite configuration file "
                "(see log).")
            return
        #Find problematic namespace tag and remove it
        pat = re.compile('<unity.*?(xmlns="(.*?)")')
        g = pat.search(xmls)
        if g is not None:
            xmlns = g.group(2)
            xmls = xmls[:g.start(1)]+xmls[g.end(1):]
        #Parse and get userSettings element
        try:
            root = ET.fromstring(xmls)
        except:
            logging.getLogger("foqus." + __name__).exception(
                "Could not parse XML")
            QtGui.QMessageBox.warning(self, "Error",
                "Could not parse XML (see log).")
        tree = ET.ElementTree()
        tree._setroot(root)
        uSetEl = root.find("userSettings")
        settingsEl = uSetEl.find(
            "SelfManagedWebApplicationWindowsService.Properties.Settings")
        netLoc=settingsEl.find("setting[@name='netloc']").find('value')
        netURL = netLoc.text.split(":")[0]
        netPort = netLoc.text.split(":")[1]
        #
        #Ask for new port
        text, result = QtGui.QInputDialog.getText(
            self,
            "TurbineLite Port",
            "Enter the new TurbineLite Port (Current {0}).".format(netPort))
        if not result:
            return
        #Back up the config file
        newcfg = "{0}_{1}".format(tcfg, int(time.time()))
        shutil.copyfile(tcfg, newcfg)
        # Make new url:port setting string
        port = int(float(text))
        newLoc = "{0}:{1}".format(netURL, port)
        #write modified config
        netLoc.text = newLoc
        tcfgs = StringIO.StringIO()
        tree.write(tcfgs, encoding="utf-8", xml_declaration=True)
        tcfgs = tcfgs.getvalue().replace(
            "<unity>", '<unity xmlns="{0}">'.format(xmlns))
        with open(tcfg, 'wb') as f:
            f.write(tcfgs)
        QtGui.QMessageBox.information(
            self,
            "TurbineLite Config Change!",
            " The TurbineLite web interface configuration"
            " has been backed up as: {0}"
            " and the port has been changed to {1}."
            " You must now restart the TurbineLite service,"
            " and edit the local TrubineLite configuration.".format(
                newcfg, port),
            QtGui.QMessageBox.Ok)


    def turbineTest(self):
        QtGui.QMessageBox.information(
            self,
            "Test",
            ("The Turbine configuration format and Turbine connection"
             " will be tested.  This may take some time." ))
        self.dat.flowsheet.turbConfig.path = self.turbConfClusterEdit.text()
        self.dat.flowsheet.turbConfig.readConfig()
        errList = self.dat.flowsheet.turbConfig.testConfig(writeConfig=False)
        if len(errList) == 0:
            QtGui.QMessageBox.information(
                self,
                "Success",
                "The Turbine configuration is okay.")
        else:
            QtGui.QMessageBox.information(
                self,
                "Error",
                str(errList))

    def turbineLiteTest(self):
        QtGui.QMessageBox.information(
            self,
            "Test",
            ("The Turbine configuration format and Turbine connection"
             " will be tested.  This may take some time." ))
        self.dat.flowsheet.turbConfig.path = self.turbConfEdit.text()
        self.dat.flowsheet.turbConfig.readConfig()
        errList = self.dat.flowsheet.turbConfig.testConfig(writeConfig=False)
        if len(errList) == 0:
            QtGui.QMessageBox.information(
                self,
                "Success",
                "The Turbine configuration is okay.")
        else:
            QtGui.QMessageBox.information(
                self,
                "Error",
                str(errList))

    def startTurbineService(self):
        proc = subprocess.Popen(
            ['net', 'start', 'Turbine Web API Service'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=None,
            creationflags=win32process.CREATE_NO_WINDOW)
        self.waiting.emit()
        out, err = proc.communicate()
        self.notwaiting.emit()
        rc = proc.returncode
        if rc != 0:
            mess = "Failed to start Turbine Web Service API.  If the "\
                   "reason given below is not clear the likely cause is that "\
                   "FOQUS does not have permision to start/stop the services."
            details = "Details:\n{0}\n{1}".format(out, err)
            QtGui.QMessageBox.information(self, "Information",
                    "\n\n".join([mess, details]))
        else:
            QtGui.QMessageBox.information(self, "Information",
                    "Result:\n{0}\n{1}".format(out, err))

    def stopTurbineService(self):
        proc = subprocess.Popen(
            ['net', 'stop', 'Turbine Web API Service'],
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE,
            stdin = None,
            creationflags=win32process.CREATE_NO_WINDOW)
        self.waiting.emit()
        out, err = proc.communicate()
        self.notwaiting.emit()
        rc = proc.returncode
        if rc != 0:
            mess = "Failed to start Turbine Web Service API.  If the "\
            "reason given below is not clear the likely cause is that"\
            "FOQUS does not have permision to start/stop the services."
            details = "Details:\n{0}\n{1}".format(out, err)
            QtGui.QMessageBox.information(self, "Information",
                    "\n\n".join([mess, details]))
        else:
            QtGui.QMessageBox.information(self, "Information",
                "Result:\n{0}\n{1}".format(out, err))

    def updateForm(self):
        # Set FOQUS options
        self.dmfCheck.setChecked(self.dat.foqusSettings.use_dmf)
        self.saveSmallCheck.setChecked(
            self.dat.foqusSettings.compactSession)
        self.saveBackCheck.setChecked(
            self.dat.foqusSettings.backupSession)
        self.settingsInWDirCheck.setChecked(
            self.dat.foqusSettings.settingsInWDir)
        # Set path settings
        self.wdirEdit.setText(self.dat.foqusSettings.new_working_dir)
        self.turbConfEdit.setText(self.dat.foqusSettings.turbConfig)
        self.turbConfClusterEdit.setText(
            self.dat.foqusSettings.turbConfigCluster)
        self.turbLiteHomeEdit.setText(
            self.dat.foqusSettings.turbLiteHome)
        self.psuadeEdit.setText(self.dat.foqusSettings.psuade_path)
        self.sinterConfigEdit.setText(
            self.dat.foqusSettings.simsinter_path)
        self.javaHomeEdit.setText(
            self.dat.foqusSettings.java_home)
        self.alamoPathEdit.setText(self.dat.foqusSettings.alamo_path)
        # Aspen version setting
        self.aspenVersionCombo.setCurrentIndex(
            self.dat.foqusSettings.aspenVersion)
        # Run method setting
        self.runMethodCombo.setCurrentIndex(
            self.dat.foqusSettings.runFlowsheetMethod)
        # set Log settings
        self.logFormatEdit.setText(self.dat.foqusSettings.logFormat)
        self.foqusLogLevelSlide.setValue(
            self.lglev.index(self.dat.foqusSettings.foqusLogLevel))
        self.turbineLogLevelSlide.setValue(
            self.lglev.index(self.dat.foqusSettings.turbLogLevel))
        self.foqusToConsoleCheck.setChecked(
            self.dat.foqusSettings.foqusLogToConsole)
        self.turbineToConsoleCheck.setChecked(
            self.dat.foqusSettings.turbLogToConsole)
        self.foqusToFileCheck.setChecked(
            self.dat.foqusSettings.foqusLogToFile)
        self.turbineToFileCheck.setChecked(
            self.dat.foqusSettings.turbLogToFile)
        self.foqusLogFileEdit.setText(
            self.dat.foqusSettings.foqusLogFile)
        self.turbineLogFileEdit.setText(
            self.dat.foqusSettings.turbineLogFile)
        self.rotateLogCheck.setChecked(
            self.dat.foqusSettings.logRotate)
        self.logSizeEdit.setText(str(self.dat.foqusSettings.maxLogSize))
        self.logSizeEdit.setEnabled(self.dat.foqusSettings.logRotate)
        self.rScriptPath.setText(self.dat.foqusSettings.rScriptPath)
        #
        self.trIntervalEdit.setText(
            str(self.dat.foqusSettings.turbineRemoteCheckFreq))
        self.trReSubEdit.setText(
            str(self.dat.foqusSettings.turbineRemoteReSub))

    def editTurbineConfigFile(self):
        '''
            Show turbine profile config dialog
        '''
        cfile = self.turbConfEdit.text()
        m = turbineConfig(self.dat, cfile, self)
        m.exec_()

    def editTurbineCConfigFile(self):
        '''
            Show turbine profile config dialog
        '''
        cfile = self.turbConfClusterEdit.text()
        m = turbineConfig(self.dat, cfile, self)
        m.exec_()

    def browseWorkingDir(self):
        '''
            Open file browser to select the working directory
        '''
        msg = QtGui.QFileDialog()
        msg.setFileMode(QtGui.QFileDialog.Directory)
        msg.setOption(QtGui.QFileDialog.ShowDirsOnly)
        if msg.exec_():
            dirs = msg.selectedFiles()
            dirs = os.path.normpath(dirs[0])
            self.wdirEdit.setText(dirs)

    def browseRScriptPath(self):
        '''
            Open file browser to select the R exe file
        '''
        fileName, filtr = QtGui.QFileDialog.getOpenFileName(
            self,
            "Find RScript exe",
            "",
            "Executable (*.exe);;All Files (*)")
        if fileName:
            fileName = os.path.normpath(fileName)
            self.rScriptPath.setText(fileName)

    def browseTurbLite(self):
        msg = QtGui.QFileDialog()
        msg.setFileMode(QtGui.QFileDialog.Directory)
        msg.setOption(QtGui.QFileDialog.ShowDirsOnly)
        if msg.exec_():
            dirs = msg.selectedFiles()
            dirs = os.path.normpath(dirs[0])
            self.turbLiteHomeEdit.setText(dirs)

    def browseJavaDir(self):
        msg = QtGui.QFileDialog()
        msg.setFileMode(QtGui.QFileDialog.Directory)
        msg.setOption(QtGui.QFileDialog.ShowDirsOnly)
        if msg.exec_():
            dirs = msg.selectedFiles()
#            dirs = '"' + os.path.normpath(dirs[0]) + '"'
            dirs = os.path.normpath(dirs[0])
            self.javaHomeEdit.setText(dirs)

    def browseALAMOPath(self):
        '''
            Open file browser to select the ALAMO exe file
        '''
        fileName, filtr = QtGui.QFileDialog.getOpenFileName(
            self,
            "Find ALMO exe",
            "",
            "Executable (*.exe);;All Files (*)")
        if fileName:
            fileName = os.path.normpath(fileName)
            self.alamoPathEdit.setText(fileName)

    def browseTurbineFile(self):
        '''
            Open file browser to select the turbine config file
        '''
        fileName, filtr = QtGui.QFileDialog.getOpenFileName(
            self,
            "Find Turbine Confguration",
            "",
            "Config Files (*.cfg);;Text Files (*.txt);;All Files (*)")
        if fileName:
            fileName = os.path.normpath(fileName)
            self.turbConfEdit.setText(fileName)

    def browseTurbineCFile(self):
        '''
            Open file browser to select the turbine config file
        '''
        fileName, filtr = QtGui.QFileDialog.getOpenFileName(
            self,
            "Find Turbine Cluster Confguration",
            "",
            "Config Files (*.cfg);;Text Files (*.txt);;All Files (*)")
        if fileName:
            fileName = os.path.normpath(fileName)
            self.turbConfClusterEdit.setText(fileName)

    def browsePsuadeFile(self):
        '''
            Open file browser to select the psuade exe file
        '''
##        fileName, filtr = QtGui.QFileDialog.getOpenFileName(
##            self,
##            "Open File",
##            "",
##            "EXE Files (*.exe);;All Files (*)")
        fileName = LocalExecutionModule.setPsuadePath(True)
        if fileName:
            fileName = os.path.normpath(fileName)
            self.psuadeEdit.setText(fileName)

    def browseSinterFile(self):
        '''
            Open file browser to select the psuade exe file
        '''
        fileName, filtr = QtGui.QFileDialog.getOpenFileName(
            self,
            "Open File",
            "",
            "EXE Files (*.exe);;All Files (*)")
        if fileName:
            fileName = os.path.normpath(fileName)
            self.sinterConfigEdit.setText(fileName)

    def applyChanges(self):
        '''
            Apply FOQUS settings from form
        '''
        # Check box options
        self.dat.foqusSettings.use_dmf = self.dmfCheck.isChecked()
        self.dat.foqusSettings.compactSession = \
            self.saveSmallCheck.isChecked()
        self.dat.foqusSettings.backupSession = \
            self.saveBackCheck.isChecked()
        self.dat.foqusSettings.settingsInWDir = \
            self.settingsInWDirCheck.isChecked()
        # Set paths
        self.dat.foqusSettings.new_working_dir = self.wdirEdit.text()
        self.dat.foqusSettings.turbConfig = self.turbConfEdit.text()
        self.dat.foqusSettings.turbConfigCluster = \
            self.turbConfClusterEdit.text()
        self.dat.foqusSettings.turbLiteHome = \
            self.turbLiteHomeEdit.text()
        self.dat.foqusSettings.psuade_path = self.psuadeEdit.text()
        self.dat.foqusSettings.simsinter_path =\
            self.sinterConfigEdit.text()
        self.dat.foqusSettings.java_home = self.javaHomeEdit.text()
        self.dat.foqusSettings.alamo_path = self.alamoPathEdit.text()
        # Aspen version
        self.dat.foqusSettings.aspenVersion =\
            self.aspenVersionCombo.currentIndex()
        # Run method
        self.dat.foqusSettings.runFlowsheetMethod =\
            self.runMethodCombo.currentIndex()
        # Set the log settings
        self.dat.foqusSettings.logFormat = self.logFormatEdit.text()
        self.dat.foqusSettings.foqusLogLevel =\
            self.lglev[self.foqusLogLevelSlide.value()]
        self.dat.foqusSettings.turbLogLevel =\
            self.lglev[self.turbineLogLevelSlide.value()]
        self.dat.foqusSettings.foqusLogToConsole =\
            self.foqusToConsoleCheck.isChecked()
        self.dat.foqusSettings.turbLogToConsole =\
            self.turbineToConsoleCheck.isChecked()
        self.dat.foqusSettings.foqusLogToFile =\
            self.foqusToFileCheck.isChecked()
        self.dat.foqusSettings.turbLogToFile =\
            self.turbineToFileCheck.isChecked()
        self.dat.foqusSettings.foqusLogFile =\
            self.foqusLogFileEdit.text()
        self.dat.foqusSettings.turbineLogFile =\
            self.turbineLogFileEdit.text()
        self.dat.foqusSettings.logRotate = \
            self.rotateLogCheck.isChecked()
        self.dat.foqusSettings.maxLogSize = \
            float(self.logSizeEdit.text())
        self.dat.foqusSettings.rScriptPath = \
        self.rScriptPath.text()
        #
        self.dat.foqusSettings.turbineRemoteCheckFreq =\
            float(self.trIntervalEdit.text())
        self.dat.foqusSettings.turbineRemoteReSub =\
            int(float(self.trReSubEdit.text()))
        #save settings file
        self.dat.saveSettings()
        #Loading the settings also applies whatever can be changed
        #without a FOQUS restart
        self.dat.loadSettings()
        if self.dat.foqusSettings.new_working_dir != self.dat.foqusSettings.working_dir:
            QtGui.QMessageBox.information(
                self,
                "Restart FOQUS",
                "Close and reopen FOQUS to change the working dir.")

    def revert(self):
        '''
            Don't update the FOQUS settings
        '''
        self.updateForm()