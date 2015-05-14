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

		# Remove when connected to incomming signals:
		u = [1, 2, 3, 4, 5, 6, 7, 8]
		i = [10, 20, 30, 40, 50, 60, 70, 80]
		p = [0, 0, 0, 0, 0, 0, 0, 0]
		self.update(u, i, p, 8, 'OK')


	def addSensorData(self):
		self.sensorGB = QtGui.QGroupBox('Sensors', self)
		self.sensorGB.setGeometry(15, 10, 340, 65)

		self.tempLbl = QtGui.QLabel('Temp.:', self.sensorGB)
		self.tempLbl.setGeometry(14, 30, 100, 20)
		self.tempValue = QtGui.QLabel('', self.sensorGB)
		self.tempValue.setGeometry(120, 30, 80, 20)
		
		self.hydrLbl = QtGui.QLabel('Hydrostat:', self.sensorGB)
		self.hydrLbl.setGeometry(193, 30, 80, 20)
		self.hydrStatus = QtGui.QLabel('', self.sensorGB)
		self.hydrStatus.setGeometry(300, 30, 80, 20)


	# To access or edit voltage, current and/or power data:
	# call the array with index = mc no. - 1, for instance for
	# mc 1, call self.mcVoltage[0]
	def addMCData(self):
		self.mcGBXpos = [15, 195, 15, 195, 15, 195, 15, 195]
		self.mcGBYpos = [85, 85, 205, 205, 325, 325, 445, 445]
		self.mcGBw = 160
		self.mcGBh = 110

		self.mcGB = []
		self.voltageValue = []
		self.currentValue = []
		self.powerValue = []

		self.gb1 = QtGui.QGroupBox('', self)
		self.mcGB.append(self.gb1)
		self.gb2 = QtGui.QGroupBox('', self)
		self.mcGB.append(self.gb2)
		self.gb3 = QtGui.QGroupBox('', self)
		self.mcGB.append(self.gb3)
		self.gb4 = QtGui.QGroupBox('', self)
		self.mcGB.append(self.gb4)
		self.gb5 = QtGui.QGroupBox('', self)
		self.mcGB.append(self.gb5)
		self.gb6 = QtGui.QGroupBox('', self)
		self.mcGB.append(self.gb6)
		self.gb7 = QtGui.QGroupBox('', self)
		self.mcGB.append(self.gb7)
		self.gb8 = QtGui.QGroupBox('', self)
		self.mcGB.append(self.gb8)
		
		self.v1 = QtGui.QLabel('', self.mcGB[0])
		self.voltageValue.append(self.v1)
		self.v2 = QtGui.QLabel('', self.mcGB[1])
		self.voltageValue.append(self.v2)
		self.v3 = QtGui.QLabel('', self.mcGB[2])
		self.voltageValue.append(self.v3)
		self.v4 = QtGui.QLabel('', self.mcGB[3])
		self.voltageValue.append(self.v4)
		self.v5 = QtGui.QLabel('', self.mcGB[4])
		self.voltageValue.append(self.v5)
		self.v6 = QtGui.QLabel('', self.mcGB[5])
		self.voltageValue.append(self.v6)
		self.v7 = QtGui.QLabel('', self.mcGB[6])
		self.voltageValue.append(self.v7)
		self.v8 = QtGui.QLabel('', self.mcGB[7])
		self.voltageValue.append(self.v8)

		self.c1 = QtGui.QLabel('', self.mcGB[0])
		self.currentValue.append(self.c1)
		self.c2 = QtGui.QLabel('', self.mcGB[1])
		self.currentValue.append(self.c2)
		self.c3 = QtGui.QLabel('', self.mcGB[2])
		self.currentValue.append(self.c3)
		self.c4 = QtGui.QLabel('', self.mcGB[3])
		self.currentValue.append(self.c4)
		self.c5 = QtGui.QLabel('', self.mcGB[4])
		self.currentValue.append(self.c5)
		self.c6 = QtGui.QLabel('', self.mcGB[5])
		self.currentValue.append(self.c6)
		self.c7 = QtGui.QLabel('', self.mcGB[6])
		self.currentValue.append(self.c7)
		self.c8 = QtGui.QLabel('', self.mcGB[7])
		self.currentValue.append(self.c8)

		self.p1 = QtGui.QLabel('', self.mcGB[0])
		self.powerValue.append(self.p1)
		self.p2 = QtGui.QLabel('', self.mcGB[1])
		self.powerValue.append(self.p2)
		self.p3 = QtGui.QLabel('', self.mcGB[2])
		self.powerValue.append(self.p3)
		self.p4 = QtGui.QLabel('', self.mcGB[3])
		self.powerValue.append(self.p4)
		self.p5 = QtGui.QLabel('', self.mcGB[4])
		self.powerValue.append(self.p5)
		self.p6 = QtGui.QLabel('', self.mcGB[5])
		self.powerValue.append(self.p6)
		self.p7 = QtGui.QLabel('', self.mcGB[6])
		self.powerValue.append(self.p7)
		self.p8 = QtGui.QLabel('', self.mcGB[7])
		self.powerValue.append(self.p8)
		

		for i in range(8):
			self.mcGB[i].setTitle('MC' + str(i+1))
			self.mcGB[i].setGeometry(self.mcGBXpos[i], self.mcGBYpos[i], 
					self.mcGBw, self.mcGBh)

			self.voltageLbl = QtGui.QLabel('Voltage [V]:', self.mcGB[i])
			self.voltageLbl.setGeometry(14, 30, 100, 20)
			self.voltageValue[i].setGeometry(120, 30, 80, 20)

			self.currentLbl = QtGui.QLabel('Current [mA]:', self.mcGB[i])
			self.currentLbl.setGeometry(14, 55, 100, 20)
			self.currentValue[i].setGeometry(120, 55, 80, 20)

			self.powerLbl = QtGui.QLabel('Power [W]:', self.mcGB[i])
			self.powerLbl.setGeometry(14, 80, 100, 20)
			self.powerValue[i].setGeometry(120, 80, 80, 20)


	def update(self, voltage, current, power, temp, hydro):
		for i in range(8):
			self.voltageValue[i].setText(str(voltage[i]))
			self.currentValue[i].setText(str(current[i]))
			self.powerValue[i].setText(str(power[i]))
			self.tempValue.setText(str(temp) +  ' °C')
			self.hydrStatus.setText(hydro)

