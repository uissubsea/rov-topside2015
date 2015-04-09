# Config Tool					
# Uis Subsea					
# Author : Tor Morten Finnesand

import configparser

class Configurator:

	def __init__(self, config_file="rov_config.cfg"):
		self.config = configparser.ConfigParser()
		try:
			self.cfgfile = open(config_file,'w+')
		except IOError:
			print ("File Not found.. Creating\n")

		print("Opened %s" %(config_file))

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
			self.config.add_section(section)
			self.config.set(section, key, value)
			print("Added")

	def check_for_section(self, section):
		return self.config.has_section(section)

	def add_section_to_file(self, sectionToAdd):
		self.config.add_section(sectionToAdd)

	def close(self):
		#self.config.write(self.cfgfile)
		self.cfgfile.close()

	def write(self):
		self.config.write(self.cfgfile)

	def open(self):
		self.cfgfile = open("rov_config.ini",'w+')
