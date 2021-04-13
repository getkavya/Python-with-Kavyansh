#scaling or resiziing and interplotation
import cv2
import numpy
image = cv2.imread('lena.jpg')
cv2.imshow('orignal image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
img_scaled = cv2.resize(image, None, fx=0.75, fy=0.75)
cv2.imshow('Scaling-linear interplotation', img_scaled)
cv2.waitKey(0)
cv2.destroyAllWindows()

img_scaled1 = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_AREA)
cv2.imshow('double sized image', img_scaled1)
cv2.waitKey(0)
cv2.destroyAllWindows()