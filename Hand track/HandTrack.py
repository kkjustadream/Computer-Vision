import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)


mpHands = mp.solutions.hands            # Hands module
hands = mpHands.Hands()                 # Hands object
mpdraw = mp.solutions.drawing_utils     # Drawing utilities

# use for frame rate
pTime, cTime = 0, 0

while True:
    success, img = cap.read()
    # change to RGB
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    # know if there is a hand
    # print(results.multi_hand_landmarks)

    # if there is a hand
    if results.multi_hand_landmarks:
        # extract info from each hand
        for handLms in results.multi_hand_landmarks:
            # landmark is a list of 21 points, they are in ratio of the image
            for id, landMark in enumerate(handLms.landmark):
                h, w, c = img.shape
                # convert ratio to pixel
                cx, cy = int(landMark.x*w), int(landMark.y*h)
                ### id, cx, cy -> we have the pixel location of each location of the hand
                print(id, cx, cy)

            # extract info from each point, draw hand points and connections
            mpdraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    # frame rate
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    # putText(img, text, org, fontFace, fontScale, color, thickness)
    cv2.putText(img, f"FPS: {int(fps)}", (10, 70), cv2.FONT_HERSHEY_PLAIN,
                3, (255, 0, 255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
