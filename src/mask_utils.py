import cv2
from config import LOWER_GREEN, UPPER_GREEN

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))

def get_green_mask(hsv):
    mask = cv2.inRange(hsv, LOWER_GREEN, UPPER_GREEN)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel)
    return mask
