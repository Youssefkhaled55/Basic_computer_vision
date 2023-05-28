import cv2 
import mediapipe as mp
import os

os.chdir(r"C:\Users\yk406\.spyder-py3")

image = cv2.imread("cars.jpg")
image = cv2.resize(image,(650,500))

# Convert it to greyscale
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Threshold the image 
ret, thresh = cv2.threshold(img,50,255,0)

#Find the contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#for each contour, find the convex hull and draw it
#on the original image.
for i in range(len(contours)):
    hull = cv2.convexHull(contours[i])
    cv2.drawContours(image, [hull], -1, (255,0,0),2)
#Display the final convex hull image
cv2.imshow('ConvexHull', image)
cv2.waitKey(0)