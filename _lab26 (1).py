import cv2
import numpy as np

img = cv2.imread("image2.png", 0)
kernel = np.ones((5,5), np.uint8)

dilated = cv2.dilate(img, kernel, 1)
cv2.imshow("original",img)
cv2.imshow("Dilated", dilated)
cv2.waitKey(0)
