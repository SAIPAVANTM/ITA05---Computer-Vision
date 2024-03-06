import cv2
import numpy as np

input_image = cv2.imread('download.jpeg', cv2.IMREAD_GRAYSCALE)

kernel = np.ones((5, 5), np.uint8)

dilated_image = cv2.dilate(input_image, kernel, iterations=1)

cv2.imshow('Original Image', input_image)
cv2.imshow('Dilated Image', dilated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
