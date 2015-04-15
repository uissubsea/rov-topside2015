'''
GUI-applikasjon som henter pådragsverdier fra thrusterene og fremstiller det 
intuitivt for bruker. Implementert i hovedprogrammet som en subwidget i mdiArea.

Elisabeth - UiS Subsea 2015
'''

import sys
from PyQt4 import QtGui, QtCore
#sys.path.insert(1, '../Joystick')
#import joystick_old_version as js


##############################################################################
# TODO
# Hent styrekontrollverdier og tilegn verdien til glob.vars (se over), som 
# igjen styrer prosessbarene i widgeten. 
# På sikt, hent verdier direkte fra thrusterene.
#
# Må nok også lage en fordelingsfunksjon slik at max/min tilsvarer lengden på 
# baren.
#
# OBS! Etterhver, lag en metode i joystick.py som leser alle kontrollerverdier,
# som så kan hentes ut til de widgeter som måtte trenge dataene. (Kan ikke 
# åpne joysticken mer enn én gang!)
#
# Men enn sålenge gjør vi som her, og leser stikkeverdier individuelt :)
# ---> se manipulatorwidget.py
#
##############################################################################

class ThrusterWidget(QtGui.QWidget):

	def __init__(self):
		super(ThrusterWidget, self).__init__()

		# Init. controller:
		#self.controller = js.Controller()
		#self.controller.open_controller(0)
		
		# Init. th-values:
		self.th1 = 0
		self.th2 = 0
		self.th3 = 0
		self.th4 = 0
		self.th5 = 0
		self.th6 = 0
		self.th7 = 0
		self.th8 = 0

		# Init. user interface:
		self.initUI()


	def initUI(self):
		# Draw widget window:
		self.setGeometry(0, 0, 350, 400)
		self.setMaximumSize (350, 400)
		self.setMinimumSize(350, 400)
		#self.center()
		self.setWindowTitle('Thruster status')
		self.addPropellers()
		#self.show()


	# paintEvent kalles automatisk med QWidget.update() !!! Jippiyay :D
	def paintEvent(self, e):
		qp = QtGui.QPainter()
		qp.begin(self)

		self.drawFixedObjects(qp)
		qp.rotate(45) # Rotates coordinate syst. 45 deg (cw)
		self.drawFixedTiltedObjects(qp)
		#qp.rotate(-45) # Rot. back to default
		qp.end()

		self.updateData()


	def addPropellers(self):
		xpos = [40, 280, 40, 280, 90, 225, 90, 225]
		ypos = [40, 40, 330, 330, 110, 110, 255, 255]
		
		for i in range (8):
			self.prop = QtGui.QLabel(self)
			self.prop.setScaledContents(True)
			self.prop.setGeometry(xpos[i], ypos[i], 30, 30)
			propimg = QtGui.QPixmap('Gui/RESOURCES/propeller.png')
			self.prop.setPixmap(propimg)


	def updateData(self):
		
		# Read controller values:
		#self.th1 = self.controller.get_button_state(3)*30
		#self.th2 = self.controller.get_button_state(1)*30
		#self.th3 = self.controller.get_button_state(0)*30
		#self.th4 = self.controller.get_button_state(2)*30
		#self.th5 = self.controller.read_axis(0,1000)
		#self.th6 = self.controller.read_axis(1,1000)
		#self.th7 = self.controller.read_axis(3,1000)
		#self.th8 = self.controller.read_axis(4,1000)
		# OBS! Thrusterverdier skal hentes direkte fra motorpådrag!

		#th_array = [th1, th2, th3, th4, th5, th6, th7, th8]
		#print(th_array)

		# Re-draw process bars:
		self.updateProcessBars()
		self.updateTiltedProcessBars()
		self.update()

		
	def drawFixedObjects(self, qp):
		# Define colors:
		DARKGRAY = QtGui.QColor(90, 90, 90)
		LIGHTGRAY = QtGui.QColor(115, 115, 115)
		YELLOW = QtGui.QColor(238, 194, 0)

		# Draw frames:
		qp.setBrush(YELLOW)
		qp.drawRect(20,20,310,360)
		qp.setBrush(DARKGRAY)
		qp.drawRect(35,35,280,330)

		# Draw process bars:
		qp.setBrush(LIGHTGRAY)
		qp.drawRect(125, 95, 20, 60)
		qp.drawRect(198, 95, 20, 60)
		qp.drawRect(125, 240, 20, 60)
		qp.drawRect(198, 240, 20, 60)


	def drawFixedTiltedObjects(self, qp):
		# Define colors:
		LIGHTGRAY = QtGui.QColor(115, 115, 115)

		# Draw process bars:
		qp.setBrush(LIGHTGRAY)
		qp.drawRect(100, -30, 20, 60)
		qp.drawRect(410, 5, 20, 60)
		qp.drawRect(255, 162, 60, 20)
		qp.drawRect(218, -145, 60, 20)


	def updateProcessBars(self):
		# Init. glob.vars:
		global th5, th6, th7, th8

		# Define colors:
		GREEN = QtGui.QColor(150,226,0)

		# Init. QPainter:
		qp = QtGui.QPainter()
		qp.begin(self)
		qp.setBrush(GREEN)

		# Thruster no. 5
		qp.drawRect(125, 125, 20, self.th5) # siste: +/- 30
		# Thruster no. 6
		qp.drawRect(198, 125, 20, self.th6) # siste: +/- 30
		# Thruster no. 7
		qp.drawRect(125, 270, 20, self.th7) # siste: +/- 30
		# Thruster no. 8
		qp.drawRect(198, 270, 20, self.th8) # siste: +/- 30

		# Close QPainter:
		qp.end()


	def updateTiltedProcessBars(self):

		# Init. QPainter:
		qp = QtGui.QPainter()
		qp.begin(self)
		qp.rotate(45)

		# Define colors:
		GREEN = QtGui.QColor(150,226,0)

		# Fill process bars:
		qp.setBrush(GREEN)

		# Thruster no. 1
		qp.drawRect(100, 0, 20, self.th1) # siste: +/- 30
		# Thruster no. 2
		qp.drawRect(248, -145, self.th2, 20) # nest siste: +/- 30
		# Thruster no. 3
		qp.drawRect(285, 162, self.th3, 20) # nest siste: +/- 30
		# Thruster no. 4
		qp.drawRect(410, 35, 20, self.th4) # siste: +/- 30

		# Close QPainter:
		#qp.rotate(-45)
		qp.end()


	def center(self):
		qr = self.frameGeometry()
		cp = QtGui.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())



##############################################################################
# For testing:
#def main():
#	app = QtGui.QApplication(sys.argv)
#	ex = ThrusterWidget()
#	sys.exit(app.exec_())


#if __name__ == '__main__':
#	main()