import cv2

# use the haarcascade_frontalface_default.xml file
faceCascade = cv2.CascadeClassifier("Resource/haarcascade_frontalface_default.xml")
img = cv2.imread("Resource/IVE_all.jpg")
img = cv2.resize(img, (847, 564))
# convert to grayscale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detect faces scale factor = 1.1(1.1~1.5), minNeighbors = 4(3~6)
faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

# draw rectangle around the face
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow("img", img)
cv2.waitKey(0)