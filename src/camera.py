import cv2
import numpy as np

from .config import CAMERA_INDEX, FRAME_WIDTH, FRAME_HEIGHT


class Camera:
    def __init__(self, camera_index: int = CAMERA_INDEX):
        self.cap = cv2.VideoCapture(camera_index)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

        if not self.cap.isOpened():
            raise RuntimeError(
                f"Could not open camera {camera_index}. "
                "On macOS, go to System Settings > Privacy & Security > Camera "
                "and make sure your terminal app has camera access."
            )

    def read(self) -> tuple[bool, np.ndarray]:
        success, frame = self.cap.read()
        if not success or frame is None or frame.size == 0:
            return False, np.array([])
        return True, frame

    def release(self):
        self.cap.release()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.release()
        return False
