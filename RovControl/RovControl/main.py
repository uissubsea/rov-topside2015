#!/usr/bin/python

import sys

sys.path.insert(1, "../RovControl")
#import joystick_old_version as js

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from Gui import mainwindow, settingswindow, statuswindow, pod1, pod2, cntrconfig2
from Gui import testWindow, manipulatorwidget, thrusterwidget, rovdata
from Gui import camerawindow, about#, openMsgBox
from Gui import remote
from RovNetwork import networkclient, receiver
from Controller import controller

##############################################################################

class MainWidget(QMainWindow):
    
    sendMessage = pyqtSignal(QByteArray);

    def __init__(self):
        super(MainWidget, self).__init__()

        # Set up the user interface from Designer.
        self.ui = mainwindow.Ui_MainWindow()
        self.ui.setupUi(self)

        self.cameraProcess = QProcess(self)

        # Make some local modifications.

        # Connect menu buttons:
        #   --> on-top widgets:
        self.ui.actionOption.triggered.connect(self.open_options)
        self.ui.actionController.triggered.connect(self.open_controllerConfig)
        self.ui.actionAboutUs.triggered.connect(self.open_aboutUiSSubsea)
        self.ui.actionAboutVehicle.triggered.connect(self.open_aboutROV)
        #   --> integrated widgets:
        self.ui.actionCamera_1.triggered.connect(self.open_cam1)
        self.ui.actionCamera_2.triggered.connect(self.open_cam2)
        self.ui.actionCamera_3.triggered.connect(self.open_cam3)
        self.ui.actionStatus.triggered.connect(self.open_statusWindow)
        self.ui.actionPOD_1.triggered.connect(self.open_pod1)
        self.ui.actionPOD_2.triggered.connect(self.open_pod2)
        self.ui.actionManipulator.triggered.connect(self.open_manipulatorWidget)
        self.ui.actionThursters.triggered.connect(self.open_thrusterWidget)
        self.ui.actionVehicleData.triggered.connect(self.open_dataWidget)
        
        self.ui.actionExit.triggered.connect(self.exit)

        self.ui.actionConnect.triggered.connect(self.connect)
        self.ui.actionDisconnect.triggered.connect(self.disconnect)

        self.show()

        # Init. subwindows:
        self.subwindow1 = QMdiSubWindow()
        self.subwindow2 = QMdiSubWindow()
        self.subwindow3 = QMdiSubWindow()
        self.subwindow4 = QMdiSubWindow()
        self.subwindow5 = QMdiSubWindow()
        self.subwindow6 = QMdiSubWindow()
        self.subwindow7 = QMdiSubWindow()
        self.subwindow8 = QMdiSubWindow()
        self.subwindow9 = QMdiSubWindow()
        self.subwindow10 = QMdiSubWindow()
        self.subwindow11 = QMdiSubWindow()
        self.subwindow12 = QMdiSubWindow()
        self.subwindow13 = QMdiSubWindow()

        # Network Client Thread
        self.netClient = networkclient.NetworkClient()

        # Receiver Thread
        self.receiverClient = receiver.Receiver()

        #Connect signals
        self.netClient.updateStatus.connect(self.update_statusWindow)

        # Connect controller
        self.control = controller.Controller()
        self.control.start()

        self.control.gotData.connect(self.netClient.sendData);

        # Create Status window for later use
        self.statWindow = QWidget()
        self.ui8 = statuswindow.Ui_StatusWindow()
        self.ui8.setupUi(self.statWindow)
        self.subwindow8.setWidget(self.statWindow)
        self.ui.mdiArea.addSubWindow(self.subwindow8)
        self.ui8.textEdit.setReadOnly(True)
        self.open_logFile()

        self.remoteWindow = remote.Remote()
        self.remoteWindow.show()
        self.remoteSubWindow = QMdiSubWindow()
        self.remoteSubWindow.setWidget(self.remoteWindow)
        self.ui.mdiArea.addSubWindow(self.remoteSubWindow)
        self.remoteSubWindow.show()

        self.remoteWindow.ui.servoSlider.valueChanged.connect(self.control.setCameraServoValue)
        self.remoteWindow.ui.laserState.stateChanged.connect(self.control.setLaserState)
        self.remoteWindow.ui.lightState.stateChanged.connect(self.control.setLightState)
        self.remoteWindow.ui.lightSlider.valueChanged.connect(self.control.setLightFrequency)

    def update_statusWindow(self):
        try:
            self.ui8.textEdit.setText(self.stream.readAll())
        except AttributeError as e:
            print(e)

    def open_logFile(self):
         # Create Q Text Stream for status window
        self.logFile = QFile('Log/status.log')
        self.logFile.resize(0)
        try:
            self.logFile.open(QIODevice.ReadOnly)
            self.stream = QTextStream(self.logFile)
            self.ui8.textEdit.setText(self.stream.readAll())
        except AttributeError as e:
            print(e)


    def open_options(self):
        self.optWindow = QWidget()
        self.ui1 = optionwindow.Ui_OptionsWindow()
        self.ui1.setupUi(self.optWindow)
        #self.subwindow1.setWidget(self.optWindow)
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
        #self.cam1Window = camerawindow.TestWindowCam1()
        #self.subwindow5.setWidget(self.cam1Window)
        #self.ui.mdiArea.addSubWindow(self.subwindow5)
        #self.cam1Window.show()
        self.cameraProcess.start("kamera.exe")

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
        self.statWindow = QWidget()
        self.ui8 = statuswindow.Ui_StatusWindow()
        self.ui8.setupUi(self.statWindow)
        self.subwindow8.setWidget(self.statWindow)
        self.ui.mdiArea.addSubWindow(self.subwindow8)
        self.statWindow.show()
        self.ui8.textEdit.setReadOnly(True)

    def open_pod1(self):
        self.pod1Window = pod1.Pod1Status()
        self.subwindow9.setWidget(self.pod1Window)
        self.ui.mdiArea.addSubWindow(self.subwindow9)
        self.pod1Window.show()

        # Connect signal to update temp
        self.receiverClient.updateTemp.connect(self.pod1Window.updateTemp)

    def open_pod2(self):
        self.pod2Window = pod2.Pod2Status()
        self.subwindow10.setWidget(self.pod2Window)
        self.ui.mdiArea.addSubWindow(self.subwindow10)
        self.pod2Window.show()

         # Connect signal to update temp
        self.receiverClient.updateTemp.connect(self.pod2Window.updateTemp)

    def open_manipulatorWidget(self):
        self.maniWindow = manipulatorwidget.ManipulatorWidget()
        self.subwindow11.setWidget(self.maniWindow)
        self.ui.mdiArea.addSubWindow(self.subwindow11)
        self.maniWindow.show()  

        self.netClient.updateManipWidget.connect(self.maniWindow.updateData) 

    def open_thrusterWidget(self):
        self.thrWindow = thrusterwidget.ThrusterWidget()
        self.subwindow12.setWidget(self.thrWindow)
        # Add subwindow to mdiArea:
        self.ui.mdiArea.addSubWindow(self.subwindow12)
        self.thrWindow.show()


        self.netClient.updateThWidget.connect(self.thrWindow.updateData)

    def open_dataWidget(self):
        self.dataWindow = rovdata.RovData()
        self.subwindow13.setWidget(self.dataWindow)
        self.ui.mdiArea.addSubWindow(self.subwindow13)
        self.dataWindow.show()

    def connect(self):
        #Start Network Client
        if self.netClient == None:
            self.netClient = networkclient.NetworkClient()
        
        #self.receiverClient.start()
        self.netClient.connectToRov()
        self.open_statusWindow()

    def disconnect(self):
        # Stop Network client
        self.netClient.disconnectFromRov()

    def exit(self):
        # Stop Network client
        self.close()
        print("Stopped?")
        sys.exit()

##############################################################################


def main():
    app = QApplication(sys.argv)
    #window = StartWindow()
    window = MainWidget()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

##############################################################################
