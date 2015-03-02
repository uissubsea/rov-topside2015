#!/usr/bin/python

import sys
from PyQt4 import QtGui
from Gui import startWindow


def main():
    app = QtGui.QApplication(sys.argv)
    window = startWindow.StartWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()