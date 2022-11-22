import cv2

frameWidth = 640
frameHeight = 320

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    cv2.imshow('AMS',img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break