#import numpy as np
import cv2 as cv
import os
os.chdir(r"C:\Users\yk406\.spyder-py3")

img = cv.imread('image.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

sift = cv.SIFT_create()
kp = sift.detect(gray)
img = cv.drawKeypoints(gray,kp,None)

cv.imshow("Keypoints", img)


cv.waitKey(0)
cv.destroyAllWindows()

img = cv.drawKeypoints(gray,kp,img,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv.imshow("Keypoints",img)

cv.waitKey(0)
cv.destroyAllWindows()

sift = cv.SIFT_creat()
kp, des = sift.detectAndCompute(gray)
imgg = cv.drawKeypoints(gray,kp,img)
cv.imshow("Keypoints", imgg)
cv.waitKey(0)
cv.destroyAllWindows()
print(des)

