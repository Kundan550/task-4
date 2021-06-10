import cv2
import numpy as np

img1 = cv2.imread("man.jpg")
img2  = cv2.imread("man2")

img1 = cv2.resize(img1,(408,612))
img2 = cv2.resize(img2,(408,612))

cv2.imshow("face1",img1)
cv2.imshow("face2",img2)
cv2.waitKey()
cv2.destroyAllWindows()

combine = np.hstack((img1,img2))

cv2.imshow("combined",combine)
cv2.waitKey()
cv2.destroyAllWindows()