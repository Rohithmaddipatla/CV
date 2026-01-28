import cv2
import numpy as np

img = cv2.imread("image3.png", 0)
kernel = np.ones((5,5), np.uint8)

tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
cv2.imshow("original",img)
cv2.imshow("Top Hat", tophat)
cv2.waitKey(0)
