# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dmfUploadDialog_UI.ui'
#
# Created: Fri Mar 25 16:11:54 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_dmfUploadDialog(object):
    def setupUi(self, dmfUploadDialog):
        dmfUploadDialog.setObjectName("dmfUploadDialog")
        dmfUploadDialog.resize(495, 631)
        dmfUploadDialog.setModal(True)
        self.verticalLayout_2 = QtGui.QVBoxLayout(dmfUploadDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtGui.QLabel(dmfUploadDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(dmfUploadDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_3 = QtGui.QLabel(dmfUploadDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.sinterConfigGUIButton = QtGui.QPushButton(dmfUploadDialog)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/edit.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sinterConfigGUIButton.setIcon(icon)
        self.sinterConfigGUIButton.setObjectName("sinterConfigGUIButton")
        self.horizontalLayout_3.addWidget(self.sinterConfigGUIButton)
        self.configFileButton = QtGui.QPushButton(dmfUploadDialog)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 104, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.configFileButton.setPalette(palette)
        font = QtGui.QFont()
        font.setUnderline(False)
        self.configFileButton.setFont(font)
        self.configFileButton.setCursor(QtCore.Qt.PointingHandCursor)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/search.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.configFileButton.setIcon(icon1)
        self.configFileButton.setFlat(False)
        self.configFileButton.setObjectName("configFileButton")
        self.horizontalLayout_3.addWidget(self.configFileButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 2, 1, 1)
        self.appEdit = QtGui.QLineEdit(dmfUploadDialog)
        self.appEdit.setEnabled(False)
        self.appEdit.setObjectName("appEdit")
        self.gridLayout.addWidget(self.appEdit, 3, 2, 1, 1)
        self.label_2 = QtGui.QLabel(dmfUploadDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.simNameEdit = QtGui.QComboBox(dmfUploadDialog)
        self.simNameEdit.setEditable(True)
        self.simNameEdit.setObjectName("simNameEdit")
        self.gridLayout.addWidget(self.simNameEdit, 1, 2, 1, 1)
        self.clearTableButton = QtGui.QPushButton(dmfUploadDialog)
        self.clearTableButton.setObjectName("clearTableButton")
        self.gridLayout.addWidget(self.clearTableButton, 1, 3, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.groupBox = QtGui.QGroupBox(dmfUploadDialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.addFileButton = QtGui.QPushButton(self.groupBox)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/add.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addFileButton.setIcon(icon2)
        self.addFileButton.setObjectName("addFileButton")
        self.horizontalLayout_2.addWidget(self.addFileButton)
        self.removeFileButton = QtGui.QPushButton(self.groupBox)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/remove.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.removeFileButton.setIcon(icon3)
        self.removeFileButton.setObjectName("removeFileButton")
        self.horizontalLayout_2.addWidget(self.removeFileButton)
        self.relpathButton = QtGui.QPushButton(self.groupBox)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/subArrow.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.relpathButton.setIcon(icon4)
        self.relpathButton.setObjectName("relpathButton")
        self.horizontalLayout_2.addWidget(self.relpathButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.fileTable = QtGui.QTableWidget(self.groupBox)
        self.fileTable.setObjectName("fileTable")
        self.fileTable.setColumnCount(2)
        self.fileTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.fileTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.fileTable.setHorizontalHeaderItem(1, item)
        self.verticalLayout.addWidget(self.fileTable)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.gridLayout1 = QtGui.QGridLayout()
        self.gridLayout1.setObjectName("gridLayout1")
        self.label1 = QtGui.QLabel(dmfUploadDialog)
        self.label1.setObjectName("label1")
        self.gridLayout1.addWidget(self.label1, 0, 0, 1, 1)
        self.dmfRepo = QtGui.QLineEdit(dmfUploadDialog)
        self.dmfRepo.setEnabled(False)
        self.dmfRepo.setObjectName("dmfRepo")
        self.gridLayout1.addWidget(self.dmfRepo, 0, 1, 1, 1)
        self.selectDMFRepoButton = QtGui.QPushButton(dmfUploadDialog)
        self.selectDMFRepoButton.setObjectName("selectDMFRepoButton")
        self.gridLayout1.addWidget(self.selectDMFRepoButton, 0, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.okButton = QtGui.QPushButton(dmfUploadDialog)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/check.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.okButton.setIcon(icon5)
        self.okButton.setIconSize(QtCore.QSize(16, 16))
        self.okButton.setObjectName("okButton")
        self.horizontalLayout.addWidget(self.okButton)
        self.cancelButton = QtGui.QPushButton(dmfUploadDialog)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/exit.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.cancelButton.setIcon(icon6)
        self.cancelButton.setIconSize(QtCore.QSize(16, 16))
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(dmfUploadDialog)
        QtCore.QMetaObject.connectSlotsByName(dmfUploadDialog)

    def retranslateUi(self, dmfUploadDialog):
        dmfUploadDialog.setWindowTitle(QtGui.QApplication.translate("dmfUploadDialog", "DMF Simulation Upload", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("dmfUploadDialog", "Add/Update DMF", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("dmfUploadDialog", "Simulation Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("dmfUploadDialog", "Application:", None, QtGui.QApplication.UnicodeUTF8))
        self.sinterConfigGUIButton.setToolTip(QtGui.QApplication.translate("dmfUploadDialog", "<html><head/><body><p>Edit or create a new SimSinter configuration file with the Sinter Config GUI.  This is a windows only option.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.sinterConfigGUIButton.setText(QtGui.QApplication.translate("dmfUploadDialog", "Create/Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.configFileButton.setToolTip(QtGui.QApplication.translate("dmfUploadDialog", "Search for a sinter configuration file.", None, QtGui.QApplication.UnicodeUTF8))
        self.configFileButton.setText(QtGui.QApplication.translate("dmfUploadDialog", "Browse...", None, QtGui.QApplication.UnicodeUTF8))
        self.appEdit.setToolTip(QtGui.QApplication.translate("dmfUploadDialog", "Application used to run the simulation", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("dmfUploadDialog", "Sinter Configuration File:", None, QtGui.QApplication.UnicodeUTF8))
        self.simNameEdit.setToolTip(QtGui.QApplication.translate("dmfUploadDialog", "Name of simulation on Turbine.  The drop down will show and allow the user to select existing simulations.  A new name can also be entered to create a new simulation.", None, QtGui.QApplication.UnicodeUTF8))
        self.clearTableButton.setToolTip(QtGui.QApplication.translate("dmfUploadDialog", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.clearTableButton.setText(QtGui.QApplication.translate("dmfUploadDialog", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("dmfUploadDialog", "Additional Files", None, QtGui.QApplication.UnicodeUTF8))
        self.addFileButton.setText(QtGui.QApplication.translate("dmfUploadDialog", "Add Files...", None, QtGui.QApplication.UnicodeUTF8))
        self.removeFileButton.setText(QtGui.QApplication.translate("dmfUploadDialog", "Remove Files", None, QtGui.QApplication.UnicodeUTF8))
        self.relpathButton.setText(QtGui.QApplication.translate("dmfUploadDialog", "Resource Relative Path", None, QtGui.QApplication.UnicodeUTF8))
        self.fileTable.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("dmfUploadDialog", "Resource", None, QtGui.QApplication.UnicodeUTF8))
        self.fileTable.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("dmfUploadDialog", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.label1.setText(QtGui.QApplication.translate("dmfUploadDialog", "DMF Repo:", None, QtGui.QApplication.UnicodeUTF8))
        self.dmfRepo.setToolTip(QtGui.QApplication.translate("dmfUploadDialog", "DMF Repo", None, QtGui.QApplication.UnicodeUTF8))
        self.selectDMFRepoButton.setToolTip(QtGui.QApplication.translate("dmfUploadDialog", "Select a DMF repo", None, QtGui.QApplication.UnicodeUTF8))
        self.selectDMFRepoButton.setText(QtGui.QApplication.translate("dmfUploadDialog", "SelectDMF", None, QtGui.QApplication.UnicodeUTF8))
        self.okButton.setText(QtGui.QApplication.translate("dmfUploadDialog", "Okay", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("dmfUploadDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

import foqus_lib.gui.icons_rc as icons_rc