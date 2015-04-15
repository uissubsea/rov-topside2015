#import sys
#sys.path.insert(1, '../Controller')

import sys
import sdl2
import sdl2.ext
import socket
import threading
import time
from Controller import controller

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

#Create File Handler

handler = logging.FileHandler('status.log')
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

class NetworkClient():
	def __init__(self, address="192.168.1.20", port=50000):
		self.rov_data = ["0","0","0","0","0"]

		self.ctrl = controller.Controller()

		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server_address = (address, port)

		self._stop = threading.Event()

		self.old = 0

		#Create thread to run
		self.thread = threading.Thread(target = self.start_client)
		self.thread.start()


	def start_client(self):

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

		while not self._stop.isSet():	
			
			# Get newest Joystick data

			self.axis_data = self.ctrl.ctrl_adata
			self.button_data = self.ctrl.ctrl_bdata

			#print(self.axis_data)
			# Only send data if controller status changed
			if (self.ctrl.changed):

				self.str = self.serialize(self.axis_data)

				#print(self.str, "\r", end="")

				self.sock.sendall(bytes(self.str, 'UTF-8'))
				#self.sock.sendall(bytes(b"heywww - 2test"))
				#print("data sendt");

				## Receive back from ROV and log
				self.old = self.axis_data

				self.data = self.sock.recv(128)

				print(self.data, "\r", end="")

			#self.data = self.sock.recv(128)
			time.sleep(0.05)
			
			


	def open_controller(self):
		sdl2.SDL_JoystickEventState(sdl2.SDL_ENABLE)
		sdl2.SDL_JoystickOpen(0)

	def serialize(self, rov_data):
		# Create ASCII string to contain data
		string = ""
		# Loop through first 4 data. Assume they are thruster values
		for i in range(4):
			string += str(rov_data[i]) + ","
		
		#string += ";"

		return string

	def stop(self):
		self._stop.set()
		self.sock.close()
		sys.exit




