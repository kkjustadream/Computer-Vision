import cv2
import time
import numpy as np
import math
import HandTrackModule as htm
import os

"""
finger count using hand tracking, and show image of the number of fingers
press q to quit
"""

w_cam, h_cam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, w_cam)
cap.set(4, h_cam)

folder_path = "pic"
my_list = os.listdir(folder_path)

# Reshape overlay images to a fixed size
overlay_list = []
overlay_width = 200
overlay_height = 200
for im_path in my_list:
    image = cv2.imread(f"{folder_path}/{im_path}")
    image = cv2.resize(image, (overlay_width, overlay_height))
    overlay_list.append(image)

p_time = 0

# create object
detector = htm.handDetector(detectionCon=0.75)

tip_ids = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        fingers = []

        # Detect hand orientation, see index finger and little finger position
        # it's mirror, so right hand x of index > little finger
        if lmList[tip_ids[1]][1] > lmList[tip_ids[4]][1]:
            # Right hand
            is_right_hand = True
        else:
            # Left hand
            is_right_hand = False

        if is_right_hand:
            # thumb，if thumb move more than index 3, it is closed for right hand
            if lmList[tip_ids[0]][1] > lmList[tip_ids[0]-1][1]:
                fingers.append(1)
            else:
                fingers.append(0)
        else:
            if lmList[tip_ids[0]][1] < lmList[tip_ids[0]-1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

        # other fingers
        for id in range(1, 5):
            if lmList[tip_ids[id]][2] < lmList[tip_ids[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        # print(fingers)
        total_fingers = fingers.count(1)

        h, w, c = overlay_list[total_fingers-1].shape
        # if 1 will show first image, 0 will show -1 image
        # overlay the picture
        img[0:h, 0:w] = overlay_list[total_fingers-1]

        cv2.putText(img, str(total_fingers), (45, 405), cv2.FONT_HERSHEY_PLAIN,
                    10, (255, 0, 0), 25)

    c_time = time.time()
    fps = 1/(c_time-p_time)
    p_time = c_time
    cv2.putText(img, f"FPS: {int(fps)}", (400, 70), cv2.FONT_HERSHEY_PLAIN,
                3, (255, 0, 255), 3)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break