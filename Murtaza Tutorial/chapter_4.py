import cv2
import numpy as np 
""" 
Shapes and Texts
"""

img = np.zeros((512, 512, 3), np.uint8)
print(img.shape)
#img[200:300, 100:300] = 255, 0, 0
#img[:] = 255, 0, 0

# line
cv2.line(img, (0,0), (img.shape[1], img.shape[0]), (0,255,0), 1)
# rectangle
cv2.rectangle(img, (10,10), (250, 350), (0, 0, 350), cv2.FILLED)
# Circle
cv2.circle(img, (400,50), 30, (255, 255, 0), 5)
# Put the text on images
cv2.putText(img, "mirac", (300, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 1)

cv2.imshow("Image", img)
cv2.waitKey(0)