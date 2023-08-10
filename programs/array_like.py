# import opencv
import cv2
import random
from PIL import Image
import numpy as np


'''
# Load the input image
image = cv2.imread('chrollo.jpg')
cv2.imshow('Original', image)
cv2.waitKey(0)

# Use the cvtColor() function to grayscale the image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Grayscale', gray_image)
cv2.waitKey(0)

'''

img = cv2.imread('monsters.jpg')

print(img.shape)
print(img)
# imread devolve um array?
# não, mat não é um array
cv2.imshow('blue Image', img)
cv2.waitKey(0)

a,b = img.shape[0:2]

for i in range(a):
 for j in range(b):
  pix = [random.random()*200,random.random()*200,random.random()*200]
  img[i][j] = pix


cv2.imshow('blue Image', img)
cv2.waitKey(0)

# Window shown waits for any key pressing event
cv2.destroyAllWindows()
