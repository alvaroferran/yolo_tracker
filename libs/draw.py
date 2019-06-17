import cv2


def draw_target_window(image, target_window, width, height):
    line_width = 2
    line_color = (0,0,0)
    x_min, x_max, y_min, y_max = target_window
    cv2.line(image, (x_min, 0), (x_min, height), line_color, line_width)
    cv2.line(image, (x_max, 0), (x_max, height), line_color, line_width)
    # cv2.line(image, (0, y_min), (width, y_min), line_color, line_width)
    cv2.line(image, (0, y_max), (width, y_max), line_color, line_width)
    return image


def draw_countertop_line(image, line_coords):
    line_width = 2
    line_color = (0, 255, 0)
    cv2.line(image, *line_coords, line_color, line_width)
    return image


def draw_text(image, text):
    font = cv2.FONT_HERSHEY_SIMPLEX
    pos = (50, 50)
    size = 1
    color = (255, 255, 255)
    thickness = 3
    cv2.putText(image, text, pos, font, size, color, thickness, cv2.LINE_AA)
    return image
