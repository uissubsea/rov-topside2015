from PyQt4 import QtGui, QtCore

class UiSSubsea(QtGui.QWidget):
	
	def __init__(self):
		super(UiSSubsea, self).__init__()
		self.initUI()

	def initUI(self):
		# Draw widget window:
		w = 550
		h = 450
		self.setGeometry(100, 100, w, h)
		self.setMaximumSize (w, h)
		self.setMinimumSize(w, h)
		self.setWindowTitle('UiS Subsea')


class Vehicle(QtGui.QWidget):
	
	def __init__(self):
		super(Vehicle, self).__init__()
		self.initUI()

	def initUI(self):
		# Draw widget window:
		w = 550
		h = 450
		self.setGeometry(100, 100, w, h)
		self.setMaximumSize (w, h)
		self.setMinimumSize(w, h)
		self.setWindowTitle('This Vehicle')