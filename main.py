import cv2
import torch
import numpy as np
import pandas as pd
from scipy.spatial.distance import cdist
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
model.conf = 0.4
path = 'your video path'
threshold = 75
frames= 10
frame_count = 0
crowd_frames = []
crowd_streak = 0
last_crowd_person_count = 0
crowd_log = []
cap = cv2.VideoCapture(path)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frame_count += 1
    results = model(frame)
    detections = results.xyxy[0]
    person_centers = []
    for *box, conf, cls in detections:
        if int(cls) == 0:
            x1, y1, x2, y2 = map(int, box)
            cx = (x1 + x2) // 2
            cy = (y1 + y2) // 2
            person_centers.append((cx, cy))
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
    crowd_detected = False
    person_count = len(person_centers)
    if person_count >= 3:
        dists = cdist(person_centers, person_centers)
        close_matrix = (dists < threshold).astype(int)
        close_counts = np.sum(close_matrix, axis=1)
        group_indices = [i for i, count in enumerate(close_counts) if count >= 3]
        if len(group_indices) >= 3:
            crowd_detected = True
    if crowd_detected:
        crowd_streak += 1
        last_crowd_person_count = len(group_indices)
    else:
        crowd_streak = 0
    if crowd_streak == frames:
        print(f"Crowd at frame {frame_count - frames + 1}")
        crowd_log.append([frame_count - frames + 1, last_crowd_person_count])
        cv2.putText(frame, "Crowd", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
    cv2.putText(frame, f"Frame: {frame_count} People: {person_count}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    cv2.imshow("Crowd Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

