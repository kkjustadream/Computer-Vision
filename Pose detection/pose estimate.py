import cv2
import mediapipe as mp
import time


cap = cv2.VideoCapture("Resource/test.mp4")
# frame rate
c_time, p_time = 0, 0

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

mp_draw = mp.solutions.drawing_utils

list = []

while True:
    success, img = cap.read()

    # convert to RGB
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # will get the detection of the pose
    results = pose.process(imgRGB)

    # get the videos pose landmarks
    # print(results.pose_landmarks)

    # if detected
    if results.pose_landmarks:
        # draw the landmarks
        mp_draw.draw_landmarks(img, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            # get the pixel value of the landmark
            cx, cy = int(lm.x * w), int(lm.y * h)
            print(id, cx, cy)
            # if id == 0:
            cv2.circle(img, (cx, cy), 3, (255, 0, 0), cv2.FILLED)
            list.append([id, cx, cy])



    c_time = time.time()
    fps = 1/(c_time - p_time)
    p_time = c_time

    cv2.putText(img, str(int(fps)), (50, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    cv2.imshow("Image", img)
    # press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
