import cv2
import matplotlib.pyplot as plt
import os
os.chdir(r"C:\Users\yk406\.spyder-py3")

#The input image
image = cv2.imread("blobs.jpg",0)

#Set up the SimpleBlibdetector with default parameters
params = cv2.SimpleBlobDetector_params()

#Define threshold
#Can define thresholdStep. See documentation
params.minThreshold = 0
params.maxThreshold = 255

#Fillter by Area
params.filterByArea = True
params.minArea = 50
params.maxArea = 10000

#Filter by Color(black=0)
params.filterByColor = False  #Set true for cast_iron
params.blobColor = 0

#Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.5
params.maxCircularity = 1

#Filter by Convexity
params.filterByConvexity = True
params.minConvexity = 0.1
params.maxConvexity = 1

#Setup the detector with parameters
detector = cv2.SimpleBlobDetector_create(params)

#Detect blobs
keypoints = detector.detect(image)
print("Number of blobs detected are: ", len(keypoints))

#Draw blobs
img_with_blobs = cv2.drawKeypoints(image,keypoints,None,(0,0,255),cv2.DRAW_MATCHS_FLAGS_DRAW_RICH_KEYPOINTS)
plt.imshow(img_with_blobs)
cv2.imshow("Keypoints", img_with_blobs)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Save all result
cv2.imwrite("particle blobs.jpg", img_with_blobs)

