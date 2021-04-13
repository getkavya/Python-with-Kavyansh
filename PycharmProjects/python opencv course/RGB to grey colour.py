import cv2
#method 1
"""
image = cv2.imread('lena.jpg', 0)
cv2.imshow('output image', image)
cv2.waitKey(0)
"""
#Method 2
"""
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('grey scale image', gray_img)
cv2.waitKey(0)
"""
cv2.destroyAllWindows()