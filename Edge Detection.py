import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read in grayscale
img = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)

if img is None:
    raise FileNotFoundError("input.jpg not found")

# Slight blur to reduce noise before edges
blur = cv2.GaussianBlur(img, (3, 3), 0)

# 1) Sobel edges
sobelx = cv2.Sobel(blur, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(blur, cv2.CV_64F, 0, 1, ksize=3)

sobel_mag = cv2.magnitude(sobelx, sobely)
sobel_mag = cv2.convertScaleAbs(sobel_mag)

# 2) Canny edges
canny_edges = cv2.Canny(blur, threshold1=100, threshold2=200)

# Show results
titles = ["Original", "Sobel Magnitude", "Canny Edges"]
images = [img, sobel_mag, canny_edges]
plt.figure(figsize=(12, 4))
for i in range(3):
    plt.subplot(1, 3, i + 1)
    plt.imshow(images[i], cmap="gray")
    plt.title(titles[i])
    plt.axis("off")
plt.tight_layout()
plt.show()