import numpy as np
import cv2

img = cv2.imread("Photos/lady.jpg", 0)
#-1, cv.IMREAD_COLOR : loads a color image. Any transparency of image will be neglected. (It is the default flag)
#0, cv.IMREAD_GRAYSCALE : loads image in grayscale 
#1, cv.IMREAD_UNCHANGED : load image as such including alpha channel

# resizing the image
img = cv2.resize(img, (900, 900))

# scaling the image
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

# rotating the image
#img = cv2.rotate(img, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)

# Saving the image
#cv2.imwrite("new_img.jpg", img)

cv2.imshow("lady", img)
cv2.waitKey(0) 
cv2.destroyAllWindows() 