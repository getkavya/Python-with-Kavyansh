import cv2
import numpy
image = cv2.imread("lena.jpg")

height, width = image.shape[:2]
print(height)
print(width)

Quarter_height, Quarter_width = height/4, width/4
print(Quarter_height)
print(Quarter_width)

#[1 0- tx]
#[0 1- ty]
# T is our translation matrix

T = numpy.float32([[1, 0, Quarter_height], [0, 1, Quarter_width]])
print(T)

#we use warpAffine to shift the image

image_translation = cv2.warpAffine(image, T, (height, width))
cv2.imshow('orignal image', image)
cv2.imshow('translation image', image_translation)
cv2.waitKey(0)
cv2.destroyAllWindows()
