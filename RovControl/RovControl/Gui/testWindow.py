
import sys
from PyQt4 import QtGui, QtCore


class Test1(QtGui.QMainWindow):

    def __init__(self):
        super(Test1, self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(1280,800)
        self.center()
        self.setWindowTitle('test modus')
        self.statusBar().showMessage('Ready')
        
        self.initMenubar()
        
        self.show()


    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def initMenubar(self):
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        fileMenu.addAction('Preferences')
        fileMenu.addAction('Save test results')
        fileMenu.addAction('Save test results As...')
        fileMenu.addAction('Open previous results')
        fileMenu.addAction('Close Raan test mode') # OBS! Virker som end, exit++ 
                                                  # er beskytta navn; funker IKKE!
                                                  # Fjerner File fra menylinja...
        settingsMenu = menubar.addMenu('Settings')
        viewMenu = menubar.addMenu('View')
        aboutMenu = menubar.addMenu('About')
        aboutMenu.addAction('Raan V0.1a')
        

    def exitAction(self):
        exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)


# For testing:
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Test1()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
