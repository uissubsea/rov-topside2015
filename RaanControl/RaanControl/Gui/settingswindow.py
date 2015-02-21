from PyQt4 import QtGui
from PyQt4 import QtCore
from Gui import settingstab
import sys


class SettingsWindow(QtGui.QTabWidget):

	def __init__(self):
		super(SettingsWindow, self).__init__()

		self.initUI()


	def initUI(self):

		st = SensorsTab()
		jt = JoystickTab()
		ct = CameraTab()

		self.addTab(st, "Sensors")
		self.addTab(jt, "Joystick")
		self.addTab(ct, "Kamera")


		self.setGeometry(300, 300, 600, 350)
		self.setWindowTitle('Instillinger')
		
		# self.setWindowIcon(QtGui.QIcon('icon.png'))

		self.show()

	def center(self):

		qr = self.frameGeometry()
		cp = QtGui.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

# Classes for each individual tab #
class SensorsTab(settingstab.SettingsTab):

	def __init__(self):
		super(SensorsTab, self).__init__()


class JoystickTab(settingstab.SettingsTab):

	def __init__(self):
		super(JoystickTab, self).__init__()


class CameraTab(settingstab.SettingsTab):

	def __init__(self):
		super(CameraTab, self).__init__()

