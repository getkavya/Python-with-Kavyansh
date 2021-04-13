#Colour filter,colour space
#hue : (0 - 180), saturation :- 0 - 255 ,value :- 0 - 255

import cv2
image = cv2.imread('lena.jpg')
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# HSV image
cv2.imshow('HSV Image', hsv_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#hue image
cv2.imshow('Hue image', hsv_image[:, :, 0])
cv2.waitKey(0)
cv2.destroyAllWindows()

#Saturation image
cv2.imshow('Saturation image', hsv_image[:, :, 1])
cv2.waitKey(0)
cv2.destroyAllWindows()

# value image
cv2.imshow('value image', hsv_image[:, :, 2])
cv2.waitKey(0)

cv2.destroyAllWindows()