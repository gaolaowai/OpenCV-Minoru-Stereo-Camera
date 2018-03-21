# Tested on Ubuntu 16.04 with opencv 3.4.0.12. Should work in any 3.X version (and probably 2.4, though I've not tested).

import numpy as np
import cv2
import time

#
# If computer already has webcam, the minoru will be devices /dev/Video1 and /dev/Video2.
# This can be tested from the command line by unplugging the minoru and running:
# "ls /dev/vid*". If your computer has a built-in camera, a single device should be shown. 
# Plug minoru back into your computer, wait 30 seconds, then run the above command again.
# It should show two new devices. These represent the right and left cameras.
# On my systems, video1 is right, and video2 is left. Yours may vary.
#

# create the video capture object for right and left sides.
right_camera = cv2.VideoCapture(1) # 1 = /dev/video1
left_camera = cv2.VideoCapture(2) # 2 = /dev/video2

#
# setting the framerate and resolution
# By default, each camera tries to send 30FPS at 640x480. For USB2, it cannot handle both cameras
# at this framerate for this resolution. So, we can either reduce the framerate, or resolution.
# I'll do both, as an example.
#

# Print the default settings:
print("Right camera height: ", right_camera.get(3))
print("Right camera width: ", right_camera.get(4))
print("Right camera FPS: ", right_camera.get(5))

print("Left camera height: ", left_camera.get(3))
print("Left camera width: ", left_camera.get(4))
print("Left camera FPS: ", left_camera.get(5))

# Change the settings:
right_camera.set(3, 240.0) # Second parameter needs to be a float.
right_camera.set(4, 320.0)
right_camera.set(5, 15.0)

left_camera.set(3, 240.0) # Second parameter needs to be a float.
left_camera.set(4, 320.0)
left_camera.set(5, 15.0)

# Print new settings, to confirm that changes stuck.
print("Right camera new height: ", right_camera.get(3))
print("Right camera new width: ", right_camera.get(4))
print("Right camera new FPS: ", right_camera.get(5))

print("Left camera new height: ", left_camera.get(3))
print("Left camera new width: ", left_camera.get(4))
print("Left camera new FPS: ", left_camera.get(5))

# Start the main capture loop.
while True:
  # The cameras are not syncronized, so by doing the below grab() method, 
  # we decrease the delay between when the data is pulled from the two cameras.
  right.grab()
  left.grab()
  
  # Pull the data from the grab.
  # This function by default returns a tuple with boolean, plus the frame data. 
  # I'm unpacking it into two variables, ret for return status, and frame for frame data.
  rret, rframe = right.retrieve() 
  lret, lframe = left.retrieve()
  
  # Show the frames
  cv2.imshow('Right', rframe)
  cv2.imshow('Left', lframe)
  
  k = cv2.waitKey(5) & 0xff # Check for 'q' key or Esc
  if k == 27:
    break

# After breaking out of loop, release the camera devices and destroy the windows used to display the frames.
right.release()
left.release()
cv2.destroyAllWindows()
  
