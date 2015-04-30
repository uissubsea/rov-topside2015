import sys
import time
from PyQt4 import QtCore, QtGui
from pyqtgraph import PlotWidget
from Controller import controller
import configparser


class ConfigWindow(QtGui.QWidget):

	def __init__(self):
		super(ConfigWindow, self).__init__()
		self.control = controller.Controller()
		self.control.inSettings = True

		self.config = configparser.ConfigParser()
		self.config.read('Config/controller.cfg')

		self.control.start()

		self.initUI()


	def initUI(self):
		self.th_LIN_DEFAULT = 10
		self.th_EXP_DEFAULT = 20
		self.ma_LIN_DEFAULT = 10
		self.ma_EXP_DEFAULT = 20
		self.DEADZONE_DEFAULT = 100

		self.w = 680
		self.h = 600
		self.tab_w = self.w - 39
		self.GB_w = self.w - 279

		self.setMinimumSize(self.w, self.h)
		self.setMaximumSize(self.w, self.h)
		self.setWindowTitle("Controller Settings")
		self.center()

		# Define tabwindow
		self.tabwindow = QtGui.QTabWidget(self)
		self.tabwindow.setGeometry(20, 20, self.tab_w, 518)
		self.tabwindow.setCurrentIndex(1)
		
		# Add tabs w/contents
		self.addKeyTab()
		self.addControllerTab()
		self.addSensTab()
		self.addMainButtons()



		self.show()
	

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
	# Main buttons:

	def addMainButtons(self):
		self.cancelButton = QtGui.QPushButton("Cancel", self)
		self.cancelButton.setGeometry(self.w - (90+15), self.h - 50, 90, 32)
		self.cancelButton.clicked.connect(self.cancelButtonHandler)

		self.applyButton = QtGui.QPushButton("Apply", self)
		self.applyButton.setGeometry(self.w - (90*2+20), self.h - 50, 90, 32)
		self.applyButton.clicked.connect(self.applyButtonHandler)

		self.resetButton = QtGui.QPushButton("Reset", self)
		self.resetButton.setGeometry(15, self.h - 50, 90, 32)
		self.resetButton.clicked.connect(self.resetButtonHandler)

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
	# Tabs

	def addKeyTab(self):
		self.keyBindingsTab = QtGui.QWidget()
		self.tabwindow.addTab(self.keyBindingsTab, "Key Bindings")

		self.addControllerBox(self.keyBindingsTab)

		# Add group boxes:
		self.thrusterGB = QtGui.QGroupBox("Flying directions", self.keyBindingsTab)
		self.thrusterGB.setGeometry(20, 80, self.GB_w, 92)
		self.addThrusterGBContents()

		self.manipulatorGB = QtGui.QGroupBox("Manipulator", self.keyBindingsTab)
		self.manipulatorGB.setGeometry(20, 190, self.GB_w, 172)
		self.addManipulatorGBContents()

		self.othersGB = QtGui.QGroupBox("ON/OFF functions", self.keyBindingsTab)
		self.othersGB.setGeometry(20, 380, self.w - 89, 92)
		self.addOthersGBContents()

		# Add radiobuttons:
		lbl = QtGui.QLabel('Set controller function:', self.keyBindingsTab)
		lbl.setGeometry(442, 15, 200, 20)
		self.thrustRB = QtGui.QRadioButton('Thrusters', self.keyBindingsTab)
		self.thrustRB.move(442, 37)
		self.manipRB = QtGui.QRadioButton('Manipulator', self.keyBindingsTab)
		self.manipRB.move(442, 60)
		
		num = len(self.controllerList) # hent len(listOfControllers)
		if (num < 1):
			self.activateManipButtons(False)
			self.activateThrustButtons(False)
			self.activateOtherButtons(False)
			self.thrustRB.setEnabled(False)
			self.manipRB.setEnabled(False)
		elif (num == 1):	
			self.activateManipButtons(True)
			self.activateThrustButtons(True)
			self.activateOtherButtons(True)
			self.thrustRB.setEnabled(False)
			self.manipRB.setEnabled(False)
		elif (num > 1):
			self.thrustRB.setEnabled(True)
			self.manipRB.setEnabled(True)
			self.thrustRB.setChecked(True)
			self.activateThrustButtons(True)
			self.activateManipButtons(False)
			self.thrustRB.toggled.connect(self.thrustToggled)
			self.manipRB.toggled.connect(self.manipToggled)
			


	def addControllerTab(self):
		self.controllerTab = QtGui.QWidget()
		self.tabwindow.addTab(self.controllerTab, "Controller")

		self.addControllerBox(self.controllerTab)


	def addSensTab(self):
		self.sensitivityTab = QtGui.QWidget()
		self.tabwindow.addTab(self.sensitivityTab, "Sensitivity")

		self.addControllerBox(self.sensitivityTab)

		self.generalGB = QtGui.QGroupBox("General", self.sensitivityTab)
		self.generalGB.setGeometry(20, 80, self.GB_w, 60)
		self.addGeneralGBContents()

		self.thSensGB = QtGui.QGroupBox("Throttle", self.sensitivityTab)
		self.thSensGB.setGeometry(20, 150, self.w - 89, 150)
		self.addThSensGBContents()

		self.maSpeedGB = QtGui.QGroupBox("Manipulator", self.sensitivityTab)
		self.maSpeedGB.setGeometry(20, 310, self.w - 89, 150)
		self.addMaSpeedGBContents()

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -	
	# Add tab contents

	def addThrusterGBContents(self):
		self.thrustButtons = []
		self.thrustFields = []

		# Add labels:
		self.thrusterLabels = ['Left/Right', 'Forward/Reverse', 'Up/Down', 'Rotate cw/ccw']
		xpos = [20, 20, 210, 210]
		ypos = [30, 60, 30, 60]

		for i in range(len(self.thrusterLabels)):
			self.thrustButtons.append(QtGui.QPushButton(self.thrusterLabels[i], self.thrusterGB))
			self.thrustButtons[i].setGeometry(xpos[i], ypos[i], 120, 20)
			self.thrustButtons[i].setCheckable(True)

		xpos = [150, 150, 340, 340]
		ypos = [30, 60, 30, 60]

		for i in range(len(xpos)):
			self.thrustFields.append(QtGui.QLabel('____', self.thrusterGB))
			self.thrustFields[i].setGeometry(xpos[i], ypos[i], 41, 20)
			self.thrustFields[i].connect(self.control, QtCore.SIGNAL('setText(QString)'), self.setThrusterField)

		
		# Add illustration:
		self.thImg = QtGui.QLabel(self.keyBindingsTab)
		self.thImg.setScaledContents(True)
		self.thImg.setGeometry(442, 100, 175, 125)
		rov = QtGui.QPixmap('Gui/RESOURCES/skrog.jpg') 
		#oppdater bilde, og fiks adresse når widget kobles opp mot main!
		self.thImg.setPixmap(rov)
		


	def addControllerBox(self, tab):
		self.comboLabel = QtGui.QLabel('Adjust settings for controller:', tab)
		self.comboLabel.setGeometry(22, 25, 200, 30)
		self.combo = QtGui.QComboBox(tab)
		self.combo.setGeometry(223, 27, 200, 30)
		
		# wait two seconds for controllers to initialize
		time.sleep(0.2)
		self.controllerList = self.control.connected_controllers()
		for i in range (len(self.controllerList)):
			self.combo.addItem(self.controllerList[i])


	def addManipulatorGBContents(self):
		self.manipButtons = []
		self.manipFields = []

		# Add labels:
		clawLabel = QtGui.QLabel('Claw:', self.manipulatorGB)
		clawLabel.setGeometry(25, 27, 150, 20)
		armLabel = QtGui.QLabel('Arm:', self.manipulatorGB)
		armLabel.setGeometry(215, 27, 150, 20)


		self.manipLabels = ['Open', 'Grip', 'Tilt', 'Rotate cw/ccw', 
					'Raise/Lower', 'Bend/Stretch']
		xpos = [20, 20, 20, 20, 210, 210]
		ypos = [50, 80, 110, 140, 50, 80]

		for i in range(len(self.manipLabels)):
			self.manipButtons.append(QtGui.QPushButton(self.manipLabels[i], self.manipulatorGB))
			self.manipButtons[i].setGeometry(xpos[i], ypos[i], 120, 20)
			self.manipButtons[i].setCheckable(True)

		xpos = [150, 150, 150, 150, 340, 340]
		ypos = [50, 80, 110, 140, 50, 80]
		
		for i in range(len(self.manipLabels)): 
			self.manipFields.append(QtGui.QLabel('____', self.manipulatorGB))
			self.manipFields[i].setGeometry(xpos[i], ypos[i], 41, 20)
			self.manipFields[i].connect(self.control, QtCore.SIGNAL('setText(QString)'), self.setManipField)
		
		
		# Add illustration:
		self.maImg = QtGui.QLabel(self.keyBindingsTab)
		self.maImg.setScaledContents(True)
		self.maImg.setGeometry(442, 233, 175, 125)
		arm = QtGui.QPixmap('Gui/RESOURCES/manipulator.jpg')
		self.maImg.setPixmap(arm)
		


	def addOthersGBContents(self):
		self.othersButtons = []
		self.othersFields = []

		# Add labels:
		self.othersLabel = ['Lights', 'Cam. 1', 'Cam. 2', 'Cam. 3', 'Laser',
								'Hold ground']

		xpos = [20, 20, 210, 210, 400, 400]
		ypos = [30, 60, 30, 60, 30, 60]

		for i in range(len(self.othersLabel)):
			self.othersButtons.append(QtGui.QPushButton(self.othersLabel[i], self.othersGB))
			self.othersButtons[i].setGeometry(xpos[i], ypos[i], 120, 20)
			self.othersButtons[i].setCheckable(True)

		xpos = [150, 150, 340, 340, 530, 530]
		ypos = [30, 60, 30, 60, 30, 60]
		
		for i in range(len(self.othersLabel)): 
			self.othersFields.append(QtGui.QLabel('____', self.othersGB))
			self.othersFields[i].setGeometry(xpos[i], ypos[i], 50, 20)
			self.othersFields[i].connect(self.control, QtCore.SIGNAL('setText(QString)'), self.setOthersField)
	

	def addGeneralGBContents(self):
		label = QtGui.QLabel('Dead zone', self.generalGB)
		label.setGeometry(50, 30, 100, 20)		

		self.dzSlider = QtGui.QSlider(self.generalGB)
		self.dzSlider.setGeometry(150, 30, 160, 22)
		self.dzSlider.setOrientation(QtCore.Qt.Horizontal)
		self.dzSlider.setTickPosition(QtGui.QSlider.NoTicks)
		self.dzSlider.setTickInterval(20)
		self.dzSlider.setMinimum(0)
		self.dzSlider.setMaximum(500)
		self.dzSlider.setValue(self.DEADZONE_DEFAULT)

		self.dzSliderValue = QtGui.QLabel(str(self.dzSlider.value()), self.generalGB)
		self.dzSliderValue.setGeometry(340, 30, 50, 20)

		self.dzSlider.actionTriggered.connect(self.updateSliders)


	def addThSensGBContents(self):
		self.thLinButton = QtGui.QRadioButton(self.thSensGB)
		self.thLinButton.setGeometry(20, 50, 20, 20)
		self.thLinButton.setChecked(True) #Default
		
		self.thLinLabel = QtGui.QLabel("Linear", self.thSensGB)
		self.thLinLabel.setGeometry(50, 50, 50, 20)
		self.thLinSliderValue = QtGui.QLabel(str(self.th_LIN_DEFAULT), self.thSensGB)
		self.thLinSliderValue.setGeometry(340, 50, 50, 20)

		self.thLinSlider = QtGui.QSlider(self.thSensGB)
		self.thLinSlider.setGeometry(150, 50, 160, 22)
		self.thLinSlider.setOrientation(QtCore.Qt.Horizontal)
		self.thLinSlider.setTickPosition(QtGui.QSlider.NoTicks)
		self.thLinSlider.setTickInterval(0)
		self.thLinSlider.setValue(self.th_LIN_DEFAULT)

		self.thExpButton = QtGui.QRadioButton(self.thSensGB)
		self.thExpButton.setGeometry(20, 80, 102, 20)
		
		self.thExpLabel = QtGui.QLabel("Exponential", self.thSensGB)
		self.thExpLabel.setGeometry(50, 80, 90, 20)
		self.thExpSliderValue = QtGui.QLabel(str(self.th_EXP_DEFAULT), self.thSensGB)
		self.thExpSliderValue.setGeometry(340, 80, 50, 20)

		self.thExpSlider = QtGui.QSlider(self.thSensGB)
		self.thExpSlider.setGeometry(150, 80, 160, 22)
		self.thExpSlider.setOrientation(QtCore.Qt.Horizontal)
		self.thExpSlider.setTickPosition(QtGui.QSlider.NoTicks)
		self.thExpSlider.setTickInterval(0)
		self.thExpSlider.setEnabled(False) #Defalut
		self.thExpSlider.setValue(self.th_EXP_DEFAULT)
		
		# Action handlers:
		self.thLinButton.clicked.connect(self.thLinButtonHandler)
		self.thExpButton.clicked.connect(self.thExpButtonHandler)
		self.thLinSlider.actionTriggered.connect(self.updateSliders)
		self.thExpSlider.actionTriggered.connect(self.updateSliders)


	def addMaSpeedGBContents(self):
		self.maLinButton = QtGui.QRadioButton(self.maSpeedGB)
		self.maLinButton.setGeometry(20, 50, 20, 20)
		self.maLinButton.setChecked(True) #Default
		
		self.maLinLabel = QtGui.QLabel("Linear", self.maSpeedGB)
		self.maLinLabel.setGeometry(50, 50, 50, 20)
		self.maLinSliderValue = QtGui.QLabel(str(self.ma_LIN_DEFAULT), self.maSpeedGB)
		self.maLinSliderValue.setGeometry(340, 50, 50, 20)

		self.maLinSlider = QtGui.QSlider(self.maSpeedGB)
		self.maLinSlider.setGeometry(150, 50, 160, 22)
		self.maLinSlider.setOrientation(QtCore.Qt.Horizontal)
		self.maLinSlider.setTickPosition(QtGui.QSlider.NoTicks)
		self.maLinSlider.setTickInterval(0)
		self.maLinSlider.setValue(self.ma_LIN_DEFAULT)

		self.maExpButton = QtGui.QRadioButton(self.maSpeedGB)
		self.maExpButton.setGeometry(20, 80, 102, 20)
		
		self.maExpLabel = QtGui.QLabel("Exponential", self.maSpeedGB)
		self.maExpLabel.setGeometry(50, 80, 90, 20)
		self.maExpSliderValue = QtGui.QLabel(str(self.ma_EXP_DEFAULT), self.maSpeedGB)
		self.maExpSliderValue.setGeometry(340, 80, 50, 20)

		self.maExpSlider = QtGui.QSlider(self.maSpeedGB)
		self.maExpSlider.setGeometry(150, 80, 160, 22)
		self.maExpSlider.setOrientation(QtCore.Qt.Horizontal)
		self.maExpSlider.setTickPosition(QtGui.QSlider.NoTicks)
		self.maExpSlider.setTickInterval(0)
		self.maExpSlider.setEnabled(False) #Defalut
		self.maExpSlider.setValue(self.ma_EXP_DEFAULT)
		
		# Action handlers:
		self.maLinButton.clicked.connect(self.maLinButtonHandler)
		self.maExpButton.clicked.connect(self.maExpButtonHandler)
		self.maLinSlider.actionTriggered.connect(self.updateSliders)
		self.maExpSlider.actionTriggered.connect(self.updateSliders)

	
	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
	# Other functions:

	def center(self):
		qr = self.frameGeometry()
		cp = QtGui.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())


	def setThrusterField(self, axis):
		# Loop through array to check which field should be set
		for i in range(len(self.thrusterLabels)):
			if self.thrustButtons[i].isChecked():
				self.thrustFields[i].setText(axis)
				self.thrustButtons[i].setChecked(False)

	def setManipField(self, axis):
		for i in range(len(self.manipLabels)):
			if self.manipButtons[i].isChecked():
				self.manipFields[i].setText(axis)
				self.manipButtons[i].setChecked(False)

	def setOthersField(self, axis):
		for i in range(len(self.othersLabel)):
			if self.othersButtons[i].isChecked():
				self.othersFields[i].setText(axis)
				self.othersButtons[i].setChecked(False)

	def activateThrustButtons(self, bool):
		for i in range(len(self.thrustButtons)):
			self.thrustButtons[i].setEnabled(bool)

	def activateManipButtons(self, bool):
		for i in range(len(self.manipButtons)):
			self.manipButtons[i].setEnabled(bool)

	def activateOtherButtons(self, bool):
		for i in range(len(self.othersButtons)):
			self.othersButtons[i].setEnabled(bool)

	def thrustToggled(self):
		self.activateThrustButtons(True)
		self.activateManipButtons(False)
		self.activateOtherButtons(True)

	def manipToggled(self):
		self.activateThrustButtons(False)
		self.activateManipButtons(True)
		self.activateOtherButtons(True)



		
