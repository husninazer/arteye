"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

import cv2

from PIL import Image, ImageDraw
import numpy as np
####
import random

from gaze_tracking import GazeTracking

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)

coordinates = []

while True:
    # We get a new frame from the webcam
    _, frame = webcam.read()

    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    text = ""

    if gaze.is_blinking():
        text = "Blinking"
    elif gaze.is_right():
        text = "Looking right"
    elif gaze.is_left():
        text = "Looking left"
    elif gaze.is_center():
        text = "Looking center"

    cv2.putText(frame, text, (20, 30),
                cv2.FONT_HERSHEY_DUPLEX, .8, 255, 2)

    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (20, 60),
                cv2.FONT_HERSHEY_DUPLEX, 0.6, 255, 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (20, 90),
                cv2.FONT_HERSHEY_DUPLEX, 0.6, 255, 1)

    x = 0
    y = 0
    x=left_pupil
    y=right_pupil

    if x:
        coordinates.append(x)
        coordinates.append(y)

    print(coordinates)

# stop looping
    length = len(coordinates)
    if length > 200:
        break

    cv2.imshow("Demo", frame)

    if cv2.waitKey(1) == 27:
        break


#####
im = Image.new('RGB', (1000, 600), (128, 128, 128))
draw = ImageDraw.Draw(im)
for n in range(len(coordinates)):
    line = (coordinates[n][0],coordinates[n][1], coordinates[n-1][0],coordinates[n-1][1])
    draw.line(line, fill=0, width=6)

im.show('my.png')



