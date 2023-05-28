import cv2
import numpy as np 
from matplotlib import pyplot as plt
import os
os.chdir(R" C:\Users\amb\Downloads")

img = cv2.imread('messi.jpg', 0)     #Sudoku
lap = cv2.Laplacian(img, cv2.CV_64F, ksize = 3)
lap = np.uint8(np.absolute(lap))

#sobel_x = cv2.Sobel(img,cv2.CV_64F, 1,0)
#sobel_y = cv2.Sobel(img,cv2.CV_64F, 0,1)

#sobel_X = np.uint8(np.absolute(sobel_X))
#sobel_Y = np.uint8(np.absolute(sobel_Y))

#compine_sobel_X_and_Y = cv2.bitwise_or(sobel_X, sobel_Y)

cv2.imshow('img', img)
cv2.imshow('laplacian', lap)
#cv2.imshow('sobel_X', sobel_X)
#cv2.imshow('sobel_Y', sobel_Y)
#cv2.imshow('compine_sobel_X_and_y', compine_sobel_X_and_y)

cv2.waitKey(0)
cv2.destroyAllWindows()