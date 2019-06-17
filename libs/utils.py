import cv2
import numpy as np


def get_target_window(width, height):
    screen_center_x = width/2.0
    screen_center_y = height/2.0
    window_percentage = 0.1
    x_min = int(screen_center_x - int(width*window_percentage))
    x_max = int(screen_center_x + int(width*window_percentage))
    y_min = int(screen_center_y - int(height*window_percentage))
    y_max = int(screen_center_y + int(height*window_percentage))
    return (x_min, x_max, y_min, y_max)


def track_object(object_x, object_y, target_window):
    centered = False
    move_x, move_y = "0", "0"
    x_min, x_max, y_min, y_max = target_window
    if object_y < y_max: 
        if object_x < x_min:
            move_x = "-"
        elif object_x > x_max:
            move_x = "+"
        else:
            centered = True
    # if object_y < y_min:
    #     move_y = "+"
    # if object_y > y_max:
    #     move_y = "-"
    return move_x, move_y, centered


def get_edges(image):
    edge_histeresis = (100, 200)
    return cv2.Canny(image, *edge_histeresis, L2gradient=True)


def get_countertop(image, height):
    edges = get_edges(image)
    valid_values = False
    line_coords = [(0, 0), (0, 0)]
    counter_center_y = 0
    threshold = 100
    min_len = 250
    max_gap = 20
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold,
                            minLineLength=min_len, maxLineGap=max_gap)
    try:
        for i, _ in enumerate(lines):
            for x1,y1,x2,y2 in lines[i]:
                line_center_y = int((y2-y1)/2 + y1)
                offset = 100
                screen_center_y = height/2 + offset/2
                max_angle = 20
                angle = np.degrees(np.arctan((y2-y1)/(x2-x1)))
                if -max_angle < angle < max_angle:
                    if screen_center_y - offset < line_center_y < screen_center_y:
                        valid_values = True
                        line_coords = ((x1, y1), (x2, y2))
                        counter_center_y = line_center_y
    except Exception:
        pass
    return (valid_values, line_coords, counter_center_y)
