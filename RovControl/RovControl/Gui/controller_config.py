# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RESOURCES/controller_config.ui'
#
# Created: Thu Mar 26 15:40:48 2015
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

class Ui_controller_config(object):
    def setupUi(self, controller_config):
        controller_config.setObjectName(_fromUtf8("controller_config"))
        controller_config.resize(680, 600)
        controller_config.setMinimumSize(QtCore.QSize(680, 600))
        controller_config.setMaximumSize(QtCore.QSize(680, 600))
        
        self.tabWindow = QtGui.QTabWidget(controller_config)
        self.tabWindow.setGeometry(QtCore.QRect(20, 10, 641, 531))
        self.tabWindow.setUsesScrollButtons(False)
        self.tabWindow.setObjectName(_fromUtf8("tabWindow"))
        
        self.keyBindingsTab = QtGui.QWidget()
        self.keyBindingsTab.setObjectName(_fromUtf8("keyBindingsTab"))
        
        self.thrusterGroupBox = QtGui.QGroupBox(self.keyBindingsTab)
        self.thrusterGroupBox.setGeometry(QtCore.QRect(20, 0, 591, 151))
        self.thrusterGroupBox.setObjectName(_fromUtf8("thrusterGroupBox"))
        
        self.thUp_label = QtGui.QLabel(self.thrusterGroupBox)
        self.thUp_label.setGeometry(QtCore.QRect(20, 30, 61, 21))
        self.thUp_label.setObjectName(_fromUtf8("thUp_label"))
        
        self.thDown_label = QtGui.QLabel(self.thrusterGroupBox)
        self.thDown_label.setGeometry(QtCore.QRect(20, 60, 61, 21))
        self.thDown_label.setObjectName(_fromUtf8("thDown_label"))
        
        self.thForward_label = QtGui.QLabel(self.thrusterGroupBox)
        self.thForward_label.setGeometry(QtCore.QRect(20, 90, 61, 21))
        self.thForward_label.setObjectName(_fromUtf8("thForward_label"))
        
        self.thRotateCCW_label = QtGui.QLabel(self.thrusterGroupBox)
        self.thRotateCCW_label.setGeometry(QtCore.QRect(220, 120, 61, 21))
        self.thRotateCCW_label.setObjectName(_fromUtf8("thRotateCCW_label"))
        
        self.thReverse_label = QtGui.QLabel(self.thrusterGroupBox)
        self.thReverse_label.setGeometry(QtCore.QRect(20, 120, 71, 21))
        self.thReverse_label.setObjectName(_fromUtf8("thReverse_label"))
        
        self.thRotateCW_label = QtGui.QLabel(self.thrusterGroupBox)
        self.thRotateCW_label.setGeometry(QtCore.QRect(220, 90, 61, 21))
        self.thRotateCW_label.setObjectName(_fromUtf8("thRotateCW_label"))
        
        self.thRight_label = QtGui.QLabel(self.thrusterGroupBox)
        self.thRight_label.setGeometry(QtCore.QRect(220, 30, 71, 21))
        self.thRight_label.setObjectName(_fromUtf8("thRight_label"))
        
        self.thLeft_label = QtGui.QLabel(self.thrusterGroupBox)
        self.thLeft_label.setGeometry(QtCore.QRect(220, 60, 61, 21))
        self.thLeft_label.setObjectName(_fromUtf8("thLeft_label"))
        
        self.thUp_key = QtGui.QLineEdit(self.thrusterGroupBox)
        self.thUp_key.setGeometry(QtCore.QRect(130, 30, 41, 20))
        self.thUp_key.setText(_fromUtf8(""))
        self.thUp_key.setObjectName(_fromUtf8("thUp_key"))
        
        self.thrusterGraphics = QtGui.QGraphicsView(self.thrusterGroupBox)
        self.thrusterGraphics.setGeometry(QtCore.QRect(390, 30, 191, 111))
        self.thrusterGraphics.setObjectName(_fromUtf8("thrusterGraphics"))
        
        self.thDown_key = QtGui.QLineEdit(self.thrusterGroupBox)
        self.thDown_key.setGeometry(QtCore.QRect(130, 60, 41, 20))
        self.thDown_key.setText(_fromUtf8(""))
        self.thDown_key.setObjectName(_fromUtf8("thDown_key"))
        
        self.thReverse_key = QtGui.QLineEdit(self.thrusterGroupBox)
        self.thReverse_key.setGeometry(QtCore.QRect(130, 120, 41, 20))
        self.thReverse_key.setText(_fromUtf8(""))
        self.thReverse_key.setObjectName(_fromUtf8("thReverse_key"))
        
        self.thForward_key = QtGui.QLineEdit(self.thrusterGroupBox)
        self.thForward_key.setGeometry(QtCore.QRect(130, 90, 41, 20))
        self.thForward_key.setText(_fromUtf8(""))
        self.thForward_key.setObjectName(_fromUtf8("thForward_key"))
        
        self.thRight_key = QtGui.QLineEdit(self.thrusterGroupBox)
        self.thRight_key.setGeometry(QtCore.QRect(330, 30, 41, 20))
        self.thRight_key.setText(_fromUtf8(""))
        self.thRight_key.setObjectName(_fromUtf8("thRight_key"))
        
        self.thLeft_key = QtGui.QLineEdit(self.thrusterGroupBox)
        self.thLeft_key.setGeometry(QtCore.QRect(330, 60, 41, 20))
        self.thLeft_key.setText(_fromUtf8(""))
        self.thLeft_key.setObjectName(_fromUtf8("thLeft_key"))
        
        self.thRotateCCW_key = QtGui.QLineEdit(self.thrusterGroupBox)
        self.thRotateCCW_key.setGeometry(QtCore.QRect(330, 120, 41, 20))
        self.thRotateCCW_key.setText(_fromUtf8(""))
        self.thRotateCCW_key.setObjectName(_fromUtf8("thRotateCCW_key"))
        
        self.thRotateCW_key = QtGui.QLineEdit(self.thrusterGroupBox)
        self.thRotateCW_key.setGeometry(QtCore.QRect(330, 90, 41, 20))
        self.thRotateCW_key.setText(_fromUtf8(""))
        self.thRotateCW_key.setObjectName(_fromUtf8("thRotateCW_key"))
        
        self.manipulatorGroupBox = QtGui.QGroupBox(self.keyBindingsTab)
        self.manipulatorGroupBox.setGeometry(QtCore.QRect(20, 160, 591, 211))
        self.manipulatorGroupBox.setObjectName(_fromUtf8("manipulatorGroupBox"))
        
        self.manipulatorGraphics = QtGui.QGraphicsView(self.manipulatorGroupBox)
        self.manipulatorGraphics.setGeometry(QtCore.QRect(390, 30, 191, 171))
        self.manipulatorGraphics.setObjectName(_fromUtf8("manipulatorGraphics"))
        
        
        


        self.mcOpen_label = QtGui.QLabel(self.manipulatorGroupBox)
        self.mcOpen_label.setGeometry(QtCore.QRect(20, 30, 71, 16))
        self.mcOpen_label.setObjectName(_fromUtf8("mcOpen_label"))
        
        self.mcRotateCW_label = QtGui.QLabel(self.manipulatorGroupBox)
        self.mcRotateCW_label.setGeometry(QtCore.QRect(20, 90, 101, 16))
        self.mcRotateCW_label.setObjectName(_fromUtf8("mcRotateCW_label"))
        
        self.mcGrip_label = QtGui.QLabel(self.manipulatorGroupBox)
        self.mcGrip_label.setGeometry(QtCore.QRect(20, 60, 62, 16))
        self.mcGrip_label.setObjectName(_fromUtf8("mcGrip_label"))
        
        self.mcRotateCCW_label = QtGui.QLabel(self.manipulatorGroupBox)
        self.mcRotateCCW_label.setGeometry(QtCore.QRect(20, 120, 111, 16))
        self.mcRotateCCW_label.setObjectName(_fromUtf8("mcRotateCCW_label"))
        
        self.maRaise_label = QtGui.QLabel(self.manipulatorGroupBox)
        self.maRaise_label.setGeometry(QtCore.QRect(220, 30, 111, 16))
        self.maRaise_label.setObjectName(_fromUtf8("maRaise_label"))
        
        self.mcDown_label = QtGui.QLabel(self.manipulatorGroupBox)
        self.mcDown_label.setGeometry(QtCore.QRect(20, 180, 111, 16))
        self.mcDown_label.setObjectName(_fromUtf8("mcDown_label"))
        
        self.mcUp_label = QtGui.QLabel(self.manipulatorGroupBox)
        self.mcUp_label.setGeometry(QtCore.QRect(20, 150, 111, 16))
        self.mcUp_label.setObjectName(_fromUtf8("mcUp_label"))
        
        self.maLower_label = QtGui.QLabel(self.manipulatorGroupBox)
        self.maLower_label.setGeometry(QtCore.QRect(220, 60, 111, 16))
        self.maLower_label.setObjectName(_fromUtf8("maLower_label"))
        
        self.maRotateCW_label = QtGui.QLabel(self.manipulatorGroupBox)
        self.maRotateCW_label.setGeometry(QtCore.QRect(220, 90, 111, 16))
        self.maRotateCW_label.setObjectName(_fromUtf8("maRotateCW_label"))
        
        self.maRotateCCW_label = QtGui.QLabel(self.manipulatorGroupBox)
        self.maRotateCCW_label.setGeometry(QtCore.QRect(220, 120, 111, 16))
        self.maRotateCCW_label.setObjectName(_fromUtf8("maRotateCCW_label"))
        
        self.maBend_label = QtGui.QLabel(self.manipulatorGroupBox)
        self.maBend_label.setGeometry(QtCore.QRect(220, 150, 111, 16))
        self.maBend_label.setObjectName(_fromUtf8("maBend_label"))
        
        self.maStretch_label = QtGui.QLabel(self.manipulatorGroupBox)
        self.maStretch_label.setGeometry(QtCore.QRect(220, 180, 111, 16))
        self.maStretch_label.setObjectName(_fromUtf8("maStretch_label"))




        self.mcRotateCCW = QtGui.QLineEdit(self.manipulatorGroupBox)
        self.mcRotateCCW.setGeometry(QtCore.QRect(130, 120, 41, 20))
        self.mcRotateCCW.setText(_fromUtf8(""))
        self.mcRotateCCW.setObjectName(_fromUtf8("mcRotateCCW"))
        
        self.mcRotateCW_key = QtGui.QLineEdit(self.manipulatorGroupBox)
        self.mcRotateCW_key.setGeometry(QtCore.QRect(130, 90, 41, 20))
        self.mcRotateCW_key.setText(_fromUtf8(""))
        self.mcRotateCW_key.setObjectName(_fromUtf8("mcRotateCW_key"))
        
        self.mcGrip_key = QtGui.QLineEdit(self.manipulatorGroupBox)
        self.mcGrip_key.setGeometry(QtCore.QRect(130, 60, 41, 20))
        self.mcGrip_key.setText(_fromUtf8(""))
        self.mcGrip_key.setObjectName(_fromUtf8("mcGrip_key"))
        
        self.mcOpen_key = QtGui.QLineEdit(self.manipulatorGroupBox)
        self.mcOpen_key.setGeometry(QtCore.QRect(130, 30, 41, 20))
        self.mcOpen_key.setText(_fromUtf8(""))
        self.mcOpen_key.setObjectName(_fromUtf8("mcOpen_key"))

        self.mcUp_key = QtGui.QLineEdit(self.manipulatorGroupBox)
        self.mcUp_key.setGeometry(QtCore.QRect(130, 150, 41, 20))
        self.mcUp_key.setText(_fromUtf8(""))
        self.mcUp_key.setObjectName(_fromUtf8("mcUp_key"))
        
        self.mcDown_key = QtGui.QLineEdit(self.manipulatorGroupBox)
        self.mcDown_key.setGeometry(QtCore.QRect(130, 180, 41, 20))
        self.mcDown_key.setText(_fromUtf8(""))
        self.mcDown_key.setObjectName(_fromUtf8("mcDown_key"))
        
        self.maRaise_key = QtGui.QLineEdit(self.manipulatorGroupBox)
        self.maRaise_key.setGeometry(QtCore.QRect(330, 30, 41, 20))
        self.maRaise_key.setText(_fromUtf8(""))
        self.maRaise_key.setObjectName(_fromUtf8("maRaise_key"))
        
        self.maLower_key = QtGui.QLineEdit(self.manipulatorGroupBox)
        self.maLower_key.setGeometry(QtCore.QRect(330, 60, 41, 20))
        self.maLower_key.setText(_fromUtf8(""))
        self.maLower_key.setObjectName(_fromUtf8("maLower_key"))
        
        self.maRotateCW_key = QtGui.QLineEdit(self.manipulatorGroupBox)
        self.maRotateCW_key.setGeometry(QtCore.QRect(330, 90, 41, 20))
        self.maRotateCW_key.setText(_fromUtf8(""))
        self.maRotateCW_key.setObjectName(_fromUtf8("maRotateCW_key"))
        
        self.maRotateCCW = QtGui.QLineEdit(self.manipulatorGroupBox)
        self.maRotateCCW.setGeometry(QtCore.QRect(330, 120, 41, 20))
        self.maRotateCCW.setText(_fromUtf8(""))
        self.maRotateCCW.setObjectName(_fromUtf8("maRotateCCW"))
        
        self.maBend_key = QtGui.QLineEdit(self.manipulatorGroupBox)
        self.maBend_key.setGeometry(QtCore.QRect(330, 150, 41, 20))
        self.maBend_key.setText(_fromUtf8(""))
        self.maBend_key.setObjectName(_fromUtf8("maBend_key"))
        
        self.maStretch_key = QtGui.QLineEdit(self.manipulatorGroupBox)
        self.maStretch_key.setGeometry(QtCore.QRect(330, 180, 41, 20))
        self.maStretch_key.setText(_fromUtf8(""))
        self.maStretch_key.setObjectName(_fromUtf8("maStretch_key"))
        


        
        self.otherGroupBox = QtGui.QGroupBox(self.keyBindingsTab)
        self.otherGroupBox.setGeometry(QtCore.QRect(20, 380, 591, 111))
        self.otherGroupBox.setObjectName(_fromUtf8("otherGroupBox"))
        
        self.lightToggle_label = QtGui.QLabel(self.otherGroupBox)
        self.lightToggle_label.setGeometry(QtCore.QRect(20, 40, 111, 16))
        self.lightToggle_label.setObjectName(_fromUtf8("lightToggle_label"))
        self.lightToggle_key = QtGui.QLineEdit(self.otherGroupBox)
        self.lightToggle_key.setGeometry(QtCore.QRect(130, 40, 41, 20))
        self.lightToggle_key.setText(_fromUtf8(""))
        self.lightToggle_key.setObjectName(_fromUtf8("lightToggle_key"))
        
        self.cam1Toggle_label = QtGui.QLabel(self.otherGroupBox)
        self.cam1Toggle_label.setGeometry(QtCore.QRect(20, 70, 111, 21))
        self.cam1Toggle_label.setObjectName(_fromUtf8("cam1Toggle_label"))
        
        self.cam1Toggle_key = QtGui.QLineEdit(self.otherGroupBox)
        self.cam1Toggle_key.setGeometry(QtCore.QRect(130, 70, 41, 20))
        self.cam1Toggle_key.setText(_fromUtf8(""))
        self.cam1Toggle_key.setObjectName(_fromUtf8("cam1Toggle_key"))
        
        self.cam2Toggle_label = QtGui.QLabel(self.otherGroupBox)
        self.cam2Toggle_label.setGeometry(QtCore.QRect(220, 40, 111, 21))
        self.cam2Toggle_label.setObjectName(_fromUtf8("cam2Toggle_label"))
        
        self.cam3Toggle_label = QtGui.QLabel(self.otherGroupBox)
        self.cam3Toggle_label.setGeometry(QtCore.QRect(220, 70, 111, 21))
        self.cam3Toggle_label.setObjectName(_fromUtf8("cam3Toggle_label"))
        
        self.cam2Toggle_key = QtGui.QLineEdit(self.otherGroupBox)
        self.cam2Toggle_key.setGeometry(QtCore.QRect(330, 40, 41, 20))
        self.cam2Toggle_key.setText(_fromUtf8(""))
        self.cam2Toggle_key.setObjectName(_fromUtf8("cam2Toggle_key"))
        
        self.cam3Toggle_key = QtGui.QLineEdit(self.otherGroupBox)
        self.cam3Toggle_key.setGeometry(QtCore.QRect(330, 70, 41, 20))
        self.cam3Toggle_key.setText(_fromUtf8(""))
        self.cam3Toggle_key.setObjectName(_fromUtf8("cam3Toggle_key"))
        
        self.holdToggle_label = QtGui.QLabel(self.otherGroupBox)
        self.holdToggle_label.setGeometry(QtCore.QRect(420, 40, 111, 21))
        self.holdToggle_label.setObjectName(_fromUtf8("holdToggle_label"))
        
        self.holdToggle_key = QtGui.QLineEdit(self.otherGroupBox)
        self.holdToggle_key.setGeometry(QtCore.QRect(510, 40, 41, 20))
        self.holdToggle_key.setText(_fromUtf8(""))
        self.holdToggle_key.setObjectName(_fromUtf8("holdToggle_key"))
        
        self.tabWindow.addTab(self.keyBindingsTab, _fromUtf8(""))
        self.controllerTab = QtGui.QWidget()
        self.controllerTab.setObjectName(_fromUtf8("controllerTab"))
        self.tabWindow.addTab(self.controllerTab, _fromUtf8(""))
        
        self.sensitivityTab = QtGui.QWidget()
        self.sensitivityTab.setObjectName(_fromUtf8("sensitivityTab"))
        
        self.throttleSensBox = QtGui.QGroupBox(self.sensitivityTab)
        self.throttleSensBox.setGeometry(QtCore.QRect(20, 10, 591, 201))
        self.throttleSensBox.setObjectName(_fromUtf8("throttleSensBox"))
        
        self.linear_radiobutton = QtGui.QRadioButton(self.throttleSensBox)
        self.linear_radiobutton.setGeometry(QtCore.QRect(20, 50, 102, 20))
        self.linear_radiobutton.setChecked(True)
        self.linear_radiobutton.setObjectName(_fromUtf8("linear_radiobutton"))
        
        self.exp_radiobutton = QtGui.QRadioButton(self.throttleSensBox)
        self.exp_radiobutton.setGeometry(QtCore.QRect(20, 80, 102, 20))
        self.exp_radiobutton.setObjectName(_fromUtf8("exp_radiobutton"))
        
        self.exp_slider = QtGui.QSlider(self.throttleSensBox)
        self.exp_slider.setGeometry(QtCore.QRect(150, 80, 160, 22))
        self.exp_slider.setOrientation(QtCore.Qt.Horizontal)
        self.exp_slider.setTickPosition(QtGui.QSlider.NoTicks)
        self.exp_slider.setTickInterval(0)
        self.exp_slider.setObjectName(_fromUtf8("exp_slider"))
        
        self.linear_slider = QtGui.QSlider(self.throttleSensBox)
        self.linear_slider.setGeometry(QtCore.QRect(150, 50, 160, 22))
        self.linear_slider.setProperty("value", 0)
        self.linear_slider.setOrientation(QtCore.Qt.Horizontal)
        self.linear_slider.setInvertedControls(False)
        self.linear_slider.setObjectName(_fromUtf8("linear_slider"))
        
        self.graphicsView = PlotWidget(self.throttleSensBox)
        self.graphicsView.setGeometry(QtCore.QRect(330, 30, 251, 161))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        
        self.manipulatorSensBox = QtGui.QGroupBox(self.sensitivityTab)
        self.manipulatorSensBox.setGeometry(QtCore.QRect(20, 230, 591, 231))
        self.manipulatorSensBox.setObjectName(_fromUtf8("manipulatorSensBox"))
        
        self.tabWindow.addTab(self.sensitivityTab, _fromUtf8(""))
        
        self.cancelButton = QtGui.QPushButton(controller_config)
        self.cancelButton.setGeometry(QtCore.QRect(570, 550, 91, 32))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        
        self.applyButton = QtGui.QPushButton(controller_config)
        self.applyButton.setGeometry(QtCore.QRect(480, 550, 91, 32))
        self.applyButton.setObjectName(_fromUtf8("applyButton"))
        
        self.resetButton = QtGui.QPushButton(controller_config)
        self.resetButton.setGeometry(QtCore.QRect(20, 550, 91, 32))
        self.resetButton.setObjectName(_fromUtf8("resetButton"))

        self.retranslateUi(controller_config)
        self.tabWindow.setCurrentIndex(1)
        QtCore.QObject.connect(self.linear_slider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.graphicsView.update)
        QtCore.QObject.connect(self.exp_slider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.graphicsView.update)
        QtCore.QObject.connect(self.linear_radiobutton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.linear_slider.setEnabled)
        QtCore.QObject.connect(self.exp_radiobutton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.exp_slider.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(controller_config)

    def retranslateUi(self, controller_config):
        controller_config.setWindowTitle(_translate("controller_config", "Controller configuration", None))
        self.thrusterGroupBox.setTitle(_translate("controller_config", "Thrusters", None))
        self.thUp_label.setText(_translate("controller_config", "Up", None))
        self.thDown_label.setText(_translate("controller_config", "Down", None))
        self.thForward_label.setText(_translate("controller_config", "Forward", None))
        self.thRotateCCW_label.setText(_translate("controller_config", "Yaw ccw", None))
        self.thReverse_label.setText(_translate("controller_config", "Reverse", None))
        self.thRotateCW_label.setText(_translate("controller_config", "Yaw cw", None))
        self.thRight_label.setText(_translate("controller_config", "Roll right", None))
        self.thLeft_label.setText(_translate("controller_config", "Roll left", None))
        self.manipulatorGroupBox.setTitle(_translate("controller_config", "Manipulator", None))
        self.mcOpen_label.setText(_translate("controller_config", "Claw: open", None))
        self.mcRotateCW_label.setText(_translate("controller_config", "Claw: rotate cw", None))
        self.mcGrip_label.setText(_translate("controller_config", "Claw: grip", None))
        self.mcRotateCCW_label.setText(_translate("controller_config", "Claw: rotate ccw", None))
        self.maRaise_label.setText(_translate("controller_config", "Arm: raise", None))
        self.mcDown_label.setText(_translate("controller_config", "Claw: tilt down", None))
        self.mcUp_label.setText(_translate("controller_config", "Claw: tilt up", None))
        self.maLower_label.setText(_translate("controller_config", "Arm: lower", None))
        self.maRotateCW_label.setText(_translate("controller_config", "Arm: rotate cw", None))
        self.maRotateCCW_label.setText(_translate("controller_config", "Arm: rotate ccw", None))
        self.maBend_label.setText(_translate("controller_config", "Arm: bend", None))
        self.maStretch_label.setText(_translate("controller_config", "Arm: stretch", None))
        self.otherGroupBox.setTitle(_translate("controller_config", "Other", None))
        self.lightToggle_label.setText(_translate("controller_config", "Lights on/off", None))
        self.cam1Toggle_label.setText(_translate("controller_config", "Cam. 1 on/off", None))
        self.cam2Toggle_label.setText(_translate("controller_config", "Cam. 2 on/off", None))
        self.cam3Toggle_label.setText(_translate("controller_config", "Cam. 3 on/off", None))
        self.holdToggle_label.setText(_translate("controller_config", "Hold on/off", None))
        self.tabWindow.setTabText(self.tabWindow.indexOf(self.keyBindingsTab), _translate("controller_config", "Key Bindings", None))
        self.tabWindow.setTabText(self.tabWindow.indexOf(self.controllerTab), _translate("controller_config", "Controller", None))
        self.throttleSensBox.setTitle(_translate("controller_config", "Throttle", None))
        self.linear_radiobutton.setText(_translate("controller_config", "Linear", None))
        self.exp_radiobutton.setText(_translate("controller_config", "Exponential", None))
        self.manipulatorSensBox.setTitle(_translate("controller_config", "Manipulator", None))
        self.tabWindow.setTabText(self.tabWindow.indexOf(self.sensitivityTab), _translate("controller_config", "Sensitivity", None))
        self.cancelButton.setText(_translate("controller_config", "Cancel", None))
        self.applyButton.setText(_translate("controller_config", "Apply", None))
        self.resetButton.setText(_translate("controller_config", "Reset", None))

from pyqtgraph import PlotWidget
