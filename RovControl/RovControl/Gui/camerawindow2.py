import sys
import cv2
import numpy as np
from PyQt4 import QtGui, QtCore, Qt

class Video(object):
	def __init__(self, capture):
		self.capture = capture
		self.currentFrame = np.array([])

	def captureNextFrame(self):

		