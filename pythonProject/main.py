import time

import cv2
import numpy as np
import datetime



camera_width = 3840
camera_height= 2160
fotoframe_boader = 100 # px
screen_width, screen_height = 1920, 1080

# Set up the camera
camera_index = 0
camera = cv2.VideoCapture(camera_index)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, camera_width)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, camera_height)


fotoframe= cv2.imread("frame.png")
fotoframe = cv2.resize(fotoframe,(camera_width+2*fotoframe_boader,camera_height+2*fotoframe_boader))
fotoframe = np.flipud(fotoframe)

running = True

while running:
    retval, image = camera.read()
    # fotoframe[100:2260,100:3940] = image
    fotoframe[fotoframe_boader:(camera_height + fotoframe_boader),
    fotoframe_boader:(camera_width + fotoframe_boader)] = image
    frame = cv2.resize(fotoframe, (screen_width, screen_height))
    cv2.imshow("frame", frame)
    k = cv2.waitKey(33)
    if k == 32:
        # Capture a photo
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"captured_photo_{timestamp}.jpg"
        cv2.imwrite(filename, fotoframe)
    elif k == 27:
        running = False
    else :
        print(k)
# Clean up

cv2.destroyAllWindows()
