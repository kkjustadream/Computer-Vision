import cv2
import mediapipe as mp
import time
import pose_estimate_module as pm

def main():
    cap = cv2.VideoCapture("Resource/test.mp4")
    # frame rate
    c_time, p_time = 0, 0

    detector = pm.PoseDetector()
    while True:
        success, img = cap.read()

        img = detector.find_pose(img)
        lm_list = detector.get_position(img)
        print(lm_list)

        c_time = time.time()
        fps = 1 / (c_time - p_time)
        p_time = c_time

        cv2.putText(img, str(int(fps)), (10, 40), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

        cv2.imshow("Image", img)
        # press q to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == "__main__":
    main()