#import sys
#sys.path.insert(1, '../Controller')

import sdl2
import sdl2.ext
import socket
import threading
import time
from Controller import controller
#import statuslogger

DEAD_ZONE = 100
CONTROLLER_SMOOTH = 100

class NetworkClient():
	def __init__(self, address="192.168.1.20", port=50000):
		self.rov_data = ["0","0","0","0","0"]

		self.ctrl = controller.Controller()

		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server_address = (address, port)

		#Create thread to run
		self.thread = threading.Thread(target = self.start_client)
		self.thread.start()


	def start_client(self):

		self.connected = False

		while (not self.connected):
			try:
				self.sock.connect(self.server_address)
				self.connected = True
			except socket.error as msg:
				# Log error
				time.sleep(2)
				print("Unable to connect");

		# Thread Loop


		self.running = True

		while self.running:	
			
			# Get newest Joystick data

			self.axis_data = self.ctrl.ctrl_adata
			self.button_data = self.ctrl.ctrl_bdata

			self.str = self.create_string(self.axis_data)

			#print(self.str, "\r", end="")

			#self.sock.sendall(bytes(self.str, 'UTF-8'))
			self.sock.sendall(bytes(b"heywww - 2test"))
			#print("data sendt");

				## Receive back from ROV and log
			self.data = self.sock.recv(128)
			time.sleep(0.05)
			
			print(self.data)

		self.sock.close()


	def open_controller(self):
		sdl2.SDL_JoystickEventState(sdl2.SDL_ENABLE)
		sdl2.SDL_JoystickOpen(0)
		print("Opened Joystick")

	def create_string(self, rov_data):
		string = ""
		#string += "T"
		for i in range(3):
			string += rov_data[i] + ","
		
		string += ";"

		return string










netClient = NetworkClient()



