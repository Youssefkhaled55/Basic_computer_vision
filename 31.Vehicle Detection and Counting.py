#31.Vehicle Detection and Counting
import cv2 
import numpy as np
#from time import sleep
import os
os.chidir(R"C:\Users\amb\Downloads")

ww = 80
hh = 80
offset = 6
y1 = 550

# FPS to video
delay = 60

detec = []
carros = 0

def pega_center(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx, cy

cap = cv2.VideoCapture('video.mp4')

BGS = cv2.bgsegm.createBackgroundSubtractorMOG()

while True:
    
    ret, frame1 = cap.read()
    #print(frame1.shape)
    #tempo = float(1/delay)
    #sleep(tempo)
    
    grey = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey, (3, 3), 5)
    img_sub = BGS.apply(blur)
    dilat = cv2.dilate(img_sub, np.ones((5, 5)))
    
    # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    # dilatada = cv2.morphologyEx(dilat, cv2.MORPH_CLOSE, kernel) #dilat then erode
    # dilatada = cv2.morphologyEx(dilatada, cv2.MORPH_CLOSE, kernel)
    
    contor, h = cv2.findContours(dilat, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    cv2.line(frame1, (25, y1), (1200, y1), (176, 130, 39), )
    
    for(i, c) in enumerate(contor):
        (x, y, w, h) = cv2.boundingRect(c)
        
        validar_contorno = (w >= ww) and (h >= hh)
        if not validar_contorno:
            continue
                
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        center = pega_center(x, y, w, h)
        detec.append(center)
        cv2.circle(frame1, center, 4, (0, 0, 255), -1)
        
        for(x,y) in detec:
            if(y < (y1 + offset)) and (y > (y1-offset)):
                carros += 1
                cv2.line(frame1, (25, y1), (1200, y1),(0, 127, 255), 3)
                detec.remove((x, y))
                print("No. of cars detected:  " + str(carros))
                
    cv2.putText(frame1, "VEHICLE COU NT: " + str(carros), (320, 70), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 4)
    cv2.imshow("Video Original", frame1)
    cv2.imshow("dilat", dilat)
    cv2.imshow("img_sub", img_sub)
    
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()
cap.release()