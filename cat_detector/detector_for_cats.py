import cv2
import os
from ultralytics import YOLO

from cat_folder.cat_folder_path import get_current_cat_folder_path


def save_cat_picture(frames) -> None:
    path = get_current_cat_folder_path() + "/cat_folder/"
    number_of_items = len(os.listdir(path))

    for frame in frames:
        number_of_items += 1
        print(f"Saved picture {path}/{number_of_items}.jpg")
        cv2.imwrite(f"{path}/{number_of_items}.jpg", frame)

def detect_cats_YOLO(frame) -> None:
    print("detecting")
    model = YOLO("yolov8x.pt")
    results = model.predict(frame, verbose=False)
    result = results[0]
    output = []
    for box in result.boxes:
        x1, y1, x2, y2 = [
            round(x) for x in box.xyxy[0].tolist()
        ]
        if box.cls[0].item() == 15.0:  # 15.0 is fot cat
          output.append(
              frame[y1:y2, x1:x2]
          )

    if len(output) != 0:
        save_cat_picture(output)
