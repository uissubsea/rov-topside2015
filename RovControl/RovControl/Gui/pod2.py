import sys
from PyQt4 import QtGui, QtCore

class Pod2Status(QtGui.QWidget):

	def __init__(self):
		super(Pod2Status, self).__init__()
		self.initUI()

	def initUI(self):
		self.setFixedSize(370, 570)
		self.setWindowTitle('POD 2 - Thrust. MCs')
		self.mainGrid = QtGui.QGridLayout(self)

		self.addSensorData()
		self.addMCData()


	def addSensorData(self):
		self.sensorGB = QtGui.QGroupBox('Sensors', self)
		self.sensorGB.setGeometry(15, 10, 340, 65)

		self.tempLbl = QtGui.QLabel('Temp. [°C]:', self.sensorGB)
		self.tempLbl.setGeometry(14, 30, 100, 20)
		self.tempValue = QtGui.QLabel('__', self.sensorGB)
		self.tempValue.setGeometry(120, 30, 80, 20)
		
		self.hydrLbl = QtGui.QLabel('Hydrostat:', self.sensorGB)
		self.hydrLbl.setGeometry(193, 30, 80, 20)
		self.hydrStatus = QtGui.QLabel('OK', self.sensorGB)
		self.hydrStatus.setGeometry(300, 30, 80, 20)


	# To access or edit voltage, current and/or power data:
	# call the array with index = mc no. - 1, for instance for
	# mc 1, call self.mcVoltage[0]
	def addMCData(self):
		self.mcVoltage = []
		self.mcCurrent = []
		self.mcPower = []

		self.mcGBXpos = [15, 195, 15, 195, 15, 195, 15, 195]
		self.mcGBYpos = [85, 85, 205, 205, 325, 325, 445, 445]
		self.mcGBw = 160
		self.mcGBh = 110

		for i in range(8):
			self.mcGB = QtGui.QGroupBox(self)
			self.mcGB.setTitle('MC' + str(i+1))
			self.mcGB.setGeometry(self.mcGBXpos[i], self.mcGBYpos[i], 
					self.mcGBw, self.mcGBh)

			self.voltageLbl = QtGui.QLabel('Voltage [V]:', self.mcGB)
			self.voltageLbl.setGeometry(14, 30, 100, 20)
			self.voltageValue = QtGui.QLabel('__', self.mcGB)
			self.voltageValue.setGeometry(120, 30, 80, 20)
			self.mcVoltage.append(self.voltageValue)

			self.currentLbl = QtGui.QLabel('Current [mA]:', self.mcGB)
			self.currentLbl.setGeometry(14, 55, 100, 20)
			self.currentValue = QtGui.QLabel('__', self.mcGB)
			self.currentValue.setGeometry(120, 55, 80, 20)
			self.mcCurrent.append(self.currentValue)

			self.powerLbl = QtGui.QLabel('Power [W]:', self.mcGB)
			self.powerLbl.setGeometry(14, 80, 100, 20)
			self.powerValue = QtGui.QLabel('__', self.mcGB)
			self.powerValue.setGeometry(120, 80, 80, 20)
			self.mcPower.append(self.powerValue)

	def updateTemp(self, string):
		self.tempValue.setText(string)
