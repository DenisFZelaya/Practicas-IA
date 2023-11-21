import cv2
import cv2 as cv
import numpy as np

import imshow as helper

imgLondon = cv.imread("london.jpeg")
helper.imshow("LONDON", imgLondon)

# Separar capas de la imagen
B, G, R = cv.split(imgLondon)

zeros = np.zeros(imgLondon.shape[:2], dtype="uint8")

print(zeros)
helper.imshow("RED", cv2.merge([B, zeros, R]))