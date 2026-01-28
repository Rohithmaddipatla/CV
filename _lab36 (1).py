import cv2
img = cv2.imread("face.png")
x1, y1, x2, y2 = 50, 50, 200, 200
cv2.rectangle(img, (x1, y1), (x2, y2), (0,250,0), 2)
cropped = img[y1:y2, x1:x2]
cv2.imshow("Original", img)
cv2.imshow("Cropped", cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
