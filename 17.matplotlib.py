import cv2
from matplotlib import pyplot as plt 

img = cv2.imread('lena.jpg', -1)
print(cv2.imshow('lena',img))

img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

plt.imshow(img)

cv2.waitKey(0)
cv2.destroyAllWindows()