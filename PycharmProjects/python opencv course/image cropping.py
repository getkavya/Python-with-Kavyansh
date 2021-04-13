import cv2
import numpy

image = cv2.imread('lena.jpg')
height, width = image.shape[:2]
start_row, start_col = int(height*.25), int(width*.25)

row_end, col_end = int(height*.75), int(width*.75)
cropped = image[start_row:row_end, start_col:col_end]

cv2.imshow('Orignal Image', image)
cv2.waitKey()

cv2.imshow('corpped image', cropped)
cv2.waitKey()
cv2.destroyAllWindows()