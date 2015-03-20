# This is the class for anything joystick related
#
# Use it to open Joysticks, read data, configure etc.
# It uses the SDL2 library with the pySDL2 wrapper
# found at: https://pysdl2.readthedocs.org/en/latest/
#
# UiS Subsea 2015

import sdl2

class Controller2():
	def __init__(self):
		# Start Sdl 2  joystick Subsystem
		sdl2.SDL_Init(sdl2.SDL_INIT_GAMECONTROLLER);

		self.controller_connected = False
		while not self.controller_connected:
			try:
				self.controller = sdl2.SDL_GameControllerOpen(0)
				print ("initialized joystick %s" %(sdl2.SDL_GameContro))

