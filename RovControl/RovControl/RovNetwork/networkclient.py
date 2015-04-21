#import sys
#sys.path.insert(1, '../Controller')

import sys
import sdl2
import sdl2.ext
import socket
import threading
import time
from Controller import controller
from PyQt4 import QtCore

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

#Create File Handler

handler = logging.FileHandler('status.log')
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

# Global variable
control = controller.Controller()

class NetworkClient(QtCore.QThread):
	def __init__(self, address="192.168.1.20", port=50000):
		super(NetworkClient, self).__init__()

		self.mutex = QtCore.QMutex

		self.rov_data = ["0","0","0","0","0"]

		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server_address = (address, port)

		self.receiver = Receiver()


		self.running = True

		# Start controller thread
		control.start()


	def run(self):
		# Start controller thread

		self.connected = False
		logger.info("Connecting to ROV...")
		while (not self.connected):
			try:
				self.sock.connect(self.server_address)
				self.connected = True
				logger.info("Connected!")
			except socket.error as msg:
				# Log error
				logger.error("Unable to connect!\nTrying again...")
				time.sleep(2)

		# Thread Loop

		while self.running:	

			# Start Receiver Thread
			self.receiver.start()
			
			# Get newest Joystick data

			#self.axis_data = control.axisData
			#self.button_data = control.axisData

			self.axis_data = packageControllerData()

			#print(self.axis_data)
			# Only send data if controller status changed
			if (control.changed):

				##self.axis_data[0][2] = self.axis_data[0][2] + 670

				self.str = self.serialize(self.axis_data)

				print(self.str)

				self.sock.sendall(bytes(self.str, 'UTF-8'))

				# Receive Data from ROV and log

				
				#self.parse_data(self.data.decode("UTF-8"))

				#print(self.data, "\r", end="")

			#self.data = self.sock.recv(128)
			time.sleep(0.05)

		# Disconnect from server
		self.sock.close()
		control.closeController()
		print("Disconnected from server, Goodbye")

	def serialize(self, rov_data):
		# Create ASCII string to contain data
		string = ""
		# Loop through first 4 data. Assume they are thruster values
		for i in range(len(rov_data)):
			for j in range(len(rov_data[i])):
				string += str(rov_data[i][j]) + ","
			#string += ";"

		return string

	def disconnect(self):
		self.running = False

	def packageControllerData():
		

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
			



