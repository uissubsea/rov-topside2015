from PyQt4 import QtGui, QtCore

class UiSSubsea(QtGui.QWidget):
	
	def __init__(self):
		super(UiSSubsea, self).__init__()
		self.initUI()


	def initUI(self):
		# Draw widget window:
		self.w = 550
		self.h = 350
		self.center()
		self.setMaximumSize (self.w, self.h)
		self.setMinimumSize(self.w, self.h)
		self.setWindowTitle('UiS Subsea')
		self.addContents()


	def addContents(self):
		lbl = QtGui.QLabel('legg til litt fornuftig tekst om uis subsea', self)
		lbl.setGeometry(30,40,300,300)

		w = 300*0.7
		h = 252*0.7
		img = QtGui.QLabel(self)
		img.setScaledContents(True)
		img.setGeometry((self.w/2)-(w/2),20,w,h)
		logo = QtGui.QPixmap('Gui/RESOURCES/subsea_logo.png')
		img.setPixmap(logo)

		self.addButtons()


	def addButtons(self):
		self.okButton = QtGui.QPushButton('OK', self)
		self.okButton.setGeometry((self.w/2)-45, self.h-50, 90, 30)
		self.okButton.clicked.connect(self.closeWindow)


	def closeWindow(self):
		self.close()


	def center(self):
		qr = self.frameGeometry()
		cp = QtGui.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())





class Vehicle(QtGui.QWidget):
	
	def __init__(self):
		super(Vehicle, self).__init__()
		self.initUI()


	def initUI(self):
		# Draw widget window:
		self.w = 550
		self.h = 200
		self.center()
		self.setMaximumSize (self.w, self.h)
		self.setMinimumSize(self.w, self.h)
		self.setWindowTitle('Holy Diver')
		self.addContents()


	def addContents(self):
		text = QtGui.QLabel('Name: not set\nSoftware version: 1.0', self)
		text.setGeometry(20,40,200,50)

		self.addButtons()


	def addButtons(self):
		self.okButton = QtGui.QPushButton('OK', self)
		self.okButton.setGeometry((self.w/2)-45, self.h-50, 90, 30)
		self.okButton.clicked.connect(self.closeWindow)


	def closeWindow(self):
		self.close()


	def center(self):
		qr = self.frameGeometry()
		cp = QtGui.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

