import sys
import time
from PyQt4 import QtCore, QtGui
from pyqtgraph import PlotWidget
from Controller import controller
import configparser


class ConfigWindow(QtGui.QWidget):

	def __init__(self):
		super(ConfigWindow, self).__init__()
		self.ctrl = controller.Controller()
		self.ctrl.inSettings = True

		self.config = configparser.ConfigParser()
		self.config.read('../Config/controller.cfg')

		self.ctrl.start()

		self.initUI()


	def initUI(self):
		self.EXP_S_DEFAULT = 20
		self.LIN_S_DEFAULT = 10

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

		self.thrusterGB = QtGui.QGroupBox("Flying directions", self.keyBindingsTab)
		self.thrusterGB.setGeometry(20, 80, self.GB_w, 92)
		self.addThrusterGBContents()

		self.manipulatorGB = QtGui.QGroupBox("Manipulator", self.keyBindingsTab)
		self.manipulatorGB.setGeometry(20, 190, self.GB_w, 172)
		self.addManipulatorGBContents()

		self.othersGB = QtGui.QGroupBox("ON/OFF functions", self.keyBindingsTab)
		self.othersGB.setGeometry(20, 380, self.w - 89, 92)
		self.addOthersGBContents()


	def addControllerTab(self):
		self.controllerTab = QtGui.QWidget()
		self.tabwindow.addTab(self.controllerTab, "Controller")

		self.addControllerBox(self.controllerTab)

		self.compCheckBox = QtGui.QCheckBox('  Compensation', self.controllerTab)
		self.compCheckBox.move(20, 70)


	def addSensTab(self):
		self.sensitivityTab = QtGui.QWidget()
		self.tabwindow.addTab(self.sensitivityTab, "Sensitivity")

		self.addControllerBox(self.sensitivityTab)

		self.generalGB = QtGui.QGroupBox("General", self.sensitivityTab)
		self.generalGB.setGeometry(20, 80, self.GB_w, 80)
		self.addGeneralGBContents()

		self.thSensGB = QtGui.QGroupBox("Throttle ", self.sensitivityTab)
		self.thSensGB.setGeometry(20, 248, self.w - 89, 150)
		self.addThSensGBContents()

		self.maSpeedGB = QtGui.QGroupBox("Manipulator", self.sensitivityTab)
		self.maSpeedGB.setGeometry(20, 300, self.w - 89, 100)
		self.addMaSpeedGBContents()

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -	
	# Add tab contents

	def addThrusterGBContents(self):
		self.thrustButtons = []
		self.thrustFields = []

		# Add labels:
		self.thrusterLabels = ['Up/Down', 'Left/Right', 'Forward/Reverse', 'Rotate cw/ccw']
		xpos = [20, 20, 210, 210]
		ypos = [30, 60, 30, 60]

		for i in range(len(self.thrusterLabels)):
			self.thrustButtons.append(QtGui.QPushButton(self.thrusterLabels[i], self.thrusterGB))
			self.thrustButtons[i].setGeometry(xpos[i], ypos[i], 120, 20)
			self.thrustButtons[i].setCheckable(True)

		xpos = [150, 150, 340, 340]
		ypos = [30, 60, 30, 60]

		for i in range(len(xpos)):
			self.thrustFields.append(QtGui.QLabel('___', self.thrusterGB))
			self.thrustFields[i].setGeometry(xpos[i], ypos[i], 41, 20)
			self.thrustFields[i].connect(self.ctrl, QtCore.SIGNAL('setText(QString)'), self.setField)

		
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
		controllerList = self.ctrl.connected_controllers()
		for i in range (len(controllerList)):
			self.combo.addItem(controllerList[i])



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
			self.manipFields.append(QtGui.QLabel('___', self.manipulatorGB))
			self.manipFields[i].setGeometry(xpos[i], ypos[i], 41, 20)
			self.manipFields[i].connect(self.ctrl, QtCore.SIGNAL('setText(QString)'), self.setField)
		
		
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
		self.othersLabel = ['Lights', 'Cam. 1', 'Cam. 2', 'Cam. 3', 'Hold ground',
								'Hold surface']

		xpos = [20, 20, 210, 210, 400, 400]
		ypos = [30, 60, 30, 60, 30, 60]

		for i in range(len(self.othersLabel)):
			self.othersButtons.append(QtGui.QPushButton(self.othersLabel[i], self.othersGB))
			self.othersButtons[i].setGeometry(xpos[i], ypos[i], 120, 20)
			self.othersButtons[i].setCheckable(True)

		xpos = [150, 150, 340, 340, 530, 530]
		ypos = [30, 60, 30, 60, 30, 60]
		
		for i in range(len(self.othersLabel)): 
			self.othersFields.append(QtGui.QLabel('___', self.othersGB))
			self.othersFields[i].setGeometry(xpos[i], ypos[i], 50, 20)
			self.othersFields[i].connect(self.ctrl, QtCore.SIGNAL('setText(QString)'), self.setField)
	

	def addGeneralGBContents(self):
		label = QtGui.QLabel('Dead zone:', self.generalGB)
		label.setGeometry(20, 30, 50, 20)


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
		

	def addMaSpeedGBContents(self):
		print('jwe')

	
	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
	# Other functions:

	def center(self):
		qr = self.frameGeometry()
		cp = QtGui.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())


	def setField(self, axis):
		# Loop through array to check which field should be set
		for i in range(8):
			if self.thrustButtons[i].isChecked():
				self.thrustFields[i].setText(axis)
				self.thrustButtons[i].setChecked(False)

		for i in range(10):
			if self.manipButtons[i].isChecked():
				self.manipFields[i].setText(axis)
				self.manipButtons[i].setChecked(False)

		
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
		self.ctrl.closeController()
		self.close()


	def applyButtonHandler(self):
		print("Settings Written to config")
		
		for i in range(4):
			self.config[str(self.ctrl.ctrl_name)][self.thrusterLabels[i]] = self.thrustFields[i]

		with open('../Config/controller.cfg', 'w') as configfile:
			self.config.write(configfile)
		




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
		self.linSlider.setValue(self.LIN_S_DEFAULT)
		self.expSlider.setValue(self.EXP_S_DEFAULT)
		self.updateSliders()
		#slett configfilene
		#
		self.sw.close()

	def resetNoHandler(self):
		self.sw.close()


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

