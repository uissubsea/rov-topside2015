# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StatusWidget.ui'
#
# Created: Thu Feb 26 10:03:10 2015
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

class Ui_StatusWindow(object):
    def setupUi(self, StatusWindow):
        StatusWindow.setObjectName(_fromUtf8("StatusWindow"))
        StatusWindow.resize(672, 512)
        self.gridLayout_3 = QtGui.QGridLayout(StatusWindow)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.groupBox = QtGui.QGroupBox(StatusWindow)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.ecStatus = QtGui.QLabel(self.groupBox)
        self.ecStatus.setObjectName(_fromUtf8("ecStatus"))
        self.gridLayout_2.addWidget(self.ecStatus, 0, 1, 1, 1)
        self.manipStatus = QtGui.QLabel(self.groupBox)
        self.manipStatus.setObjectName(_fromUtf8("manipStatus"))
        self.gridLayout_2.addWidget(self.manipStatus, 2, 1, 1, 1)
        self.tcuLabel = QtGui.QLabel(self.groupBox)
        self.tcuLabel.setObjectName(_fromUtf8("tcuLabel"))
        self.gridLayout_2.addWidget(self.tcuLabel, 1, 0, 1, 1)
        self.manipulatorLabel = QtGui.QLabel(self.groupBox)
        self.manipulatorLabel.setObjectName(_fromUtf8("manipulatorLabel"))
        self.gridLayout_2.addWidget(self.manipulatorLabel, 2, 0, 1, 1)
        self.ecLabel = QtGui.QLabel(self.groupBox)
        self.ecLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.ecLabel.setObjectName(_fromUtf8("ecLabel"))
        self.gridLayout_2.addWidget(self.ecLabel, 0, 0, 1, 1)
        self.tcuStatus = QtGui.QLabel(self.groupBox)
        self.tcuStatus.setObjectName(_fromUtf8("tcuStatus"))
        self.gridLayout_2.addWidget(self.tcuStatus, 1, 1, 1, 1)
        self.sensorStatus = QtGui.QLabel(self.groupBox)
        self.sensorStatus.setObjectName(_fromUtf8("sensorStatus"))
        self.gridLayout_2.addWidget(self.sensorStatus, 3, 1, 1, 1)
        self.sensorLabel = QtGui.QLabel(self.groupBox)
        self.sensorLabel.setObjectName(_fromUtf8("sensorLabel"))
        self.gridLayout_2.addWidget(self.sensorLabel, 3, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)
        self.logBox = QtGui.QGroupBox(StatusWindow)
        self.logBox.setObjectName(_fromUtf8("logBox"))
        self.gridLayout = QtGui.QGridLayout(self.logBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.textEdit = QtGui.QTextEdit(self.logBox)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.logBox, 1, 0, 1, 1)

        self.retranslateUi(StatusWindow)
        QtCore.QMetaObject.connectSlotsByName(StatusWindow)

    def retranslateUi(self, StatusWindow):
        StatusWindow.setWindowTitle(_translate("StatusWindow", "Rov Status", None))
        self.groupBox.setTitle(_translate("StatusWindow", "Status", None))
        self.ecStatus.setText(_translate("StatusWindow", "StatusEC", None))
        self.manipStatus.setText(_translate("StatusWindow", "StatusManip", None))
        self.tcuLabel.setText(_translate("StatusWindow", "TCU", None))
        self.manipulatorLabel.setText(_translate("StatusWindow", "Manipulator", None))
        self.ecLabel.setText(_translate("StatusWindow", "Ethernet/Can", None))
        self.tcuStatus.setText(_translate("StatusWindow", "StatusTCU", None))
        self.sensorStatus.setText(_translate("StatusWindow", "Status Sensor", None))
        self.sensorLabel.setText(_translate("StatusWindow", "Sensor Unit", None))
        self.logBox.setTitle(_translate("StatusWindow", "Log", None))

