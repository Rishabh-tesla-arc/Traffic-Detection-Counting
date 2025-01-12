import math
from ultralytics import YOLO
import cv2, cvzone
import numpy as np
from sort import *

model = YOLO("yolov8n.pt")
cap = cv2.VideoCapture("istockphoto-924733400-640_adpp_is.mp4")

# Setting width and height
cap.set(3, 640)
cap.set(4, 480)

classnames = ["Car", "Bus", "Truck", "Van"]

# Tracker for Object creation
tracker = Sort(max_age=20, min_hits=3, iou_threshold=0.3)

# Drawing Line on the screen
line = [10, 350, 800, 350]

counter = []


while True:
    success, frame = cap.read()
    if not success:
        break


    results = model(frame, stream=True)
    detect = np.empty((0, 5))


    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2 - x1, y2 - y1

            conf = math.ceil((box.conf[0] * 100))/100
            cls = int(box.cls[0])

            if 0 <= cls < len(classnames):
                if classnames[cls] in classnames and conf > 0.4:
                    cvzone.cornerRect(frame, l=9, bbox=(x1, y1, w, h), colorR=(255, 0, 255), rt=4)
                    cvzone.putTextRect(frame, f'{classnames[cls]} {conf}', (max(0, x1), max(35, y1)),
                                       thickness=4, offset=3)
                    array = np.array([x1, y1, x2, y2, conf])
                    detect = np.vstack((detect, array))
    resultsTacker = tracker.update(detect)
    cv2.line(frame, (line[0], line[1]), (line[2], line[3]), (0, 0, 255), 6)



    line_range = 20
    for result in resultsTacker:
        x1, y1, x2, y2, id = result
        x1, y1, x2, y2, id = int(x1), int(y1), int(x2), int(y2), int(id)
        w, h = x2 - x1, y2 - y1

        centerx, centery = x1 + w // 2, y1 + h // 2
        cv2.circle(frame, (centerx, centery), radius=5, color=(255, 0, 255), thickness=cv2.FILLED)

        if (line[0] < centerx < line[2]) and (line[1] - line_range < centery < line[1] + line_range):
            if id not in counter:
                counter.append(id)
                cv2.line(frame, (line[0], line[1]), (line[2], line[3]), (0, 255, 0), 6)
    cvzone.putTextRect(frame, f' Cars : {len(counter)}', (30, 50), thickness=4, offset=3)




    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
