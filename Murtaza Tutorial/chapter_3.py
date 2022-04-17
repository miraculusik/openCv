import cv2
import numpy as np 
"""
Resizing and Cropping
"""
img = cv2.imread("Photos/group 1.jpg")
print(img.shape)

# resize image (width, height)
imgResize = cv2.resize(img, (300, 200))
print(imgResize.shape)
# crop image (height, width) // bu resize yapmaz direk resmin belirli bölgelerini alır
imgCropped = img[0:200, 200:500]


cv2.imshow("Group", img)
cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Cropped", imgCropped)
cv2.waitKey(0)