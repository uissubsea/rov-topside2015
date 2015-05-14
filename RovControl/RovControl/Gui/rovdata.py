'''
Henter data fra trykksensoren og fremstiller data som aktuell nå verdi
pluss evnt. tidshistorikk x antall målinger/tidsenheter tilbake i tid.
'''

import sys
from PyQt4 import QtGui, QtCore
# bruk joystick som tester for real-time plott fram til sensor kobles til :)


class RovData(QtGui.QWidget):

	def __init__(self):
		super(RovData, self).__init__()


		self.initUI()


	def initUI(self):
		# Draw widget window:
		self.w = 500
		self.h = 300
		self.setGeometry(100, 100, self.w, self.h)
		self.setFixedSize (self.w, self.h)
		self.setMaximumSize(self.w, self.h)
		self.setWindowTitle('Vehicle Data')

		self.font = QtGui.QFont()
		self.font.setBold(True)
		self.font.setPointSize(55)


		self.addDepthLogger()
		self.addData()

		self.receiveData([0, 0, 0, 0])
		self.update()

		self.show() 
		

	def addDepthLogger(self):
		self.depthFrame = QtGui.QGroupBox('', self)
		self.depthFrame.setGeometry(205, 10, 285, 285)

		self.currentDepth = QtGui.QLabel('', self.depthFrame)
		self.currentDepth.setFont(self.font)
		self.currentDepth.setAlignment(QtCore.Qt.AlignRight)
		self.currentDepth.setGeometry(0,20,270,70)

		# Add logging graph


	def addData(self):
		self.dataFrame = QtGui.QGroupBox('', self)
		self.dataFrame.setGeometry(10, 10, 185, 100)

		lbl = QtGui.QLabel('Place compass here!\nNot implemented yet...', self)
		lbl.setGeometry(25, 200, 200, 60)

		
		self.SOGLbl = QtGui.QLabel('SOG:', self.dataFrame)
		self.SOGLbl.setGeometry(14,15,100,20)
		self.currentSOG = QtGui.QLabel('', self.dataFrame)
		self.currentSOG.setGeometry(60,15,80,20)
		self.currentSOG.setAlignment(QtCore.Qt.AlignRight)

		self.STWLbl = QtGui.QLabel('STW:', self.dataFrame)
		self.STWLbl.setGeometry(14,40,100,20)
		self.currentSTW = QtGui.QLabel('', self.dataFrame)
		self.currentSTW.setGeometry(60,40,80,20)
		self.currentSTW.setAlignment(QtCore.Qt.AlignRight)

		self.headingLbl = QtGui.QLabel('Heading:', self.dataFrame)
		self.headingLbl.setGeometry(14,65,100,20)
		self.currentHeading = QtGui.QLabel('', self.dataFrame)
		self.currentHeading.setGeometry(60,65,80,20)
		self.currentHeading.setAlignment(QtCore.Qt.AlignRight)

		# Add Compass


	def receiveData(self, data):
		self.depth = str(data[0])
		self.heading = str(data[1]) + '°   '
		self.SOG = str(data[2]) + ' kn'
		self.STW = str(data[3]) + ' kn'


	def update(self):
		self.currentDepth.setText(self.depth + ' m')
		self.currentHeading.setText(self.heading)
		self.currentSOG.setText(self.SOG)
		self.currentSTW.setText(self.STW)


	def run(self):
		print('run')
		#mekk så widgeten oppdaterer seg!




# For testing:
def main():
	app = QtGui.QApplication(sys.argv)
	ex = RovData()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()