import cv2
import numpy as np
 
image = cv2.imread('chrollo.jpg')
 
# Print error message if image is null
if image is None:
    print('Could not read image')
 
k = -50
# Apply identity kernel
kernel1 = np.array([[k, 0, k],
                    [k, 0, k],
                    [k, 0, k]])
 
identity = cv2.filter2D(src=image, ddepth=-1, kernel=kernel1)
 
cv2.imshow('Original', image)
cv2.imshow('Identity', identity)
     
cv2.waitKey()
cv2.imwrite('identity.jpg', identity)
cv2.destroyAllWindows()
 
# Apply blurring kernel
kernel2 = np.ones((5, 5), np.float32) / 25
img = cv2.filter2D(src=image, ddepth=-1, kernel=kernel2)
 
cv2.imshow('Original', image)
cv2.imshow('Kernel Blur', img)
     
cv2.waitKey()
cv2.imwrite('blur_kernel.jpg', img)
cv2.destroyAllWindows()
