import cv2

image = cv2.imread('lena.jpg')
height, width = image.shape[:2]
rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), 70, .6)
rotate_image = cv2.warpAffine(image, rotation_matrix, (width, height))

cv2.imshow('orignal image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('rotation_matrix', rotate_image)
cv2.waitKey(0)
cv2.destroyAllWindows()