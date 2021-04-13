import cv2
import numpy

image = cv2.imread('lena.jpg')
smaller = cv2.pyrDown(image)
greater = cv2.pyrUp(image)

cv2.imshow('Original image', image)
cv2.waitKey()
cv2.imshow('smaller image', smaller)
cv2.waitKey()
cv2.imshow('larger image', greater)
cv2.waitKey()
cv2.destroyAllWindows()
