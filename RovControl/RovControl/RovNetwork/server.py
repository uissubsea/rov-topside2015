import socket
import sys
import threading
import logging

class Server(object):


	def __init__(self, server_address='localhost', port=10000):

		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# Bind socket to port

		self.server_address = (server_address, port)
		self.sock.bind(self.server_address)

	def start_server(self):
		self.sock.listen(1)

		while True:
			# Wait for a connection
			print ("Waiting for connection")
			self.connection, self.client_address = self.sock.accept()

			try:
				print ("Connection from: ", self.client_address)

				# Receive data in chunks and retransmit them
				while True:
					self.buffer = self.receive_data()
					print ("Received :", self.buffer)
					if self.buffer:
						print ("Sending back to client")
						self.send_all(self.buffer)
					else:
						print("No more data from Client: ", self.client_address)
						break

			finally:
				self.close_connection()

	def close_connection(self):
		self.connection.close()

	def send_all(self, data):
		self.connection.sendall(data)

	def receive_data(self):
		return self.connection.recv(16)

def main():
	network = Server()
	network.start_server()


if __name__ == '__main__':
    main()