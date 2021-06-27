import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('Bupati.png',0)
hist,bins = np.histogram(img.flatten(),256,[0,256])

plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.show()
