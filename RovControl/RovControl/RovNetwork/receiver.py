import socket
import time
from PyQt4 import QtCore

class Receiver(QtCore.QThread):
	
	updateTemp = QtCore.pyqtSignal(str)
	updateThPower = QtCore.pyqtSignal(str)
	updateManipPower = QtCore.pyqtSignal(str)

	def __init__(self, address="192.168.1.20", port=50001):
		super(Receiver, self).__init__()

		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server_address = (address, port)

	def run(self):
		# This thread will connect to the ROV and wait for data to arrive

		self.connected = False

		while not self.connected:
			try:
				self.socket.connect(self.server_address)
				self.connected = True
				print("Receiver Connected")
			except socket.error as msg:
				# Log error
				time.sleep(2)
				print("Receiver thread unable to connect, trying again in 2 seconds")

		time.sleep(1)
		while(self.connected):

			# Request Temperature
			self.socket.sendall(bytes("temp", 'UTF-8'))

			self.tempData = self.socket.recv(128)
			self.updateTemp.emit(str(self.tempData))
			
			time.sleep(2)

	def processData(self, stringtoparse):
		print("") # placeholder