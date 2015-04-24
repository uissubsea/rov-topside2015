#import sys
#sys.path.insert(1, '../Controller')

import sys
import sdl2
import sdl2.ext
import socket
import threading
import time
import configparser
import re
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


class NetworkClient(QtCore.QThread):
	def __init__(self, address="192.168.1.20", port=50000):
		super(NetworkClient, self).__init__()

		self.mutex = QtCore.QMutex

		self.config = configparser.ConfigParser()
		self.config.read('Config/controller.cfg')

		self.rov_data = ["0","0","0","0","0"]

		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server_address = (address, port)

		self.receiver = Receiver()

		self.controllerMap = []
		self.stringMap = []
		self.controlFunction = []

		self.thrusterMap = []
		self.manipMap = []

		self.running = True

		self.thData = [0] * 4
		self.manipData = [0] * 5


	def run(self):
		# Start controller thread
		self.control = controller.Controller()
		# Start controller thread
		self.control.start()

		# Thread Loop

		# Sleep 1 second for controller to be fully initialized Then configure
		time.sleep(1)

		self.configController()

		while True:
			while self.running:	

				# Start Receiver Thread
				#self.receiver.start()
			
				# Get newest Joystick data

				self.axis_data = self.control.axisData
				self.button_data = self.control.axisData

				print(self.axis_data)
				print(self.manipData)

				for i in range(4):
					self.thData[i] = self.axis_data[0][self.thrusterMap[i]]

				for i in range(4):
					self.manipData[i] = self.axis_data[1][self.manipMap[i]]

				#print(self.axis_data)
				# Only send data if controller status changed
				if (self.control.changed):

					##self.axis_data[0][2] = self.axis_data[0][2] + 670

					#self.str = self.serialize(self.axis_data)

					print(self.thData)

					#self.sock.sendall(bytes(self.str, 'UTF-8'))

					# Receive Data from ROV and log

				
					#self.parse_data(self.data.decode("UTF-8"))

					#print(self.data, "\r", end="")

				#self.data = self.sock.recv(128)
				time.sleep(0.05)
			time.sleep(5)

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
		# Disconnect from server
		self.sock.close()
		print("Disconnected from server, Goodbye")

	def connect(self):
		self.connected = False
		logger.info("Connecting to ROV...")
		try:
			self.sock.connect(self.server_address)
			self.connected = True
			logger.info("Connected!")
		except socket.error as msg:
			# Log error
			logger.error("Unable to connect!\n")


	def configController(self):
		for i in range(len(self.control.controllerNames)):
			self.controllerMap.append([0] * (self.control.controllerNumAxis[i] + 1))

		# Get map for each controller
		for idx, controller in enumerate(self.control.controllerNames):
			self.stringMap.append(self.config[str(controller)]["Map"])
			self.controlFunction.append(self.config[str(controller)]["Function"])
			self.controllerMap[idx] = re.findall(r'\d+', self.stringMap[idx])

		# Make ints of list
		for i in range(len(self.controllerMap)):
			for j in range(len(self.controllerMap[i])):
				self.controllerMap[i][j] = int(self.controllerMap[i][j])

		self.thrusterMap = self.controllerMap[0]
		self.manipMap = self.controllerMap[1]
		print(self.thrusterMap)
		print(self.manipMap)
		

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
			



