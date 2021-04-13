import cv2
import numpy
image = cv2.imread('lena.jpg')
cv2.imshow('orignal image', image)



cv2.waitKey(0)

B, G, R = cv2.split(image)
zeros = numpy.zeros(image.shape[:2], dtype="uint8")

cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
cv2.waitKey(0)

cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
cv2.waitKey(0) 

cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))
cv2.waitKey(0)

cv2.destroyAllWindows()
