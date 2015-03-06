from Joystick import Joystick

import socket
import threading
import logging
import time


logger = logging.getLogger("clientlog")
logger.setLevel(logging.DEBUG)
FORMAT = '[%(asctime)-15s][%(levelname)s][%(module)s][%(funcName)s] %(message)s'
logging.basicConfig(format=FORMAT)

def client():

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	server_address = ('localhost', 10000)
	
	try:
		sock.connect(server_address)
	except socket.error as msg:
		logger.error("Unable to connect, %s" %(msg))

	#Open joystick
	controller = Joystick.Joystick()
	controller.open_joystick(0) # Open first joystick
	while True:
		
		if (controller.get_button_state(1)):
			sock.sendall(bytes("Quit", 'UTF-8')) # Send Stop string to server
			break
			
		value = str(controller.read_axis(1, 100))
		sock.sendall(bytes(value, 'UTF-8'))
		#print(value)
		time.sleep(0.05)

	sock.close()

def main():
	thread = threading.Thread(target=client)
	thread.start()

if __name__ == '__main__':
    main()




