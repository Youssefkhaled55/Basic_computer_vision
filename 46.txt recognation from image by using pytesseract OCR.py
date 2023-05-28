import cv2
import pytesseract
import os
os.chdir(r"C:\Users\yk406\.spyder-py3")

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\yk406\.spyder-py3\tesseract.exe"

#1.Load the image
img = cv2.imread("book_page.jpg")

#2.Resize the image
#img = cv2.resize(img, None, fx=0.5, fy=0.5)

#3.Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#4.Convert image to black and white(using adaptive threshold)
adaptivethreshold = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,85,11)

config = "--psm 3"   #Look Down   #page segmentation mode
text = pytesseract.image_to_string(img) #chi_sim
print(text)

cv2.imshow("gray", gray)
cv2.imshow("adaptive th", adaptivethreshold)
cv2.waitKey(0)
cv2.destroyAlWindows()

#pagesegmode values are: 0 = Orientation and script detection (OSD) only.
#1.Automatic page segmentation with OSD
#2.Automatic page segmentation but not with OSD(Default)
#3.Fully automatic page segmentation, but no OSD(Default)
#4.Assume a single column of text of varibale sizes
#5.Assume a single uniform block of vertically aligned text
#6.Assume a single uniform block of text
#7.Treat the image as single text line
#8.Treat the image as single word
#9.Treat the image as single word in circle
#10.Treat the image as single character
