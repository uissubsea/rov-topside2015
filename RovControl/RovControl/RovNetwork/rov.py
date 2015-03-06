# Rov
"""
1. Look for connection \
2. Accept connection
3. send status
4. receive config
5. send status
Two threads
6. receive joystick signal
7. send back sensor data

_____

package:
first 8 bit determine type of package
after 8 bit received message follows
"""

import socket
import threading
import logging

logger = logging.getLogger("rovSim")
logger.setLevel(logging.DEBUG)
FORMAT = '[%(asctime)-15s][%(levelname)s][%(module)s][%(funcName)s] %(message)s'
logging.basicConfig(format=FORMAT)

class RovServer():
	def __init__(self, address="127.0.0.1", port = 12345):

		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		self.server_address = (address, port)
		# Bind address and port to socket.
		self.sock.bind(self.server_address)

	def start_server(self):
		#Listen for connection
		self.sock.listen(1)

		while True:
			logger.debug("Waiting for connection")
			self.connection, self.client_address = self.sock.accept()
			try:
				logger.debug("Received connetion from %s" %(self.client_address))
				# Send Status
				self.sock.sendall(self.status_package("Allright"))
				# Receive config
				self.data = connection.recv(4096)
				if not self.data:
					# Config not received. Using standard settings
					logger.debug("Config not received, Using standard settings")
			except socket.error as msg:
				logger.error(msg)

			finally:
				self.socket.close()



	def status_package(self, msg):
		return 'STATUS' + msg

class RovClient():
	def __init__(self):

		self.sock.socket(socket.AF_INET, socket.SOCK_STREAM)

		
		
	
	def connect_to_server(self, address="127.0.0.1", port = 12345):
		self.server_address = (address, port)
		self.sock.connect(server_address)

		while True:

			try:
				



def main():
    rov_server = RovServer()
    rov_server.start_server()

if __name__ == '__main__':
    main()
