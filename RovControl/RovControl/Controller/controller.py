# This is the class for anything joystick related
#
# Use it to open Joysticks, read data, configure etc.
# It uses the SDL2 library with the pySDL2 wrapper
# found at: https://pysdl2.readthedocs.org/en/latest/
#
# UiS Subsea 2015

import sdl2
import sdl2.ext
import threading
import time

CONTROLLER_SMOOTH = 100
DEAD_ZONE = 100

class Controller(object):



	def __init__(self):

		sdl2.SDL_Init(sdl2.SDL_INIT_JOYSTICK)
		if not (self.check_SDL_Error()):
			print ("Joystick subsystem initialized")

		sdl2.SDL_JoystickEventState(sdl2.SDL_ENABLE)

		# Create thread

		# Try to open joystick

		self.open_controller()
		
		self.ctrl_adata = [""]
		self.ctrl_bdata = [""]

		self.thread = threading.Thread(target = self.controller_loop)
		self.thread.start()

	def controller_loop(self):

		# Get events
		self.running = True
		while(self.running):
			self.events = sdl2.ext.get_events()
			for event in self.events:
				self.handle_events(event)

			time.sleep(0.05)

	def handle_events(self, event):
		# If Controller Event

		if event.type == sdl2.SDL_JOYDEVICEADDED:
			# Open connected joystick
			self.open_controller()

		elif event.type == sdl2.SDL_JOYAXISMOTION:
			for i in range(self.num_axes): 
				
				if event.jaxis.axis == i:
					# Left- right movement (x)
				
					value = int(event.jaxis.value/CONTROLLER_SMOOTH)
					if (value < -DEAD_ZONE):
						value = value + DEAD_ZONE
						self.ctrl_adata[i] = str(value)
					elif (value > DEAD_ZONE):
						value = value - DEAD_ZONE
						self.ctrl_adata[i] = str(value)


		elif event.type == sdl2.SDL_JOYBUTTONDOWN or event.type == sdl2.SDL_JOYBUTTONUP:
			for i in range(self.num_btns):
				if event.jbutton.button == i:
					self.ctrl_bdata[i] = str(event.jbutton.state)
				print("Key pressed")
				#self.running = False

		# Other Events

	def open_controller(self):
		self.num_ctrl = sdl2.SDL_NumJoysticks()
		if self.num_ctrl != 0:
			self.ctrl = sdl2.SDL_JoystickOpen(self.num_ctrl - 1)
			print("Opened controller %s" %(sdl2.SDL_JoystickName(self.ctrl)))

			self.num_axes = sdl2.SDL_JoystickNumAxes(self.ctrl)
			self.num_btns = sdl2.SDL_JoystickNumButtons(self.ctrl)
			self.ctrl_adata = [""] * self.num_axes
			self.ctrl_bdata = [""] * self.num_btns
		else:
			print("No Controller detected!, Connect now")

	def get_buttonData(self):
		return self.ctrl_bdata

	def get_axisData(self):
		return self.ctrl_adata

def main():

	ctrl = Controller()

if __name__ == '__main__':
    main()

"""
elif event.type == sdl2.SDL_JOYAXISMOTION:
			for i in range(self.num_axes): 
				if event.jaxis.axis == 0:
					# Left- right movement (x)
				
					xValue = int(event.jaxis.value/CONTROLLER_SMOOTH)
					if (xValue < -DEAD_ZONE):
						xValue = xValue + DEAD_ZONE
						self.ctrl_data[0] = str(xValue)
					elif (xValue > DEAD_ZONE):
						xValue = xValue - DEAD_ZONE
						self.ctrl_data[0] = str(xValue)
			
			elif event.jaxis.axis == 1:
				# Up Down movement (y)
				yValue = int(event.jaxis.value/CONTROLLER_SMOOTH)

				if (yValue < -DEAD_ZONE):
					yValue = yValue + DEAD_ZONE
					self.ctrl_data[1] = str(yValue)
				elif (yValue > DEAD_ZONE):
					yValue = yValue - DEAD_ZONE
					self.ctrl_data[1] = str(yValue)
					"""
