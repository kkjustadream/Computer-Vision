import cv2
import mediapipe as mp
import time
import HandTrackModule as htm


pTime, cTime = 0, 0

cap = cv2.VideoCapture(0)

# create object
detector = htm.handDetector()

while True:
    success, img = cap.read()

    # call the function to draw
    img = detector.findHands(img)
    # call the function to find the position of the hand
    lmList = detector.findPosition(img)
    # if we detect the hand, print out the position of the specific
    # coordinate of the hand
    if len(lmList) != 0:
        print(lmList[4])

    # frame rate
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    # putText(img, text, org, fontFace, fontScale, color, thickness)
    cv2.putText(img, f"FPS: {int(fps)}", (10, 70), cv2.FONT_HERSHEY_PLAIN,
                3, (255, 0, 255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)