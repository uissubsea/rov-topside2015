# Config Tool					
# Uis Subsea					
# Author : Tor Morten Finnesand
# Configurations are saved in a config file using the following 
# Syntax:
# 'Option' \t 'value' \n
#

def open_config(str):
	# check if file exists. If not create empty file and give a warning
	try:
		f = open(str, 'r+')
	except IOError:
		print ("File Not found.. Creating\n")
		f = open(str, 'r+')
	else:
		print ("File opened successfully!")
		return f

def write_config(option, value, f):
	# Check if option exists
	for line in f:
		splitted = line.split("\t", 2)
		if splitted[0] == option:
			f.seek(0)
			f.write(option + "\t" + value + "\n")
			f.seek(0, 0) 	# Set pointer to start of file
			return True
	
	f.seek(0, 2)			# Set pointer to end of file
	f.write(option + "\t" + value + "\n")

def close_config(f):
	f.close()
	print ("File closed")

# f = open_config("config.cfg")
# write_config("Test", "211", f)
# write_config("Test", "233", f)
# write_config("Test2", "000", f)
# close_config(f)


