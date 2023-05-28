#In this code I will begin control on img by moving parts and resize it
#And merge both img together and split BGR from img 

#In this code Assume I've this material and work with it 
import cv2
import os 
os.chdir(R"C:\Users\amb\Dowunloads")
#(import os):It's an libirary that shown that I didn't want to maej all photos
#That I work on same path of code, So I can import it from os libirary and
#Write down path of photos that I want

img = cv2.imread("messi.jpg")
img2 = cv2.imread("apple.jpg")
print(img.shape)
print(img.size)
print(img2.size)

print(img.dtybe)

b, g, r = cv2.split(img)
#Firsr featuer here is spliting BGR from img and make
#Every color alone

img = cv2.merge((b,g,r))
#Second featuer is collect all BGR together again in one value 

ball = img[280:340, 330:390]  #y2:y1 , x2:x1
img[273:333, 100:160] = ball
#Third part I copy every part I want and past it every were in img
#That could be by coordinate old region of ball and 
#next part is to coordinate new region of ball 
#Notice: I Can determine coordinates by Code number.8  

img = cv2.resize(img, (512,512))
img2 = cv2.resize(img2, (512,512))
#Fourth part is to manage img size by control width and height of pixels

dst = cv2.add(img, img2)
#Fiveth part is to merge to imgs together and I could by write down 
#img1 and img2 that I want to add and It could add more than one img

dst = cv2.addWeighted(img, 0.5, img2, 0.5, 100)
#Meaning of control that I control by two merged img by writing imgs added
#and choose which img I want appear most by the  two imgs

cv2.imshow("frame", img)
#Here will dispaly coppied part

cv2.imshow("frame", dst)
#Here will display merged imgs

cv2.waitKey(0)
cv2.destroyAllWindows( )