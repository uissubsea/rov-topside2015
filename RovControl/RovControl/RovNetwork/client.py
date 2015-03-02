import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print ("Connecting to '%s' port '%s'" %(server_address))
sock.connect(server_address)

try:

	# send Data

	message = "This is the message. It will be repeated."
	print ("sending message")
	sock.sendall(bytes(message, 'UTF-8'))

	amount_received = 0
	amount_expected = len(message)

	while amount_received < amount_expected:
		data = sock.recv(16)
		amount_received += len(data)
		print ("Received %s" % data)

finally:
	print ("Closing socket")
	sock.close()