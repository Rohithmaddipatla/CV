import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image in grayscale
img = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)

# ----- Add artificial salt-and-pepper noise for demo -----
noisy = img.copy()
p = 0.02  # noise probability
rnd = np.random.rand(*img.shape)

noisy[rnd < p / 2] = 0      # pepper noise
noisy[rnd > 1 - p / 2] = 255  # salt noise

# 1) Smoothing with Gaussian blur
gaussian = cv2.GaussianBlur(noisy, (5, 5), 1.0)

# 2) Median filtering
median = cv2.medianBlur(noisy, 5)

# Show results
titles = ["Original", "Noisy", "Gaussian Smoothing", "Median Filtering"]
images = [img, noisy, gaussian, median]

plt.figure(figsize=(10, 6))
for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.imshow(images[i], cmap="gray")
    plt.title(titles[i])
    plt.axis("off")

plt.tight_layout()
plt.show()