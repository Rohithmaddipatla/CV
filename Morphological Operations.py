import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image and convert to binary (assuming bright objects on dark background)
img = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)

if img is None:
    raise FileNotFoundError("input.jpg not found")

# Threshold to get binary image (Otsu)
_, binary = cv2.threshold(
    img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
)

# Structuring element (kernel)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

# 1) Erosion
eroded = cv2.erode(binary, kernel, iterations=1)

# 2) Dilation
dilated = cv2.dilate(binary, kernel, iterations=1)

# 3) Opening (erosion followed by dilation)
opened = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)

# 4) Closing (dilation followed by erosion)
closed = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)

# Show results
titles = [
    "Original Gray",
    "Binary",
    "Erosion",
    "Dilation",
    "Opening",
    "Closing"
]
images = [img, binary, eroded, dilated, opened, closed]

plt.figure(figsize=(12, 8))
for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], cmap="gray")
    plt.title(titles[i])
    plt.axis("off")

plt.tight_layout()
plt.show()