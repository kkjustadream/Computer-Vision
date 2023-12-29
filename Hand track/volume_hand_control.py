import cv2
import time
import numpy as np
import math
import HandTrackModule as htm
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
"""
volume control using hand tracking
use pycaw to control the volume
press q to quit
"""

# set camera width and height
wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

p_time = 0

# create detector object
detector = htm.handDetector(detectionCon=0.7)

# initialize the volume control
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
# volume.GetMute()
volume.GetMasterVolumeLevel()
# volume range -65.25 to 0.0
volume_range = volume.GetVolumeRange()
min_volume = volume_range[0]
max_volume = volume_range[1]

vol = 0
bar_length = 400    # zero is at 400
vol_percentage = 0

while True:
    success, img = cap.read()
    img = detector.findHands(img)

    # get the position
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        # id 4 and 8 are the tip of the thumb and index finger
        # print(lmList[4], lmList[8])

        # extract the x and y coordinates of the tip of the thumb and index finger
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        # find the center of the line
        cx, cy = (x1+x2)//2, (y1+y2)//2

        # draw
        cv2.circle(img, (x1, y1), 10, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

        # get the length of the line
        length = math.hypot(x2-x1, y2-y1)
        max_length = 180
        min_length = 30

        if length > max_length:
            cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED)
            length = max_length
        if length < min_length:
            cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED)
            length = min_length

        # hand range 30 - 180
        # volume range -65.25 to 0.0
        # convert the length to volume
        vol = np.interp(length, [min_length, max_length], [min_volume, max_volume])

        # set the volume
        volume.SetMasterVolumeLevel(vol, None)

        # print(length, vol)
        print(vol)

        # draw the bar
        bar_length = np.interp(length, [min_length, max_length], [400, 150])
        vol_percentage = np.interp(length, [min_length, max_length], [0, 100])

    cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)
    cv2.rectangle(img, (50, int(bar_length)), (85, 400), (255, 0, 0), cv2.FILLED)
    cv2.putText(img, f"{int(vol_percentage)}%", (40, 450), cv2.FONT_HERSHEY_PLAIN,
                2, (255, 0, 0), 2)

    # flip the image
    # img = cv2.flip(img, 1)

    # define fps
    c_time = time.time()
    fps = 1/(c_time-p_time)
    p_time = c_time
    cv2.putText(img, f"FPS: {int(fps)}", (20, 30), cv2.FONT_HERSHEY_PLAIN,
                2, (255, 0, 0), 2)

    # show the image
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break