# This is the class for anything joystick related
#
# Use it to open Joysticks, read data, configure etc.
# It uses the SDL2 library with the pySDL2 wrapper
# found at: https://pysdl2.readthedocs.org/en/latest/
#
# UiS Subsea 2015

import sdl2

class Joystick(object):

	def __init__(self):
		# List connected joysticks ?
		sdl2.SDL_Init(sdl2.SDL_INIT_JOYSTICK)
		if not (self.check_SDL_Error()):
			print ("Joystick subsystem initialized")

	def list_joysticks(self):
		# Read Number of joysticks and 
		# print the name and index to console
		number_of_sticks = sdl2.SDL_NumJoysticks()
		if number_of_sticks > 0:
			for i in range(number_of_sticks):
				print ("Joystick %d : %s" %(i + 1, sdl2.SDL_JoystickNameForIndex(i)))
		else:
			print ("No Joysticks connected")

	def open_joystick(self, id):
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

	def close_joystick(self):
		sdl2.SDL_JoystickClose(self.joy)
		#sdl2.SDL_Quit()

	## Todo ##
	# Add method:
	# Calibrate_Joystick
	# Method to read button values
	# Method to list buttons

joystick = Joystick()

joystick.list_joysticks()

joystick.open_joystick(0)

while True:
	print ("X: %d \t\t Y: %d\r" %(joystick.read_axis(0,100), joystick.read_axis(1,100)), end="")
