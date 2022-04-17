
import cv2
import mediapipe as mp 
import numpy as np 
import time
import pose_estimation_module as pm

cap = cv2.VideoCapture('Videos/curls.mp4')

detector = pm.poseDetector()
count = 0
dir_ = 0
pTime = 0
while True:
    success, img = cap.read()
    img = cv2.resize(img, (1280, 720))
    # img = cv2.imread('AiTrainer/test.jpg')
    img = detector.findPose(img, draw=False)
    lmList = detector.findPosition(img, draw=False)
    # print(lmList)

    if len(lmList)!= 0:
        # # Right Arm
        # detector.findAngel(img, 12, 14, 16)
        
        # Left Arm
        angle = detector.findAngel(img, 11, 13, 16)
        per = np.interp(angle, (210, 310), (0, 100))
        bar = np.interp(angle, (210, 310), (650, 100))
        # print(angle, per)

        #Check for the dumbbell curls
        color = (255, 0, 255)
        if per == 100:
            color = (0, 255, 0)
            if dir_ == 0:
                count+=0.5
                dir_ = 1
        if per == 0:
            color = (0, 255, 0)
            if dir_==1:
                count+=0.5
                dir_ = 0
        # print(count)
        
        # Draw Bar
        cv2.rectangle(img, (1100, 100), (1175, 650), color, 3)
        cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
        cv2.putText(img, f'{int(per)}', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 4, color, 4)
        # Draw Curl Count
        cv2.rectangle(img, (0, 450), (250, 720), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)

        cTime = time.time()
        fps = 1 /(cTime-pTime)
        cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 15, (255, 0, 0), 25)
    cv2.imshow('Image', img)
    if cv2.waitKey(30) == ord('q'):
        break