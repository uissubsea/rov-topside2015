from PyQt4 import QtGui, QtCore
from Joystick import Joystick

class JoystickTester(QtGui.QWidget):

	def __init__(self):
		super(JoystickTester, self).__init__()

		self.initUI()

	def initUI(self):

		self.setGeometry(300, 300, 500, 500)
		self.setWindowTitle('Joystick Tester')
		self.show()
		self.painter = QtGui.QPainter()

		self.thread = testThread(self.painter)
		self.painter.begin(self)
		self.thread.start()

	#def paintEvent(self, e):
#
	#	qp = QtGui.QPainter()
	#	qp.begin(self)
	#	self.drawRectangles(qp)
	#	qp.end()

class testThread(QtCore.QThread):
	def __init__(self, painter):
		QtCore.QThread.__init__(self)
		self.joystick = Joystick.Joystick()
		self.joystick.open_joystick(0)
		self.painter = painter

	def run(self):
		run = True
		while run:
			
			x = self.joystick.read_axis(0, 100)
			y = self.joystick.read_axis(1, 100)
			self.drawRectangles(x, y)
		
		self.painter.end()





	def drawRectangles(self, x, y):

		color = QtGui.QColor(0, 0, 0)
		color.setNamedColor('#d4d4d4')
		self.painter.setPen(color)

		self.painter.setBrush(QtGui.QColor(200, 0, 0))
		self.painter.drawRect(x, y, 90, 60)


