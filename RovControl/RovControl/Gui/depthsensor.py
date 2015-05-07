'''
Henter data fra trykksensoren og fremstiller data som aktuell nå verdi
pluss evnt. tidshistorikk x antall målinger/tidsenheter tilbake i tid.
'''

import sys
from PyQt4 import QtGui, QtCore
# bruk joystick som tester for real-time plott fram til sensor kobles til :)


class DepthWidget(QtGui.QWidget):

	def __init__(self):
		super(DepthWidget, self).__init__()


		self.initUI()


	def initUI(self):
		# Draw widget window:
		w = 370
		h = 150
		self.setGeometry(100, 100, w, h)
		self.setMaximumSize (w, h)
		self.setMinimumSize(w, h)
		self.setWindowTitle('Depth Data')
		
		self.pressureLabel = QtGui.QLabel("0", self)
		self.pressureLabel.setGeometry(10,120,50,20)
		self.button = QtGui.QPushButton('User input', self)
		self.button.setGeometry(160, 120, 80, 20)
		self.button.clicked.connect(self.openDialog)

		self.show() #!!


	def openDialog(self):
		self.y, ok = QtGui.QInputDialog.getDouble(self, 'Input Dialog', 
			'Enter y value:')
        
		if ok:
			self.pressureLabel.setText(str(self.y))


	def getPressure(self):
		self.pressure = self.y
		return self.pressure



# For testing:
def main():
	app = QtGui.QApplication(sys.argv)
	ex = DepthWidget()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()