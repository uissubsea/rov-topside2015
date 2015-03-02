import cv2

from PyQt4 import QtGui

class OpenCVQImage(QtGui.QImage):

	def __init__(self, opencvBgrImg):
		depth, nChannels = opemcvBgrImg.depth, opencvBgrImg.nChannels
		if depth != cv2.IPL_DEPTH_8U or nChannels != 3:
			raise ValueError("The input image must be 8-bit, 3 channel")

		w, h = cv.GetSize(opencvBgrImg)
		opencvRgbImg = cv2.CreateImage((w, h), depth, nChannels)

		# Assuming the image is in BGR format

		cv2.CvtColor(opencvBgrImg, opencvRgbImg, cv2.CV_BGR2RGB)
		self._imgData = opencvRgbImg.tostring()

		super(OpenCVQImage, self).__init__(self._imgData, w, h, QtGui.QImage.Format_RGB888)

class CameraDevice(QtCore.QObject):

	_DEFAULT_FPS = 30

	newFrame = QtCore.pyqtSignal(cv2.iplimage)

	def __init__(self, cameraId=0, mirrored=False, parent=None):
		super(CameraDevice, self).__init__(parent)

		self.mirrored = mirrored

		self._cameraDevice = cv2.VideoCapture(cameraId)

		self._timer = QtCore.QTimer(self)
		self._timer.timeout.connect(self._queryFrame)
		self._timer.setInterval(1000/self.fps)

		self.paused = False

	@QtCore.pyqtSlot()
	def _queryFrame(self):
		frame = cv2.QueryFrame(self._cameraDevice)
		if self.mirrored:
			mirroredFrame = cv2.CreateImage(cv2.GetSize(frame), frame.depth, \
				frame.nChannels)
			cv2.Flip(frame, mirroredFrame, 1)
			frame = mirroredFrame
		self.newFrame.emit(frame)

	@property
	def frameSize(self):
		w = cv2.GetCaptureProperty(self._cameraDevice, cv2.CV_CAP_PROP_FRAME_WIDTH)
		h = cv2.GetCaptureProperty(self._cameraDevice, cv2.CV_CAP_PROP_FRAME_HEIGHT)

		return int(w), int(h)

	@property
	def fps(self):
		fps = int(cv2.GetCaptureProperty(self._cameraDevice, cv2.CV_CAP_PROP_FPS))
		if not fps > 0:
			fps = self._DEFAULT_FPS
		return fps

class CameraWidget(QtGui.QWidget):

	newFrame = QtCore.pyqtSignal(cv2.iplimage)

	def __init__(self, cameraDevice, parent=None):
		super(CameraWidget, self).__init__(parent)

		self._frame = None

		self._cameraDevice = cameraDevice

		self._cameraDevice.newFrame.connect(self._onNewFrame)

		w, h = self._cameraDevice.frameSize

		self.setMinimumSize(w, h)
		self.setMaximumSize(w, h)

	@QtCore.pyqtSlot(cv2.iplimage)
	def _onNewFrame(self, frame):
		self._frame = cv2.CloneImage(frame)
		self.newFrame.emit(self._frame)
		self.update()

	def changeEvent(self, e):
		if e.type() == QtCore.QEvent.EnabledChange:
			if self.isEnabled():
				self._cameraDevice.newFrame.connect(self._onNewFrame)
			else:
				self._cameraDevice.newFrame.disconnect(self._onNewFrame)

	def paintEvent(self, e):
		if self._frame is None:
			return
		painter = QtGui.QPainter(self)
		painter.drawImage(QtCore.QPoint(0, 0), OpenCVQImage(self._frame))

def _main():

	@QtCore.pyqtSlot(cv2.iplimage)
	def onNewFrame(frame):
		cv2.CvtColor(frame, frame, cv2.CV_RGB2BGR)
		msg = "processed frame"
		font = cv2.InitFont(cv2.CV_FONT_HERSHEY_DUPLEX, 1.0, 1.0)
		tsize, baseline = cv2.GetTextSize(msg, font)
		w, h = cv2.GetSize(frame)
		tpt = (w - tsize[0]) / 2, (h - tsize[1]) / 2
		cv2.PutText(frame, msg, tpt, font, cv2.RGB(255, 0, 0))

	import sys

	app = QtGui.QApplication(sys.argv)

	cameraDevice = CameraDevice(cameraId='backer.avi')

	cameraWidget = CameraWidget(cameraDevice)
	cameraWidget.newFrame.connect(onNewFrame)
	cameraWidget.show()

	sys.exit(app.exec_())

if __name__ == '__main__':
    main()