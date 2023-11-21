import cv2
import  numpy as np

# cv2.VideoCapture -> Utilizado para leer ya sea un archivo o la camara
video = cv2.VideoCapture("videoSalida.avi")

# Mostrar el video
while(video.isOpened()):
    ret, imagen = video.read()
    if ret == True:
        cv2.imshow("Video", imagen)

        if(cv2.waitKey(30) & 0xFF == ord("s")):
            break
    else:
        break

video.release()
cv2.destroyAllWindows()