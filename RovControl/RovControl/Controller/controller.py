# This is the class for anything joystick related
#
# Use it to open Joysticks, read data, configure etc.
# It uses the SDL2 library with the pySDL2 wrapper
# found at: https://pysdl2.readthedocs.org/en/latest/
#
# UiS Subsea 2015

import sdl2
import sys


class Controller(object):

	# Initiates joystick:
	def __init__(self):

		sdl2.SDL_Init(sdl2.SDL_INIT_JOYSTICK)
		print ("initialized controller subsystem")

		controller_connected = False
		num = self.number_of_controllers_connected()
		
		if (not controller_connected and num > 0):
			for i in range (num):
				self.open_controller(i)
				#print(sdl2.SDL_JoystickNameForIndex(i))
				controller_connected = True
		else:
			print("Make sure the controller is plugged in correctly!", 
				file = sys.stderr)


	def open_controller(self, id):
		self.controller = sdl2.SDL_JoystickOpen(id) #input: device index (Obs for flere kontrollere)


	def close_controller(self, id):
		sdl2.SDL_JoystickClose(id)
	

	def number_of_controllers_connected(self):
		return sdl2.SDL_NumJoysticks()


	def get_controller_name(self):
		num = self.number_of_controllers_connected()
		name_list = []
		
		if num > 0:
			for i in range(num):
				name_list.append(sdl2.SDL_JoystickNameForIndex(i))	
		else:
			print("No controllers connected")
			#list = NULL

		return name_list


	def get_controller_id(self):
		num = self.number_of_controllers_connected()
		id_list = []
		
		if num > 0:
			for i in range(num):
				#id_list.append(sdl2.SDL_JoystickInstanceID(self.controller))
				# --> returnerer kun idnr til siste tilkoblede kontroller!	
				id_list.append(i)
		else:
			print("No controllers connected")
			id_list = NULL

		return id_list


	def recognize_controllers(self):
		cntrs = self.get_controller_name()

		for i in range (len(cntrs)):
			if cntrs[i] == b'Controller':
				cntrs[i] = "xbox_" + str(i)
			if cntrs[i] == b'Logitech Extreme 3D':
				cntrs[i] = "logitech_joystick_" + str(i)
			if len(cntrs) == 0:
				cntrs = NULL
		
		# Returnerer liste med nye controller navn. Siste tall tilsvarer id-nr.
		return cntrs


	def read_axis(self, axis, smoothing):
		sdl2.SDL_JoystickUpdate()
		return sdl2.SDL_JoystickGetAxis(self.controller, axis) / smoothing


	# Returns axes to controller with ID id:
	def get_axes(self, id):
		return sld2.SDL_JoystickNumAxes(self.controller)


	def get_button_state(self, button):
		return sdl2.SDL_JoystickGetButton(self.controller, button)


	def get_buttons(self, id):
		list = []
		return list

##############################################################################
# For testing:
def main():
	test = Controller()
	print(test.get_controller_name())
	print(test.get_controller_id())
	print(test.recognize_controllers())

	
if __name__ == '__main__':
	main()

