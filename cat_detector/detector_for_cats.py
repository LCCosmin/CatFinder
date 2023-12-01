from ultralytics import YOLO

def detect_cats_YOLO(frame) -> bool:
    model = YOLO("yolov8x.pt")
    results = model.predict(frame)
    result = results[0]
    output = []
    for box in result.boxes:
        x1, y1, x2, y2 = [
            round(x) for x in box.xyxy[0].tolist()
        ]
        items = box.cls[0].item()
        print(type(items))
        print(items)
        if box.cls[0].item() == 15.0:  # 15.0 is fot cat
          output.append(
              frame[y1:y2, x1:x2]
          )
    return (
      True
      if len(output) is not 0
      else
      False
      ,
      output
    )
