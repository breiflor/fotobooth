import time

import cv2
import numpy as np
import datetime
from pathlib import Path
import pygame

pygame.init()

camera_width = 1920
camera_height = 1080
fotoframe_boader = 100  # px
screen_width, screen_height = 1920, 1080
imgwindow = "fotobooth"


event_name = "weddding" #defined the name where the images are stored
frame_name = "frame.png" #the name of the custom frame

screen = pygame.display.set_mode((screen_width, screen_height),pygame.FULLSCREEN)

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

running = True

while running:
    retval, image = camera.read()
    canvas = np.zeros_like(fotoframe)
    canvas[fotoframe_boader:(camera_height + fotoframe_boader),fotoframe_boader:(camera_width + fotoframe_boader)] = image
    canvas[:,:,0] = canvas[:,:,0] * alpha
    canvas[:, :, 1] = canvas[:, :, 1] * alpha
    canvas[:, :, 2] = canvas[:, :, 2] * alpha
    canvas = canvas + fotoframe


    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Capture a photo
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                filename = storage_path / f"{timestamp}.jpg"
                cv2.imwrite(filename.__str__(), canvas)
                screen.fill((255, 255, 255))  # Set background to black
                pygame.display.flip()
                time.sleep(0.3)
            elif event.key == pygame.K_ESCAPE:
                running = False

    frame = cv2.resize(canvas, (screen_width, screen_height))
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    frame = np.rot90(frame)
    frame = np.flipud(frame)
    frame = pygame.surfarray.make_surface(frame)
    screen.blit(frame, (0, 0))
    pygame.display.flip()

# Clean up
pygame.quit()
cv2.destroyAllWindows()
