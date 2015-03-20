#import sys
#sys.path.insert(1, '../Controller')


from Controller import controller
import socket
import threading
import time
#import statuslogger

class NetworkClient():
	def __init__(self, address="192.168.1.20", port=50000):

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

		# Open Joystick

		controll = controller.Controller()
		controll.open_controller(0)

		# Thread Loop
		while True:
			if (controll.get_button_state(1)):
				self.sock.sendall(bytes("Quit", "UTF-8"))
				break

			self.value = str(int(controll.read_axis(1, 5)))
			self.sock.sendall(bytes(self.value, 'UTF-8'))

			# Receive back from ROV and log
			self.data = self.sock.recv(64)
			time.sleep(0.05)
			print(self.data)

		self.sock.close()

netClient = NetworkClient()