################################################################################
#   BUTTON HANDLERS --- class ConfigWindow()
################################################################################

	def thLinButtonHandler(self):
		self.thLinSlider.setEnabled(True)
		self.thExpSlider.setEnabled(False)
		self.updateSliders()


	def thExpButtonHandler(self):
		self.thLinSlider.setEnabled(False)
		self.thExpSlider.setEnabled(True)
		self.updateSliders()

	def maLinButtonHandler(self):
		self.maLinSlider.setEnabled(True)
		self.maExpSlider.setEnabled(False)
		self.updateSliders()


	def maExpButtonHandler(self):
		self.maLinSlider.setEnabled(False)
		self.maExpSlider.setEnabled(True)
		self.updateSliders()
	

	def cancelButtonHandler(self):
		self.control.running = False
		self.close()


	def applyButtonHandler(self):
		# This function saves settings to configfile
		# Save to section with current name in comboBox
		stringOut = ""
		thrustOrMan = ""
		for i in range(len(self.thrusterLabels)):
			stringOut += str(self.thrustFields[i].text()) + ","
			
		self.config[str(self.combo.currentText())]['Map'] = stringOut
		if self.thrustRB.isChecked():
			self.config[str(self.combo.currentText())]['Function'] = "Thruster"
		elif self.manipRB.isChecked():
			self.config[str(self.combo.currentText())]['Function'] = "Manip"
		else:
			self.config[str(self.combo.currentText())]['Function'] = "Thruster"


		with open('Config/controller.cfg', 'w') as configfile:
			self.config.write(configfile)

		self.applyOK = QtGui.QWidget()
		self.applyOK.resize(300, 110)
		lbl = QtGui.QLabel('Controller settings have\nsuccessfully been updated!', self.applyOK)
		lbl.setGeometry(90,17,300,60)
		okBtn = QtGui.QPushButton('OK', self.applyOK)
		okBtn.setGeometry(105, 73, 90, 32)
		icon = QtGui.QLabel(self.applyOK)
		icon.setScaledContents(True)
		icon.setGeometry(20,25,50,50)
		thumb = QtGui.QPixmap('Gui/RESOURCES/thumb.png')
		icon.setPixmap(thumb)
		self.applyOK.show()

		okBtn.clicked.connect(self.applyOKHandler)


	def applyOKHandler(self):
		self.applyOK.close()


	def resetButtonHandler(self):
		# first, open "are-you-sure" window
		self.sw = QtGui.QWidget()
		self.sw.resize(400, 160)
		
		line1 = QtGui.QLabel('Are you sure you want to reset?', self.sw)
		line2 = QtGui.QLabel('This will erase all current settings, including\ncalibration data for all controllers.', self.sw)
		line1.setGeometry(90,20,320,25)
		line2.setGeometry(90,50,320,50)

		yesBtn = QtGui.QPushButton('Yes', self.sw)
		yesBtn.setGeometry(100,113,90,32)
		noBtn = QtGui.QPushButton('No', self.sw)
		noBtn.setGeometry(200,113,90,32)

		icon = QtGui.QLabel(self.sw)
		icon.setScaledContents(True)
		icon.setGeometry(20, 40, 50, 50)
		warning = QtGui.QPixmap('Gui/RESOURCES/warning.png')
		icon.setPixmap(warning)
		
		self.sw.show()

		yesBtn.clicked.connect(self.resetYesHandler)
		noBtn.clicked.connect(self.resetNoHandler)

	def resetYesHandler(self):
		self.thLinSlider.setValue(self.th_LIN_DEFAULT)
		self.thExpSlider.setValue(self.th_EXP_DEFAULT)
		self.maLinSlider.setValue(self.ma_LIN_DEFAULT)
		self.maExpSlider.setValue(self.ma_EXP_DEFAULT)
		self.dzSlider.setValue(self.DEADZONE_DEFAULT)
		self.updateSliders()
		
		#erase config
		open("Config/controller.cfg","w").close()

		self.sw.close()

	def resetNoHandler(self):
		self.sw.close()

	def updateSliders(self):
		self.thLinSliderValue.setText(str(self.thLinSlider.value()))
		self.thExpSliderValue.setText(str(self.thExpSlider.value()))
		self.maLinSliderValue.setText(str(self.maLinSlider.value()))
		self.maExpSliderValue.setText(str(self.maExpSlider.value()))
		self.dzSliderValue.setText(str(self.dzSlider.value()))
		
################################################################################
#   MAIN
################################################################################

def main():
	app = QtGui.QApplication(sys.argv)
	ex = ConfigWindow()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()

