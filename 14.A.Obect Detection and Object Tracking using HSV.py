import cv2
import numpy as np
import os
os.chdir(r'C:\Users\yk406\.spyder-py3')

while(True):
    frame = cv2.imread("apple.jpg")
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    l_b = np.array([40,50,20])
    u_b = np.array([65,255,255])
    
    mask = cv2.inRange(hsv, l_b, u_b)  #Threshold the HSV image to get Color blue
    
    res = cv2.bitwise_and(frame, frame, mask=mask)
    
    cv2.imshow("detecting the blue ball", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)
    
    k = cv2.waitKey(0)
    if k == 27:
         break
            
cv2.destroyAllWindows()