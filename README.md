# Face Recognition with OpenCV and face_recognition

A friend of mine wanted a camera to be installed on the door when he stood in front of it to see if it was really him. My friend holds up his face. The camera looks to see if it is him, and if it is, it opens the lock on the door. If it's not him, the door stays closed, but a snapshot is taken to see who it was.

The future: Can detect when someone is stealing something in front of the door, an anti-burglary system, which is then connected to the cloud and automatically forwarded to the police.

This project demonstrates real-time face recognition using OpenCV and the face_recognition library. It allows you to recognize faces captured by your webcam and label them accordingly.

## Requirements
- Python 3.x
- OpenCV (`cv2`)
- face_recognition library

## Installation
1. Install Python if you haven't already. You can download it from the [official Python website](https://www.python.org/downloads/).
2. Install OpenCV and face_recognition:
   ```
   pip install opencv-python-headless
   pip install face_recognition
   ```

## Usage
1. Clone or download this repository to your local machine.
2. Place an image of the face you want to recognize in the project directory and update the filename in the code.
3. Run the script:
   ```
   python face_recognition_demo.py
   ```
4. The webcam will activate, and faces in the video feed will be recognized in real-time.

## Important Notes
- Ensure that your webcam is correctly connected and recognized by your operating system.
- OpenCV is required to read from your webcam. However, it is not necessary to use the face_recognition library alone.
- If you encounter difficulties installing OpenCV, you may want to try alternative demos provided by face_recognition that do not require it.

## Credits
This project utilizes the following libraries:
- [OpenCV](https://opencv.org/)
- [face_recognition](https://github.com/ageitgey/face_recognition)

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
