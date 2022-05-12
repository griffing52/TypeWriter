# send gcode to machine
# https://3dprinting.stackexchange.com/questions/17845/how-to-send-g-code-directly-from-a-raspberry-pi-to-my-printer-without-using-any
# https://www.thingiverse.com/groups/raspberry-pi564/forums/general/topic:31728

import numpy as np
import imutils
import cv2.aruco as aruco
import cv2

def findArucoMarkers(img, markerSize=6, totalMarkers=250, draw=True):
    """
    It takes an image, converts it to grayscale, and then uses the aruco library to find aruco markers
    in the image
    
    :param img: The image to be processed
    :param markerSize: The size of the markers in cm, defaults to 6 (optional)
    :param totalMarkers: The number of markers in the dictionary, defaults to 250 (optional)
    :param draw: If True, the detected markers will be drawn on the image, defaults to True (optional)
    """
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    arucoDict = arucod.Dictionary_get(aruco.DICT_6x6_250)