import cv2
import numpy as np
import os
os.chdir(r'C:\Users\yk406\.spyder-py3')

while(True):
    frame = cv2.imread("pp.jpg")
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower = np.array([35,50,20])
    upper = np.array([65,255,255])
    
    mask = cv2.inRange(hsv, lower, upper)  #Threshold the HSV image to get Color blue
    res = cv2.bitwise_and(frame, frame, mask=mask)
    
    contours, hierarchy = cv2.findContours(mask,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if len(contours) != 0:
        for contour in contours:
            if cv2.contourArea(contour) > 500:
                x,y,w,h = cv2.boundingRect(contour)
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
    
    cv2.imshow("detecting the blue ball", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)
    
    k = cv2.waitKey(0)
    if k == 27:
         break
            
cv2.destroyAllWindows()