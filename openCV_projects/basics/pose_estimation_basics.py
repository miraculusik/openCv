
import cv2
import mediapipe as mp 
import time


mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture('Videos/pos7.mp4')
pTime = 0

while True:
    success, img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    # print(results.pose_landmarks)
    
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            print(id, lm)
            cx, cy = int(lm.x*w), int(lm.y*h)
            cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)


    cTime = time.time()
    fps = int(1/(cTime-pTime))
    pTime = cTime
    cv2.putText(img, str(fps), (70, 200), cv2.FONT_HERSHEY_PLAIN, 15, (255, 255, 255), 10)
    
    cv2.imshow('Image', img)
    if cv2.waitKey(10) == 113:
        break