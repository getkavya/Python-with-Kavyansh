import cv2
image = cv2.imread('lena.jpg')
cv2.imshow('output image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()