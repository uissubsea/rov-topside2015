import sys
from PyQt4 import QtGui, QtCore

class SubWindow(QtGui.QWidget):

	def __init__(self):
		super(SubWindow,self).__init__()
		self.initUI()

	def initUI(self):
		self.setGeometry(100,100,400,600) #or fullscreen
		self.setWindowTitle('POD 2')
		self.mainGrid = QtGui.QGridLayout(self)
       	
	
		#Sensordata pod2
		self.pod2_sensordata_groupBox = QtGui.QGroupBox(self)
		self.pod2_sensordata_groupBox.setTitle('Sensors')
		self.mainGrid.addWidget(self.pod2_sensordata_groupBox,0,0,1,2)
		#self.pod2_sensordata_groupBox.setMinimumSize(QtCore.QSize(0, 60))
		#self.pod2_sensordata_groupBox.setMaximumSize(QtCore.QSize(200, 60))
		
		self.pod2_temp_label = QtGui.QLabel(self.pod2_sensordata_groupBox)
		self.pod2_temp_label.setText('Temperatur [°C]')
		self.pod2_temp = QtGui.QLCDNumber(self.pod2_sensordata_groupBox)
		self.pod2_hydro_label = QtGui.QLabel(self.pod2_sensordata_groupBox)
		self.pod2_hydro_label.setText('Hydrostat failure')
		# varsellampe

		self.sensorGrid = QtGui.QGridLayout(self.pod2_sensordata_groupBox)
		self.sensorGrid.addWidget(self.pod2_temp_label,0,0,1,1)
		self.sensorGrid.addWidget(self.pod2_temp,0,1,1,1)
		self.sensorGrid.addWidget(self.pod2_hydro_label,0,2,1,1)
		#varsellampe


		#mc1
		self.mc1_groupBox = QtGui.QGroupBox(self)
		self.mc1_groupBox.setTitle('MC 1')
		self.mainGrid.addWidget(self.mc1_groupBox, 1,0,1,1)

		self.mc1_voltage_label = QtGui.QLabel(self.mc1_groupBox)
		self.mc1_voltage_label.setText('Voltage [V]')
		self.mc1_current_label = QtGui.QLabel(self.mc1_groupBox)
		self.mc1_current_label.setText('Current [mA]')
		self.mc1_power_label = QtGui.QLabel(self.mc1_groupBox)
		self.mc1_power_label.setText('Power [W]')

		self.mc1_voltage = QtGui.QLCDNumber(self.mc1_groupBox)
		self.mc1_current = QtGui.QLCDNumber(self.mc1_groupBox)
		self.mc1_power = QtGui.QLCDNumber(self.mc1_groupBox)
		
		self.mc1_grid = QtGui.QGridLayout(self.mc1_groupBox)
		self.mc1_grid.addWidget(self.mc1_voltage_label, 0,0,1,1)
		self.mc1_grid.addWidget(self.mc1_voltage, 0,1,1,1)
		self.mc1_grid.addWidget(self.mc1_current_label, 1,0,1,1)
		self.mc1_grid.addWidget(self.mc1_current, 1,1,1,1)
		self.mc1_grid.addWidget(self.mc1_power_label, 2,0,1,1)
		self.mc1_grid.addWidget(self.mc1_power, 2,1,1,1)

		#mc2
		self.mc2_groupBox = QtGui.QGroupBox(self)
		self.mc2_groupBox.setTitle('MC 2')
		self.mainGrid.addWidget(self.mc2_groupBox, 1,1,1,1)

		self.mc2_voltage_label = QtGui.QLabel(self.mc1_groupBox)
		self.mc2_voltage_label.setText('Voltage [V]')
		self.mc2_current_label = QtGui.QLabel(self.mc1_groupBox)
		self.mc2_current_label.setText('Current [mA]')
		self.mc2_power_label = QtGui.QLabel(self.mc1_groupBox)
		self.mc2_power_label.setText('Power [W]')

		self.mc2_voltage = QtGui.QLCDNumber(self.mc2_groupBox)
		self.mc2_current = QtGui.QLCDNumber(self.mc2_groupBox)
		self.mc2_power = QtGui.QLCDNumber(self.mc2_groupBox)
		
		self.mc2_grid = QtGui.QGridLayout(self.mc2_groupBox)
		self.mc2_grid.addWidget(self.mc2_voltage_label, 0,0,1,1)
		self.mc2_grid.addWidget(self.mc2_voltage, 0,1,1,1)
		self.mc2_grid.addWidget(self.mc2_current_label, 1,0,1,1)
		self.mc2_grid.addWidget(self.mc2_current, 1,1,1,1)
		self.mc2_grid.addWidget(self.mc2_power_label, 2,0,1,1)
		self.mc2_grid.addWidget(self.mc2_power, 2,1,1,1)

		#mc3
		self.mc3_groupBox = QtGui.QGroupBox(self)
		self.mc3_groupBox.setTitle('MC 3')
		self.mainGrid.addWidget(self.mc3_groupBox, 2,0,1,1)

		self.mc3_voltage_label = QtGui.QLabel(self.mc3_groupBox)
		self.mc3_voltage_label.setText('Voltage [V]')
		self.mc3_current_label = QtGui.QLabel(self.mc3_groupBox)
		self.mc3_current_label.setText('Current [mA]')
		self.mc3_power_label = QtGui.QLabel(self.mc3_groupBox)
		self.mc3_power_label.setText('Power [W]')

		self.mc3_voltage = QtGui.QLCDNumber(self.mc3_groupBox)
		self.mc3_current = QtGui.QLCDNumber(self.mc3_groupBox)
		self.mc3_power = QtGui.QLCDNumber(self.mc3_groupBox)
		
		self.mc3_grid = QtGui.QGridLayout(self.mc3_groupBox)
		self.mc3_grid.addWidget(self.mc3_voltage_label, 0,0,1,1)
		self.mc3_grid.addWidget(self.mc3_voltage, 0,1,1,1)
		self.mc3_grid.addWidget(self.mc3_current_label, 1,0,1,1)
		self.mc3_grid.addWidget(self.mc3_current, 1,1,1,1)
		self.mc3_grid.addWidget(self.mc3_power_label, 2,0,1,1)
		self.mc3_grid.addWidget(self.mc3_power, 2,1,1,1)

		#mc4
		self.mc4_groupBox = QtGui.QGroupBox(self)
		self.mc4_groupBox.setTitle('MC 4')
		self.mainGrid.addWidget(self.mc4_groupBox, 2,1,1,1)

		self.mc4_voltage_label = QtGui.QLabel(self.mc4_groupBox)
		self.mc4_voltage_label.setText('Voltage [V]')
		self.mc4_current_label = QtGui.QLabel(self.mc4_groupBox)
		self.mc4_current_label.setText('Current [mA]')
		self.mc4_power_label = QtGui.QLabel(self.mc4_groupBox)
		self.mc4_power_label.setText('Power [W]')

		self.mc4_voltage = QtGui.QLCDNumber(self.mc4_groupBox)
		self.mc4_current = QtGui.QLCDNumber(self.mc4_groupBox)
		self.mc4_power = QtGui.QLCDNumber(self.mc4_groupBox)
		
		self.mc4_grid = QtGui.QGridLayout(self.mc4_groupBox)
		self.mc4_grid.addWidget(self.mc4_voltage_label, 0,0,1,1)
		self.mc4_grid.addWidget(self.mc4_voltage, 0,1,1,1)
		self.mc4_grid.addWidget(self.mc4_current_label, 1,0,1,1)
		self.mc4_grid.addWidget(self.mc4_current, 1,1,1,1)
		self.mc4_grid.addWidget(self.mc4_power_label, 2,0,1,1)
		self.mc4_grid.addWidget(self.mc4_power, 2,1,1,1)

		#mc5
		self.mc5_groupBox = QtGui.QGroupBox(self)
		self.mc5_groupBox.setTitle('MC 5')
		self.mainGrid.addWidget(self.mc5_groupBox, 3,0,1,1)

		self.mc5_voltage_label = QtGui.QLabel(self.mc5_groupBox)
		self.mc5_voltage_label.setText('Voltage [V]')
		self.mc5_current_label = QtGui.QLabel(self.mc5_groupBox)
		self.mc5_current_label.setText('Current [mA]')
		self.mc5_power_label = QtGui.QLabel(self.mc5_groupBox)
		self.mc5_power_label.setText('Power [W]')

		self.mc5_voltage = QtGui.QLCDNumber(self.mc5_groupBox)
		self.mc5_current = QtGui.QLCDNumber(self.mc5_groupBox)
		self.mc5_power = QtGui.QLCDNumber(self.mc5_groupBox)
		
		self.mc5_grid = QtGui.QGridLayout(self.mc5_groupBox)
		self.mc5_grid.addWidget(self.mc5_voltage_label, 0,0,1,1)
		self.mc5_grid.addWidget(self.mc5_voltage, 0,1,1,1)
		self.mc5_grid.addWidget(self.mc5_current_label, 1,0,1,1)
		self.mc5_grid.addWidget(self.mc5_current, 1,1,1,1)
		self.mc5_grid.addWidget(self.mc5_power_label, 2,0,1,1)
		self.mc5_grid.addWidget(self.mc5_power, 2,1,1,1)

		#mc6
		self.mc6_groupBox = QtGui.QGroupBox(self)
		self.mc6_groupBox.setTitle('MC 6')
		self.mainGrid.addWidget(self.mc6_groupBox, 3,1,1,1)

		self.mc6_voltage_label = QtGui.QLabel(self.mc6_groupBox)
		self.mc6_voltage_label.setText('Voltage [V]')
		self.mc6_current_label = QtGui.QLabel(self.mc6_groupBox)
		self.mc6_current_label.setText('Current [mA]')
		self.mc6_power_label = QtGui.QLabel(self.mc6_groupBox)
		self.mc6_power_label.setText('Power [W]')

		self.mc6_voltage = QtGui.QLCDNumber(self.mc6_groupBox)
		self.mc6_current = QtGui.QLCDNumber(self.mc6_groupBox)
		self.mc6_power = QtGui.QLCDNumber(self.mc6_groupBox)
		
		self.mc6_grid = QtGui.QGridLayout(self.mc6_groupBox)
		self.mc6_grid.addWidget(self.mc6_voltage_label, 0,0,1,1)
		self.mc6_grid.addWidget(self.mc6_voltage, 0,1,1,1)
		self.mc6_grid.addWidget(self.mc6_current_label, 1,0,1,1)
		self.mc6_grid.addWidget(self.mc6_current, 1,1,1,1)
		self.mc6_grid.addWidget(self.mc6_power_label, 2,0,1,1)
		self.mc6_grid.addWidget(self.mc6_power, 2,1,1,1)

		#mc7
		self.mc7_groupBox = QtGui.QGroupBox(self)
		self.mc7_groupBox.setTitle('MC 7')
		self.mainGrid.addWidget(self.mc7_groupBox, 4,0,1,1)

		self.mc7_voltage_label = QtGui.QLabel(self.mc7_groupBox)
		self.mc7_voltage_label.setText('Voltage [V]')
		self.mc7_current_label = QtGui.QLabel(self.mc7_groupBox)
		self.mc7_current_label.setText('Current [mA]')
		self.mc7_power_label = QtGui.QLabel(self.mc7_groupBox)
		self.mc7_power_label.setText('Power [W]')

		self.mc7_voltage = QtGui.QLCDNumber(self.mc7_groupBox)
		self.mc7_current = QtGui.QLCDNumber(self.mc7_groupBox)
		self.mc7_power = QtGui.QLCDNumber(self.mc7_groupBox)
		
		self.mc7_grid = QtGui.QGridLayout(self.mc7_groupBox)
		self.mc7_grid.addWidget(self.mc7_voltage_label, 0,0,1,1)
		self.mc7_grid.addWidget(self.mc7_voltage, 0,1,1,1)
		self.mc7_grid.addWidget(self.mc7_current_label, 1,0,1,1)
		self.mc7_grid.addWidget(self.mc7_current, 1,1,1,1)
		self.mc7_grid.addWidget(self.mc7_power_label, 2,0,1,1)
		self.mc7_grid.addWidget(self.mc7_power, 2,1,1,1)

		#mc8
		self.mc8_groupBox = QtGui.QGroupBox(self)
		self.mc8_groupBox.setTitle('MC 8')
		self.mainGrid.addWidget(self.mc8_groupBox, 4,1,1,1)

		self.mc8_voltage_label = QtGui.QLabel(self.mc8_groupBox)
		self.mc8_voltage_label.setText('Voltage [V]')
		self.mc8_current_label = QtGui.QLabel(self.mc8_groupBox)
		self.mc8_current_label.setText('Current [mA]')
		self.mc8_power_label = QtGui.QLabel(self.mc8_groupBox)
		self.mc8_power_label.setText('Power [W]')

		self.mc8_voltage = QtGui.QLCDNumber(self.mc8_groupBox)
		self.mc8_current = QtGui.QLCDNumber(self.mc8_groupBox)
		self.mc8_power = QtGui.QLCDNumber(self.mc8_groupBox)
		
		self.mc8_grid = QtGui.QGridLayout(self.mc8_groupBox)
		self.mc8_grid.addWidget(self.mc8_voltage_label, 0,0,1,1)
		self.mc8_grid.addWidget(self.mc8_voltage, 0,1,1,1)
		self.mc8_grid.addWidget(self.mc8_current_label, 1,0,1,1)
		self.mc8_grid.addWidget(self.mc8_current, 1,1,1,1)
		self.mc8_grid.addWidget(self.mc8_power_label, 2,0,1,1)
		self.mc8_grid.addWidget(self.mc8_power, 2,1,1,1)

		#self.show()


# For testing:
#def main():
#	app = QtGui.QApplication(sys.argv)
#	ex = SubWindow()
#	sys.exit(app.exec_())


#if __name__ == '__main__':
#	main()