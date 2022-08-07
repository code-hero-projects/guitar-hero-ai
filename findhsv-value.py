#finding hsv range of target object(pen)
import cv2
import numpy as np


# A required callback method that goes into the trackbar function.
def nothing(x):
    pass

# Initializing the webcam feed.
#cap = cv2.VideoCapture(0)
#cap.set(3,1280)
#cap.set(4,720)

# Create a window named trackbars.
cv2.namedWindow("Trackbars")

# Now create 6 trackbars that will control the lower and upper range of 
# H,S and V channels. The Arguments are like this: Name of trackbar, 
# window name, range,callback function. For Hue the range is 0-179 and
# for S,V its 0-255.
cv2.createTrackbar("L - H", "Trackbars", 19, 179, nothing)
cv2.createTrackbar("L - S", "Trackbars", 168, 255, nothing)
cv2.createTrackbar("L - V", "Trackbars", 60, 255, nothing)
cv2.createTrackbar("U - H", "Trackbars", 45, 179, nothing)
cv2.createTrackbar("U - S", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U - V", "Trackbars", 255, 255, nothing)
 
image_frame = cv2.imread('orange.png')
    
# Convert the BGR image to HSV image.
image_hsv = cv2.cvtColor(image_frame, cv2.COLOR_BGR2HSV)

sparkle_frame = cv2.imread('sparkle-1.png')
sparkle_hsv = cv2.cvtColor(sparkle_frame, cv2.COLOR_BGR2HSV)

while True:
    # Get the new values of the trackbar in real time as the user changes 
    # them
    l_h = cv2.getTrackbarPos("L - H", "Trackbars")
    l_s = cv2.getTrackbarPos("L - S", "Trackbars")
    l_v = cv2.getTrackbarPos("L - V", "Trackbars")
    u_h = cv2.getTrackbarPos("U - H", "Trackbars")
    u_s = cv2.getTrackbarPos("U - S", "Trackbars")
    u_v = cv2.getTrackbarPos("U - V", "Trackbars")
 
    # Set the lower and upper HSV range according to the value selected
    # by the trackbar
    lower_range = np.array([l_h, l_s, l_v])
    upper_range = np.array([u_h, u_s, u_v])
    
    # Filter the image and get the binary mask, where white represents 
    # your target color
    image_mask = cv2.inRange(image_hsv, lower_range, upper_range)
    sparkle_mask = cv2.inRange(sparkle_hsv, lower_range, upper_range)
    
    # Show this stacked frame at 40% of the size.
    cv2.imshow('image',cv2.resize(image_mask,None,fx=1.5,fy=1.5))
    cv2.imshow('sparkle',cv2.resize(sparkle_mask,None,fx=1.5,fy=1.5))
    
    # If the user presses ESC then exit the program
    key = cv2.waitKey(1)
    if key == 27:
        break
    
    # If the user presses `s` then print this array.
    if key == ord('s'):
        
        thearray = [[l_h,l_s,l_v],[u_h, u_s, u_v]]
        print(thearray)
        
        # Also save this array as penval.npy
        np.save('hsv_value',thearray)
        break
    
# Release the camera & destroy the windows.    
#cap.release()
cv2.destroyAllWindows()
