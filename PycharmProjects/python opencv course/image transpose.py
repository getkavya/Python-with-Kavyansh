import cv2

image = cv2.imread("lena.jpg")
rotated_image = cv2.transpose(image)

cv2.imshow('orignal image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('rotated image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()