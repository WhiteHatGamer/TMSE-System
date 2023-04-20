import cv2
from pyzbar.pyzbar import decode
import time

cap = cv2.VideoCapture('http://192.168.0.100:4747/video')
cap.set(3, 640)
cap.set(4, 480)

while True:
    success ,frame = cap.read()
    for code in decode(frame):
        print(code.data.decode('utf-8'))
    cv2.imshow("Scanner",frame)
    cv2.waitKey(1)
