import numpy as np
import os

# ===== PROJECT ROOT =====
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ASSETS_DIR = os.path.join(BASE_DIR, "assets")

BG1_PATH = os.path.join(ASSETS_DIR, "bg1.jpg")
BG2_PATH = os.path.join(ASSETS_DIR, "bg2.jpg")
BG_VIDEO_PATH = os.path.join(ASSETS_DIR, "bg_video.mp4")

# ===== HSV RANGE FOR GREEN =====
LOWER_GREEN = np.array([35, 40, 40])
UPPER_GREEN = np.array([85, 255, 255])

# ===== CAMERA SETTINGS =====
CAMERA_INDEX = 0
FRAME_WIDTH = 640
FRAME_HEIGHT = 480
