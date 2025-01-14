<h1 align="center" id="title">Traffic Detection &amp; Counting using YOLO and SORT</h1>

<p align="center"><img src="https://socialify.git.ci/Rishabh-tesla-arc/Traffic-Detection-Counting/image?font=Bitter&amp;forks=1&amp;issues=1&amp;language=1&amp;name=1&amp;owner=1&amp;pattern=Floating+Cogs&amp;pulls=1&amp;stargazers=1&amp;theme=Dark" alt="project-image"></p>

<p id="description">This project implements a real-time traffic detection and counting system using the YOLO (You Only Look Once) object detection model and the SORT (Simple Online and Realtime Tracking) algorithm. The system is designed to process video footage whether from pre-recorded files or live camera feeds to identify and track vehicles dynamically. By combining the robust object detection capabilities of YOLO with the efficient tracking mechanism of SORT it achieves accurate and consistent tracking of individual vehicles even across frames. The system works by drawing a virtual line in the video frame which serves as a counting threshold. Vehicles are counted when their center points cross this line with each vehicle assigned a unique ID to prevent duplicate counting. Additionally the system displays bounding boxes tracking IDs and a real-time vehicle count on the processed video stream making it an intuitive and effective tool for traffic analysis.</p>
<p id="description">The system works by drawing a virtual line in the video frame which serves as a counting threshold. Vehicles are counted when their center points cross this line with each vehicle assigned a unique ID to prevent duplicate counting. Additionally the system displays bounding boxes tracking IDs and a real-time vehicle count on the processed video stream making it an intuitive and effective tool for traffic analysis.</p>

  
  
<h2> SORT:</h2>
<p>A simple online and realtime tracking algorithm for 2D multiple object tracking in video sequences.
<p>More on here: https://github.com/abewley/sort</p>

<h2>🧐 Features</h2>
Here're some of the project's best features:

*   Object Detection
*   Object Tracking
*   Vehicle Counting
*   Real-Time Processing
*   Dynamic Visualization
*   Vehicle Classification
*   Multi-Lane Tracking
*   Scalability for Multiple Cameras
*   AI Model Customization

<h2>🛠️ Installation Steps:</h2>

<p>1. Clone the repository:</p>

```
git clone https://github.com/Rishabh-tesla-arc/Traffic-Detection-Counting.git
cd Traffic-Detection-Counting 
```

<p>2. Install the required dependencies:</p>

```
pip install -r requirements.txt
```

<p>3. Download YOLO Weights. Download the YOLOv8 weights (yolov8n.pt) from the Ultralytics repository and place it in the project directory.</p>

<p>4. Run the script:</p>

```
python main.py
```

<p>5. Press q to stop the video playback.</p>

  
<h2>💻 Built with</h2>

Technologies used in the project:

*   Python
*   YOLO (You Only Look Once)
*   SORT (Simple Online and Realtime Tracking)
*   OpenCV
*   cvzone
*   NumPy
*   Ultralytics YOLO API
*   Video Processing


![f2cfd2d2-2560-4ce2-a37d-2abf9b5b7c22](https://github.com/user-attachments/assets/6f046913-41ba-4557-85bb-f4a0a3430dd1)


