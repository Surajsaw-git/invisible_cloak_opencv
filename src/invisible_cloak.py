import cv2
import numpy as np
from utils import get_green_mask
from background_capture import capture_background

def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("❌ Camera not accessible")
        return

    # Capture background
    background = capture_background(cap)

    print("🧥 Invisible cloak started. Press ESC to exit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Flip for natural mirror view
        frame = cv2.flip(frame, 1)

        # Convert to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Get green mask
        mask = get_green_mask(hsv)
        mask_inv = cv2.bitwise_not(mask)

        # Extract non-green part (person)
        person_part = cv2.bitwise_and(frame, frame, mask=mask_inv)

        # Extract background where green is present
        bg_part = cv2.bitwise_and(background, background, mask=mask)

        # Combine both
        final_output = cv2.add(person_part, bg_part)

        cv2.imshow("Invisible Cloak", final_output)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
