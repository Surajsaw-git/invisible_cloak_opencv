# invisible_cloak_opencv
This repository implements a real-time "Invisibility Cloak" effect using OpenCV and Python. By capturing a background frame and using HSV color segmentation, it identifies a specific colored cloth and replaces it with the background. It utilizes morphological transformations and bitwise operations to create a seamless magical effect.

The project utilizes color-based segmentation (specifically in the HSV color space) to detect a specific color of fabric, such as a red or blue cloth, and replaces it in real-time with a pre-captured background image [1].

Key Features
Real-time Image Processing: Uses cv2.VideoCapture to process live webcam feeds.
Color Detection & Masking: Employs thresholding to create a binary mask of the cloak.
Morphological Operations: Includes cv2.dilate and cv2.morphologyEx to remove noise and smooth the edges of the cloak [2].
Bitwise Operations: Combines the background and current frame using cv2.bitwise_and and cv2.bitwise_or to create the final invisibility effect.

Getting Started
To run this project, you can install the necessary dependencies via OpenCV's official documentation:

pip install opencv-python numpy

Citations:
[1] OpenCV Image Processing Tutorials
[2] Morphological Transformations Documentation
