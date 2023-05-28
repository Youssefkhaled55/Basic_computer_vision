#Here we begain to resize video captuer
import cv2 
from tkinter import *

def display_coordinates(event):
    my_label['text']=f'x=[event.x] y=[event.y]'
    
my_window = Tk()
my_canvas = Canvas(my_window, width=400,height=400,background='white')
my_label = Label(bd=4,relief="solid",font="Times 22 bold",bg="white",fg="black")
my_canvas.bind('<Button-1>',display_coordinates)
my_canvas.grid(row=0, column=0)
my_label.grid(row=1, column=0)
my_window.mainloop()
cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(3,1000)
cap.set(4,1000)
#(cap.set):used to parameter width and height
#Of the video 

print(cap.get(3))
print(cap.get(4))
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',gray)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()


