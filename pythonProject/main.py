import time

import pygame
import cv2
import numpy as np
import datetime

# Initialize Pygame
pygame.init()

camera_width = 3840
camera_height= 2160
fotoframe_boader = 100 # px
screen_width, screen_height = 1920, 1080

# Set up the camera
camera_index = 0
camera = cv2.VideoCapture(camera_index)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, camera_width)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, camera_height)

# Load the custom frame (replace 'frame.png' with your own frame)
frame_path = "frame.png"
frame_image = pygame.image.load(frame_path)

# Create a Pygame window

screen = pygame.display.set_mode((screen_width, screen_height),pygame.FULLSCREEN)

fotoframe= cv2.imread("frame.png")
fotoframe = cv2.resize(fotoframe,(camera_width+2*fotoframe_boader,camera_height+2*fotoframe_boader))
print(fotoframe.shape)



def get_cam_frame(camera):
    retval, image = camera.read()
    #fotoframe[100:2260,100:3940] = image
    fotoframe[fotoframe_boader:(camera_height+fotoframe_boader),fotoframe_boader:(camera_width+fotoframe_boader)] = image
    frame = cv2.resize(fotoframe,(screen_width,screen_height))
    frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
    frame = np.rot90(frame)
    frame = pygame.surfarray.make_surface(frame)
    return frame,fotoframe

def add_frame_around_image(frame, custom_frame):
    # Resize the custom frame to match the webcam frame size
    custom_frame = pygame.transform.scale(custom_frame, (frame.get_width(), frame.get_height()))
    frame.blit(custom_frame, (0, 0))
    return frame

running = True


while running:
    frame,image = get_cam_frame(camera=camera)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Capture a photo
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                filename = f"captured_photo_{timestamp}.jpg"
                cv2.imwrite(filename, image)
                screen.fill((255, 255, 255))  # Set background to black
                pygame.display.flip()
                time.sleep(0.3)
            elif event.key == pygame.K_ESCAPE:
                running = False


    screen.fill((0, 0, 0))  # Set background to black
    screen.blit(frame, (0, 0))
    pygame.display.flip()

# Clean up
pygame.quit()
cv2.destroyAllWindows()
