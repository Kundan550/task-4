import cv2
import numpy

blank_image = numpy.zeros((1600,1600,3))

parallelogram =  numpy.array([(500,300),(900,300),(1100,500),(700,500)])
cv2.drawContours(blank_image,[parallelogram],0,(25,0,255),-1)

cv2.rectangle(blank_image,(700,500),(1100,800),(0,234,12), -1)
cv2.rectangle(blank_image,(300,500),(700,800),(254,204,12), -1)
cv2.rectangle(blank_image,(460,660),(540,800),(0,20,12), -1)

cv2.imshow("home",blank_image)
cv2.waitKey(0)
cv2.destoryAllWindows()