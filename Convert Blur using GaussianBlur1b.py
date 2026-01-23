import cv2

# Read the image
image = cv2.imread("input.jpg")

# Apply Gaussian Blur
blur = cv2.GaussianBlur(image, (5, 5), 0)

# Display the blurred image
cv2.imshow("Gaussian Blurred Image", blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
