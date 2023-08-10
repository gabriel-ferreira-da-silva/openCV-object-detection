'''

o proposito deste programa  é criar funções para avaliar
a similaridade entre duas imagens utilizando openCV.

'''

import cv2
import math

'''

first implementing the MSE algorithm.

'''

def MSEsim(img1, img2):
 m,n = img1.shape[0:2]
 result = 0
 for i in range(m):
  res = 0
  for j in range(n):
   di = img1[i][j][0] - img2[i][j][0]
   dj = img1[i][j][1] - img2[i][j][1]
   dk = img1[i][j][2] - img2[i][j][2]
   
   r = di**2 + dj**2 + dk**2
   res += r
  result += res
 result /= (m*n)
 return  result
   

img = cv2.imread('monsters.jpg')
img2 = cv2.imread('monsters.jpg')


print(MSEsim(img, img2))

(row, col) = img.shape[0:2]

for i in range(row):
    for j in range(col):
        # Find the average of the BGR pixel values
        #img[i, j] = sum(img[i, j]) * 0.33
        a = sum(img[i, j]) * 0.33
        b = img[i,j]
        img[i,j] = [b[0], 0,0]

print(MSEsim(img, img2))



