# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RESOURCES/MainWindow.ui'
#
# Created: Wed May 13 18:20:15 2015
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(705, 553)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.mdiArea = QtGui.QMdiArea(self.centralwidget)
        self.mdiArea.setObjectName(_fromUtf8("mdiArea"))
        self.gridLayout.addWidget(self.mdiArea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 705, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionCamera_1 = QtGui.QAction(MainWindow)
        self.actionCamera_1.setObjectName(_fromUtf8("actionCamera_1"))
        self.actionCamera_2 = QtGui.QAction(MainWindow)
        self.actionCamera_2.setObjectName(_fromUtf8("actionCamera_2"))
        self.actionOptions = QtGui.QAction(MainWindow)
        self.actionOptions.setObjectName(_fromUtf8("actionOptions"))
        self.actionStatus = QtGui.QAction(MainWindow)
        self.actionStatus.setObjectName(_fromUtf8("actionStatus"))
        self.actionPOD_1 = QtGui.QAction(MainWindow)
        self.actionPOD_1.setObjectName(_fromUtf8("actionPOD_1"))
        self.actionPOD_2 = QtGui.QAction(MainWindow)
        self.actionPOD_2.setObjectName(_fromUtf8("actionPOD_2"))
        self.actionController = QtGui.QAction(MainWindow)
        self.actionController.setObjectName(_fromUtf8("actionController"))
        self.actionCamera_3 = QtGui.QAction(MainWindow)
        self.actionCamera_3.setObjectName(_fromUtf8("actionCamera_3"))
        self.actionManipulator = QtGui.QAction(MainWindow)
        self.actionManipulator.setObjectName(_fromUtf8("actionManipulator"))
        self.actionThursters = QtGui.QAction(MainWindow)
        self.actionThursters.setObjectName(_fromUtf8("actionThursters"))
        self.actionVehicleData = QtGui.QAction(MainWindow)
        self.actionVehicleData.setObjectName(_fromUtf8("actionVehicleData"))
        self.actionAboutUs = QtGui.QAction(MainWindow)
        self.actionAboutUs.setObjectName(_fromUtf8("actionAboutUs"))
        self.actionAboutVehicle = QtGui.QAction(MainWindow)
        self.actionAboutVehicle.setObjectName(_fromUtf8("actionAboutVehicle"))
        self.actionOption = QtGui.QAction(MainWindow)
        self.actionOption.setObjectName(_fromUtf8("actionOption"))
        self.actionConnect = QtGui.QAction(MainWindow)
        self.actionConnect.setObjectName(_fromUtf8("actionConnect"))
        self.actionDisconnect = QtGui.QAction(MainWindow)
        self.actionDisconnect.setObjectName(_fromUtf8("actionDisconnect"))
        self.menuFile.addAction(self.actionConnect)
        self.menuFile.addAction(self.actionDisconnect)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionAboutUs)
        self.menuAbout.addAction(self.actionAboutVehicle)
        self.menuView.addAction(self.actionCamera_1)
        self.menuView.addAction(self.actionCamera_2)
        self.menuView.addAction(self.actionCamera_3)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionPOD_1)
        self.menuView.addAction(self.actionPOD_2)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionManipulator)
        self.menuView.addAction(self.actionThursters)
        self.menuView.addAction(self.actionVehicleData)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionStatus)
        self.menuSettings.addAction(self.actionController)
        self.menuSettings.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.toolBar.addAction(self.actionConnect)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionDisconnect)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "RovControl v 0.1a", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuAbout.setTitle(_translate("MainWindow", "About", None))
        self.menuView.setTitle(_translate("MainWindow", "View", None))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionExit.setToolTip(_translate("MainWindow", "Exit the application", None))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.actionCamera_1.setText(_translate("MainWindow", "Camera 1", None))
        self.actionCamera_2.setText(_translate("MainWindow", "Camera 2", None))
        self.actionOptions.setText(_translate("MainWindow", "Options", None))
        self.actionStatus.setText(_translate("MainWindow", "Status", None))
        self.actionPOD_1.setText(_translate("MainWindow", "POD 1", None))
        self.actionPOD_2.setText(_translate("MainWindow", "POD 2", None))
        self.actionController.setText(_translate("MainWindow", "Controller", None))
        self.actionCamera_3.setText(_translate("MainWindow", "Camera 3", None))
        self.actionManipulator.setText(_translate("MainWindow", "Manipulator", None))
        self.actionThursters.setText(_translate("MainWindow", "Thursters", None))
        self.actionVehicleData.setText(_translate("MainWindow", "Vehicle data", None))
        self.actionAboutUs.setText(_translate("MainWindow", "UiS Subsea", None))
        self.actionAboutVehicle.setText(_translate("MainWindow", "ROV v.1.0", None))
        self.actionOption.setText(_translate("MainWindow", "Options", None))
        self.actionConnect.setText(_translate("MainWindow", "Connect", None))
        self.actionDisconnect.setText(_translate("MainWindow", "Disconnect", None))

