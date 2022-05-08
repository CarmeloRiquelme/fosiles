import cv2
import numpy as np

while(True):
    url = "http://10.216.4.182:8080/shot.jpg"
    cp = cv2.VideoCapture(url)
    camera, frame = cap.read()
    if frame is not None:
        cv2.imshow("Frame", frame)
    q = cv2.waitKey(1)
    if q==ord("q"):
        break
cv2.destroyAllWindows()
