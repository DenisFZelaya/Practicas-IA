import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import imshow as helper

img = np.zeros((512,512,3), np.uint8)

## Dibujar
font = cv.FONT_HERSHEY_SIMPLEX
cv.rectangle(img, (384,0), (510,128), (2,255,0), 3)
cv.line(img, (0,0), (511,511), (255,0,0), 5)
cv.circle(img, (477,63), 63, (0,0,255), -1)
cv.ellipse(img, (256,256), (100,50), 0 , 0, 180, 255, -1)

# cv.putText; Agrega una texto a la imagen
cv.putText(img, "OPENCV", (10,500), font, 4, (255,255,255), 2, cv.LINE_AA)
img_scaled = cv.resize(img, (100,200), interpolation= cv.INTER_AREA)

plt.imshow(cv.cvtColor(img_scaled, cv.COLOR_BGR2RGB))
plt.title("IMG")
plt.show()

cv.waitKey()
cv.destroyAllWindows()