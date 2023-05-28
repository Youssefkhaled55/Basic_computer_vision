#Didn't finished
#Code Used to detect car plate and 
#Extract info from palte

import cv2 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import imutils
import easyocr
import os
os.chdir(r"C:\Users\yk406\.spyder-py3")

img = cv2.imread("image1.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.imshow(cv2.cvtColor(gray,cv2.COLOR_BGR2RGB))
bfilter = cv2.bilateralFilter(gray,11,17,17) #Noise reduction
edged = cv2.Canny(bfilter, 30, 200) #Edge detection
