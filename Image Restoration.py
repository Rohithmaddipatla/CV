import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read grayscale
img = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)

if img is None:
    raise FileNotFoundError("input.jpg not found")

# ----- Create a blurred + noisy version for demo -----
blurred = cv2.GaussianBlur(img, (7, 7), 1.5)

noise = np.random.normal(0, 10, img.shape)
noisy_blurred = blurred.astype(np.float32) + noise
noisy_blurred = np.clip(noisy_blurred, 0, 255).astype(np.uint8)

# 1) Deblurring using a sharpening kernel
sharpen_kernel = np.array(
    [[0, -1, 0],
     [-1,  5, -1],
     [0, -1, 0]],
    dtype=np.float32
)

deblurred = cv2.filter2D(noisy_blurred, -1, sharpen_kernel)

# 2) Denoising using Non-Local Means
denoised = cv2.fastNlMeansDenoising(
    noisy_blurred,
    None,
    h=15,
    templateWindowSize=7,
    searchWindowSize=21
)

# Show results
titles = [
    "Original",
    "Noisy + Blurred",
    "Deblurred (Sharpen)",
    "Denoised (NLM)"
]
images = [img, noisy_blurred, deblurred, denoised]

plt.figure(figsize=(10, 8))
for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.imshow(images[i], cmap="gray")
    plt.title(titles[i])
    plt.axis("off")

plt.tight_layout()
plt.show()