# send gcode to machine
# https://3dprinting.stackexchange.com/questions/17845/how-to-send-g-code-directly-from-a-raspberry-pi-to-my-printer-without-using-any
# https://www.thingiverse.com/groups/raspberry-pi564/forums/general/topic:31728

import numpy as np
import cv2.aruco as aruco
import cv2

test = cv2.imread('C:\\Users\\griff\\Documents\\Github\\TypeWriter\\vision\\markertest.jpg')

def findArucoMarkers(img, marker_size=6, total_markers=250, draw=True):
    """
    It takes an image, converts it to grayscale, and then uses the aruco library to find aruco markers
    in the image
    
    :param img: The image to be processed
    :param markerSize: The size of the markers in cm, defaults to 6 (optional)
    :param totalMarkers: The number of markers in the dictionary, defaults to 250 (optional)
    :param draw: If True, the detected markers will be drawn on the image, defaults to True (optional)
    """
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    key = getattr(aruco, f'DICT_{marker_size}X{marker_size}_{total_markers}')
    dict = aruco.Dictionary_get(key)
    params = aruco.DetectorParameters_create()
    boxs, ids, rejects = aruco.detectMarkers(gray_img, dict, parameters=params)

    if draw:
        aruco.drawDetectedMarkers(img, boxs)

def main():
    # cap = cv2.VideoCapture(0)

    findArucoMarkers(test)
    
    cv2.imshow('Test', test)


    # to use it in a loop
    k = cv2.waitKey(0)
    if k == 27:         # wait for ESC key to exit
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()