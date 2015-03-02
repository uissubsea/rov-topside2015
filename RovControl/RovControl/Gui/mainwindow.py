# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Thu Feb 26 10:02:39 2015
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
        self.actionExit_2 = QtGui.QAction(MainWindow)
        self.actionExit_2.setObjectName(_fromUtf8("actionExit_2"))
        self.actionCamera_1 = QtGui.QAction(MainWindow)
        self.actionCamera_1.setObjectName(_fromUtf8("actionCamera_1"))
        self.actionCamera_2 = QtGui.QAction(MainWindow)
        self.actionCamera_2.setObjectName(_fromUtf8("actionCamera_2"))
        self.actionOptions = QtGui.QAction(MainWindow)
        self.actionOptions.setObjectName(_fromUtf8("actionOptions"))
        self.actionStatus = QtGui.QAction(MainWindow)
        self.actionStatus.setObjectName(_fromUtf8("actionStatus"))
        self.menuFile.addAction(self.actionExit_2)
        self.menuView.addAction(self.actionCamera_1)
        self.menuView.addAction(self.actionCamera_2)
        self.menuView.addAction(self.actionStatus)
        self.menuSettings.addAction(self.actionOptions)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "RovControl v 0.1a", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuAbout.setTitle(_translate("MainWindow", "About", None))
        self.menuView.setTitle(_translate("MainWindow", "View", None))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings", None))
        self.actionExit_2.setText(_translate("MainWindow", "Exit", None))
        self.actionExit_2.setToolTip(_translate("MainWindow", "Exit the application", None))
        self.actionExit_2.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.actionCamera_1.setText(_translate("MainWindow", "Camera 1", None))
        self.actionCamera_2.setText(_translate("MainWindow", "Camera 2", None))
        self.actionOptions.setText(_translate("MainWindow", "Options", None))
        self.actionStatus.setText(_translate("MainWindow", "Status", None))

