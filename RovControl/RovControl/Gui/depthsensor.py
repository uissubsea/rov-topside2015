'''
Henter data fra trykksensoren og fremstiller data som aktuell nå verdi
pluss evnt. tidshistorikk x antall målinger/tidsenheter tilbake i tid.
'''

import sys
from PyQt4 import QtGui, QtCore
from pyqtgraph import PlotWidget as pw

class DepthWidget(QtGui.QWidget):

	def __init__(self):
		super(DepthWidget, self).__init__()

		# init. fila som leser data fra ROV
		# self.readPressure = ...

		self.initUI()


	def initUI(self):
		# Draw widget window:
		w = 250
		h = 150
		self.setGeometry(100, 100, w, h)
		self.setMaximumSize (w, h)
		self.setMinimumSize(w, h)
		self.setWindowTitle('Depth Data')
		#self.show() #remove when adding to main window!

	def getPressure(self):
		# self.pressure = self.readPressure.getValue()
		self.pressure = 2.1
		return self.pressure



# For testing:
def main():
	app = QtGui.QApplication(sys.argv)
	ex = DepthWidget()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()