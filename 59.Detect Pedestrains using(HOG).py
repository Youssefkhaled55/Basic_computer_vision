# Description: Detect pedestrains in video using 
# Histogram of Oriented Gradients (HOG) method

import cv2
import numpy as np
from imutils.object_detection import non_max_suppression
import os

os.chdir(r"C:\Users\yk406\.spyder-py3") 

#Make sure the video file is in the same directory as your code
filename = 'vtest.AVI'
file_size = (1920,1080)  #Assumes 1920x1080

#We want to save the output to video file 
output_filename = 'pedestrians_on_street.mp4'
output_frames_per_second = 20.0

def main():
    #Create a HOGDescriptor object
    hog = cv2.HOGDescriptor()
    
    #Initialize the people Detector
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    
    #Load a Video
    cap = cv2.VideoCapture(filename)
    
    #Create a VideoWriter object so we can save the video output
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    result = cv2.VideoWriter(output_filename,fourcc,output_frames_per_second,file_size)
    
    #Process the Video
    while cap.isOpened():
         #Capture one frame at time
         success, frame = cap.read()
            
         #Do we have a video frame? if true, procceed.
         if success:
            
         #Store the original frame
          orig_frame = frame.copy()
        
         (bounding_boxes, weights) = hog.detectMultiScale(frame,winStride=(4,4),padding=(8,8),scale=0.01)
        #Draw bounding boxes on the frame
         for(x,y,w,h) in bounding_boxes:
            cv2.rectangle(orig_frame,(x,y),(x+w,y+h),(0,0,255),2)
            
            #Get rid of overlapping bounding boxes
            #You can tweak the overlapThresh value for better results
            
            bounding_boxes = np.array([[x,y,x+w,y+h]for(x,y,w,h) in bounding_boxes])
            selection = non_max_suppression(bounding_boxes)
            
            #Draw the final bounding boxes
            for (x1,y1,x2,y2) in selection:
                cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),4)
            
            #Write the frame to the output Video file
            result.write(frame)
            
            #Display the frame
            cv2.imshow("Frame",frame)
            
            #Display frame for X milliseconds and checkif q key is pressed
            #  q == quit
            if cv2.waitKey(1) == ord('q'):
               break
            
        #No more video frames left
         else:
            break
    # Stop when the Video is finished
    cap.release()
    # Close all windows
    cv2.destroyAllWindows()
    
main()