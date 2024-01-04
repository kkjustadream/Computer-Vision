# Hand Tracking Project

This project is a collection of Python scripts that use hand tracking to perform various tasks. The project uses the MediaPipe library for hand tracking and the OpenCV library for image processing.

## Modules

The project consists of the following modules:

- `HandTrackModule.py`: This module contains the `handDetector` class which is used to detect hands in an image. It provides methods to find hands in an image and draw points and connections, and to find the position of a specific hand.

- `volume_hand_control.py`: This script uses the `handDetector` class to control the system volume. The distance between the thumb and the index finger is used to determine the volume level.

- `finger_count.py`: This script uses the `handDetector` class to count the number of fingers that are open(single hand). It also displays an image corresponding to the number of fingers that are open.

- `main.py`: This script prints the path to the site-packages directory where Python packages are installed(not important).

## Requirements

- Python 3.6 or higher
- OpenCV
- MediaPipe
- PyCaw
- comtypes
- numpy

## Usage

To use the modules in this project, you need to import them in your Python script. For example, to use the `handDetector` class in your script, you would do:

```python
import HandTrackModule as htm
detector = htm.handDetector()
```

You can then use the `findHands` and `findPosition` methods of the `handDetector` class to find hands in an image and get the position of a specific hand.

For the `volume_hand_control.py` and `finger_count.py` scripts, you can run them directly from the command line, and press 'q' to quit

```bash
python volume_hand_control.py
python finger_count.py
```
