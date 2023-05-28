#This same output of code but the difference here that I
#control number of times that I want to minimize or maxmize
import cv2
import numpy as np
img = cv2.imread("lena.jpg")

layer = img.copy()
gp = [layer]

for i in range(6):
    layer = cv2.pryDown(layer)
    gp.append(layer)
    cv2.imshow(str(i), layer)
    
cv2.imshow("Original image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()