#This code used to determine information in img by mouse event function
#left click used to determine coordinates in img
#right click used to determine color RGB range in img
import numpy as np
import cv2
import os 
os.chdir(r"C:\Users\yk406\.spyder-py3\media")

events = [i for i in dir(cv2) if 'EVENT' in  i]
print(events)
#(event): is many functions by same name of event but difference 
#in use all that un numpy library, but here we use to control 
#by mouse 

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,', ' ,y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ', '+ str(y)
        cv2.putText(img, strXY, (x, y), font, .5, (255, 255, 0), 2)
        cv2.imshow('image', img)
#(cv2.EVENT_LBUTTONDOWN): In this sector we use to show 
#up coordiantes by left click of mouse and write this text 
#by determine font type and scale of coordinates and color abd thickness
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        print(blue,', ' ,green,', ',red)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ', '+ str(green)+ ', '+ str(red)
        cv2.putText(img, strBGR, (x, y), font, .5, (0, 255, 255), 2)
        cv2.imshow('image', img)
#(cv2.EVENT_RBUTTONDOWN): In this sector we use to show 
#up RGB by right click of mouse and write this text 
#by determine font type and scale of RGB and color abd thickness
   

#img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread('apple.jpg')
cv2.imshow('image', img)

cv2.setMouseCallback('image', click_event)
#This part of code to return value of click to use more
#than one click
cv2.waitKey(0)
cv2.destroyAllWindows() 