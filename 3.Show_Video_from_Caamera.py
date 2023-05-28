#This code used to capture video live
#From laptop
#Video will close after press q word 
import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#(fourcc): It's an video code used to 
#Improve video visual pixels 
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
#I determin width and height of frame 
print(cap.isOpened())
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        out.write(frame)
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #(cv2.COLOR_BGR2GRAY): function to turn video from 
        #Color video to Gray video 
        cv2.imshow('frame', gray)
        #cv2.imshow('frame', frame)
           
        if cv2.waitKey(1)== ord('q'):
            #[ord('q')]:Want to close window by press q letter
            break
    else:
            break
        
cap.release()
out.release()
cv2.destroyAllWindows()


#Video will close after time duration 
#after sec video will close
import cv2
import time

timeout = time.time() + 10  # 10 s
cap = cv2.VideoCapture(0)

while time.time() < timeout: # set the time out rule
  _, frame = cap.read()
  cv2.waitKey(1)
  cv2.imshow('Frame', frame)
  
cap.release()
cv2.destroyAllWindows()





