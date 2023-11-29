import cv2

static_back = None
video = cv2.VideoCapture("ip") 

while True: 
    check, frame = video.read() 
    motion = 0

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
        print("something found! better check!")

    cv2.imshow("Gray Frame", gray) 
    cv2.imshow("Color Frame", frame)

    key = cv2.waitKey(1) 
    if key == ord('q'): 
        break

video.release() 

cv2.destroyAllWindows() 