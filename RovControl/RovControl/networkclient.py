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

		# Thread Loop


		self.running = True

		while self.running:	
			self.events = sdl2.ext.get_events()
			for event in self.events:
				self.handle_events(event)
			
			self.str = self.create_string(self.rov_data)

			print(self.str, "\r", end="")

			self.sock.sendall(bytes(self.str, 'UTF-8'))

				## Receive back from ROV and log
			self.data = self.sock.recv(64)
			time.sleep(0.05)
			
			#print(self.data)

		self.sock.close()


	def open_controller(self):
		sdl2.SDL_JoystickEventState(sdl2.SDL_ENABLE)
		sdl2.SDL_JoystickOpen(0)
		print("Opened Joystick")

	def handle_events(self, event):
		# If Controller Event

		if event.type == sdl2.SDL_JOYAXISMOTION:
			if event.jaxis.axis == 0:
				# Left- right movement (x)
				
				xValue = int(event.jaxis.value/CONTROLLER_SMOOTH)
				if (xValue < -DEAD_ZONE):
					xValue = xValue + DEAD_ZONE
					self.rov_data[0] = str(xValue)
				elif (xValue > DEAD_ZONE):
					xValue = xValue - DEAD_ZONE
					self.rov_data[0] = str(xValue)
			
			elif event.jaxis.axis == 1:
				# Up Down movement (y)
				yValue = int(event.jaxis.value/CONTROLLER_SMOOTH)

				if (yValue < -DEAD_ZONE):
					yValue = yValue + DEAD_ZONE
					self.rov_data[1] = str(yValue)
				elif (yValue > DEAD_ZONE):
					yValue = yValue - DEAD_ZONE
					self.rov_data[1] = str(yValue)


		if event.type == sdl2.SDL_JOYBUTTONDOWN:
			print("Key pressed")
			self.running = False

		# Other Events

	def create_string(self, rov_data):
		string = ""
		string += "T"
		for i in range(2):
			string += rov_data[i] + ","
		
		string += ";"

		return string










netClient = NetworkClient()



