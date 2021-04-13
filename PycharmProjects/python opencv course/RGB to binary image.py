import cv2

image = cv2.imread('lena.jpg', 0)
cv2.imshow('output image', image)
cv2.waitKey(0)

ret, bw = cv2.threshold(image, 127, 225, cv2.THRESH_BINARY)
cv2.imshow("black_white", bw)
cv2.waitKey(0)

cv2.destroyAllWindows()