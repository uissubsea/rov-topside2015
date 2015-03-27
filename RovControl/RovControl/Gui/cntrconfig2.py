import sys
from PyQt4 import QtCore, QtGui
from pyqtgraph import PlotWidget

class ConfigWindow(QtGui.QWidget):

	def __init__(self):
		super(ConfigWindow, self).__init__()
		self.initUI()


	def initUI(self):
		self.resize(680, 600)
		self.setMinimumSize(680, 600)
		self.setMaximumSize(680, 600)
		self.setWindowTitle("Controller Settings")

		# Define tabwindow
		self.tabwindow = QtGui.QTabWidget(self)
		self.tabwindow.setGeometry(20, 10, 641, 531)
		#self.tabwindow.usesScrollButtons(False)
		#self.tabWindow.setCurrentIndex(1)
		self.addKeyTab()
		self.addControllerTab()
		self.addSensTab()
		self.addMainButtons()

		self.show()


	def addMainButtons(self):
		self.cancelButton = QtGui.QPushButton("Cancel", self)
		self.cancelButton.setGeometry(575, 550, 91, 32)
		self.cancelButton.clicked.connect(self.cancelButtonHandler)

		self.applyButton = QtGui.QPushButton("Apply", self)
		self.applyButton.setGeometry(480, 550, 91, 32)
		self.applyButton.clicked.connect(self.applyButtonHandler)

		self.resetButton = QtGui.QPushButton("Reset", self)
		self.resetButton.setGeometry(14, 550, 91, 32)
		self.resetButton.clicked.connect(self.resetButtonHandler)


	def cancelButtonHandler(self):
		print("Cancel pressed")
		self.close()

	def applyButtonHandler(self):
		print("Apply pressed")

	def resetButtonHandler(self):
		print("Reset pressed")


	def addKeyTab(self):
		self.keyBindingsTab = QtGui.QWidget()
		self.tabwindow.addTab(self.keyBindingsTab, "Key Bindings")

		self.thrusterGB = QtGui.QGroupBox("Thrusters", self.keyBindingsTab)
		self.thrusterGB.setGeometry(20, 0, 591, 151)
		self.addThrusterGBContents()

		self.manipulatorGB = QtGui.QGroupBox("Manupilator", self.keyBindingsTab)
		self.manipulatorGB.setGeometry(20, 160, 591, 211)
		self.addManipulatorGBContents()

		self.othersGB = QtGui.QGroupBox("Miscellaneous", self.keyBindingsTab)
		self.othersGB.setGeometry(20, 380, 591, 111)
		self.addOthersGBContents()

	def addControllerTab(self):
		self.controllerTab = QtGui.QWidget()
		self.tabwindow.addTab(self.controllerTab, "Controller")

	def addSensTab(self):
		self.sensitivityTab = QtGui.QWidget()
		self.tabwindow.addTab(self.sensitivityTab, "Sensitivity")


	def addThrusterGBContents(self):
		
		# Add labels:
		text = ['Up', 'Down', 'Forward', 'Reverse', 
					'Right', 'Left', 'Rotate CW', 'Rotate CCW']
		xpos = [20, 20, 20, 20, 220, 220, 220, 220]
		ypos = [30, 60, 90, 120, 30, 60, 90, 120]

		for i in range(len(text)):
			self.label = QtGui.QLabel(text[i], self.thrusterGB)
			self.label.setGeometry(xpos[i], ypos[i], 75, 20)

		# Add key inputs:
		self.thUp_key = QtGui.QLineEdit(self.thrusterGB)
		self.thUp_key.setGeometry(130, 30, 41, 20) 
		self.thDown_key = QtGui.QLineEdit(self.thrusterGB)
		self.thDown_key.setGeometry(130, 60, 41, 20)
		self.thReverse_key = QtGui.QLineEdit(self.thrusterGB)
		self.thReverse_key.setGeometry(130, 120, 41, 20)
		self.thForward_key = QtGui.QLineEdit(self.thrusterGB)
		self.thForward_key.setGeometry(130, 90, 41, 20)
		self.thRight_key = QtGui.QLineEdit(self.thrusterGB)
		self.thRight_key.setGeometry(330, 30, 41, 20)
		self.thLeft_key = QtGui.QLineEdit(self.thrusterGB)
		self.thLeft_key.setGeometry(330, 60, 41, 20)
		self.thRotateCCW_key = QtGui.QLineEdit(self.thrusterGB)
		self.thRotateCCW_key.setGeometry(330, 120, 41, 20)
		self.thRotateCW_key = QtGui.QLineEdit(self.thrusterGB)
		self.thRotateCW_key.setGeometry(330, 90, 41, 20)

		# Add illustration:
		self.thImg = QtGui.QLabel(self.thrusterGB)
		self.thImg.setScaledContents(True)
		self.thImg.setGeometry(390, 30, 191, 111)
		rov = QtGui.QPixmap('RESOURCES/skrog.jpg') 
		#oppdater bilde, og fiks adresse når widget kobles opp mot main!
		self.thImg.setPixmap(rov)

	def addManipulatorGBContents(self):
		
		# Add labels:
		text = ['Claw: open', 'Claw: grip', 'Claw: rotate cw', 'Claw: rotate ccw',
					'Claw: tilt up', 'Claw: tilt down', 
					'Arm: raise', 'Arm: lower', 'Arm: rotate cw', 'Arm: rotate ccw',
					'Arm: bend', 'Arm: stretch']
		xpos = [20, 20, 20, 20, 20, 20, 220, 220, 220, 220, 220, 220]
		ypos = [30, 60, 90, 120, 150, 180, 30, 60, 90, 120, 150, 180]

		for i in range(len(text)):
			self.label = QtGui.QLabel(text[i], self.manipulatorGB)
			self.label.setGeometry(xpos[i], ypos[i], 110, 20)

		# Add key labels:
		self.mcRotateCCW = QtGui.QLineEdit(self.manipulatorGB)
		self.mcRotateCCW.setGeometry(130, 120, 41, 20)
		self.mcRotateCW_key = QtGui.QLineEdit(self.manipulatorGB)
		self.mcRotateCW_key.setGeometry(130, 90, 41, 20)
		self.mcGrip_key = QtGui.QLineEdit(self.manipulatorGB)
		self.mcGrip_key.setGeometry(130, 60, 41, 20)
		self.mcOpen_key = QtGui.QLineEdit(self.manipulatorGB)
		self.mcOpen_key.setGeometry(130, 30, 41, 20)
		self.mcUp_key = QtGui.QLineEdit(self.manipulatorGB)
		self.mcUp_key.setGeometry(130, 150, 41, 20)
		self.mcDown_key = QtGui.QLineEdit(self.manipulatorGB)
		self.mcDown_key.setGeometry(130, 180, 41, 20)
		self.maRaise_key = QtGui.QLineEdit(self.manipulatorGB)
		self.maRaise_key.setGeometry(330, 30, 41, 20)
		self.maLower_key = QtGui.QLineEdit(self.manipulatorGB)
		self.maLower_key.setGeometry(330, 60, 41, 20)
		self.maRotateCW_key = QtGui.QLineEdit(self.manipulatorGB)
		self.maRotateCW_key.setGeometry(330, 90, 41, 20)
		self.maRotateCCW = QtGui.QLineEdit(self.manipulatorGB)
		self.maRotateCCW.setGeometry(330, 120, 41, 20)
		self.maBend_key = QtGui.QLineEdit(self.manipulatorGB)
		self.maBend_key.setGeometry(330, 150, 41, 20)
		self.maStretch_key = QtGui.QLineEdit(self.manipulatorGB)
		self.maStretch_key.setGeometry(330, 180, 41, 20)
        

		# Add illustration:
		self.maImg = QtGui.QLabel(self.manipulatorGB)
		self.maImg.setScaledContents(True)
		self.maImg.setGeometry(390, 30, 191, 171)
		arm = QtGui.QPixmap('RESOURCES/manipulator.jpg')
		self.maImg.setPixmap(arm)

	def addOthersGBContents(self):
		print("elfn")
	

		

# For testing:
def main():
	app = QtGui.QApplication(sys.argv)
	ex = ConfigWindow()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()