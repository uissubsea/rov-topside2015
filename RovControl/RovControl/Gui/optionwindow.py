# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'options.ui'
#
# Created: Wed Mar 11 11:45:31 2015
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

class Ui_OptionsWindow(object):
    def setupUi(self, OptionsWindow):
        print('opt')
        OptionsWindow.setObjectName(_fromUtf8("OptionsWindow"))
        OptionsWindow.resize(620, 455)
        self.gridLayout = QtGui.QGridLayout(OptionsWindow)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.tabWidget = QtGui.QTabWidget(OptionsWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(594, 390))
        self.tabWidget.setMaximumSize(QtCore.QSize(594, 390))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.sensor_tab = QtGui.QWidget()
        self.sensor_tab.setObjectName(_fromUtf8("sensor_tab"))
        self.tempLabel = QtGui.QLabel(self.sensor_tab)
        self.tempLabel.setGeometry(QtCore.QRect(20, 20, 267, 20))
        self.tempLabel.setObjectName(_fromUtf8("tempLabel"))
        self.tempBox = QtGui.QComboBox(self.sensor_tab)
        self.tempBox.setGeometry(QtCore.QRect(160, 10, 71, 31))
        self.tempBox.setObjectName(_fromUtf8("tempBox"))
        self.tempBox.addItem(_fromUtf8(""))
        self.tempBox.addItem(_fromUtf8(""))
        self.depthLabel = QtGui.QLabel(self.sensor_tab)
        self.depthLabel.setGeometry(QtCore.QRect(20, 60, 267, 20))
        self.depthLabel.setObjectName(_fromUtf8("depthLabel"))
        self.depthBox = QtGui.QComboBox(self.sensor_tab)
        self.depthBox.setGeometry(QtCore.QRect(160, 50, 71, 31))
        self.depthBox.setObjectName(_fromUtf8("depthBox"))
        self.depthBox.addItem(_fromUtf8(""))
        self.depthBox.addItem(_fromUtf8(""))
        self.compassLabel = QtGui.QLabel(self.sensor_tab)
        self.compassLabel.setGeometry(QtCore.QRect(20, 100, 267, 20))
        self.compassLabel.setObjectName(_fromUtf8("compassLabel"))
        self.compassBox = QtGui.QComboBox(self.sensor_tab)
        self.compassBox.setGeometry(QtCore.QRect(160, 90, 71, 31))
        self.compassBox.setObjectName(_fromUtf8("compassBox"))
        self.compassBox.addItem(_fromUtf8(""))
        self.compassBox.addItem(_fromUtf8(""))
        self.gyroBox = QtGui.QComboBox(self.sensor_tab)
        self.gyroBox.setGeometry(QtCore.QRect(160, 130, 71, 31))
        self.gyroBox.setObjectName(_fromUtf8("gyroBox"))
        self.gyroBox.addItem(_fromUtf8(""))
        self.gyroBox.addItem(_fromUtf8(""))
        self.compassLabel_2 = QtGui.QLabel(self.sensor_tab)
        self.compassLabel_2.setGeometry(QtCore.QRect(20, 140, 267, 20))
        self.compassLabel_2.setObjectName(_fromUtf8("compassLabel_2"))
        self.tabWidget.addTab(self.sensor_tab, _fromUtf8(""))
        self.mCU_tab = QtGui.QWidget()
        self.mCU_tab.setObjectName(_fromUtf8("mCU_tab"))
        self.tabWidget.addTab(self.mCU_tab, _fromUtf8(""))
        self.gridLayout_5.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_5, 1, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(OptionsWindow)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 1, 1, 1)

        self.retranslateUi(OptionsWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(OptionsWindow)

    def retranslateUi(self, OptionsWindow):
        OptionsWindow.setWindowTitle(_translate("OptionsWindow", "Settings", None))
        self.tempLabel.setText(_translate("OptionsWindow", "Thermometer", None))
        self.tempBox.setItemText(0, _translate("OptionsWindow", "On", None))
        self.tempBox.setItemText(1, _translate("OptionsWindow", "Off", None))
        self.depthLabel.setText(_translate("OptionsWindow", "Depth Sensors", None))
        self.depthBox.setItemText(0, _translate("OptionsWindow", "On", None))
        self.depthBox.setItemText(1, _translate("OptionsWindow", "Off", None))
        self.compassLabel.setText(_translate("OptionsWindow", "Compass", None))
        self.compassBox.setItemText(0, _translate("OptionsWindow", "On", None))
        self.compassBox.setItemText(1, _translate("OptionsWindow", "Off", None))
        self.gyroBox.setItemText(0, _translate("OptionsWindow", "On", None))
        self.gyroBox.setItemText(1, _translate("OptionsWindow", "Off", None))
        self.compassLabel_2.setText(_translate("OptionsWindow", "Gyro", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sensor_tab), _translate("OptionsWindow", "Sensors", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mCU_tab), _translate("OptionsWindow", "μCU", None))

