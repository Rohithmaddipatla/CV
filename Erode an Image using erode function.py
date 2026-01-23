import cv2
import numpy as np

# Read the image (grayscale preferred)
image = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)

# Create a structuring element (kernel)
kernel = np.ones((5, 5), np.uint8)

# Apply erosion
eroded = cv2.erode(image, kernel, iterations=1)

# Display the result
cv2.imshow("Eroded Image", eroded)
cv2.waitKey(0)
cv2.destroyAllWindows()
