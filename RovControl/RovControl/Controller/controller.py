# This is the class for anything joystick related
#
# Use it to open Joysticks, read data, configure etc.
# It uses the SDL2 library with the pySDL2 wrapper
# found at: https://pysdl2.readthedocs.org/en/latest/
#
# UiS Subsea 2015
import sys
import sdl2
import sdl2.ext
import threading
import time
import configparser


CIRCLE = True

class Controller(object):

	def __init__(self):

		self.config = configparser.ConfigParser()
		self.config.read('controller.cfg')

		sdl2.SDL_Init(sdl2.SDL_INIT_JOYSTICK)

		sdl2.SDL_JoystickEventState(sdl2.SDL_ENABLE)

		#Default values
		self.DEAD_ZONE = 100
		self.CONTROLLER_SMOOTH = 100

		# Create thread

		# Try to open joystick

		self.open_controller()
		
		self.ctrl_adata = [0]
		self.ctrl_bdata = [0]

		self.thread = threading.Thread(target = self.controller_loop)
		self.thread.start()

	def controller_loop(self):

		# Get events
		self.running = True
		while(self.running):
			self.events = sdl2.ext.get_events()
			self.changed = False
			for event in self.events:
				self.handle_events(event)
			#self.changed = False
			#print(self.ctrl_adata)

			time.sleep(0.05)

	def handle_events(self, event):
		# If Controller Event
		if event.type == sdl2.SDL_JOYDEVICEADDED:
			# Open connected joystick
			self.open_controller()

		elif event.type == sdl2.SDL_JOYAXISMOTION:
			self.changed = True
			for i in range(self.num_axes): 
				
				if event.jaxis.axis == i:
					# Left- right movement (x)
					value = int(event.jaxis.value/self.CONTROLLER_SMOOTH)
					if (value > -self.DEAD_ZONE and value < self.DEAD_ZONE):
						#Inside Dead zone
						self.ctrl_adata[i] = 0

					elif (value < -self.DEAD_ZONE):
						value = value + self.DEAD_ZONE
						if (value < -1000):
							self.ctrl_adata[i] = -1000
						else:
							self.ctrl_adata[i] = value
					
					elif (value > self.DEAD_ZONE):
						value = value - self.DEAD_ZONE
						if (value > 1000):
							self.ctrl_adata[i] = 1000
						else:
							self.ctrl_adata[i] = value


		elif event.type == sdl2.SDL_JOYBUTTONDOWN or event.type == sdl2.SDL_JOYBUTTONUP:
			self.changed = True
			for i in range(self.num_btns):
				if event.jbutton.button == i:
					self.ctrl_bdata[i] = event.jbutton.state
				#print("Key pressed")
				#self.running = False
		# Other Events

	def open_controller(self):
		self.num_ctrl = sdl2.SDL_NumJoysticks()
		if self.num_ctrl != 0:
			self.ctrl = sdl2.SDL_JoystickOpen(self.num_ctrl - 1)
			self.ctrl_name = sdl2.SDL_JoystickName(self.ctrl)
			print("Opened controller %s" %(self.ctrl_name))

			self.num_axes = sdl2.SDL_JoystickNumAxes(self.ctrl)
			self.num_btns = sdl2.SDL_JoystickNumButtons(self.ctrl)
			self.ctrl_adata = [0] * self.num_axes
			self.ctrl_bdata = [0] * self.num_btns

			# Determine if controller needs calibration.
			# Else Load data
			if( not str(self.ctrl_name) in self.config.sections()):
				self.calibrate()
			else:
				try:
					self.DEAD_ZONE = int(self.config[str(self.ctrl_name)]['DEAD_ZONE'])
					self.CONTROLLER_SMOOTH = int(self.config[str(self.ctrl_name)]['SMOOTH'])
					#self.CONTROLLER_SMOOTH = self.CONTROLLER_SMOOTH + self.DEAD_ZONE
				except:
					print("Error getting config values")

		else:
			print("No Controller detected!, Connect now")

	def get_buttonData(self):
		return self.ctrl_bdata

	def get_axisData(self):
		return self.ctrl_adata

	def calibrate(self):
		# If We have entered this function, the config has no
		# section for our controller and needs to be calibrated
		# Let's add a section for our controller.

		self.config[str(self.ctrl_name)] = {}
		
		sdl2.SDL_JoystickUpdate()

		# While loop to determine max min values
		print("No controller config for this model was found")
		print("Calibration is required\n")
		print("Move all joystick axes and press main button when done")

		# create arrays to hold Max/Min Values
		self.ctrl_amax = [0] * self.num_axes
		self.ctrl_amin = [0] * self.num_axes

		while( not sdl2.SDL_JoystickGetButton(self.ctrl, 0)):
			for i in range(self.num_axes):
				sdl2.SDL_JoystickUpdate()
				value = sdl2.SDL_JoystickGetAxis(self.ctrl, i)
				if(value > self.ctrl_amax[i]):
					self.ctrl_amax[i] = value;
				if(value < self.ctrl_amin[i]):
					self.ctrl_amin[i] = value
				

		# Max values should now be in ctrl_adata list.
		# Write values to config.
		for i in range(self.num_axes):
			#self.config.save_to_config(str(self.ctrl_name), "Axis" + str(i), str(self.ctrl_adata[i]))
			self.config[str(self.ctrl_name)]['Axis' + str(i) + "Max"] = str(self.ctrl_amax[i])
			self.config[str(self.ctrl_name)]['Axis' + str(i) + "Min"] = str(self.ctrl_amin[i])


		# Add default deadzone and filter
		self.config[str(self.ctrl_name)]['DEAD_ZONE'] = '100'
		self.config[str(self.ctrl_name)]['SMOOTH'] = "100"

		with open('controller.cfg', 'w') as configfile:
			self.config.write(configfile)

		print("Done calibrating")


def main():

	ctrl = Controller()

if __name__ == '__main__':
    main()