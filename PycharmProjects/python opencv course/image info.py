import cv2
image = cv2.imread('lena.jpg')
cv2.imshow('output image', image)
print("Height:", image.shape[0])
print("Width:", image.shape[1])
print("RGB Layers:", image.shape[2])
cv2.destroyAllWindows()