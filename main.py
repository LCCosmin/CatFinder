import cv2
from time import sleep

def main():
    # works
    # must figure out how to add here credentials to the server
    capture =cv2.VideoCapture("ip")
    
    while True:
        live, frame = capture.read()
        
        cv2.imshow("livestream", frame)
        
        if cv2.waitKey(1) == ord("q") or not live:
            break
    
    capture.release()
    cv2.destroyAllWindows()
    
main()