import numpy as np
from scipy.fftpack import dct, idct
import matplotlib.pyplot as plt

image = np.random.rand(8, 8) * 255
image = image.astype(np.float32)

def dct2(a):
    return dct(dct(a.T, norm='ortho').T, norm='ortho')


def idct2(a):
    return idct(idct(a.T, norm='ortho').T, norm='ortho')


dct_image = dct2(image)


reconstructed = idct2(dct_image)

plt.figure(figsize=(10, 4))
plt.subplot(1, 3, 1)
plt.title("Original Image")
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title("DCT Coefficients")
plt.imshow(np.log(abs(dct_image) + 1), cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title("Reconstructed Image")
plt.imshow(reconstructed, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
