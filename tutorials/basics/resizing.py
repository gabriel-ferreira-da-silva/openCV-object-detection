import cv2
import numpy as np
import matplotlib.pyplot as plt
 
image = cv2.imread("chrollo.jpg", cv2.IMREAD_COLOR)
# Loading the image
 
half = cv2.resize(image, (0, 0), fx = 0.1, fy = 0.1)
bigger = cv2.resize(image, (1050, 1610))
 
stretch_near = cv2.resize(image, (780, 540), interpolation = cv2.INTER_LINEAR)
 
Titles =["Original", "Half", "Bigger", "Interpolation Nearest"]
images =[image, half, bigger, stretch_near]
count = 4

cv2.imshow("original", image)
cv2.imshow("half", half)
cv2.imshow("bigger", bigger)
cv2.imshow("strech", stretch_near)

cv2.waitKey(0)

cv2.destroyAllWindows()
