import sys
from PyQt4 import QtGui, QtCore
sys.path.insert(1, '../Joystick')
import Joystick as js

##############################################################################
# Global variables:
# (Range: [-100, 100]% <--> [-30, 30])?
m1 = 0
m2 = 0
m3 = 0
m4 = 0
m5 = 0

##############################################################################
#
# Hent styrekontrollverdier og tilegn verdien til glob.vars (se over), som 
# igjen styrer prosessbarene i widgeten. 
# På sikt, hent verdier direkte fra manipulatormotorene.
#
# Må nok også lage en fordelingsfunksjon slik at max/min tilsvarer lengden på 
# baren.
#
# OBS! Etterhver, lag en metode i joystick.py som leser alle kontrollerverdier,
# som så kan hentes ut til de widgeter som måtte trenge dataene. (Kan ikke 
# åpne joysticken mer enn én gang!)
#
# Men enn sålenge gjør vi som her, og leser stikkeverdier individuelt :)
# ---> se thrusterwidget.py
#
##############################################################################

class ManipulatorWidget(QtGui.QWidget):

	def __init__(self):
		super(ManipulatorWidget, self).__init__()

		# Init. controller:
		self.controller = js.Joystick()
		self.controller.open_joystick(0)

		self.initUI()


	def initUI(self):
		# Draw widget window:
		self.setGeometry(0, 0, 400, 270)
		self.center()
		self.setWindowTitle('Manipulator status')
		#self.addGraphics()
		self.show()


	def addGraphics(self):
		self.image = QtGui.QLabel(self)
		self.image.setScaledContents(True)
		self.image.setGeometry(0, 0, 400, 300)
		manimg = QtGui.QPixmap('RESOURCES/manipulator.png')
		self.image.setPixmap(manimg)
	

	def paintEvent(self, e):
		qp = QtGui.QPainter()
		qp.begin(self)

		manimg = QtGui.QPixmap('RESOURCES/manipulator.png')
		qp.drawPixmap(self, 0, 0, 400, 300, manimg)
		#self.drawManipulatorFrame(qp)
		#self.drawProcessBars(qp)

		qp.end()

		#self.updateData()


	def drawManipulatorFrame(self, qp):
		manimg = QtGui.QPixmap('RESOURCES/manipulator.png')
		qp.drawPixmap(self, 0, 0, 400, 300, manimg)


	def drawProcessBars(self, qp):
		print("ierf")


	def updateData(self):
		global m1, m2, m3, m4, m5

		# Read controller values:
		m1 = int(self.controller.read_axis(1,1000))
		m2 = m1
		m3 = m1
		m4 = m1
		m5 = m1

		print(m1)

		# Re-draw process bars:
		#self.updateProcessBars()
		self.update() # Default function: calls QPaintEvent


	def updateProcessBars(self):
		# Init. glob.vars:
		global m1, m2, m3, m4, m5

		# Init. QPainter:
		qp = QtGui.QPainter()
		qp.begin(self)

		# Define colors:
		GREEN = QtGui.QColor(150,226,0)

		# Fill process bars:
		qp.setBrush(GREEN)

		# M1 - add description!
		qp.drawRect(0,0,10,10)


	def center(self):
		qr = self.frameGeometry()
		cp = QtGui.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

##############################################################################
# For testing:
def main():
	app = QtGui.QApplication(sys.argv)
	ex = ManipulatorWidget()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()








