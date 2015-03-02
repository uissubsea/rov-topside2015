
from PyQt4 import QtGui
from Gui import mainwindow
from Gui import settingswindow
from Gui import statuswindow

class MainWidget(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QWidget.__init__(self)

        # Set up the user interface from Designer.
        self.ui = mainwindow.Ui_MainWindow()
        self.ui.setupUi(self)

        # Make some local modifications.

        # Connect up the buttons.
        self.ui.actionOptions.triggered.connect(self.open_settingsWindow)
        self.ui.actionStatus.triggered.connect(self.open_statusWindow)

        self.show()


    def open_settingsWindow(self):
        self.cfgWindow = QtGui.QWidget()
        self.ui2 = settingswindow.Ui_SettingsWindow()
        self.ui2.setupUi(self.cfgWindow)
        self.cfgWindow.show()

    def open_statusWindow(self):
    	self.statWindow = QtGui.QWidget()
    	self.ui3 = statuswindow.Ui_StatusWindow()
    	self.ui3.setupUi(self.statWindow)
    	self.statWindow.show()