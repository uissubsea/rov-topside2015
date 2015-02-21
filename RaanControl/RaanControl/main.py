from PyQt4 import QtGui
import sys
from Gui import mainwindow

def main():

	app = QtGui.QApplication(sys.argv)
	window = mainwindow.MainWindow()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()