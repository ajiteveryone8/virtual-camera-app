def initialize_camera(camera_index=0):
    import cv2
    camera = cv2.VideoCapture(camera_index)
    if not camera.isOpened():
        raise Exception("Could not open video device")
    return camera

def release_camera(camera):
    camera.release()