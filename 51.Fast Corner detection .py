import cv2 as cv
import os
os.chdir(r"C:\Users\yk406\.spyder-py3")

img = cv.imread('house.jpg',0)

#initiate Fast object with default values
fast = cv.FastFeatureDetector_create()

#find and draw the keypoints
kp = fast.detect(img,None)
img2 = cv.drawKeypoints(img, kp, None, color=(255,0,0))

#print all default params
print("Threshold: {}".format(fast.getThreshold()))
print("nonmaxSuppression: {}".format(fast.getNonmaxSuppression()))
print("neighborhood: {}".format(fast.getType()))
print("Total keypoints with nonmaxSuppression: {}".format(len(kp)))
cv.imshow('fast_true',img2)

#Disable nonmaxSuppression
fast.setNonmaxSuppression(0)
kp = fast.detect(img,None)
print("Total keypoints without nonmaxSuppression: {}".format(len(kp)))
img3= cv.drawKeypoints(img, kp, None, color=(255,0,0))
cv.imshow('fast_false',img3)
cv.waitKey(0)
cv.destroyAllWindows()
