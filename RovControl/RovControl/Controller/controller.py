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
from PyQt4 import QtCore


CIRCLE = True

class Controller(QtCore.QThread):

	def __init__(self):
		super(Controller, self).__init__()

		self.config = configparser.ConfigParser()
		self.config.read('Config/controller.cfg')

		self.inSettings = False

		sdl2.SDL_Init(sdl2.SDL_INIT_JOYSTICK)
		sdl2.SDL_JoystickEventState(sdl2.SDL_ENABLE)
		
		# List to hold references to connected controllers
		self.controllers = []

		# List to hold names, numbers and instance ids of connected controllers
		self.controllerNames = []
		self.controllerNumAxis = []
		self.controllerNumButtons = []
		self.instanceIDs = []

		# List to hold axisData for connected controllers
		self.axisData = []
		self.buttonData = []

		#Default values
		self.DEAD_ZONE = 100
		self.CONTROLLER_SMOOTH = 100


	def run(self):

		# Try to open Controllers
		#self.open_controller(0)
		
		# Get events
		if self.inSettings == False:

			self.running = True
			while(self.running):
				self.events = sdl2.ext.get_events()
				self.changed = False
				for event in self.events:
					self.handle_events(event)
				#self.changed = False
				#print(self.axisData)

				time.sleep(0.05)
		else:
			self.running = True
			while(self.running):
				self.events = sdl2.ext.get_events()
				self.changed = False
				for event in self.events:
					self.handle_SettingEvents(event)
				#self.changed = False
				#print(self.ctrl_axisdata)

				time.sleep(0.05)


	def handle_events(self, event):
		# If Controller Event

		if event.type == sdl2.SDL_JOYDEVICEADDED:
			# Open connected joystick
			self.open_controller()
			print("SDL_JOYDEVICEADDED")

		elif event.type == sdl2.SDL_JOYAXISMOTION:
			self.changed = True
			for i in range(len(self.instanceIDs)):
				if event.jaxis.which == i:
					for j in range(self.controllerNumAxis[i]): 
				
						if event.jaxis.axis == j:
							value = int(event.jaxis.value/self.CONTROLLER_SMOOTH)
							# Left- right movement (x)
							if event.jaxis.axis == 3:
								value = value + 670
							
							if (value > -self.DEAD_ZONE and value < self.DEAD_ZONE):
								#Inside Dead zone
								self.axisData[i][j] = 0

							elif (value < -self.DEAD_ZONE):
								value = value + self.DEAD_ZONE
								if (value < -1000):
									self.axisData[i][j] = -1000
								else:
									self.axisData[i][j] = value
					
							elif (value > self.DEAD_ZONE):
								value = value - self.DEAD_ZONE
								if (value > 1000):
									self.axisData[i][j] = 1000
								else:
									self.axisData[i][j] = value


		elif event.type == sdl2.SDL_JOYBUTTONDOWN or event.type == sdl2.SDL_JOYBUTTONUP:
			self.changed = True
			for i in range(self.controllerNumButtons[-1]):
				if event.jbutton.button == i:
					self.buttonData[i] = event.jbutton.state
				#print("Key pressed")
				#self.running = False
		# Other Events

	def handle_SettingEvents(self, event):
		# If Controller Event

		if event.type == sdl2.SDL_JOYDEVICEADDED:
			# Open connected joystick
			self.open_controller()
			print("SDL_JOYDEVICEADDED")

		elif event.type == sdl2.SDL_JOYAXISMOTION:
			self.changed = True
			for i in range(len(self.instanceIDs)):
				if event.jaxis.which == i:
					for j in range(self.controllerNumAxis[i]): 
				
						if event.jaxis.axis == j:
							value = int(event.jaxis.value/self.CONTROLLER_SMOOTH)
							# Left- right movement (x)
							if event.jaxis.axis == 3:
								value = value + 670
							
							if (value > -self.DEAD_ZONE and value < self.DEAD_ZONE):
								#Inside Dead zone
								self.axisData[i][j] = 0


							elif (value < -self.DEAD_ZONE):
								value = value + self.DEAD_ZONE
								self.emit(QtCore.SIGNAL('setText(QString)'), "Axis" + str(i))
								if (value < -1000):
									self.axisData[i][j] = -1000
								else:
									self.axisData[i][j] = value
					
							elif (value > self.DEAD_ZONE):
								value = value - self.DEAD_ZONE
								self.emit(QtCore.SIGNAL('setText(QString)'), "Axis" + str(i))
								if (value > 1000):
									self.axisData[i][j] = 1000
								else:
									self.axisData[i][j] = value


		elif event.type == sdl2.SDL_JOYBUTTONDOWN or event.type == sdl2.SDL_JOYBUTTONUP:
			self.changed = True
			for i in range(self.controllerNumButtons[-1]):
				if event.jbutton.button == i:
					self.buttonData[i] = event.jbutton.state
				#print("Key pressed")
				#self.running = False
		# Other Events



	def open_controller(self, index = None):
		
		self.num_ctrl = sdl2.SDL_NumJoysticks()
		
		if self.num_ctrl != 0:
			
			if index is None:
				self.controllers.append(sdl2.SDL_JoystickOpen(self.num_ctrl - 1))
				# Get instanceID
				self.instanceIDs.append(sdl2.SDL_JoystickInstanceID(self.controllers[-1]))
			else:
				self.controllers.append(sdl2.SDL_JoystickOpen(index))
				# Get instanceID
				self.instanceID.append(sdl2.SDL_JoystickInstanceID(self.controllers[-1]))

			# Log name of last connected joystick. -1 list index is last element
			self.controllerNames.append(sdl2.SDL_JoystickName(self.controllers[-1]))
			print("Opened controller %s" %(self.controllerNames[-1]))

			# The following 
			self.controllerNumAxis.append(sdl2.SDL_JoystickNumAxes(self.controllers[-1]))
			self.controllerNumButtons.append(sdl2.SDL_JoystickNumButtons(self.controllers[-1]))
			
			self.axisData.append([0] * self.controllerNumAxis[-1])
			self.buttonData.append([0] * self.controllerNumButtons[-1])

			# Determine if controller needs calibration.
			# Else Load data
			if( not str(self.controllerNames[-1]) in self.config.sections()):
				self.calibrate()
			else:
				try:
					self.DEAD_ZONE = int(self.config[str(self.controllerNames[-1])]['DEAD_ZONE'])
					self.CONTROLLER_SMOOTH = int(self.config[str(self.controllerNames[-1])]['SMOOTH'])
					#self.CONTROLLER_SMOOTH = self.CONTROLLER_SMOOTH + self.DEAD_ZONE
				except:
					print("Error getting config values")

		else:
			print("No Controller detected, Connect now")

	def connected_controllers(self):
		controllerList = []
		for i in range(len(self.controllers)):
			controllerList.append(str(sdl2.SDL_JoystickNameForIndex(i)))

		return controllerList


	def calibrate(self):
		# If We have entered this function, the config has no
		# section for our controller and needs to be calibrated
		# Let's add a section for our controller.

		self.config[str(self.controllerNames[-1])] = {}
		
		sdl2.SDL_JoystickUpdate()

		# While loop to determine max min values
		print("No controller config for this model was found")
		print("Calibration is required\n")
		print("Move all joystick axes and press main button when done")

		# create arrays to hold Max/Min Values
		self.ctrl_amax = [0] * self.controllerNumAxis[-1]
		self.ctrl_amin = [0] * self.controllerNumAxis[-1]

		while( not sdl2.SDL_JoystickGetButton(self.controllers[-1], 0)):
			for i in range(self.self.controllerNumAxis[-1]):
				sdl2.SDL_JoystickUpdate()
				value = sdl2.SDL_JoystickGetAxis(self.controllers[-1], i)
				if(value > self.ctrl_amax[i]):
					self.ctrl_amax[i] = value;
				if(value < self.ctrl_amin[i]):
					self.ctrl_amin[i] = value
				

		# Max values should now be in ctrl_axisdata list.
		# Write values to config.
		for i in range(self.controllerNumAxis[-1]):
			#self.config.save_to_config(str(self.ctrl_name), "Axis" + str(i), str(self.ctrl_axisdata[i]))
			self.config[str(self.controllerNames[-1])]['Axis' + str(i) + "Max"] = str(self.ctrl_amax[i])
			self.config[str(self.controllerNames[-1])]['Axis' + str(i) + "Min"] = str(self.ctrl_amin[i])


		# Add default deadzone and filter
		self.config[str(self.controllerNames[-1])]['DEAD_ZONE'] = '100'
		self.config[str(self.controllerNames[-1])]['SMOOTH'] = '100'

		with open('Config/controller.cfg', 'w') as configfile:
			self.config.write(configfile)

		print("Done calibrating")

	def closeController(self):
		# Close controller and stop thread
		for i in range(len(self.controllers)):
			sdl2.SDL_JoystickClose(self.controllers[i])
			print("Closed controller %s" %(self.controllers[i]))