import sys
sys.path.insert(1, '../Controller')


from Controller import controller
import socket
import threading
import time
#import statuslogger

class NetworkClient():
	def __init__(self, address=192.168.1.20, port=50000):

		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server_address = (address, port)

		#Create thread to run
		self.thread = threading.Thread(target = start_client)
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

		# Open Joystick

		controller = controller.Controller()
		controller.open_controller(0)

		# Thread Loop
		while True:
			if (controller.get_button_state(1)):
				self.sock.sendall(bytes("Quit", "UTF-8"))
				break

			self.value = str(controller.read_axis(1, 100))
			self.sock.sendall(bytes(self.value, 'UTF-8'))

			# Receive back from ROV and log
			self.data = sock.recv(16)
			time.sleep(0.05)

		self.sock.close()





