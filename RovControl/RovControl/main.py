#!/usr/bin/python

import sys

sys.path.insert(1, 'Joystick')
#import joystick_old_version as js

from PyQt4 import QtGui, QtCore
from Gui import mainwindow, settingswindow, statuswindow, pod2, controller_config
from Gui import testWindow, manipulatorwidget, thrusterwidget


##############################################################################
# Globale variable:

start_modus = "" 

##############################################################################

class StartWindow(QtGui.QMainWindow):
    
    def __init__(self):
        super(StartWindow, self).__init__()
        self.initUI()
        

    def initUI(self):      

        # Quit button
        qbtn = QtGui.QPushButton('Quit', self)
        qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        qbtn.move(40, 350)

        # Start button
        sbtn = QtGui.QPushButton('Start', self)
        sbtn.clicked.connect(self.startButtonHandler)
        sbtn.move(500, 350)

        # Combobox w/label
        self.lbl = QtGui.QLabel("Select statup mode:", self)
        self.lbl.setGeometry(200,270,150,15)
        combo = QtGui.QComboBox(self)
        combo.addItem("")
        combo.addItem("Normal")
        combo.addItem("Test")
        # NB!!! Must mach conditions in method startButtonHandler()!
        combo.setGeometry(194,290,252,28)
        combo.activated[str].connect(self.onActivated)

        # Image
        self.img = QtGui.QLabel(self)
        self.img.setScaledContents(True);
        self.img.setGeometry(194,40,252,210) #xpos,ypos,w,h
        
        pxmp = QtGui.QPixmap('Gui/RESOURCES/subsea_logo.png')
        self.img.setPixmap(pxmp) 

        # Window settings
        self.resize(640,400)
        self.center()
        self.setWindowTitle('UiS Subsea - startup')
        self.setWindowIcon(QtGui.QIcon('Gui/RESOURCES/subsea_logo.png'))
        self.show()
     

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    

    # Closes startup window, opens program window
    def startButtonHandler(self):

        # reads global variable start_modus, and initiates next window
        if start_modus == "Normal":
            self.win = MainWidget()
            self.hide()
            self.win.show()
         
        elif start_modus == "Test":
            self.close()
            self.win = testWindow.Test1()
            self.win.__init__()

        # If no match, show help option:
        else:
            print("Please choose a program option")
            

    # Reads combobox option chosen by user
    def onActivated(self, text):
        global start_modus
        start_modus = text

class MainWidget(QtGui.QMainWindow):
    
    def __init__(self):
        super(MainWidget, self).__init__()

        # Set up the user interface from Designer.
        self.ui = mainwindow.Ui_MainWindow()
        self.ui.setupUi(self)

       # Make some local modifications.

        # Connecting buttons:
        #   --> on-top widgets:
        self.ui.actionOptions.triggered.connect(self.open_options)
        self.ui.actionController.triggered.connect(self.open_controllerConfig)
        #   --> integrated widgets:
        self.ui.actionStatus.triggered.connect(self.open_statusWindow)
        self.ui.actionPOD_2.triggered.connect(self.open_pod2)
        self.ui.actionThursters.triggered.connect(self.open_thrusterWidget)
        self.ui.actionManipulator.triggered.connect(self.open_manipulatorWidget)
        
        self.ui.actionExit.triggered.connect(self.exit)

        self.show()

        self.subwindow1 = QtGui.QMdiSubWindow()
        self.subwindow2 = QtGui.QMdiSubWindow()
        self.subwindow3 = QtGui.QMdiSubWindow()
        self.subwindow4 = QtGui.QMdiSubWindow()
        self.subwindow5 = QtGui.QMdiSubWindow()
        self.subwindow6 = QtGui.QMdiSubWindow()

        

    def open_options(self):
        self.optWindow = QtGui.QWidget()
        self.ui1 = optionwindow.Ui_OptionsWindow()
        self.ui1.setupUi(self.optWindow)
        self.subwindow1.setWidget(self.optWindow)
        self.optWindow.show()

    def open_statusWindow(self):
        self.statWindow = QtGui.QWidget()
        self.ui2 = statuswindow.Ui_StatusWindow()
        self.ui2.setupUi(self.statWindow)
        self.subwindow2.setWidget(self.statWindow)
        self.ui.mdiArea.addSubWindow(self.subwindow2)
        self.statWindow.show()

    def open_pod2(self):
        self.pod2Window = pod2.SubWindow()
        self.subwindow3.setWidget(self.pod2Window)
        self.ui.mdiArea.addSubWindow(self.subwindow3)
        self.pod2Window.show()

    def open_controllerConfig(self):
        self.cntrConfigWindow = QtGui.QWidget()
        self.ui4 = controller_config.Ui_controller_config()
        self.ui4.setupUi(self.cntrConfigWindow)
        self.subwindow4.setWidget(self.cntrConfigWindow)
        #self.ui.mdiArea.addSubWindow(self.subwindow4)
        self.cntrConfigWindow.show()

    def open_thrusterWidget(self):
        self.thrWindow = thrusterwidget.ThrusterWidget()
        self.subwindow5.setWidget(self.thrWindow)
        # Add subwindow to mdiArea:
        self.ui.mdiArea.addSubWindow(self.subwindow5)
        self.thrWindow.show()

    def open_manipulatorWidget(self):
        self.maniWindow = manipulatorwidget.ManipulatorWidget()
        self.subwindow6.setWidget(self.maniWindow)
        self.ui.mdiArea.addSubWindow(self.subwindow6)
        self.maniWindow.show()

    def exit(self):
        self.close()


def main():
    app = QtGui.QApplication(sys.argv)
    window = StartWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()