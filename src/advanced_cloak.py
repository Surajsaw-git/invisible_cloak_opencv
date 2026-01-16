import cv2
from mask_utils import get_green_mask
from background_manager import BackgroundManager
from config import (
    CAMERA_INDEX,
    FRAME_WIDTH,
    FRAME_HEIGHT,
    BG1_PATH,
    BG2_PATH,
    BG_VIDEO_PATH
)

def main():
    # ✅ FORCE DirectShow backend (FIXES MSMF ERROR)
    cap = cv2.VideoCapture(CAMERA_INDEX, cv2.CAP_DSHOW)

    if not cap.isOpened():
        print("❌ Camera not accessible")
        return

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

    bg = BackgroundManager()
    bg.load_image(BG1_PATH)

    print("""
ADVANCED INVISIBLE CLOAK
-----------------------
1 : Background Image 1
2 : Background Image 2
3 : Background Video
ESC : Exit
""")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("⚠️ Camera frame skipped, retrying...")
            continue   # 🔥 DO NOT EXIT, just retry

        frame = cv2.flip(frame, 1)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        mask = get_green_mask(hsv)
        mask_inv = cv2.bitwise_not(mask)

        background = bg.get(frame.shape)

        if background is None:
            output = frame
        else:
            person = cv2.bitwise_and(frame, frame, mask=mask_inv)
            bg_part = cv2.bitwise_and(background, background, mask=mask)
            output = cv2.add(person, bg_part)

        cv2.imshow("Advanced Invisible Cloak", output)

        key = cv2.waitKey(1) & 0xFF

        if key == 27:
            break
        elif key == ord('1'):
            bg.load_image(BG1_PATH)
        elif key == ord('2'):
            bg.load_image(BG2_PATH)
        elif key == ord('3'):
            bg.load_video(BG_VIDEO_PATH)

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
