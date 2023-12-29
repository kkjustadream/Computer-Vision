import cv2
import numpy as np

img = cv2.imread("Resource/IVE.jpg")
img = cv2.resize(img, (480, 720))
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgGray = cv2.cvtColor(imgGray, cv2.COLOR_GRAY2RGB)  # Convert to RGB
# img_hor = np.hstack((img, img))
# img_ver = np.vstack((img, img))
combined_image = cv2.hconcat([img, imgGray, img])
cv2.imshow("img", combined_image)
cv2.waitKey(0)