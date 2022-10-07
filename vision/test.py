import cv2
import cv2.aruco as aruco
import numpy as np
 
# Turn on Laptop's webcam
cap = cv2.VideoCapture(0)
 
w = 200
h = 150

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
    dictionary = aruco.Dictionary_get(key)
    params = aruco.DetectorParameters_create()
    corners, ids, rejects = aruco.detectMarkers(gray_img, dictionary, parameters=params)


    # for corner in corners:
    #     cv2.circle(img, (int(corner[0][0][0]), int(corner[0][0][1])), 10, (0, 0, 255), 3)

    if draw:
        aruco.drawDetectedMarkers(img, corners, ids)
        # aruco.estimatePoseSingleMarkers(corners, 0.05, np.array([0]), np.array([0]), np.array([0]), np.array([0]))
    
    return (corners, ids)

pos=[None, None, None, None]
# positions: 0=tl, 1=tr, 2=bl, 3=br
pos_id = {203: 3, 62: 0, 98: 1, 40: 2}

while True:
     
    ret, frame = cap.read()
 
    corners, ids = findArucoMarkers(frame)

    for i, c in zip(ids, corners):
        if i[0] in pos_id:
            pos[pos_id[i[0]]] = c[0][0]

    try:
        pts1 = np.array(pos)
        pts2 = np.float32([[0,0], [w, 0], [w, h], [0, h]])
        # Apply Perspective Transform Algorithm
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        result = cv2.warpPerspective(frame, matrix, (w, h ))
        cv2.imshow('result', result) # Initial Capture
    except:
        pass    

    cv2.imshow('frame', frame) # Initial Capture
 
    if cv2.waitKey(24) == 27:
        break
 
cap.release()
cv2.destroyAllWindows()