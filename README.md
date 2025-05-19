# 👥 Crowd Detection System 📹

![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.6%2B-brightgreen)
![OpenCV](https://img.shields.io/badge/OpenCV-4.5.0%2B-orange)

## 🌟 Overview

This project is a smart crowd detection system that uses computer vision to identify gatherings of people in video footage. The system leverages YOLOv5 object detection to recognize people in each frame, then analyzes their spatial distribution to determine if crowds are forming.

## ✨ Features

- 🔍 **Person Detection**: Uses YOLOv5 to detect and count people in video frames
- 👥 **Crowd Analysis**: Identifies crowds based on spatial proximity of detected individuals
- ⏱️ **Persistent Crowd Detection**: Only flags crowds that are present for a specified number of consecutive frames
- 🖥️ **Visual Feedback**: Displays bounding boxes around detected people and annotates frames with crowd alerts
- 📊 **Logging**: Records frame numbers and crowd sizes when crowds are detected

## 📋 Requirements

- Python 3.6+
- PyTorch
- OpenCV (cv2)
- NumPy
- Pandas
- SciPy
- YOLOv5 (loaded via torch.hub)

## 🚀 Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/crowd-detection.git
   cd crowd-detection
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
   
   (Create a `requirements.txt` file containing:)
   ```
   torch>=1.7.0
   opencv-python>=4.5.0
   numpy>=1.19.0
   pandas>=1.1.0
   scipy>=1.5.0
   ```

## 🛠️ Usage

1. Replace `'your video path'` with the path to your video file:
   ```python
   path = 'path/to/your/video.mp4'
   ```

2. Adjust parameters as needed:
   ```python
   model.conf = 0.4  # Detection confidence threshold
   threshold = 75    # Proximity threshold for crowd detection (in pixels)
   frames = 10       # Number of consecutive frames needed to confirm a crowd
   ```

3. Run the script:
   ```
   python main.py
   ```

4. Press 'q' to exit the video display.

## ⚙️ How It Works

1. **Object Detection**: The system processes each frame of video using YOLOv5 to detect people.
2. **Spatial Analysis**: For each frame with 3+ people, it calculates distances between all detected individuals.
3. **Crowd Identification**: If 3+ people are in close proximity (closer than the threshold distance), a potential crowd is identified.
4. **Persistence Check**: To filter out momentary gatherings, a crowd is only confirmed after being detected in a specified number of consecutive frames.
5. **Visualization**: Confirmed crowds trigger visual alerts and logging.

## 🎛️ Parameters

- `model.conf`: Confidence threshold for YOLO detections (default: 0.4)
- `threshold`: Maximum distance (in pixels) between people to be considered "close" (default: 75)
- `frames`: Number of consecutive frames a crowd must be detected before being logged (default: 10)

## ⚠️ Limitations

- Performance depends on video resolution and system resources
- Fixed distance threshold may not work optimally for all camera perspectives
- Detection quality is contingent on YOLOv5's performance

## 🔮 Future Improvements

- Implement dynamic distance thresholds based on perspective
- Add density-based crowd analysis
- Include crowd movement direction tracking
- Create a web interface for parameter tuning
- Support multiple camera inputs

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- [YOLOv5](https://github.com/ultralytics/yolov5) for object detection

---

### 📊 Sample Output

The system outputs information about detected crowds, including:
- Frame number where the crowd was first detected
- Number of people in the crowd
- Visual indicators on the video feed

### 🔄 Workflow Diagram

```
Video Input → Frame Processing → Person Detection → 
Spatial Analysis → Crowd Identification → Alert Generation
```

---

Made with ❤️ by [Your Name]
