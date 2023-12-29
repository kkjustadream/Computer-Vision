import cv2
import mediapipe as mp
import time


class PoseDetector():
    def __init__(self, mode=False, up_body=False, smooth_l=True, smooth_s = True, detectionCon=0.5, trackCon=0.5,
                 model_complexity=1, enable = False):
        self.mode = mode
        self.model_complexity = model_complexity
        self.smooth_l = smooth_l
        self.smooth_s = smooth_s
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.enable = enable

        self.mp_draw = mp.solutions.drawing_utils

        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(self.mode, self.model_complexity, self.smooth_l, self.smooth_s,
                                      self.detectionCon, self.trackCon, self.enable)

    def find_pose(self, img, draw=True):
        """
        find the pose of the image and draw the landmarks on the image, return the image
        """
        # convert to RGB
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # will get the detection of the pose
        self.results = self.pose.process(imgRGB)
        # if detected
        if self.results.pose_landmarks:
            if draw:
                # draw the landmarks
                self.mp_draw.draw_landmarks(img, self.results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS)

        return img

    def get_position(self, img, draw=True):
        lm_list = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                # get the pixel value of the landmark
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 3, (255, 0, 0), cv2.FILLED)
        return lm_list



def main():
    cap = cv2.VideoCapture("Resource/test.mp4")
    # frame rate
    c_time, p_time = 0, 0

    detector = PoseDetector()
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