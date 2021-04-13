import cv2
image = cv2.imread('lena.jpg')
cv2.imshow('orignal image', image)
cv2.imwrite('output.jpg', image)
cv2.waitKey(0)
cv2.destroyAllWindows()