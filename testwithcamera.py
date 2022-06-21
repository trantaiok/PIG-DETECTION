import cv2
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import torch
from detecto import core
from detecto.utils import normalize_transform
import time

model = core.Model.load('heo_model_weights.pth', ['heo'])
  
cv2.namedWindow('Detecto')
try:
    video = cv2.VideoCapture(0)
 
except:
    print('No webcam available.')
  

while True:
    ret, frame = video.read()
    if not ret:
        break

    labels, boxes, scores = model.predict(frame)

    #Plot each box with its label and score
    for i in range(boxes.shape[0]):
        if scores[i] < 0.8:
            continue

        box = boxes[i]
        cv2.rectangle(frame, (int(box[0]), int(box[1])), (int(box[2]), int(box[3])), (255, 0, 0), 3)
        if labels:
            cv2.putText(frame, '{}: {}'.format(labels[i]+ "#" + str(i+1), round(scores[i].item(), 2)), (int(box[0]), int(box[1] - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

    cv2.imshow('Detecto', frame)

    # If the 'q' or ESC key is pressed, break from the loop
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == 27:
        break

cv2.destroyWindow('Detecto')
video.release()

