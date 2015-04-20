from PyQt4 import QtGui, QtCore

class UiSSubsea(QtGui.QWidget):
	
	def __init__(self):
		super(UiSSubsea, self).__init__()
		self.initUI()


	def initUI(self):
		# Draw widget window:
		self.w = 550
		self.h = 450
		self.center()
		self.setMaximumSize (self.w, self.h)
		self.setMinimumSize(self.w, self.h)
		self.setWindowTitle('UiS Subsea')
		self.addContents()
		self.show()


	def addContents(self):
		lbl = QtGui.QLabel('legg til litt fornuftig tekst om uis subsea', self)
		lbl.setGeometry(30,40,300,300)


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
		self.setWindowTitle('Add name of ROV')
		self.addContents()
		self.show()


	def addContents(self):
		text = QtGui.QLabel('Add some specs.. :)\n\nName:', self)
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

