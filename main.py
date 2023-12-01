from threading import Thread
from motion_sensor.motion_camera import camera_sensor
from helper.config import yaml_to_dict

def main():
    thread_list = []
    cameras = yaml_to_dict("config.yaml")["cameras"]
    
    for camera in cameras:
        new_thread = Thread(target=camera_sensor, args=([cameras[camera]["url"]]))
        thread_list.append(new_thread)
    
    for thread in thread_list:
        thread.start()

    
if __name__ == "__main__":
    main()
