import cv2

captura = cv2.VideoCapture(0)
salida = cv2.VideoWriter("videoSalida.avi", 0, 30, (640, 480), True)

while(captura.isOpened()):
    ret, imagen = captura.read()
    if ret == True:
        cv2.imshow("Video", imagen)
        salida.write(imagen)
        if cv2.waitKey(1) & 0xFF == ord("s"):
            break

# Inicializar captura
captura.release()
salida.release()
cv2.destroyAllWindows()