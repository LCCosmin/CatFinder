import cv2
from threading import Thread
from time import sleep

from cat_detector.detector_for_cats import detect_cats_YOLO


def camera_sensor(camera_url: str) -> None:
    print(f"Starting camera sensor for {camera_url}")

    static_back = None
    

    try:
        while True:
            video = cv2.VideoCapture(
                0
                if camera_url == "0"
                else
                camera_url
            )
            # get video stream
            _, frame = video.read()

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
            gray = cv2.GaussianBlur(gray, (21, 21), 0) 

            if static_back is None:
                static_back = gray
                continue

            diff_frame = cv2.absdiff(static_back, gray) 
            thresh_frame = cv2.threshold(diff_frame, 30, 255, cv2.THRESH_BINARY)[1]
            thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2)

            cnts,_ = cv2.findContours(
                thresh_frame.copy(),
                cv2.RETR_EXTERNAL,
                cv2.CHAIN_APPROX_SIMPLE
            )

            # check for cats if motion sensor found something
            if cnts !=  ():
                thread = Thread(target=detect_cats_YOLO, args=([frame]))
                thread.start()

            key = cv2.waitKey(1)
            if key == ord('q'):
                break

            video.release()
            sleep(5)
            
    finally:
        print(f"Ending camera sensor for {camera_url}")
        video.release()
        cv2.destroyAllWindows()
