from PyQt4 import QtGui
from PyQt4 import QtCore
from Gui import settingswindow
import sys

class MainWindow(QtGui.QMainWindow):
	
	def __init__(self):
		super(MainWindow, self).__init__()

		# This Function must be called befor initUI
		self.defineActions()

		self.initUI()


	def initUI(self):
		
		self.setWindowTitle("RaanControl V0.1a")
		self.setGeometry(300, 300, 800, 600) # posx, posy, hx, hy
		#self.center()
		self.show()

		self.mdiarea = QtGui.QMdiArea()
		self.mdiarea.setTabPosition(QtGui.QTabWidget.North)
		self.mdiarea.setTabShape(QtGui.QTabWidget.Rounded)
		self.mdiarea.show()
		self.setCentralWidget(self.mdiarea)

		self.statusBar().showMessage('Ready')

		self.initMenuBar()

	def initMenuBar(self):

		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(self.exitAction)
		fileMenu.addAction(self.settingsAction)
		
		fileMenu = menubar.addMenu('&About')
		

	def defineActions(self):
		# This function defines all Actions for our window
		self.exitAction = QtGui.QAction('&Exit', self)
		self.exitAction.setShortcut('Ctrl+Q')
		self.exitAction.setStatusTip('Exit application')
		self.exitAction.triggered.connect(QtGui.qApp.quit)

		# Action to go to settings screen
		self.settingsAction = QtGui.QAction('&Settings', self)
		self.settingsAction.setShortcut('Ctrl+P')
		self.settingsAction.setStatusTip('Open Settings window')
		self.settingsAction.triggered.connect(self.openSettings)

	def openSettings(self):

		self.cfgWindow = settingswindow.SettingsWindow()

