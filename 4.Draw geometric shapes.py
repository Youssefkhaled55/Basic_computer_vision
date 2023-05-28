#In this section I will draw using opencv
#By Importing numpy library and cv
#note: I comment most of code to not show all in window
#So real comments will be numerical
import numpy as np 
import cv2 

#img = cv2.imread('DG.jpg',1)
img = np.zeros([512, 512, 3], np.uint8)
#1.(np.zeros): function to get black window by  adding
#size of width and height and number of matrix

img = cv2.line(img, (0,0), (256,256), (0,255,0), 10)
#2.(cv2.line): will be by choose img and determine point.a
#And point.b and then add color at least choose thickness

img = cv2.arrowedLine(img, (0,255), (256,255), (255,0,0), 10)
#3.(cv2.arrowedLine): will draw arrow line by choose img and adding point.a
#point.b and color and thickness

img = cv2.rectangle(img, (384,0), (510,128), (0,0,255), 10)
#4.(cv2.rectangLe): drawing rectangle by select img and  write point.a
#And point.b and choose color at last thickness

#Note: In Thickness part if I wrote -1 it will full up shape 
#The shape will not be hollow

img = cv2.circle(img, (447,63), 63, (0, 255, 0), 1)
#5.(cv2.circle): Drawing circle by select img and write point to draw
#And write raduis of circle and choose color and thickness

font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'OpenCv', (10,190), font, 4, (0,255,255), 10)
#6.(cv2.FONT_HERSHEY_SIMPLEX),(cv2.putText): Writing text will be by
#Select img and put text I want to wrote and coordinates and type of
#font and font scale at last color and thickness


img = cv2.ellipse(img, (256,256),(100,50),0,0,180,255,-1)
#7.(cv2.ellipse):drawing ellipse by select img and  write center
#And axes,angle, startAngle, endAngle and choose color at last thickness

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
img = cv2.polylines(img,[pts],True,(0,255,255))
#8.(np.array)(cv2.polyLines):Here to draw anything I want by adding points and 
#select img at first and (True) if I want to connect last point to 
#first point and (False) if to not connect and choose color

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()