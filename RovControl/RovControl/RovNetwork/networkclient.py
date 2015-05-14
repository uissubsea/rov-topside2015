#import sys
#sys.path.insert(1, '../Controller')

import sys
import sdl2
import sdl2.ext
import socket
import threading
import time
import configparser
from Controller import controller
from PyQt4 import QtCore

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

#Create File Handler

handler = logging.FileHandler('Log/status.log')
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)


class NetworkClient(QtCore.QThread):
	
	# Signal to update statusWindow
	updateStatus = QtCore.pyqtSignal()

	def __init__(self):
		super(NetworkClient, self).__init__()

		self.mutex = QtCore.QMutex

		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		self.config = configparser.ConfigParser()
		self.config.read('Config/controller.cfg')

		self.rov_data = ["0","0","0","0","0"]

		self.receiver = Receiver()

		self.useManip = False
		self.useThrust = False

		self.running = True


	def run(self):
		self.connect()

		# Start controller thread
		self.control = controller.Controller()
		# Start controller thread
		self.control.start()

		while self.connected:
			while self.running:	

				# Start Receiver Thread
				#self.receiver.start()
			
				# Process controller and get newest data
				self.control.process_controller()

				# Only send data if controller status changed
				if (self.control.changed):

					self.str = self.serialize(self.control.thData, self.control.manipData)

					#print(self.str)
					self.sock.sendall(bytes(self.str, 'UTF-8'))

					# Receive Data from ROV and log

					self.data = self.sock.recv(128)
					#self.parse_data(self.data.decode("UTF-8"))

					print(self.data, "\r", end="")

				
				time.sleep(0.05)
			time.sleep(5)

	def serialize(self, thData, manipData):
		# Create ASCII string to contain data
		string = ""
		# Loop through first 4 data. Assume they are thruster values
		for item in thData:
			string += str(item) + ","
		for item in manipData:
			string += str(item) + ","

		return string

	def disconnect(self):
		self.running = False
		# Disconnect from server
		self.sock.close()
		self.connected = False
		self.log("Disconnected from server, Goodbye", "info")
		self.terminate()

	def connect(self, address="192.168.1.20", port=50000):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server_address = (address, port)

		self.connected = False
		self.sock.settimeout(5)
		self.log("Connecting to ROV...", "info")
		try:
			self.sock.connect(self.server_address)
			self.connected = True
			self.log("Connected!", "info")
		except socket.error as msg:
			# Log error
			self.log("Unable to connect!\n", "error")
		
		if self.connected == False:
			self.log("Failed to connect, make sure your ethernet ip is set to 192.168.1.2\n", "error")
		
		self.sock.settimeout(None)


	def log(self, string, logType):
		if logType == "error":
			logger.error(string)
		elif logType == "info":
			logger.info(string)
	
		self.updateStatus.emit()


class Receiver(QtCore.QThread):
	def __init__(self, address="192.168.1.20", port=50001):
		super(Receiver, self).__init__()

		self.mutex = QtCore.QMutex

		self.rsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server_address = (address, port)

	def run(self):
		# This thread will connect to the ROV and wait for data to arrive

		self.connected = False

		while not self.connected:
			try:
				self.rsocket.connect(self.server_address)
				self.connected = True
				print("Receiver Connected")
			except socket.error as msg:
				# Log error
				time.sleep(2)
				print("Receiver thread unable to connect, trying again in 2 seconds")

		while(True):
			self.receivedData = self.rsocket.recv(128)
			
			#self.receivedString = parseData(self.receivedData)

			print(self.receivedData)

			#if self.receivedString == "Manip":
				# Update Manipulator widget

			#elif self.receivedString == "Th":
				# Update Thruster widget
			#elif self.receivedString == "adc":
				# update temp, power etc

	def parseData(self, stringtoparse):
		output = stringtoparse
		#output.split("_")
		#print(output)
			



