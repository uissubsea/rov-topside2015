## Config 2

import configparser

class Configurator:

	def __init__(self):
		self.config = configparser.ConfigParser()
		try:
			self.cfgfile = open("rov_config.ini",'w+')
		except IOError:
			print ("File Not found.. Creating\n")

		print("Config Opened!")

	def get_config(self, section):
		self.dict = {}
		self.options = self.config.options(section)

		for option in self.options:
			try:
				self.dict[option] = self.config.get(section, option)
				if self.dict[option] == -1:
					DebugPrint("skip: %s" %(option))
			except:
				print("Exception on %s!" % option)
				self.dict[option] = None

		return self.dict

	def save_to_config(self, section, key, value):
		try:
			self.config.set(section, key, value)
		except configparser.NoSectionError:
			print("No section with name %s" %(section))
			self.config.add_section(sectionToAdd)
			print("Added")

	def add_section_to_file(self, sectionToAdd):
		self.config.add_section(sectionToAdd)

	def close(self):
		#self.config.write(self.cfgfile)
		self.cfgfile.close()

	def write(self):
		self.config.write(self.cfgfile)

	def open(self):
		self.cfgfile = open("rov_config.ini",'w+')


#configurator = Configurator()

#configurator.add_section_to_file('Joystick')
#configurator.save_to_config('Joystick', 'deadzone', '10')
#configurator.save_to_config('Joystick', 'xmax', '260')
#configurator.save_to_config('Joystick', 'ymax', '260')
#configurator.save_to_config('Joystick', 'deadzone', '50')

#configurator.save_to_config('Test', 'test', 'Hey')

#configurator.write()
#configurator.close()
