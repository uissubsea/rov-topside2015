# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Settings.ui'
#
# Created: Thu Feb 26 10:02:56 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        SettingsWindow.setObjectName(_fromUtf8("SettingsWindow"))
        SettingsWindow.resize(620, 455)
        self.gridLayout = QtGui.QGridLayout(SettingsWindow)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.tabWidget = QtGui.QTabWidget(SettingsWindow)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.sensorTab = QtGui.QWidget()
        self.sensorTab.setObjectName(_fromUtf8("sensorTab"))
        self.gridLayout_4 = QtGui.QGridLayout(self.sensorTab)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.onOffGroup = QtGui.QGroupBox(self.sensorTab)
        self.onOffGroup.setObjectName(_fromUtf8("onOffGroup"))
        self.gridLayout_2 = QtGui.QGridLayout(self.onOffGroup)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.tempLabel = QtGui.QLabel(self.onOffGroup)
        self.tempLabel.setObjectName(_fromUtf8("tempLabel"))
        self.gridLayout_2.addWidget(self.tempLabel, 0, 0, 1, 1)
        self.tempBox = QtGui.QComboBox(self.onOffGroup)
        self.tempBox.setObjectName(_fromUtf8("tempBox"))
        self.tempBox.addItem(_fromUtf8(""))
        self.tempBox.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.tempBox, 0, 1, 1, 1)
        self.depthLabel = QtGui.QLabel(self.onOffGroup)
        self.depthLabel.setObjectName(_fromUtf8("depthLabel"))
        self.gridLayout_2.addWidget(self.depthLabel, 1, 0, 1, 1)
        self.depthBox = QtGui.QComboBox(self.onOffGroup)
        self.depthBox.setObjectName(_fromUtf8("depthBox"))
        self.depthBox.addItem(_fromUtf8(""))
        self.depthBox.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.depthBox, 1, 1, 1, 1)
        self.compassLabel = QtGui.QLabel(self.onOffGroup)
        self.compassLabel.setObjectName(_fromUtf8("compassLabel"))
        self.gridLayout_2.addWidget(self.compassLabel, 2, 0, 1, 1)
        self.compassBox = QtGui.QComboBox(self.onOffGroup)
        self.compassBox.setObjectName(_fromUtf8("compassBox"))
        self.compassBox.addItem(_fromUtf8(""))
        self.compassBox.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.compassBox, 2, 1, 1, 1)
        self.gyroLabel = QtGui.QLabel(self.onOffGroup)
        self.gyroLabel.setObjectName(_fromUtf8("gyroLabel"))
        self.gridLayout_2.addWidget(self.gyroLabel, 3, 0, 1, 1)
        self.gyroBox = QtGui.QComboBox(self.onOffGroup)
        self.gyroBox.setObjectName(_fromUtf8("gyroBox"))
        self.gyroBox.addItem(_fromUtf8(""))
        self.gyroBox.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.gyroBox, 3, 1, 1, 1)
        self.gridLayout_4.addWidget(self.onOffGroup, 0, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.sensorTab)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.tabWidget.addTab(self.sensorTab, _fromUtf8(""))
        self.mcuTab = QtGui.QWidget()
        self.mcuTab.setObjectName(_fromUtf8("mcuTab"))
        self.tabWidget.addTab(self.mcuTab, _fromUtf8(""))
        self.joystickTab = QtGui.QWidget()
        self.joystickTab.setObjectName(_fromUtf8("joystickTab"))
        self.gridLayout_6 = QtGui.QGridLayout(self.joystickTab)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.groupBox_3 = QtGui.QGroupBox(self.joystickTab)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.formLayout = QtGui.QFormLayout(self.groupBox_3)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_5 = QtGui.QLabel(self.groupBox_3)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_5)
        self.comboBox_5 = QtGui.QComboBox(self.groupBox_3)
        self.comboBox_5.setObjectName(_fromUtf8("comboBox_5"))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.comboBox_5)
        self.pushButton = QtGui.QPushButton(self.groupBox_3)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.pushButton_2)
        spacerItem = QtGui.QSpacerItem(20, 70, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtGui.QFormLayout.LabelRole, spacerItem)
        self.gridLayout_6.addWidget(self.groupBox_3, 0, 0, 1, 1)
        self.graphicsView = QtGui.QGraphicsView(self.joystickTab)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.gridLayout_6.addWidget(self.graphicsView, 0, 1, 1, 1)
        self.tabWidget.addTab(self.joystickTab, _fromUtf8(""))
        self.gridLayout_5.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_5, 1, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(SettingsWindow)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 1, 1, 1)

        self.retranslateUi(SettingsWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(SettingsWindow)

    def retranslateUi(self, SettingsWindow):
        SettingsWindow.setWindowTitle(_translate("SettingsWindow", "Settings", None))
        self.onOffGroup.setTitle(_translate("SettingsWindow", "On/off", None))
        self.tempLabel.setText(_translate("SettingsWindow", "Temperature", None))
        self.tempBox.setItemText(0, _translate("SettingsWindow", "On", None))
        self.tempBox.setItemText(1, _translate("SettingsWindow", "Off", None))
        self.depthLabel.setText(_translate("SettingsWindow", "Depth Sensors", None))
        self.depthBox.setItemText(0, _translate("SettingsWindow", "On", None))
        self.depthBox.setItemText(1, _translate("SettingsWindow", "Off", None))
        self.compassLabel.setText(_translate("SettingsWindow", "Compass", None))
        self.compassBox.setItemText(0, _translate("SettingsWindow", "On", None))
        self.compassBox.setItemText(1, _translate("SettingsWindow", "Off", None))
        self.gyroLabel.setText(_translate("SettingsWindow", "Gyroscope", None))
        self.gyroBox.setItemText(0, _translate("SettingsWindow", "On", None))
        self.gyroBox.setItemText(1, _translate("SettingsWindow", "Off", None))
        self.groupBox_2.setTitle(_translate("SettingsWindow", "GroupBox", None))
        self.label_4.setText(_translate("SettingsWindow", "Place Holder", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sensorTab), _translate("SettingsWindow", "Sensors", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mcuTab), _translate("SettingsWindow", "MCU", None))
        self.groupBox_3.setTitle(_translate("SettingsWindow", "Joystick", None))
        self.label_5.setText(_translate("SettingsWindow", "Connected Sticks", None))
        self.comboBox_5.setItemText(0, _translate("SettingsWindow", "Joystick 1", None))
        self.pushButton.setText(_translate("SettingsWindow", "Calibrate", None))
        self.pushButton_2.setText(_translate("SettingsWindow", "Choose", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.joystickTab), _translate("SettingsWindow", "Joystick", None))

