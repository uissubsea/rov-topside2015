"""This is a simple echo server to test
	sending of controller signal """

import socket
import sys
import logging

logger = logging.getLogger("echoserverlog")
logger.setLevel(logging.DEBUG)
FORMAT = '[%(asctime)-15s][%(levelname)s][%(module)s][%(funcName)s] %(message)s'
logging.basicConfig(format=FORMAT)

def main():
	
	BUFFER_SIZE = 4092

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	server_address = ('localhost', 10000)

	logger.info("started server on %s, port %s" % server_address)

	sock.bind(server_address)
	# Listen for incomming connections
	sock.listen(1)

	while True:
		# Wait for connection
		logger.info("Waiting for connection")
		connection, client_address = sock.accept()

		try:
			#logger.info("Connection from", client_address)
			logger.info("Connected")

			while True:
				data = connection.recv(BUFFER_SIZE)
				if data:
					logger.info("Received %s" %(data))
				elif data == "Quit":
					break
		finally:
			connection.close()
			sock.close()
			break

if __name__ == '__main__':
    main()
