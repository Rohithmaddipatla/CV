import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image in grayscale (good to test with a low-contrast image)
img = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)

if img is None:
    raise FileNotFoundError("input.jpg not found")

# 1) Histogram Equalization
hist_eq = cv2.equalizeHist(img)

# 2) Contrast Stretching (min-max normalization)
min_val = np.min(img)
max_val = np.max(img)

# Avoid division by zero if image is flat
if max_val > min_val:
    contrast_stretched = ((img - min_val) * (255.0 / (max_val - min_val))).astype(np.uint8)
else:
    contrast_stretched = img.copy()

# Show results
titles = ["Original", "Histogram Equalization", "Contrast Stretching"]
images = [img, hist_eq, contrast_stretched]

plt.figure(figsize=(12, 4))
for i in range(3):
    plt.subplot(1, 3, i + 1)
    plt.imshow(images[i], cmap="gray")
    plt.title(titles[i])
    plt.axis("off")

plt.tight_layout()
plt.show()