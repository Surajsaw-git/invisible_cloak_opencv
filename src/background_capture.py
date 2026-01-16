import cv2
import time

def capture_background(cap, num_frames=30):
    """
    Capture background by averaging multiple frames
    """
    print("📸 Capturing background... Please move out of frame.")
    time.sleep(2)

    background = None

    for i in range(num_frames):
        ret, frame = cap.read()
        if not ret:
            continue

        if background is None:
            background = frame.copy().astype("float")
        else:
            cv2.accumulateWeighted(frame, background, 0.5)

    print("✅ Background captured")
    return background.astype("uint8")
