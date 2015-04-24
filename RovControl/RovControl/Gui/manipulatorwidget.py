'''
GUI-applikasjon som henter pådragsverdier fra alle motorer i manipulatorarmen og 
fremstiller det intuitivt for bruker. Implementert i hovedprogrammet som en 
subwidget i mdiArea.

Elisabeth - UiS Subsea 2015
'''

import sys
from PyQt4 import QtGui, QtCore
from Controller import controller
#sys.path.insert(1, '../Joystick')
#import joystick_old_version as js

##############################################################################
# Global variables:
'''# (Range: [-100, 100]% <--> [-30, 30])?

m1 = 0
m2 = 0
m3 = 0
m4 = 0
m5 = 0
'''

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
		#self.ctrl = controller.Controller()
		#self.axis_data = self.ctrl.ctrl_axisdata
		#self.button_data = self.ctrl.ctrl_buttondata

		# Init. m values:
		self.m1 = 0 
		self.m2 = 0
		self.m3 = 0
		self.m4 = 0
		self.m5 = 0

		# Init. UI:
		self.initUI()


	def initUI(self):
		# Draw widget window:
		self.setGeometry(0, 0, 400, 270)
		self.setMaximumSize (400, 270)
		self.setMinimumSize(400, 270)
		#self.center()
		self.setWindowTitle('Manipulator status')
		self.addGraphics()	
		self.addLabels()	
		#self.show()

	
	# paintEvent kalles automatisk med QWidget.update() !!! Jippiyay :D
	def paintEvent(self, e):
		qp = QtGui.QPainter()
		qp.begin(self)
		
		self.drawManipulator(qp)
		self.drawProcessBars(qp)

		qp.end()
		self.updateData()
	

	def addGraphics(self):
		# adds an image of the grip claw:
		self.image = QtGui.QLabel(self)
		self.image.setScaledContents(True)
		self.image.setGeometry(149, 25, 280, 200)
		claw = QtGui.QPixmap('Gui/RESOURCES/klo.png')
		self.image.setPixmap(claw)


	def addLabels(self):
		xpos = [22, 13, 73, 176, 222, 215, 278, 145, 327, 324]
		ypos = [159, 238, 45, 45, 70, 152, 170, 170, 155, 75]
		text = ['up', 'down', 'bend', 'stretch', 'tilt up', 'tilt down', 
					'rotate cw', 'rotate ccw', 'grip', 'open']
		
		for i in range (len(xpos)):
			self.label = QtGui.QLabel(self)
			self.label.setText(text[i])
			self.label.setGeometry(xpos[i], ypos[i], 70, 20)


	def updateData(self):
		#global m1, m2, m3, m4, m5
		'''
		self.m1 = self.axis_data[0]
		self.m2 = self.axis_data[1]
		self.m3 = self.axis_data[2]
		self.m4 = self.axis_data[3]
		self.m5 = self.axis_data[4]
		'''
		#print(self.m1)
		# Read controller values:
		#m1 = int(self.controller.read_axis(0,1000))
		#m2 = int(self.controller.read_axis(3,1000))
		#m3 = int(self.controller.read_axis(4,1000))
		#m4 = int(self.controller.read_axis(1,1000))
		#m5 = int(self.controller.read_axis(2,1000))

		# Re-draw process bars:
		self.updateProcessBars()
		self.update() # Default function: calls QPaintEvent


	def drawManipulator(self, qp):
		# Define colors:
		LIGHTBLUE = QtGui.QColor(100, 130, 130)
		GRAY = QtGui.QColor(100, 100, 100)
		YELLOW = QtGui.QColor(238, 194, 0)
		
		# Draw arm:
		qp.rotate(15)
		qp.setBrush(GRAY)
		qp.drawRoundRect(141, 38, 130, 40, 25, 90)
		qp.rotate(15)
		qp.setBrush(GRAY)
		qp.drawRoundRect(150, -5, 40, 170, 90, 20)
		qp.rotate(-15)
		qp.drawRoundRect(244, 38, 40, 40, 90, 90)
		qp.rotate(-15)


	def drawProcessBars(self, qp):
		# Define colors:
		GRAY = QtGui.QColor(190, 190, 190)
		
		qp.setBrush(GRAY)

		# Tilt arm:
		qp.drawRect(20, 180, 20, 60)
		# Bend arm:
		qp.drawRect(110, 45, 60, 20)
		# Rotate claw:
		qp.drawRect(212, 170, 60, 20)
		# Tilt claw:
		qp.drawRect(230, 93, 20, 60)
		# Open/close claw
		qp.drawRect(330, 96, 20, 60)


	def updateProcessBars(self):
		# Init. glob.vars:
		#global m1, m2, m3, m4, m5

		# Define colors:
		GREEN = QtGui.QColor(150,226,0)

		# Init. QPainter:
		qp = QtGui.QPainter()
		qp.begin(self)
		qp.setBrush(GREEN)

		# Tilt arm:
		qp.drawRect(20, 210, 20, self.m1) #m1: +-30
		# Bend arm:
		qp.drawRect(140, 45, self.m2, 20)
		# Rotate claw:
		qp.drawRect(242, 170, self.m3, 20)
		# Tilt claw:
		qp.drawRect(230, 123, 20, self.m4)
		# Open/close claw
		qp.drawRect(330, 126, 20, self.m5)
		
		qp.end()


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
