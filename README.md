### Crowd Detection System
#### Overview
This project is a crowd detection system that uses computer vision to identify gatherings of people in video footage. The system leverages YOLOv5 object detection to recognize people in each frame, then analyzes their spatial distribution to determine if crowds are forming.
#### Features

- Person Detection: Uses YOLOv5 to detect and count people in video frames
- Crowd Analysis: Identifies crowds based on spatial proximity of detected individuals
- Persistent Crowd Detection: Only flags crowds that are present for a specified number of consecutive frames
- Visual Feedback: Displays bounding boxes around detected people and annotates frames with crowd alerts
- Logging: Records frame numbers and crowd sizes when crowds are detected

#### Requirements

- Python 3.6+
- PyTorch
- OpenCV (cv2)
- SciPy
- YOLOv5 (loaded via torch.hub)

#### Installation

Clone this repository:
```
git clone https://github.com/yourusername/crowd-detection.git
cd crowd-detection
```
Install the required packages:
```
pip install -r requirements.txt
```
Usage

Adjust parameters as needed:
pythonmodel.conf = 0.4  # Detection confidence threshold
threshold = 75    # Proximity threshold for crowd detection (in pixels)
frames = 10       # Number of consecutive frames needed to confirm a crowd

Run the script:
python main.py

Press 'q' to exit the video display.

#### How It Works

- Object Detection: The system processes each frame of video using YOLOv5 to detect people.
- Spatial Analysis: For each frame with 3+ people, it calculates distances between all detected individuals.
- Crowd Identification: If 3+ people are in close proximity (closer than the threshold distance), a potential crowd is identified.
- Persistence Check: To filter out momentary gatherings, a crowd is only confirmed after being detected in a specified number of consecutive frames.
- Visualization: Confirmed crowds trigger visual alerts and logging.

#### Parameters

- model.conf: Confidence threshold for YOLO detections (default: 0.4)
- threshold: Maximum distance (in pixels) between people to be considered "close" (default: 75)
- frames: Number of consecutive frames a crowd must be detected before being logged (default: 10)

#### Limitations

- Performance depends on video resolution and system resources
- Fixed distance threshold may not work optimally for all camera perspectives
- Detection quality is contingent on YOLOv5's performance

#### Future Improvements

- Implement dynamic distance thresholds based on perspective
- Add density-based crowd analysis
- Include crowd movement direction tracking
- Create a web interface for parameter tuning
- Support multiple camera inputs

#### License
This project is licensed under the MIT License - see the LICENSE file for details.
#### Acknowledgments

YOLOv5 for object detection
