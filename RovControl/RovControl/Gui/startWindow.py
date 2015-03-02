

from PyQt4 import QtGui, QtCore
import sys, os
from Gui import testWindow
#import mainWindow
from Gui import mainwidget

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
            self.close()
            win = mainwidget.MainWidget()
            win.__init__()
         
        elif start_modus == "Test":
            self.close()
            win = testWindow.Test1()
            win.__init__()

        # If no match, show help option:
        else:
            print("Please choose a program option")
            

    # Reads combobox option chosen by user
    def onActivated(self, text):
        global start_modus
        start_modus = text

    


