import cv2

img = cv2.imread("Resource/IVE.jpg")
imgResize = cv2.resize(img, (600, 900))
imgCropped = imgResize[0:200, 200:500]
print(img.shape)
# cv2.imshow("img1", imgResize)
# cv2.imshow("img", imgCropped)
# cv2.waitKey(0)
