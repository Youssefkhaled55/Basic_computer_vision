#New feature here to text parameter of 
# the video and time and show  all
# at window
import cv2 
import datetime
cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(3,3000)
cap.set(4,3000)

print(cap.get(3))
print(cap.get(4))
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        font = cv2.FONT_HERSHEY_SIMPLEX
#(cv2.FONT_HERSHEY_SIMPLEX): Function to start texting in video
        text = 'Width: '+ str(cap.get(3)) + 'Height: ' + str(cap.get(4))
#Text width and height on screen of video
        datet = str(datetime.datetime.now())
#(str(datetime.datetime.now())): Determine time as string to get
#Real time by year, month, day, time 
        frame = cv2.putText(frame, text, (10, 50), font, 1, (0, 255, 255), 2)
        frame = cv2.putText(frame, datet, (10, 100), font, 1, (0, 255, 255), 2)
        cv2.imshow('frame',frame)
#Show parameter and time and determine coordinates and font type and scale
#Also a color and Thickness   
    ch = cv2.waitKey(1)
    if ch & 0xFF == ord('q'):
       break
cap.release()
cv2.destroyAllWindows() 