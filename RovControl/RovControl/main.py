#!/usr/bin/python

import sys

sys.path.insert(1, "../RovControl")
#import joystick_old_version as js

from PyQt4 import QtGui, QtCore
from Gui import mainwindow, settingswindow, statuswindow, pod1, pod2, cntrconfig2
from Gui import testWindow, manipulatorwidget, thrusterwidget, depthsensor
from Gui import camerawindow, about
from RovNetwork import networkclient

##############################################################################
# Globale variable:

start_modus = "" 

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

##############################################################################

class MainWidget(QtGui.QMainWindow):
    
    def __init__(self):
        super(MainWidget, self).__init__()

        # Set up the user interface from Designer.
        self.ui = mainwindow.Ui_MainWindow()
        self.ui.setupUi(self)

       # Make some local modifications.

        # Connect menu buttons:
        #   --> on-top widgets:
        self.ui.actionOption.triggered.connect(self.open_options)
        self.ui.actionController.triggered.connect(self.open_controllerConfig)
        self.ui.actionUiS_Subsea.triggered.connect(self.open_aboutUiSSubsea)
        #self.ui.actionAboutROV.triggered.connect(self.open_aboutROV)
        #   --> integrated widgets:
        self.ui.actionCamera_1.triggered.connect(self.open_cam1)
        self.ui.actionCamera_2.triggered.connect(self.open_cam2)
        self.ui.actionCamera_3.triggered.connect(self.open_cam3)
        self.ui.actionStatus.triggered.connect(self.open_statusWindow)
        self.ui.actionPOD_1.triggered.connect(self.open_pod1)
        self.ui.actionPOD_2.triggered.connect(self.open_pod2)
        self.ui.actionManipulator.triggered.connect(self.open_manipulatorWidget)
        self.ui.actionThursters.triggered.connect(self.open_thrusterWidget)
        self.ui.actionDepth_sensor.triggered.connect(self.open_depthWidget)
        
        self.ui.actionExit.triggered.connect(self.exit)

        self.ui.actionConnect.triggered.connect(self.connect)
        self.ui.actionDisconnect.triggered.connect(self.disconnect)

        self.show()

        self.subwindow1 = QtGui.QMdiSubWindow()
        self.subwindow2 = QtGui.QMdiSubWindow()
        self.subwindow3 = QtGui.QMdiSubWindow()
        self.subwindow4 = QtGui.QMdiSubWindow()
        self.subwindow5 = QtGui.QMdiSubWindow()
        self.subwindow6 = QtGui.QMdiSubWindow()
        self.subwindow7 = QtGui.QMdiSubWindow()
        self.subwindow8 = QtGui.QMdiSubWindow()
        self.subwindow9 = QtGui.QMdiSubWindow()
        self.subwindow10 = QtGui.QMdiSubWindow()
        self.subwindow11 = QtGui.QMdiSubWindow()
        self.subwindow12 = QtGui.QMdiSubWindow()
        self.subwindow13 = QtGui.QMdiSubWindow()

        # Network Client Thread
        self.netClient = networkclient.NetworkClient()
        

    def open_logFile(self):
         # Create Q Text Stream for status window
        print("awdawawdaw")
        self.logFile = QtCore.QFile('status.log')
        try:
            self.logFile.open(QtCore.QIODevice.ReadOnly)
            self.stream = QtCore.QTextStream(self.logFile)
            self.ui.textEdit.setText(self.stream.readAll())
        except e:
            print(e)


    def open_options(self):
        self.optWindow = QtGui.QWidget()
        self.ui1 = optionwindow.Ui_OptionsWindow()
        self.ui1.setupUi(self.optWindow)
        self.subwindow1.setWidget(self.optWindow)
        self.optWindow.show()

    def open_controllerConfig(self):
        self.cnfigWindow = cntrconfig2.ConfigWindow()
        self.cnfigWindow.show()

    def open_aboutUiSSubsea(self):
        self.uissubseaWindow = about.UiSSubsea()
        self.uissubseaWindow.show()
    
    def open_aboutROV(self):
        self.rovWindow = about.Vehicle()
        self.rovWindow.show()

    def open_cam1(self):
        self.cam1Window = camerawindow.TestWindowCam1()
        self.subwindow5.setWidget(self.cam1Window)
        self.ui.mdiArea.addSubWindow(self.subwindow5)
        self.cam1Window.show()

    def open_cam2(self):
        self.cam2Window = camerawindow.TestWindowCam2()
        self.subwindow6.setWidget(self.cam2Window)
        self.ui.mdiArea.addSubWindow(self.subwindow6)
        self.cam2Window.show()

    def open_cam3(self):
        self.cam3Window = camerawindow.TestWindowCam3()
        self.subwindow7.setWidget(self.cam3Window)
        self.ui.mdiArea.addSubWindow(self.subwindow7)
        self.cam3Window.show()

    def open_statusWindow(self):
        self.statWindow = QtGui.QWidget()
        self.ui8 = statuswindow.Ui_StatusWindow()
        self.ui8.setupUi(self.statWindow)
        self.subwindow8.setWidget(self.statWindow)
        self.ui.mdiArea.addSubWindow(self.subwindow8)
        self.statWindow.show()
        self.open_logFile()

    def open_pod1(self):
        self.pod1Window = pod1.SubWindow()
        self.subwindow9.setWidget(self.pod1Window)
        self.ui.mdiArea.addSubWindow(self.subwindow9)
        self.pod1Window.show()

    def open_pod2(self):
        self.pod2Window = pod2.SubWindow()
        self.subwindow10.setWidget(self.pod2Window)
        self.ui.mdiArea.addSubWindow(self.subwindow10)
        self.pod2Window.show()

    def open_manipulatorWidget(self):
        self.maniWindow = manipulatorwidget.ManipulatorWidget()
        self.subwindow11.setWidget(self.maniWindow)
        self.ui.mdiArea.addSubWindow(self.subwindow11)
        self.maniWindow.show()   

    def open_thrusterWidget(self):
        self.thrWindow = thrusterwidget.ThrusterWidget()
        self.subwindow12.setWidget(self.thrWindow)
        # Add subwindow to mdiArea:
        self.ui.mdiArea.addSubWindow(self.subwindow12)
        self.thrWindow.show()

    def open_depthWidget(self):
        self.depthWindow = depthsensor.DepthWidget()
        self.subwindow13.setWidget(self.depthWindow)
        self.ui.mdiArea.addSubWindow(self.subwindow13)
        self.depthWindow.show()

    def connect(self):
        #Start Network Client
        self.netClient.start()
        #self.open_statusWindow()

    def disconnect(self):
        # Stop Network client
        self.netClient.disconnect()


    def exit(self):
        # Stop Network client
        self.netClient.disconnect()
        self.close()
        print("Stopped?")
        sys.exit()

##############################################################################


def main():
    app = QtGui.QApplication(sys.argv)
    #window = StartWindow()
    window = MainWidget()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

##############################################################################
