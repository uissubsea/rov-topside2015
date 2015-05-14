
from PyQt4 import QtGui
from Gui import mainwindow, settingswindow, statuswindow, pod2, controller_config

class MainWidget(QtGui.QMainWindow):
    
    def __init__(self):
        super(MainWidget, self).__init__()

        # Set up the user interface from Designer.
        self.ui = mainwindow.Ui_MainWindow()
        self.ui.setupUi(self)

        # Make some local modifications.

        # Connecting buttons
        self.ui.actionOptions.triggered.connect(self.open_settingsWindow)
        self.ui.actionStatus.triggered.connect(self.open_statusWindow)
        self.ui.actionPOD_2.triggered.connect(self.open_pod2)
        self.ui.actionController.triggered.connect(self.open_controllerConfig)

        self.show()

        self.subwindow1 = QtGui.QMdiSubWindow()
        self.subwindow2 = QtGui.QMdiSubWindow()
        self.subwindow3 = QtGui.QMdiSubWindow()
        self.subwindow4 = QtGui.QMdiSubWindow()


    def open_settingsWindow(self):
        self.cfgWindow = QtGui.QWidget()
        self.ui1 = settingswindow.Ui_SettingsWindow()
        self.ui1.setupUi(self.cfgWindow)
        self.subwindow1.setWidget(self.cfgWindow)
        self.ui.mdiArea.addSubWindow(self.subwindow1)
        self.cfgWindow.show()

    def open_statusWindow(self):
        self.statWindow = QtGui.QWidget()
        self.ui2 = statuswindow.Ui_StatusWindow()
        self.ui2.setupUi(self.statWindow)
        self.subwindow2.setWidget(self.statWindow)
        self.ui.mdiArea.addSubWindow(self.subwindow2)
        self.statWindow.show()

    def open_pod2(self):
        self.pod2Window = pod2.SubWindow()
        self.subwindow3.setWidget(self.pod2Window)
        self.ui.mdiArea.addSubWindow(self.subwindow3)
        self.pod2Window.show()

    def open_controllerConfig(self):
        self.cntrConfigWindow = QtGui.QWidget()
        self.ui4 = controller_config.Ui_controller_config()
        self.ui4.setupUi(self.cntrConfigWindow)
        self.subwindow4.setWidget(self.cntrConfigWindow)
        #self.ui.mdiArea.addSubWindow(self.subwindow4)
        self.cntrConfigWindow.show()


