# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'remote.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_Remote(object):
    def setupUi(self, Remote):
        Remote.setObjectName(_fromUtf8("Remote"))
        Remote.resize(400, 300)
        self.gridLayout_4 = QtGui.QGridLayout(Remote)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.groupBox_2 = QtGui.QGroupBox(Remote)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 1, 2, 2)
        self.servoSlider = QtGui.QSlider(self.groupBox_2)
        self.servoSlider.setMinimum(0)
        self.servoSlider.setMaximum(1000)
        self.servoSlider.setSliderPosition(750)
        self.servoSlider.setOrientation(QtCore.Qt.Vertical)
        self.servoSlider.setObjectName(_fromUtf8("servoSlider"))
        self.gridLayout_2.addWidget(self.servoSlider, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(Remote)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.laserState = QtGui.QCheckBox(self.groupBox)
        self.laserState.setObjectName(_fromUtf8("laserState"))
        self.gridLayout.addWidget(self.laserState, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox, 1, 0, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(Remote)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.lightState = QtGui.QCheckBox(self.groupBox_3)
        self.lightState.setObjectName(_fromUtf8("lightState"))
        self.gridLayout_3.addWidget(self.lightState, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_3, 1, 1, 1, 1)
        self.groupBox_4 = QtGui.QGroupBox(Remote)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.lightSlider = QtGui.QSlider(self.groupBox_4)
        self.lightSlider.setMinimum(0)
        self.lightSlider.setMaximum(10000)
        self.lightSlider.setProperty("value", 10000)
        self.lightSlider.setOrientation(QtCore.Qt.Vertical)
        self.lightSlider.setObjectName(_fromUtf8("lightSlider"))
        self.gridLayout_5.addWidget(self.lightSlider, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_4)
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_5.addWidget(self.label_2, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_4, 0, 1, 1, 1)

        self.retranslateUi(Remote)
        QtCore.QObject.connect(self.servoSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.label.setNum)
        QtCore.QMetaObject.connectSlotsByName(Remote)

    def retranslateUi(self, Remote):
        Remote.setWindowTitle(_translate("Remote", "Rov Controller", None))
        self.groupBox_2.setTitle(_translate("Remote", "Camera Servo", None))
        self.groupBox.setTitle(_translate("Remote", "Laser", None))
        self.laserState.setText(_translate("Remote", "On/off", None))
        self.groupBox_3.setTitle(_translate("Remote", "Lights", None))
        self.lightState.setText(_translate("Remote", "On/off", None))
        self.groupBox_4.setTitle(_translate("Remote", "Light Dim", None))

