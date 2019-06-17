from keras_yolo3.yolo import YOLO
from PIL import Image
from libs.utils import *
import cv2
import numpy as np
import yaml
import serial
import time


# Read configuration
with open("config.yml", 'r') as ymlfile:
    config = yaml.load(ymlfile)

yolo = YOLO()
bt = serial.Serial('/dev/rfcomm0', 19200)
while True:
    in_data = bt.read_until().decode()
    if in_data[:-2] == "a":
        bt.write("b".encode())
        break
print("Connected!")

try:
    # Input video stream
    vid = cv2.VideoCapture(0)
    if not vid.isOpened():
        raise IOError("Couldn't open webcam or video") 
    video_size = (int(vid.get(cv2.CAP_PROP_FRAME_WIDTH)),
                  int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))) 

    # Output stream to save the video output
    if config["save_video"]:
        video_name = config["output_name"] + ".mp4"
        video_fps = config["output_fps"]
        video_fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(video_name, video_fourcc, video_fps, video_size)

    first_centered = True
    while True:
        return_value, frame = vid.read()
        image = Image.fromarray(frame)
        image, object_center = yolo.detect_image(image)
        image = np.asarray(image)
        # Add target zone to image
        target_window = get_target_window(*video_size)
        image = draw_target_window(image, target_window, *video_size)
        # If object found
        if object_center is not None:
            move_x, move_y = track_object(*object_center, target_window)
            shoot = "0"
            # If object centered
            if move_x == "0" and move_y == "0":
                shoot_delay = 3
                # Restart countdown if object lost or decentered
                if first_centered == True:
                    start_time = time.time()
                    first_centered = False
                time_remaining = shoot_delay - int(time.time() - start_time)
                if time_remaining > 0:
                    image = draw_text(image, str(time_remaining))
                elif time_remaining == 0:
                    image = draw_text(image, "Shoot")
                    shoot = "1"
            else:
                first_centered = True
            data = move_x + "," + move_y + "," + shoot + "\n"
            bt.write(data.encode())
            bt.flush()
        else:
            first_centered = True
        # Show yolo stream
        if config["show_stream"]:
            cv2.namedWindow("image", cv2.WINDOW_NORMAL)
            cv2.imshow("image", image)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        # Save frame to output video
        if config["save_video"]:
            out.write(image)

finally:
    if config["save_video"]:
        out.release()
    vid.release()
    cv2.destroyAllWindows()
    yolo.close_session()

