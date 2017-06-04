# Python 2/3 compatibility
from __future__ import print_function
import sys
PY3 = sys.version_info[0] == 3

import numpy as np
import cv2
from imutils import perspective
from imutils import contours
import numpy as np
import imutils
import os

import sys
fn = sys.argv[1]
global segged
img = cv2.imread(fn)
segged=img
if img is None:
	print('Failed to load image file:', fn)
	sys.exit(1)

cv2.imshow('original', img)

def update(dummy=None):
	rmin = cv2.getTrackbarPos('Rmin', 'color_sel')
	gmin = cv2.getTrackbarPos('Gmin', 'color_sel')
	bmin=cv2.getTrackbarPos('Bmin', 'color_sel')
	rmax=cv2.getTrackbarPos('Rmax', 'color_sel')
	gmax=cv2.getTrackbarPos('Gmax', 'color_sel')
	bmax=cv2.getTrackbarPos('Bmax', 'color_sel')
	segged=cv2.inRange(img,(bmin,gmin,rmin),(bmax,gmax,rmax))
	X=None
	X=cv2.bitwise_and(img,img,mask=segged)
	cv2.imshow('segmented',X)
cv2.namedWindow('segmented')
cv2.namedWindow('color_sel')
cv2.createTrackbar('Rmin', 'color_sel', 0, 255, update)
cv2.createTrackbar('Gmin', 'color_sel', 0, 255, update)
cv2.createTrackbar('Bmin', 'color_sel', 0, 255, update)
cv2.createTrackbar('Rmax', 'color_sel', 0, 255, update)
cv2.createTrackbar('Gmax', 'color_sel', 0, 255, update)
cv2.createTrackbar('Bmax', 'color_sel', 0, 255, update)
update()
while True:
	ch = 0xFF & cv2.waitKey()
	if ch == 27:
		break
	update()
cv2.destroyAllWindows()