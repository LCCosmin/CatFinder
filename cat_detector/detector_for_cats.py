import cv2
from numpy import ndarray
from time import sleep

from ultralytics import YOLO

face_cascade = cv2.CascadeClassifier('cat_detector/haarcascade_frontalcatface_extended.xml')

def detect_cats(frame: ndarray) -> bool:
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  

    # Detects faces of different sizes in the input image  
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)  

    cat_face = ""
    for (x,y,w,h) in faces:
      cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
      cat_face = frame[y:y+h, x:x+w]

    return(
        True
        if type(faces) is ndarray
        else
        False,
        cat_face
    )



def detect_cats_YOLO(frame) -> bool:
    """
    Function receives an image,
    passes it through YOLOv8 neural network
    and returns an array of detected objects
    and their bounding boxes
    :param buf: Input image file stream
    :return: Array of bounding boxes in format 
    [[x1,y1,x2,y2,object_type,probability],..]
    """
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