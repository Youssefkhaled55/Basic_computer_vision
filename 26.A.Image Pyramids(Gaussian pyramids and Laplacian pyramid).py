#So pyrimad function used to minimize or maxmize origianl 
#img with same reslution
import cv2 
import numpy as np

img = cv2.imread("lena.jpg")
lr1 = cv2.pyrDown(img)
lr2 = cv2.pyrDown(lr1)

hr2 = cv2.pryUp(lr2)

cv2.imshow("Origianl image", img)
cv2.imshow("lr1", lr1)
cv2.imhow("lr2",lr2)
cv2.imhow("hr2",hr2)

cv2.waitKey(0)
cv2.destroyAllWindows()