import cv2
import mediapipe as mp
import time

class handDetector():
    # basic parameters for Hands module
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5,
                 modelComplexity=1,):
        self.mode = mode                            # static image mode
        self.maxHands = maxHands                    # max number of hands
        self.detectionCon = detectionCon            # detection confidence
        self.trackCon = trackCon                    # tracking confidence
        self.modelComplex = modelComplexity      # model complexity

        self.mpHands = mp.solutions.hands           # Hands module
        # Hands object
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelComplex,
                                        self.detectionCon, self.trackCon)
        self.mpdraw = mp.solutions.drawing_utils    # Drawing utilities


    def findHands(self, img, draw=True):
        """
        Find hands in the image and draw the points and connections
        return the image with points and connections
        """
        # change to RGB
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        # know if there is a hand
        # print(results.multi_hand_landmarks)

        # if there is a hand
        if self.results.multi_hand_landmarks:
            # extract info from each hand
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    # extract info from each point, draw hand points and connections
                    self.mpdraw.draw_landmarks(img, handLms,
                                               self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo=0, draw=True):
        """
        Find the position of specific hand(handNo)
        return a list of the position of specific hand(handNo)
        """
        lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            # landmark is a list of 21 points, they are in ratio of the image
            for id, landMark in enumerate(myHand.landmark):
                h, w, c = img.shape
                # convert ratio to pixel
                cx, cy = int(landMark.x * w), int(landMark.y * h)
                ### id, cx, cy -> we have the pixel location of each location of the hand
                # print(id, cx, cy)
                lmList.append([id, cx, cy])
                if draw:
                    # draw a circle on the specific point
                    cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)

        return lmList

def main():
    """
    how to use the module:
    copy the program in your folder
    import HandTrackModule as htm
    and use the main function
    :return:
    """
    # use for frame rate
    pTime, cTime = 0, 0

    cap = cv2.VideoCapture(0)

    # create object
    detector = handDetector()

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


if __name__ == "__main__":
    main()