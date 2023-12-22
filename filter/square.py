import cv2
import numpy as np
import matplotlib.pyplot as plt


img2 = cv2.imread("flower.jpg", cv2.IMREAD_COLOR)

height, width = img2.shape[0:2]

pixel_size = 20

mean_red=0
mean_green=0
mean_blue=0

img1 = np.zeros((height,width,3), np.uint8)

for i in range(height):
 for j in range(width):
  if (i % pixel_size==0 and j % pixel_size==0 )and (i+pixel_size) <= height and (j+pixel_size) <= width:
   mean_red= 0
   mean_blue=0
   mean_green=0
   for ii in range(i, i+pixel_size):
    for jj in range(j, j+pixel_size):
     mean_red = mean_red +  img2[ii][jj][0]
     mean_blue = mean_blue +  img2[ii][jj][1]
     mean_green = mean_green +  img2[ii][jj][2]
   mean_red = mean_red /(pixel_size*pixel_size)
   mean_green = mean_green /(pixel_size*pixel_size)
   mean_blue = mean_blue /(pixel_size*pixel_size)
   for ii in range(i, i+pixel_size):
    for jj in range(j, j+pixel_size):
     img1[ii][jj][0] = mean_red
     img1[ii][jj][1] = mean_blue
     img1[ii][jj][2] = mean_green
     
print(mean_red)
print(mean_green)
print(mean_blue)

cv2.imshow("image", img1)

cv2.waitKey(0)

cv2.destroyAllWindows()
