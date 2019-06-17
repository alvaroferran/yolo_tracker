import cv2


def get_target_window(width, height):
    screen_center_x = width/2.0
    screen_center_y = height/2.0
    window_percentage = 0.1
    x_min = int(screen_center_x - int(width*window_percentage))
    x_max = int(screen_center_x + int(width*window_percentage))
    y_min = int(screen_center_y - int(height*window_percentage))
    y_max = int(screen_center_y + int(height*window_percentage))
    return (x_min, x_max, y_min, y_max)


def draw_target_window(image, target_window, width, height):
    line_width = 2
    line_color = (0,0,0)
    x_min, x_max, y_min, y_max = target_window
    cv2.line(image, (x_min, 0), (x_min, height), line_color, line_width)
    cv2.line(image, (x_max, 0), (x_max, height), line_color, line_width)
    cv2.line(image, (0, y_min), (width, y_min), line_color, line_width)
    cv2.line(image, (0, y_max), (width, y_max), line_color, line_width)
    return image


def track_object(object_x, object_y, target_window):
    move_x, move_y = "0", "0"
    x_min, x_max, y_min, y_max = target_window   
    if object_x < x_min:
        move_x = "-"
    if object_x > x_max:
        move_x = "+"
    if object_y < y_min:
        move_y = "+"
    if object_y > y_max:
        move_y = "-"
    return move_x, move_y


def draw_text(image, text):
    font = cv2.FONT_HERSHEY_SIMPLEX
    pos = (50, 50)
    size = 1
    color = (255, 255, 255)
    thickness = 3
    cv2.putText(image, text, pos, font, size, color, thickness, cv2.LINE_AA)
    return image
