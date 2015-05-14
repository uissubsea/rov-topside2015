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
import time
import configparser
from PyQt4 import QtCore, QtGui
import re
import math

CIRCLE = True

class Controller(QtCore.QThread):
	#gui-signal for calibreringsvindu:
	calibrateNow = QtCore.pyqtSignal()
	calibrateDone = QtCore.pyqtSignal()

	def __init__(self):
		super(Controller, self).__init__()

		self.config = configparser.ConfigParser()
		self.config.read('Config/controller.cfg')

		self.inSettings = False

		sdl2.SDL_Init(sdl2.SDL_INIT_JOYSTICK)
		sdl2.SDL_JoystickEventState(sdl2.SDL_ENABLE)

		self.changed = False
		
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

		# Lists to hold Settings for connected Controllers
		self.controllerDeadZone = []
		self.controllerSmooth = []

		self.controllerMap = []
		self.stringMap = []
		self.controlFunction = []

		self.thrusterMap = []
		self.manipMap = []
		self.inverseMap = []

		self.thData = [0] * 4
		self.manipData = [0] * 6

		self.ThLinValue = []
		self.thExpvalue = []
		self.manipExpValue = []
		self.manipLinValue = []

		# Define Qt Signals
		self.ControlAdded = QtCore.pyqtSignal(str)
		self.AxisChanged = QtCore.pyqtSignal(str)

		


	def run(self):

		# Try to open Controllers
		for i in range(sdl2.SDL_NumJoysticks()):
			self.open_controller(i)
		
		self.configController()

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

			self.closeController()

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

			self.closeController()


	def handle_events(self, event):
		# If Controller Event

		#if event.type == sdl2.SDL_JOYDEVICEADDED:
		#	# Open connected joystick
		#	self.open_controller()
		#	print("SDL_JOYDEVICEADDED")

		if event.type == sdl2.SDL_JOYAXISMOTION:
			self.changed = True
			for i in range(len(self.instanceIDs)):
				if event.jaxis.which == i:
					for j in range(self.controllerNumAxis[i]): 
				
						if event.jaxis.axis == j:
							value = int(event.jaxis.value)
							if j == 1:
								value = value *-1							
							# Left- right movement (x)
							#if event.jaxis.axis == 2:
							#	value = value + 670
							
							if (value > -self.controllerDeadZone[i]*50 and value < self.controllerDeadZone[i]*50):
								#Inside Dead zone
								self.axisData[i][j] = 0

							elif (value < -self.controllerDeadZone[i]*50):
								value = value + self.controllerDeadZone[i]
								self.axisData[i][j] = value
					
							elif (value > self.controllerDeadZone[i]*50):
								value = value - self.controllerDeadZone[i]
								self.axisData[i][j] = value


		elif event.type == sdl2.SDL_JOYBUTTONDOWN or event.type == sdl2.SDL_JOYBUTTONUP:
			self.changed = True
			for i in range(len(self.instanceIDs)):
				if event.jaxis.which == i:
					
					for j in range(self.controllerNumButtons[i]):
						if event.jbutton.button == j:
							self.buttonData[i][j] = event.jbutton.state
							#print("Key pressed")
							#self.running = False
		# Other Events

	def handle_SettingEvents(self, event):
		
		# If Controller Event

		#if event.type == sdl2.SDL_JOYDEVICEADDED:
		#	# Open connected joystick
		#	self.open_controller()
		#	print("SDL_JOYDEVICEADDED")

		if event.type == sdl2.SDL_JOYAXISMOTION:
			self.changed = True
			for i in range(len(self.instanceIDs)):
				if event.jaxis.which == i:
					for j in range(self.controllerNumAxis[i]): 
				
						if event.jaxis.axis == j:
							value = int(event.jaxis.value)
							# Left- right movement (x)
							#if event.jaxis.axis == 2:
							#	value = value + 670

							if (value < -5000):
								value = value + self.controllerDeadZone[i]
								self.emit(QtCore.SIGNAL('setText(QString)'), "Axis" + str(j))
						
							elif (value > 5000):
								value = value - self.controllerDeadZone[i]
								self.emit(QtCore.SIGNAL('setText(QString)'), "Axis" + str(j))


		elif event.type == sdl2.SDL_JOYBUTTONDOWN or event.type == sdl2.SDL_JOYBUTTONUP:
			self.changed = True
			for i in range(len(self.instanceIDs)):
				if event.jaxis.which == i:
					
					for j in range(self.controllerNumButtons[i]):
						if event.jbutton.button == j:
							self.emit(QtCore.SIGNAL('setText(QString)'), "Btn" + str(j))
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
				self.instanceIDs.append(sdl2.SDL_JoystickInstanceID(self.controllers[-1]))

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

	def configController(self):

		# Get map for each controller
		for idx, controller in enumerate(self.controllerNames):
			self.thrusterMap.append(self.config[str(controller)]["ThMap"])
			self.manipMap.append(self.config[str(controller)]["ManipMap"])
			self.ThLinValue.append(self.config[str(controller)]["thlin"])
			self.thExpvalue.append(self.config[str(controller)]["thExp"])
			self.manipLinValue.append(self.config[str(controller)]["malin"])
			self.manipExpValue.append(self.config[str(controller)]["maExp"])
			self.thrusterMap[idx] = re.findall(r'\d+', self.thrusterMap[idx])
			self.manipMap[idx] = re.findall(r'\d+', self.manipMap[idx])
			self.controllerDeadZone.append(int(self.config[str(self.controllerNames[-1])]['DEAD_ZONE']))
			self.controllerSmooth.append(int(self.config[str(self.controllerNames[-1])]['SMOOTH']))

		# Convert from string to int
		for i in range(len(self.controllerNames)):
			for j in range(len(self.thrusterMap[i])):
				self.thrusterMap[i][j] = int(self.thrusterMap[i][j])

		for i in range(len(self.controllerNames)):
			for j in range(len(self.manipMap[i])):
				self.manipMap[i][j] = int(self.manipMap[i][j])

		for i in range(len(self.controllerNames)):
			self.ThLinValue[i] = int(self.ThLinValue[i])

		for i in range(len(self.controllerNames)):
			self.thExpvalue[i] = int(self.thExpvalue[i])

		for i in range(len(self.controllerNames)):
			self.manipLinValue[i] = int(self.manipLinValue[i])

		for i in range(len(self.controllerNames)):
			self.manipExpValue[i] = int(self.manipExpValue[i])


	def process_controller(self):
		
		for i in range(len(self.axisData)):
			for j in range(len(self.thrusterMap[i])):
				valueTh = self.axisData[i][self.thrusterMap[i][j]]
				if(self.ThLinValue[i] > 1):
					valueTh = int(valueTh/self.ThLinValue[i])
				else:
					#Use exponential
					valueTh = int(valueTh*0.02*math.pow(self.thExpvalue[i],3))
				#if j == 0 or j == 2:
				#	self.thData[j] = value * -1
				#else:
				self.thData[j] = valueTh
			for j in range(len(self.manipMap[i])):
				valueManip = self.axisData[i][self.manipMap[i][j]]
				if(self.manipLinValue[i] > 1):
					valueManip = int(valueManip/self.manipLinValue[i])
				else:
					#Use exponential
					valueManip = int(valueManip*0.02*math.pow(self.manipExpValue[i],3))

				if j == 4 or j == 5:
					valueManip = valueManip + 65
				self.manipData[j] = valueManip



	def calibrate(self):
		# If We have entered this function, the config has no
		# section for our controller and needs to be calibrated
		# Let's add a section for our controller.

		self.config[str(self.controllerNames[-1])] = {}
		
		sdl2.SDL_JoystickUpdate()

		# While loop to determine max min values
		self.calibrateNow.emit()
		print("No controller config for this model was found")
		print("Calibration is required\n")
		print("Move all joystick axes and press main button when done")		

		# Add default deadzone and filter
		self.config[str(self.controllerNames[-1])]['DEAD_ZONE'] = '100'
		self.config[str(self.controllerNames[-1])]['SMOOTH'] = '29'

		# Add map subsection
		self.config[str(self.controllerNames[-1])]['ManipMap'] = ''
		self.config[str(self.controllerNames[-1])]['thMap'] = ''
		self.config[str(self.controllerNames[-1])]['btnMap'] = ''

		# Add exp and lin values
		self.config[str(self.controllerNames[-1])]['thLin'] = ''
		self.config[str(self.controllerNames[-1])]['maLin'] = ''
		self.config[str(self.controllerNames[-1])]['thExp'] = ''
		self.config[str(self.controllerNames[-1])]['maExp'] = ''

		self.controllerDeadZone.append(int(self.config[str(self.controllerNames[-1])]['DEAD_ZONE']))
		self.controllerSmooth.append(int(self.config[str(self.controllerNames[-1])]['SMOOTH']))

		# create arrays to hold Max/Min Values
		self.ctrl_amax = [0] * self.controllerNumAxis[-1]
		self.ctrl_amin = [0] * self.controllerNumAxis[-1]

		while( not sdl2.SDL_JoystickGetButton(self.controllers[-1], 0)):
			for i in range(self.controllerNumAxis[-1]):
				sdl2.SDL_JoystickUpdate()
				value = sdl2.SDL_JoystickGetAxis(self.controllers[-1], i)
				value = value / self.controllerSmooth[-1]
				
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


		with open('Config/controller.cfg', 'w') as configfile:
			self.config.write(configfile)

		print("Done calibrating")
		self.calibrateDone.emit()


	def closeController(self):
		# Close controller

		self.running = False

		for i in range(len(self.controllers)):
			sdl2.SDL_JoystickClose(self.controllers[i])
			print("Closed controller %s" %(self.controllers[i]))








