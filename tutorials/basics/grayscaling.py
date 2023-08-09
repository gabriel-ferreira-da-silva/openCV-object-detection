# import opencv
import cv2


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
  
# Obtain the dimensions of the image array
# using the shape method
(row, col) = img.shape[0:2]

print(img.shape)
print(img[100,100])
  
# Take the average of pixel values of the BGR Channels
# to convert the colored image to grayscale image
for i in range(row):
    for j in range(col):
        # Find the average of the BGR pixel values
        #img[i, j] = sum(img[i, j]) * 0.33
        a = sum(img[i, j]) * 0.33
        b = img[i,j]
        img[i,j] = [b[0], 0,0]


cv2.imshow('blue Image', img)
cv2.waitKey(0)
  
img1 = cv2.imread('monsters.jpg')
cv2.waitKey(0)

for i in range(row):
    for j in range(col):
        # Find the average of the BGR pixel values
        #img[i, j] = sum(img[i, j]) * 0.33
        b = img1[i,j]
        img1[i,j] = [b[2], b[0], b[1]]
  
cv2.imshow('blue plus media Image', img1)
cv2.waitKey(0)

# Window shown waits for any key pressing event
cv2.destroyAllWindows()
