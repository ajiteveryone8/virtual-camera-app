import cv2
import time
import pyvirtualcam # type: ignore
from pyvirtualcam import PixelFormat # type: ignore

class VirtualCamera:
    def __init__(self, video_path, backend='obs'):
        self.video_path = video_path
        self.backend = backend  # Backend can be 'obs' or 'unitycapture'
        self.cap = None
        self.is_running = False
        self.virtual_cam = None

    def start(self):
        if not self.is_running:
            self.cap = cv2.VideoCapture(self.video_path)
            if not self.cap.isOpened():
                raise ValueError(f"Error: Could not open video file {self.video_path}")
            
            # Get video properties
            original_width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            original_height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fps = int(self.cap.get(cv2.CAP_PROP_FPS)) or 30  # Default to 30 FPS if not available

            # you can set a standard resolution (e.g., 640x480)
            width, height = original_width, original_height

            print(f"Original video properties: {original_width}x{original_height}, {fps} FPS")
            #print(f"Resizing video to: {width}x{height}")

            # Initialize the virtual camera with the specified backend
            self.virtual_cam = pyvirtualcam.Camera(
                width=width,
                height=height,
                fps=fps,
                fmt=PixelFormat.RGB,
                backend=self.backend  # Use the specified backend
            )
            
            # Print the name of the virtual camera
            print(f"Virtual camera started: {self.virtual_cam.device}")
            
            self.is_running = True

    def stop(self):
        if self.is_running:
            if self.cap:
                self.cap.release()
            if self.virtual_cam:
                self.virtual_cam.close()
            self.is_running = False

    def capture_and_send_frame(self):
        if self.is_running and self.cap and self.virtual_cam:
            start_time = time.time()  # Start timing

            # Read a frame from the video
            ret, frame = self.cap.read()
            if not ret:
                print("Restarting video...")
                self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                return

            # Crop the frame to 640x480
            crop_width, crop_height = 640, 480
            original_height, original_width, _ = frame.shape
            x_start = (original_width - crop_width) // 2
            y_start = (original_height - crop_height) // 2
            cropped_frame = frame[0:480, 0:640]  # Crop the frame to 640x480

            # Resize the cropped frame to match the virtual camera's resolution
            resized_frame = cv2.resize(frame, (self.virtual_cam.width, self.virtual_cam.height))

            # Convert BGR to RGB
            frame_rgb = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB)

            # Send the frame to the virtual camera
            self.virtual_cam.send(frame_rgb)

            # Wait for the next frame
            self.virtual_cam.sleep_until_next_frame()

            end_time = time.time()  # End timing
            # Uncomment the following line to print the frame processing time
            # print(f"Frame processing time: {1/(end_time - start_time):.4f} FPS")