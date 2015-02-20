from PyQt4 import QtGui
from PyQt4 import QtCore
import sys

class SettingsTab(QtGui.QWidget):

	def __init__(self):
		super(SettingsTab, self).__init__()

		self.initTab()

	def initTab(self):

		# Create Buttons for "apply", "cancel" and "load Default"
		applyButton = QtGui.QPushButton('Apply', self)
		applyButton.resize(applyButton.sizeHint())

		cancelButton = QtGui.QPushButton('Cancel', self)
		cancelButton.resize(cancelButton.sizeHint())

		defaultButton = QtGui.QPushButton('Default', self)
		defaultButton.resize(defaultButton.sizeHint())

		# Place Buttons in HBox in lower right corner
		hbox = QtGui.QHBoxLayout()
		hbox.addStretch(1)
		hbox.addWidget(applyButton)
		hbox.addWidget(cancelButton)
		hbox.addWidget(defaultButton)

		vbox = QtGui.QVBoxLayout()
		vbox.addStretch(1)
		vbox.addLayout(hbox)

		# Create Options and put them in form
		#sampleLabel = QtGui.QLabel('Sample Frequency', self)


		#formLayout = QtGui.QFormLayout()

		#formLayout.addRow()


		self.setLayout(vbox)
		self.setGeometry(300, 300, 250, 150)
		self.setWindowTitle('Sensors')
		self.show()


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

class SensorsTab(SettingsTab):

	def __init__(self):
		super(SensorsTab, self).__init__()


class JoystickTab(SettingsTab):

	def __init__(self):
		super(JoystickTab, self).__init__()


class CameraTab(SettingsTab):

	def __init__(self):
		super(CameraTab, self).__init__()


def main():

	app = QtGui.QApplication(sys.argv)
	window = SettingsWindow()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()

