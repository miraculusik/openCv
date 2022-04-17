import numpy as np 
import cv2
"""
Basic Functions
"""
img = cv2.imread("Photos/lady.jpg")

# Gray image
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Blur image
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
# Edge Dedector
imgCanny = cv2.Canny(img, 150, 200)
# Image Dialation
kernel = np.ones((5,5), np.uint8)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
# Image Eroded
kernel = np.ones((5,5), np.uint8)
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)

cv2.imshow("Gray image", imgGray)
cv2.imshow("Blur image", imgBlur)
cv2.imshow("Canny image", imgCanny)
cv2.imshow("Dialation image", imgDialation)
cv2.imshow("Eroded image", imgEroded)
cv2.waitKey(0)

