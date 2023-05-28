import cv2
import numpy as np 
from matplotlib import pyplot as plt

img = cv2.imread('smarties.png',0)
_,mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

kernel = np.ones((5,5), np.uint8)
dilation = cv2.dilate(mask,kernel,iterations=2)   #Good but increase that balls
erosion = cv2.erode(mask,kernel,iterations=1)     #It erode the balls because
opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel,iterations=1) #eros
closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel,iterations=1) #dilation

cv2.imshow('gray_img',img)
cv2.imshow('mask',mask)
cv2.imshow('after dilation', dilation)
cv2.imshow('after erosion', erosion)
cv2.imshow('after opening', opening)
cv2.imshow('after closing', closing)

cv2.waitKey(0)
cv2.destroyAllWindows()