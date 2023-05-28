import cv2
import numpy as np 
from matplotlib import pyplot as plt

img = cv2.imread('early_1800.png')

averaging = cv2.blur(img, (5,5))    #mean pixel
gblur = cv2.GaussianBlur(img, (5,5), 0) #for noise images but not all type
median = cv2.medianBlur(img,5)  #for salt and paper images
bilateralFilter = cv2.bilateralFilter(img, 9, 75, 75) #preserve the border

cv2.imshow('img', img)
cv2.imshow('averaging', averaging)
#cv2.imshow('gblur',gblur)
#cv2.imshow('median', median)
#cv2.imshow('bilateralFilter', bilateralFilter)

cv2.waitKey(0)
cv2.destroyAllWindows()
