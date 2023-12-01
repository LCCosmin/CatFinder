import cv2

def camera_sensor(camera_url: str) -> None:
    print(f"Starting camera sensor for {camera_url}")

    static_back = None
    if camera_url == "0":
        video = cv2.VideoCapture(0) 
    else:
        video = cv2.VideoCapture(camera_url) 

    try:
        while True: 
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

            if cnts !=  ():
                print(f"something found! better check! with camera url {camera_url}")

            cv2.imshow(f"Gray Frame {camera_url}", gray) 
            cv2.imshow(f"Color Frame {camera_url}", frame)

            key = cv2.waitKey(1) 
            if key == ord('q'): 
                break
    finally:
        print(f"Ending camera sensor for {camera_url}")
        video.release() 
        cv2.destroyAllWindows() 
