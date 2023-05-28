import cv2
import time

print(cv2.__version__)

img = cv2.imread('apple.jpg',1)

print(img)

cv2.imshow('first image',img)
k = cv2.waitKey(0)
#Error(1): I wrote waitkey wrong
# It should be written by capital 
# k letter to be waitKey

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
#(ord) used to make order like 
#if I want to make somthing by press 
#Any key I want
#So here  I want to close tap 
#By pressing s letter
 
     cv2.imwrite('sec image.jpg',img)
cv2.destroyAllWindows()
     