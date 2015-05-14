'''
GUI-applikasjon som henter pådragsverdier fra thrusterene og fremstiller det 
intuitivt for bruker. Implementert i hovedprogrammet som en subwidget i mdiArea.

Elisabeth - UiS Subsea 2015
'''

import sys
import re
import math
from PyQt4 import QtGui, QtCore

# Define colors:
GREEN = QtGui.QColor(150,226,0)
DARKGRAY = QtGui.QColor(90, 90, 90)
LIGHTGRAY = QtGui.QColor(115, 115, 115)
YELLOW = QtGui.QColor(238, 194, 0)

class ThrusterWidget(QtGui.QWidget):


	def __init__(self):
		super(ThrusterWidget, self).__init__()
		
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
		self.updateProcessBars(qp)
		qp.rotate(45) # Rotates coordinate syst. 45 deg (cw)
		self.drawFixedTiltedObjects(qp)
		self.updateTiltedProcessBars(qp)
		qp.rotate(-45) # Rot. back to default
		qp.end()


	def addPropellers(self):
		xpos = [40, 280, 40, 280, 90, 225, 90, 225]
		ypos = [40, 40, 330, 330, 110, 110, 255, 255]
		
		for i in range (8):
			self.prop = QtGui.QLabel(self)
			self.prop.setScaledContents(True)
			self.prop.setGeometry(xpos[i], ypos[i], 30, 30)
			propimg = QtGui.QPixmap('Gui/RESOURCES/propeller.png')
			self.prop.setPixmap(propimg)


	def updateData(self, string):
		
		self.thData = re.findall(r'-?\d+', string)

		self.x = int(int(self.thData[0])*30/1000)
		self.y = int(int(self.thData[1])*30/1000)
		self.z = int(int(self.thData[2])*30/1000)
		self.rot = int(int(self.thData[3])*30/1000)

		self.r = math.sqrt(abs(pow(self.x, 2)) + abs(pow(self.y, 2)))
		
		self.theta = math.atan2(self.x, self.y)

		self.scale = 1;
		# Read controller values:
		self.th1 = int(self.r * math.cos(math.pi/4 - self.theta) * self.scale)
		self.th2 = int(self.r * math.cos(math.pi/4 - self.theta) * self.scale)
		self.th3 = self.th1 * -1
		self.th4 = self.th2 * -1
		self.th5 = int(self.thData[2])
		self.th6 = int(self.thData[2])
		self.th7 = int(self.thData[2])
		self.th8 = int(self.thData[2])
		# OBS! Thrusterverdier skal hentes direkte fra motorpådrag!

		# Re-draw process bars:
		self.update()
		
	def drawFixedObjects(self, qp):


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


	def updateProcessBars(self, qp):

		qp.setBrush(GREEN)

		# Thruster no. 5
		qp.drawRect(125, 125, 20, self.th5) # siste: +/- 30
		# Thruster no. 6
		qp.drawRect(198, 125, 20, self.th6) # siste: +/- 30
		# Thruster no. 7
		qp.drawRect(125, 270, 20, self.th7) # siste: +/- 30
		# Thruster no. 8
		qp.drawRect(198, 270, 20, self.th8) # siste: +/- 30


	def updateTiltedProcessBars(self, qp):

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