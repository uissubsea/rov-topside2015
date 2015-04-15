import sys
import time
from PyQt4 import QtCore, QtGui
from pyqtgraph import PlotWidget

class ConfigWindow(QtGui.QWidget):

	def __init__(self):
		super(ConfigWindow, self).__init__()
		self.initUI()


	def initUI(self):
		self.EXP_S_DEFAULT = 20
		self.LIN_S_DEFAULT = 10

		#self.resize(680, 600)
		self.setMinimumSize(680, 600)
		self.setMaximumSize(680, 600)
		self.setWindowTitle("Controller Settings")
		self.center()

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

		self.thSensGB = QtGui.QGroupBox("Throttle", self.sensitivityTab)
		self.thSensGB.setGeometry(20, 10, 591, 201)
		self.addThSensGBContents()

		self.maSensGB = QtGui.QGroupBox("Manipulator", self.sensitivityTab)
		self.maSensGB.setGeometry(20, 230, 591, 231)
		self.addMaSensGBContents()


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
					'Arm: raise', 'Arm: lower', 'Arm: bend', 'Arm: stretch']
		xpos = [20, 20, 20, 20, 20, 20, 220, 220, 220, 220]
		ypos = [30, 60, 90, 120, 150, 180, 30, 60, 90, 120]

		for i in range(len(text)):
			self.label = QtGui.QLabel(text[i], self.manipulatorGB)
			self.label.setGeometry(xpos[i], ypos[i], 110, 20)

		# Add key inputs:
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
		self.maBend_key = QtGui.QLineEdit(self.manipulatorGB)
		self.maBend_key.setGeometry(330, 90, 41, 20)
		self.maStretch_key = QtGui.QLineEdit(self.manipulatorGB)
		self.maStretch_key.setGeometry(330, 120, 41, 20)

		# Add illustration:
		self.maImg = QtGui.QLabel(self.manipulatorGB)
		self.maImg.setScaledContents(True)
		self.maImg.setGeometry(390, 30, 191, 171)
		arm = QtGui.QPixmap('RESOURCES/manipulator.jpg')
		self.maImg.setPixmap(arm)


	def addOthersGBContents(self):
		# Add labels:
		text = ['Lights: on/off', 'Cam. 1: on/off', 'Cam. 2: on/off',
				'Cam. 3: on/off', '?DP knapp?']
		xpos = [20, 20, 220, 220, 420]
		ypos = [40, 70, 40, 70, 40]

		for i in range(len(text)):
			self.label = QtGui.QLabel(text[i], self.othersGB)
			self.label.setGeometry(xpos[i], ypos[i], 110, 20)
		
		# Add key inputs:
		self.lightToggle_key = QtGui.QLineEdit(self.othersGB)
		self.lightToggle_key.setGeometry(130, 40, 41, 20)
		self.cam1Toggle_key = QtGui.QLineEdit(self.othersGB)
		self.cam1Toggle_key.setGeometry(130, 70, 41, 20)
		self.cam2Toggle_key = QtGui.QLineEdit(self.othersGB)
		self.cam2Toggle_key.setGeometry(330, 40, 41, 20)
		self.cam3Toggle_key = QtGui.QLineEdit(self.othersGB)
		self.cam3Toggle_key.setGeometry(330, 70, 41, 20)
		self.holdToggle_key = QtGui.QLineEdit(self.othersGB)
		self.holdToggle_key.setGeometry(510, 40, 41, 20)
	

	def addThSensGBContents(self):
		self.linButton = QtGui.QRadioButton(self.thSensGB)
		self.linButton.setGeometry(20, 50, 20, 20)
		self.linButton.setChecked(True) #Default
		
		self.linLabel = QtGui.QLabel("Linear", self.thSensGB)
		self.linLabel.setGeometry(50, 50, 50, 20)
		self.linSliderValue = QtGui.QLabel(str(self.LIN_S_DEFAULT), self.thSensGB)
		self.linSliderValue.setGeometry(340, 50, 50, 20)

		self.linSlider = QtGui.QSlider(self.thSensGB)
		self.linSlider.setGeometry(150, 50, 160, 22)
		self.linSlider.setOrientation(QtCore.Qt.Horizontal)
		self.linSlider.setTickPosition(QtGui.QSlider.NoTicks)
		self.linSlider.setTickInterval(0)
		self.linSlider.setValue(self.LIN_S_DEFAULT)


		self.expButton = QtGui.QRadioButton(self.thSensGB)
		self.expButton.setGeometry(20, 80, 102, 20)
		
		self.expLabel =QtGui.QLabel("Exponential", self.thSensGB)
		self.expLabel.setGeometry(50, 80, 90, 20)
		self.expSliderValue = QtGui.QLabel(str(self.EXP_S_DEFAULT), self.thSensGB)
		self.expSliderValue.setGeometry(340, 80, 50, 20)

		self.expSlider = QtGui.QSlider(self.thSensGB)
		self.expSlider.setGeometry(150, 80, 160, 22)
		self.expSlider.setOrientation(QtCore.Qt.Horizontal)
		self.expSlider.setTickPosition(QtGui.QSlider.NoTicks)
		self.expSlider.setTickInterval(0)
		self.expSlider.setEnabled(False) #Defalut
		self.expSlider.setValue(self.EXP_S_DEFAULT)
		
		# Action handlers:
		self.linButton.clicked.connect(self.linButtonHandler)
		self.expButton.clicked.connect(self.expButtonHandler)
		self.linSlider.actionTriggered.connect(self.updateSliders)
		self.expSlider.actionTriggered.connect(self.updateSliders)
		#print(self.linSlider.value())
		

	def addMaSensGBContents(self):
		print("ejlrf")


	def center(self):
		qr = self.frameGeometry()
		cp = QtGui.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())
		
################################################################################
#   BUTTON HANDLERS --- class ConfigWindow()
################################################################################

	def linButtonHandler(self):
		self.linSlider.setEnabled(True)
		self.expSlider.setEnabled(False)
		self.updateSliders()


	def expButtonHandler(self):
		self.linSlider.setEnabled(False)
		self.expSlider.setEnabled(True)
		self.updateSliders()
	

	def cancelButtonHandler(self):
		self.close()


	def applyButtonHandler(self):
		print("Apply pressed")


	def resetButtonHandler(self):
		self.linSlider.setValue(self.LIN_S_DEFAULT)
		self.expSlider.setValue(self.EXP_S_DEFAULT)
		self.updateSliders()

		print("Reset pressed")

	def updateSliders(self):
		self.linSliderValue.setText(str(self.linSlider.value()))
		self.expSliderValue.setText(str(self.expSlider.value()))
		
################################################################################
#   MAIN
################################################################################

def main():
	app = QtGui.QApplication(sys.argv)
	ex = ConfigWindow()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()

