import cv2
import os

class BackgroundManager:
    def __init__(self):
        self.image = None
        self.video = None
        self.mode = None

    def load_image(self, path):
        if not os.path.exists(path):
            print(f"❌ Image not found: {path}")
            self.image = None
            return

        self.image = cv2.imread(path)
        if self.image is None:
            print(f"❌ Failed to load image: {path}")
        else:
            print(f"✅ Background image loaded")
            self.mode = "image"

    def load_video(self, path):
        if not os.path.exists(path):
            print(f"❌ Video not found: {path}")
            self.video = None
            return

        self.video = cv2.VideoCapture(path)
        if not self.video.isOpened():
            print(f"❌ Failed to open video")
        else:
            print(f"✅ Background video loaded")
            self.mode = "video"

    def get(self, shape):
        h, w = shape[:2]

        if self.mode == "image" and self.image is not None:
            return cv2.resize(self.image, (w, h))

        if self.mode == "video" and self.video is not None:
            ret, frame = self.video.read()
            if not ret:
                self.video.set(cv2.CAP_PROP_POS_FRAMES, 0)
                ret, frame = self.video.read()
            return cv2.resize(frame, (w, h))

        return None
