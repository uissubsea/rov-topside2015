from PyQt4.QtGui import QWidget
from PyQt4 import QtCore
from Gui import ui_remote

class Remote(QWidget):

    servoValueChanged = QtCore.pyqtSignal(int)

    def __init__(self):
        QWidget.__init__(self)

        self.ui = ui_remote.Ui_Remote()
        self.ui.setupUi(self)



