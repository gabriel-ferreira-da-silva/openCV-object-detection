# importing libraries
import cv2
import numpy as np

image = cv2.imread('chrollo.jpg')

cv2.imshow('Original Image', image)
cv2.waitKey(0)

# Gaussian Blur
Gaussian = cv2.GaussianBlur(image, (7, 7), 0)
cv2.imshow('Gaussian Blurring 7 7', Gaussian)
cv2.waitKey(0)

# Gaussian Blur
Gaussian = cv2.GaussianBlur(image, (17, 17), 0)
cv2.imshow('Gaussian Blurring 16 16', Gaussian)
cv2.waitKey(0)

# Gaussian Blur
Gaussian = cv2.GaussianBlur(image, (211, 7), 0)
cv2.imshow('Gaussian Blurring 20 7', Gaussian)
cv2.waitKey(0)



cv2.destroyAllWindows()

