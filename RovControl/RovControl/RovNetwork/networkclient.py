#import sys
#sys.path.insert(1, '../Controller')

import sys
import configparser
from PyQt4 import QtCore
from PyQt4.QtNetwork import *

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

#Create File Handler

handler = logging.FileHandler('Log/status.log')
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

class NetworkClient(QtCore.QObject):
	
	# Signal to update statusWindow
	updateStatus = QtCore.pyqtSignal()
	updateThWidget = QtCore.pyqtSignal(str)
	updateManipWidget = QtCore.pyqtSignal(str)

	def __init__(self):
		super(NetworkClient, self).__init__()

		self.socket = QTcpSocket()

		self.socket.readyRead.connect(self.readData)

		self.config = configparser.ConfigParser()
		self.config.read('Config/controller.cfg')

		self.rov_data = ["0","0","0","0","0"]

		#self.receiver = Receiver()

		self.useManip = False
		self.useThrust = False

		self.running = True


	def serialize(self, thData, manipData):
		# Create ASCII string to contain data
		string = ""
		# Loop through first 4 data. Assume they are thruster values
		for item in thData:
			string += str(item) + ","
		for item in manipData:
			string += str(item) + ","

		return string

	def sendData(self, string):
		
		self.socket.write(bytes(string, "UTF-8"))
		#print(string)
		#self.socket.read()


	def disconnectFromRov(self):
		self.socket.disconnectFromHost()

		self.log("Disconnected from server, Goodbye", "info")

	def connectToRov(self, address="192.168.1.20", port=50000):
		self.socket.connectToHost(address, port)

		if(self.socket.waitForConnected(5000)):
			print("Connected!")
			return True
		else:
			print("Failed to connect")
			return False

	def readData(self):
		print(self.socket.readAll(), end="\r")

	def log(self, string, logType):
		if logType == "error":
			logger.error(string)
		elif logType == "info":
			logger.info(string)
	
		self.updateStatus.emit()
