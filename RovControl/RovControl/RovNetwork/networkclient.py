#import sys
#sys.path.insert(1, '../Controller')

import sys
from PyQt4 import QtCore

class NetworkClient(QtCore.QObject):
	
	# Signal to update statusWindow
	updateStatus = QtCore.pyqtSignal()
	updateThWidget = QtCore.pyqtSignal(str)
	updateManipWidget = QtCore.pyqtSignal(str)

	def __init__(self):
		super(NetworkClient, self).__init__()

		self.socket = QTcpSocket()

		self.config = configparser.ConfigParser()
		self.config.read('Config/controller.cfg')

		self.send = False;

	def disconnect(self):
		self.running = False
		self.control.running = False
		self.control = None
		# Disconnect from server
		self.sock.close()
		self.connected = False
		self.log("Disconnected from server, Goodbye", "info")

	def connectToRov(self, address="192.168.1.20", port=50000):
		self.socket.connectToHost(address, port)

		if(socket.waitForConnected(5000)):
			print("Connected to Rov")



	def disconnected(self):
		print("Disconnected!")

	def connected(self):
		print("Connected To Rov")

	def readyRead(self):
		print(self.socket.readAll())


	def log(self, string, logType):
		if logType == "error":
			logger.error(string)
		elif logType == "info":
			logger.info(string)
	
		self.updateStatus.emit()
