# This is the class for anything joystick related
#
# Use it to open Joysticks, read data, configure etc.
# It uses the SDL2 library with the pySDL2 wrapper
# found at: https://pysdl2.readthedocs.org/en/latest/
#
# UiS Subsea 2015

import sdl2

class Controller(object):

	def __init__(self):
		
		# List connected joysticks ?
		sdl2.SDL_Init(sdl2.SDL_INIT_JOYSTICK)
		if not (self.check_SDL_Error()):
			print ("Joystick subsystem initialized")

	def num_of_controllers(self):
		return sdl2.SDL_NumJoysticks()

	def list_controllers(self):
		
		# Read Number of joysticks and 
		# print the name and index to console
		number_of_controllers = self.num_of_controllers()
		if number_of_controllers > 0:
			for i in range(number_of_controllers):
				print ("Joystick %d : %s" %(i, sdl2.SDL_JoystickNameForIndex(i)))
		else:
			print ("No Joysticks connected")

	def get_controllers(self):
		
		# Returns the names of the attached joysticks in a list
		list = []
		for i in range(self.num_of_sticks()):
			list.append(sdl2.SDL_JoystickNameForIndex(i))

		return list

	def num_of_axes(self, id):
		return sld2.SDL_JoystickNumAxes(self.joy)

	def open_controller(self, id):
		
		self.joy = sdl2.SDL_JoystickOpen(id)
		self.check_SDL_Error()

	def check_SDL_Error(self):
		
		err = sdl2.SDL_GetError()
		if (err):
			print (err)
			return True
		else:
			return False

	def read_axis(self, axis, smoothing):
		
		sdl2.SDL_JoystickUpdate()

		return sdl2.SDL_JoystickGetAxis(self.joy, axis) / smoothing

	def get_button_state(self, button):
		return sdl2.SDL_JoystickGetButton(self.joy, button)

	def close_controller(self):
		sdl2.SDL_JoystickClose(self.joy)
		#sdl2.SDL_Quit()

	## Todo ##
	# Add method:
	# Calibrate_Joystick
	# Method to read button values
	# Method to list buttons
