import cv2
from cat_detector.detector_for_cats import detect_cats, detect_cats_YOLO
from time import sleep

def main():
    # works
    # must figure out how to add here credentials to the server
    
    # while True:
    #     capture = cv2.VideoCapture("https://192.168.1.160:8080/video")
    #     live, frame = capture.read()
        
    #     is_cat, cat_image = detect_cats(frame)
    #     if is_cat:
    #         print("AM GASIT_O PE EMA!")
    #         cv2.imshow("livestream", cat_image)
    #     if cv2.waitKey(1) == ord("q") or not live:
    #         break
    #     else:
    #         cv2.imshow("livestream", frame)
    
    while True:
        capture = cv2.VideoCapture("ip")
        live, frame = capture.read()
        
        is_cat, cat_images = detect_cats_YOLO(frame)
        if is_cat:
            print("AM GASIT_O PE EMA!")
            cv2.imshow("livestream", cat_images[0])
        if cv2.waitKey(1) == ord("q") or not live:
            break
        # else:
        #     cv2.imshow("livestream", frame)
            
    
    capture.release()
    cv2.destroyAllWindows()
    
    # frame = cv2.imread("catts.jpg")
    # print(type(frame))
    # is_cat, cats = detect_cats_YOLO(frame)
    # print(is_cat)
    # for cat in cats:
    #     cv2.imshow("cat", cat)
    #     if cv2.waitKey(500) == ord("q"):
    #         break
    
main()