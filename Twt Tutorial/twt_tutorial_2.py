import cv2
import random

img = cv2.imread("Photos/cat.jpg", -1)

#accessing pixel values
print(img[257][400])

# Changing pixcel colors
for i in range(100):
    for j in range(img.shape[1]):
        img[i][j]=[random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

# Copying & Pasting parts of image
# capture the face of cat
tag = img[80:200, 400:500]
# Pasting
img[100:220, 200:300] = tag

cv2.imshow("Cat",img)
cv2.waitKey(0)
cv2.destroyAllWindows()