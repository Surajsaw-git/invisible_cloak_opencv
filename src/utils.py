import cv2
import numpy as np

def get_green_mask(hsv_frame):
    """
    Detect green color in HSV frame and return mask
    """
    lower_green = np.array([35, 40, 40])
    upper_green = np.array([85, 255, 255])

    mask = cv2.inRange(hsv_frame, lower_green, upper_green)

    # Remove noise
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, None)
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, None)

    return mask
