import cv2
from matplotlib import pyplot as plt
import numpy as np
import imshow as helper

# IMG
img = cv2.imread("flowers.jpeg")

#plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("IMAGEN")
#plt.show()

# Capas
print(img.shape)

# UTILIZAR cv2.split para obtener cada color separado

# La funcion cv2.split separa las capas de la imagen
B, G, R = cv2.split(img)

zeros = np.zeros(img.shape[:2], dtype="uint8")

helper.imshow("RED", cv2.merge([B, zeros, R]))
helper.imshow("GREEN", cv2.merge([zeros, G, zeros]))
helper.imshow("BLUE", cv2.merge([B, zeros, zeros]))
