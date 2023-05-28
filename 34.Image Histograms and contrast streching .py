import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread("lena.jpg",0)
#img = np.zeros((500,500),np.uint8)
#cv2.rectangle(img,(0,250),(500,500),(255),-1)
#cv2.rectangle(img,(0,125),(250,250),(127),-1)
#b,g,r = cv2.split(img)
#cv2.imshow("b",b)
#cv2.imshow("g",g)
#cv2.imshow("r",r)

#plt.hist(img.ravel(), 255,[0,255])
#plt.hist(b.ravel(), 255,[0,255])
#plt.hist(g.ravel(), 255,[0,255])
#plt.hist(r.ravel(), 255,[0,255])
#hist = cv2.calcHist(img,[0],None,[256],[0,256])
#plt.plot(hist)

plt.show()
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()