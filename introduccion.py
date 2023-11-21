import random

import cv2 as cv

# Version de openCV
print(cv.__version__)

# Imagenes
img01 = cv.imread('flowers.jpeg')
img02 = cv.imread('flowers.jpeg', cv.IMREAD_GRAYSCALE)


# matplotlib
from matplotlib import pyplot as plt
plt.imshow(cv.cvtColor(img01, cv.COLOR_RGB2BGR))
plt.title("Img 1")
# plt.show()

# mpl img gray
plt.imshow(cv.cvtColor(img02, cv.COLOR_BGR2RGB))
plt.title("Imagen GRAY")
# plt.show()

# print(img01.shape)
# print(img02.shape)

import numpy as np
h,w, c = img01.shape
img = np.zeros((h,w,3), np.uint8)
for i in range(h):
    for j in range(w):
        # Random color
        img[i,j] = ( random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
plt.title('img')
# plt.show()

# Another img
# h2, w2 = img01.shape
img3 = img01.copy()
for i in range(100, 450):
    for j in range(350, 400):
        img01[i,j]=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

plt.imshow(cv.cvtColor(img01, cv.COLOR_BGR2RGB))
plt.title("Custom IMG")
plt.show()