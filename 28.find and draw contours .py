#Contours makes colored border in shape 
#But it's different types that can colored border by 
#just inside or outsid also can be both of them
import numpy as np
import cv2

img = cv2.imread('logo.png')
img = cv2.resize(img,(512,512))
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(imgray, 20, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

print("Number of contours = " + str(len(contours)))
print(contours[0])

cv2.drawContours(img, contours,-1, (0, 255, 0), 3)

cv2.imshow('Image', img)
cv2.imshow('Image GRAY', imgray)
cv2.imshow('thresh', thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()