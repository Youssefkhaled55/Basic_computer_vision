#More example for event function by using mouse is by
#draw lines by put point.a and point.b in window
import numpy as np
import cv2

events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)
#Here to output all event libirary and their names

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),13,(255,0,0),-1)
#Raduis and Color of circle point in sketch and thickness 

        points.append((x,y))
        if len(points)>=2:
            cv2.line(img,points[-1],points[-2],(0, 255, 255))
            cv2.imshow('image', img)
#drawing be like put point a and put point b and draw line
#between the two points 
            
img = np.zeros((512, 512, 3), np.uint8)
#img = cv2.imread('apple.jpg')
cv2.imshow('image', img)
points = []

cv2.setMouseCallback('image', click_event)
#To return value of mouse and continues pointing and making lines

cv2.waitKey(0)
cv2.destroyAllWindows( )