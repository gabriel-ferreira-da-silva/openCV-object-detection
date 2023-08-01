#!/usr/bin/env python3

# opening a image


import cv2
import numpy
import matplotlib.pyplot as plt
 
 
img1 = cv2.imread("chrollo.jpg", cv2.IMREAD_COLOR)
img2 = cv2.imread("chrollo.jpg", cv2.IMREAD_GRAYSCALE)
img3 = cv2.add(img1, img1)
img3 = cv2.add(img3, img3)

print(img1.shape)
print(img2.shape)

cv2.imshow("image1", img3)
cv2.imshow("image2", img1)
cv2.imshow("image3", img2)

#plt.imshow(img1)

#plt.waitforbuttonpress()
#plt.close('all')

cv2.waitKey(0)

cv2.destroyAllWindows()
