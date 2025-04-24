# Virtual Camera App

This project is a virtual camera application built in Python. It allows users to create a virtual camera for use in video conferencing tools, streaming platforms, testing pipelines, and virtual backgrounds.

## Project Structure

```
virtual-camera-app
├── src
│   ├── main.py                 # Entry point of the application
│   ├── camera
│   │   ├── virtual_camera.py   # Contains the VirtualCamera class
│   │   └── utils.py            # Utility functions for camera setup
├── screenshot-video            # Folder containing videos and GIFs
│   ├── WebcamTest1.gif         # Demo GIF 1 showing the application
│   ├── WebcamTest1.mp4         # Demo Video 1 showing the application
│   ├── WebcamTest2.gif         # Demo GIF 2 showing the application
│   └── WebcamTest2.mp4         # Demo Video 2 showing the application
├── sample-videos               # Folder containing sample video files
│   ├── sample1.mp4             # Sample video for testing
│   └── sample2.mp4             # Another sample video for testing
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/ajiteveryone8/virtual-camera-app
   cd virtual-camera-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Install Virtual Camera Drivers:
   - Install **OBS Virtual Camera**:
     - Download and install OBS Studio from [https://obsproject.com/](https://obsproject.com/).
     - Enable the OBS Virtual Camera from the OBS Studio interface.
   - Install **UnityCapture Virtual Camera**:
     - Download and install UnityCapture from [UnityCapture GitHub](https://github.com/schellingb/UnityCapture/tree/master/Install).
	 
	 
## Requirements

The project requires the following Python libraries, which are listed in the `requirements.txt` file:

- `opencv-python`: For video processing
- `numpy`: For numerical operations and frame manipulation
- `Pillow`: For image processing
- `imageio`: For handling image and video I/O
- `imageio[ffmpeg]`: For video encoding/decoding
- `pyvirtualcam`: For virtual camera integration

To install all dependencies, run:
```
pip install -r requirements.txt
```


## Usage

To run the application, execute the following command:
```
python src/main.py <video_path> <backend>
```

### Example:
- To use the OBS Virtual Camera backend:
  ```
  python src/main.py "sample-video/sample1.mp4" obs
  ```
- To use the UnityCapture Virtual Camera backend:
  ```
  python src/main.py "sample-video/sample2.mp4" unitycapture
  ```

## Features

- Start and stop the virtual camera.
- Capture and send frames to the virtual camera.
- Support for multiple backends (`obs` and `unitycapture`).
- Crop and resize video frames to match the virtual camera resolution.

## Where to Use the Virtual Camera

The virtual camera can be used in various applications, including:
- **Video Conferencing Tools**: Use the virtual camera as a video source in applications like Zoom, Microsoft Teams, or Google Meet.
- **Streaming Platforms**: Stream the virtual camera output to platforms like Twitch or YouTube using OBS Studio.
- **Testing and Development**: Test video processing pipelines or simulate camera input for software development.
- **Virtual Backgrounds**: Use the virtual camera to apply custom video backgrounds in video calls.

## Test Your Virtual Camera Online

You can test your virtual camera online using [Webcam Test](https://webcamtests.com/). This tool allows you to verify if your virtual camera is working correctly.

## Demo

Here’s a demo of the application:

##### UnityCapture Virtual Camera
![Demo GIF 1](screenshot-video/WebcamTest1.gif)
##### This demo shows video streaming through the UnityCapture Virtual Camera.

##### OBS Virtual Camera
![Demo GIF 2](screenshot-video/WebcamTest2.gif)
##### This demo shows video streaming through the OBS Virtual Camera.


## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
