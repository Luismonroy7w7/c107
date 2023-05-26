import cv2
import time
import math
video = cv2.VideoCapture("bb3.mp4")
while True:
    
    check, img = video.read()   
  # Cerrar la ventana de muestra cuando la barra espaciadora sea presionada
    cv2.imshow("Resultado", img)
    key = cv2.waitKey(1000)
    if key == 32:
        print("Detenido")
        break
video.release()
cv2.destroyALLwindows()