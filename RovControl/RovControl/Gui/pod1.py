import sys
from PyQt4 import QtGui, QtCore

class SubWindow(QtGui.QWidget):
    def __init__(self):
        super(SubWindow,self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100,100,400,600) #or fullscreen
        self.setWindowTitle('POD 1')
        self.mainGrid = QtGui.QGridLayout(self)
        
