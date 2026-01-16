# Invisible Cloak with OpenCV

This repository implements a real-time "Invisibility Cloak" effect using Python and OpenCV. By capturing a background frame and using HSV color segmentation, it identifies a specific colored cloth (like green or red) and replaces it with the background in real-time.



## Features
* **Real-time Processing:** Uses `cv2.VideoCapture` for live webcam interaction.
* **Color Detection:** Employs HSV thresholding for precise color masking.
* **Noise Reduction:** Uses morphological operations (dilation) to smooth the cloak edges.
* **Dynamic Background:** Supports static images or pre-captured background frames.

## Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Surajsaw-git/invisible_cloak_opencv.git](https://github.com/Surajsaw-git/invisible_cloak_opencv.git)
   cd invisible_cloak_opencv

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/Scripts/activate  # For Windows

3. **Install dependencies:**
    ```bash
    pip install opencv-python numpy


4. **How to Run**
    ```bash
    python src/advanced_cloak.py
