#task 4.2

import cv2
import numpy as np

img1 = cv2.imread("man.jpg")
img2  = cv2.imread("man2")

swap2=img2[ 41:157,247:361]
img1[41:157,247:361] = swap2


cv2.imshow("swap2",img1)
cv2.waitKey()
cv2.destroyAllWindows()

swap1=img1[ 66:180,256:370]
img2[66:180,256:370] = swap1

cv2.imshow("swap1",img2)
cv2.waitKey()
cv2.destroyAllWindows()



