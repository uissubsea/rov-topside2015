from PyQt4 import QtGui
from PyQt4 import QtCore

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