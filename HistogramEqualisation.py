from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
# Histogram equalization
def histeq(imarr):
    hist, bins = np.histogram(imarr, 255)
    cdf = np.cumsum(hist)
    cdf = 255 * (cdf / cdf[-1])
    res = np.interp(imarr.flatten(), bins[:-1], cdf)
    res = res.reshape(imarr.shape)
    return res, hist


img = Image.open("Bupati.png")
gray_image = img.convert('L')
gray_arr = np.array(gray_image)

plt.imshow(Image.fromarray(gray_arr),cmap='gray')
plt.axis("off")
plt.show()

plt.hist(gray_arr.flatten(), 256)  # flatten can transform a matrix into a one-dimensional sequence
plt.show()

res, hist = histeq(gray_arr)
plt.imshow(Image.fromarray(res))
plt.axis("off")
plt.show()

plt.hist(res.flatten(), 256)  # flatten can transform a matrix into a one-dimensional sequence
plt.show()
