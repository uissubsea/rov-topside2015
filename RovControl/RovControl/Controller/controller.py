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

		#Default values
		self.DEAD_ZONE = 100
		self.CONTROLLER_SMOOTH = 100
		
		# Stores value from axis no. i in ctrl_axisdata[i]
		self.ctrl_axisdata = [0]
		# Stores value from button no. i in ctrl_buttondata[i]
		self.ctrl_buttondata = [0]



	def run(self):

		# Try to open joystick
		#self.open_controller()
		
		# Get events
		if self.inSettings == False:

			self.running = True
			while(self.running):
				self.events = sdl2.ext.get_events()
				self.changed = False
				for event in self.events:
					self.handle_events(event)
				#self.changed = False
				#print(self.ctrl_axisdata)

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

		elif event.type == sdl2.SDL_JOYAXISMOTION:
			self.changed = True
			for i in range(self.num_axes): 
				
				if event.jaxis.axis == i:
					# Left- right movement (x)
					value = int(event.jaxis.value/self.CONTROLLER_SMOOTH)
					if (value > -self.DEAD_ZONE and value < self.DEAD_ZONE):
						#Inside Dead zone
						self.ctrl_axisdata[i] = 0

					elif (value < -self.DEAD_ZONE):
						value = value + self.DEAD_ZONE
						if (value < -1000):
							self.ctrl_axisdata[i] = -1000
						else:
							self.ctrl_axisdata[i] = value
					
					elif (value > self.DEAD_ZONE):
						value = value - self.DEAD_ZONE
						if (value > 1000):
							self.ctrl_axisdata[i] = 1000
						else:
							self.ctrl_axisdata[i] = value


		elif event.type == sdl2.SDL_JOYBUTTONDOWN or event.type == sdl2.SDL_JOYBUTTONUP:
			self.changed = True
			for i in range(self.num_btns):
				if event.jbutton.button == i:
					self.ctrl_buttondata[i] = event.jbutton.state
				#print("Key pressed")
				#self.running = False
		# Other Events

	def handle_SettingEvents(self, event):
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
						self.ctrl_axisdata[i] = 0

					elif (value < -self.DEAD_ZONE):
						value = value + self.DEAD_ZONE
						if (value < -1000):
							self.ctrl_axisdata[i] = -1000
						else:
							self.ctrl_axisdata[i] = value
							# Emit Axis changed signal to Qt
							self.emit(QtCore.SIGNAL('setText(QString)'), "Axis" + str(i))
					
					elif (value > self.DEAD_ZONE):
						value = value - self.DEAD_ZONE
						if (value > 1000):
							self.ctrl_axisdata[i] = 1000
						else:
							self.ctrl_axisdata[i] = value
							# Emit Axis changed signal to Qt
							self.emit(QtCore.SIGNAL('setText(QString)'), "Axis" + str(i))


		elif event.type == sdl2.SDL_JOYBUTTONDOWN or event.type == sdl2.SDL_JOYBUTTONUP:
			self.changed = True
			for i in range(self.num_btns):
				if event.jbutton.button == i:
					self.emit(QtCore.SIGNAL('setText(Qstring)'), "Button" + str(i))
					self.ctrl_buttondata[i] = event.jbutton.state
				#print("Key pressed")
				#self.running = False
		# Other Events


	def open_controller(self, index = None):
		self.num_ctrl = sdl2.SDL_NumJoysticks()
		if self.num_ctrl != 0:
			if index is None:
				self.ctrl = sdl2.SDL_JoystickOpen(self.num_ctrl - 1)
			else:
				self.ctrl = sdl2.SDL_JoystickOpen(index)

			self.ctrl_name = sdl2.SDL_JoystickName(self.ctrl)
			print("Opened controller %s" %(self.ctrl_name))

			self.num_axes = sdl2.SDL_JoystickNumAxes(self.ctrl)
			self.num_btns = sdl2.SDL_JoystickNumButtons(self.ctrl)
			self.ctrl_axisdata = [0] * self.num_axes
			self.ctrl_buttondata = [0] * self.num_btns

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
			print("No Controller detected, Connect now")

	def connected_controllers(self):
		controllerList = []
		for i in range(self.num_ctrl):
			controllerList.append(str(sdl2.SDL_JoystickNameForIndex(i)))

		return controllerList


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
				

		# Max values should now be in ctrl_axisdata list.
		# Write values to config.
		for i in range(self.num_axes):
			#self.config.save_to_config(str(self.ctrl_name), "Axis" + str(i), str(self.ctrl_axisdata[i]))
			self.config[str(self.ctrl_name)]['Axis' + str(i) + "Max"] = str(self.ctrl_amax[i])
			self.config[str(self.ctrl_name)]['Axis' + str(i) + "Min"] = str(self.ctrl_amin[i])


		# Add default deadzone and filter
		self.config[str(self.ctrl_name)]['DEAD_ZONE'] = '100'
		self.config[str(self.ctrl_name)]['SMOOTH'] = '100'

		with open('Config/controller.cfg', 'w') as configfile:
			self.config.write(configfile)

		print("Done calibrating")

	def closeController(self):
		# Close controller and stop thread
		sdl2.SDL_JoystickClose(self.ctrl)
		print("Closed controller %s" %(self.ctrl_name))