import cv2
import numpy as np
import imutils

image = cv2.imread("tesla1.jpg", 0)
image= imutils.resize(image, width=400)


_, binarizada = cv2.threshold(image, 210, 255, cv2.THRESH_BINARY)
_, binarizadaInv = cv2.threshold(image, 210, 255, cv2.THRESH_BINARY_INV)
adapt = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11,2)
# _, Trunc = cv2.threshold(image, 250, 255, cv2.THRESH_TRUNC)


cv2.imshow("Imagen", image)
cv2.imshow("Tipos Binary - BInary", binarizada)
cv2.imshow("Tipos Binary - BInary INV", binarizadaInv)
cv2.imshow("adapt", adapt)

#cv2.imshow("Tipos Trunc", Trunc)


cv2.waitKey(0)
cv2.destroyAllWindows()

#https://docs.opencv.org/3.4/d7/d4d/tutorial_py_thresholding.html