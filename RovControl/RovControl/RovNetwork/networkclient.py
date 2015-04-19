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

class NetworkClient(QtCore.QThread):
	def __init__(self, address="192.168.1.20", port=50000):
		super(NetworkClient, self).__init__()

		self.rov_data = ["0","0","0","0","0"]

		self.ctrl1 = controller.Controller()
		self.ctrl2 = controller.Controller()

		self.controllers = []
		self.controllers.append(self.ctrl1)
		self.controllers.append(self.ctrl2)

		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server_address = (address, port)


		self.running = True

	def init_controllers(self):
		self.numOfControllers = len(self.controllers)
		# Create Array to hold thruster and manipulator data
		self.controllerData = [None] * self.numOfControllers
		
		# Open Controllers and start threads
		for i in range(self.numOfControllers):
			self.controllers[i].open_controller(i)
			self.controllers[i].start()

	def run(self):
		# Start controller thread

		self.init_controllers()

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
			
			# Get newest Joystick data
			for i in range(self.numOfControllers):
				self.controllerData[i] = self.controllers[i].ctrl_axisdata
				self.controllerData[i] = self.controllers[i].ctrl_buttondata

			print(self.controllerData[0])
			# Only send data if controller status changed
			if self.controllers[0].changed or self.controllers[1].changed:

				self.str = self.serialize(self.controllerData)

				print(self.str, "\r", end="")

				self.sock.sendall(bytes(self.str, 'UTF-8'))

				# Receive Data from ROV and log

				self.data = self.sock.recv(128)
				#self.parse_data(self.data.decode("UTF-8"))

				#print(self.data, "\r", end="")

			#self.data = self.sock.recv(128)
			time.sleep(0.05)

		# Disconnect from server
		self.sock.close()
		self.ctrl[0].closeController()
		print("Disconnected from server, Goodbye")

	def parse_data(self, stringtoparse):
		output = stringtoparse
		#output.split("_")
		print(output)
			

	def open_controller(self):
		sdl2.SDL_JoystickEventState(sdl2.SDL_ENABLE)
		sdl2.SDL_JoystickOpen(0)

	def serialize(self, rov_data):
		# Create ASCII string to contain data
		string = ""
		# Loop through first 4 data. Assume they are thruster values
		# Add data from both controllers
		for i in range(len(rov_data)):
			for j in range(len(rov_data[i])):
				string = string + str(rov_data[i][j]) + ","
	
		
		#string += ";"

		return string

	def disconnect(self):
		self.running = False
