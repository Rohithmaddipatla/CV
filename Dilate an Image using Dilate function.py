import cv2
import numpy as np

# Read the image (grayscale works best for morphology)
image = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)

# Create a structuring element (kernel)
kernel = np.ones((5, 5), np.uint8)

# Apply dilation
dilated = cv2.dilate(image, kernel, iterations=1)

# Display the result
cv2.imshow("Dilated Image", dilated)
cv2.waitKey(0)
cv2.destroyAllWindows()
