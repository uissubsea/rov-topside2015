
from PyQt4 import QtGui
#from Gui import cntrconfig2

class Apply(QtGui.QWidget):

	def __init__(self):
		super(Apply, self).__init__()
		
		self.window = QtGui.QWidget()
		self.window.resize(300, 110)
		
		self.lbl = QtGui.QLabel('Controller settings have\nsuccessfully been updated!', self.window)
		self.lbl.setGeometry(90,17,300,60)
		
		okBtn = QtGui.QPushButton('OK', self.window)
		okBtn.setGeometry(105, 73, 90, 32)
		
		icon = QtGui.QLabel(self.window)
		icon.setScaledContents(True)
		icon.setGeometry(20,25,50,50)
		thumb = QtGui.QPixmap('Gui/RESOURCES/thumb.png')
		icon.setPixmap(thumb)
		
		self.window.show()

		okBtn.clicked.connect(self.close)


	def close(self):
		self.window.close()


class Reset(QtGui.QWidget):

	def __init__(self):
		super(Reset, self).__init__()
		
		self.initUI()


	def initUI(self):
		self.qWindow = QtGui.QWidget()
		self.qWindow.resize(400, 160)

		line1 = QtGui.QLabel('Are you sure you want to reset?', self.qWindow)
		line2 = QtGui.QLabel('This will erase all current settings, including\ncalibration data for all controllers.', self.qWindow)
		line1.setGeometry(90,20,320,25)
		line2.setGeometry(90,50,320,50)

		yesBtn = QtGui.QPushButton('Yes', self.qWindow)
		yesBtn.setGeometry(100,113,90,32)
		noBtn = QtGui.QPushButton('No', self.qWindow)
		noBtn.setGeometry(200,113,90,32)

		icon = QtGui.QLabel(self.qWindow)
		icon.setScaledContents(True)
		icon.setGeometry(20, 40, 50, 50)
		warning = QtGui.QPixmap('Gui/RESOURCES/warning.png')
		icon.setPixmap(warning)
		
		self.qWindow.show()

		yesBtn.clicked.connect(self.resetYesHandler)
		noBtn.clicked.connect(self.resetNoHandler)


	def resetYesHandler(self):
		self.parentWindow = cntrconfig2.ConfigWindow()

		self.thLinSlider.setValue(self.parentWindow.th_LIN_DEFAULT)
		self.thExpSlider.setValue(self.parentWindow.th_EXP_DEFAULT)
		self.maLinSlider.setValue(self.parentWindow.ma_LIN_DEFAULT)
		self.maExpSlider.setValue(self.parentWindow.ma_EXP_DEFAULT)
		self.dzSlider.setValue(self.parentWindow.DEADZONE_DEFAULT)
		self.parentWindow.updateSliders()
		
		#erase config
		open("Config/controller.cfg","w").close()

		self.qWindow.close()

	def resetNoHandler(self):
		self.qWindow.close()


class Calibrate(QtGui.QWidget):

	def __init__(self):
		super(Calibrate, self).__init__()

		self.window = QtGui.QWidget()
		self.window.resize(470, 140)
		
		self.lbl = QtGui.QLabel('No controller config for this model was found.\n' \
							'Calibration is required!\n\n' \
							'Move all joystick axes and press main button when done.', self.window)
		self.lbl.setGeometry(90,17,470,80)

		self.okBtn = QtGui.QPushButton('OK', self.window)
		self.okBtn.setGeometry(175, 98, 90, 32)
		self.okBtn.setEnabled(False)

		self.icon = QtGui.QLabel(self.window)
		self.icon.setScaledContents(True)
		self.icon.setGeometry(20, 40, 50, 50)
		warning = QtGui.QPixmap('Gui/RESOURCES/warning.png')
		self.icon.setPixmap(warning)

		self.window.show()
	

	def doneCalibrating(self):
		self.lbl.setText('Done Calibrating!')
		self.okBtn.setEnabled(True)

		thumb = QtGui.QPixmap('Gui/RESOURCES/thumb.png')
		self.icon.setPixmap(thumb)
		
		self.okBtn.clicked.connect(self.close)


	def close(self):
		self.window.close()




