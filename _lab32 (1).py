import cv2

img1 = cv2.imread("image5.png")
img2 = cv2.imread("image5.png")

orb = cv2.ORB_create(nfeatures=2000)

kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)

result = cv2.drawMatches(img1, kp1, img2, kp2, matches[:20], None)

cv2.imshow("Watch Recognition", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
