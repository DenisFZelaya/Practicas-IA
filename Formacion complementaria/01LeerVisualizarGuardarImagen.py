import cv2

# cv2.imread -> utilizado para leer la imagen
imagen = cv2.imread("opencv-logo.png", 0)

# cv2.imshow utilizado para mostrar la imagen
cv2.imshow("image", imagen)

# Guardar imagen
cv2.imwrite("grises.png", imagen)

# cvw.waitKey(0) -> utilizado para esperar que se presione una tecla
cv2.waitKey(0)

# cv2.destroyAllWindows() -> Utilizado para destruir las ventanas abiertas
cv2.destroyAllWindows()