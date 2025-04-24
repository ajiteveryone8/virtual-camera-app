import sys
from camera.virtual_camera import VirtualCamera

def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py <video_path> <backend>")
        print("Example: python main.py video.mp4 obs")
        return

    video_path = sys.argv[1]
    backend = sys.argv[2]  # Backend can be 'obs' or 'unitycapture'

    # Initialize the virtual camera with the specified backend
    camera = VirtualCamera(video_path, backend)
    camera.start()

    try:
        while True:
            camera.capture_and_send_frame()
    except KeyboardInterrupt:
        print("Virtual camera stopped.")
    finally:
        camera.stop()

if __name__ == "__main__":
    main()