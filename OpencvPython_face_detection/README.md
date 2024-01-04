# Face Detection Project

This project uses OpenCV to detect faces in an image.

## Prerequisites

- Python
- OpenCV

## Installation

1. Clone the repository
2. Install the dependencies using pip:
   ```
   pip install -r requirements.txt
   ```

## Usage

Replace the directory of your own picture and run the script `face-detection.py`:
```
python face-detection.py
```

## How it works

The script uses the Haar Cascade classifier provided by OpenCV to detect faces in an image. The image is first converted to grayscale as the OpenCV algorithm for object detection works on grayscale images.

Once the faces are detected, the script draws rectangles around the detected faces and displays the image.

