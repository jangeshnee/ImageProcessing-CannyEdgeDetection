import numpy as np
import cv2

#read the image
original_img = cv2.imread('sample.jpg',1)
processed_img = original_img.copy()
#copy a grayscale version of the image
gray = cv2.cvtColor(processed_img ,cv2.COLOR_BGR2GRAY)
#apply canny edge detection in the image
#cv
processed_img  = cv2.Canny(gray,100,200)

cv2.imshow('Input Image',original_img)
cv2.imshow('Result:Canny Edge Detection',processed_img )
cv2.waitKey(0)
cv2.destroyAllWindows()
