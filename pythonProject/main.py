import time

import cv2
import numpy as np
import datetime
from pathlib import Path


camera_width = 1920
camera_height = 1080
fotoframe_boader = 100  # px
screen_width, screen_height = 1920, 1080
imgwindow = "fotobooth"


event_name = "weddding" #defined the name where the images are stored
frame_name = "frame.png" #the name of the custom frame

script_path = Path(__file__).parent
storage_path = script_path/event_name
Path.mkdir(storage_path,exist_ok=True)
frame_path = script_path/frame_name

# Set up the camera
camera_index = 0
camera = cv2.VideoCapture(camera_index)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, camera_width)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, camera_height)

fotoframe = cv2.imread(frame_path.name, cv2.IMREAD_UNCHANGED)
fotoframe = cv2.resize(fotoframe, (camera_width + 2 * fotoframe_boader, camera_height + 2 * fotoframe_boader))
alpha_ = fotoframe[:, :, 3]
fotoframe = fotoframe[:, :, :3]
alpha = ((alpha_ / 255)-1)*-1

flashimage = np.ones_like(fotoframe)*200


cv2.namedWindow(imgwindow, cv2.WINDOW_NORMAL)
cv2.setWindowProperty(imgwindow,  cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

running = True

while running:
    retval, image = camera.read()
    # fotoframe[100:2260,100:3940] = image
    canvas = np.zeros_like(fotoframe)
    canvas[fotoframe_boader:(camera_height + fotoframe_boader),fotoframe_boader:(camera_width + fotoframe_boader)] = image
    canvas[:,:,0] = canvas[:,:,0] * alpha
    canvas[:, :, 1] = canvas[:, :, 1] * alpha
    canvas[:, :, 2] = canvas[:, :, 2] * alpha
    canvas = canvas + fotoframe
    canvas = cv2.resize(canvas, (screen_width, screen_height))
    cv2.imshow(imgwindow, canvas)
    k = cv2.waitKey(33)
    if k == 32:
        # Capture a photo
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = storage_path/f"{timestamp}.jpg"
        cv2.imwrite(filename.__str__(), canvas)
        cv2.imshow(imgwindow, flashimage )
        cv2.waitKey(60)
    elif k == 27:
        running = False
    #else:
        #print(k)
# Clean up

cv2.destroyAllWindows()
