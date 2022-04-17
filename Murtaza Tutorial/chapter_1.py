import cv2
"""
Read Images-Videos-Webcam
"""

cap = cv2.VideoCapture(0)

cap.set(3, 640) # setting of width
cap.set(4, 480) # setting of height
cap.set(10, 100) # setting of brightness
while True:
    ret, frame = cap.read()
    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) == ord("q"):
        break