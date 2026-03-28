from dataclasses import dataclass

import numpy as np
import torch
from ultralytics import YOLO

from .config import MODEL_NAME, CONFIDENCE_THRESHOLD


@dataclass
class Detection:
    label: str
    confidence: float
    bbox: tuple[int, int, int, int]  # x1, y1, x2, y2


class Detector:
    def __init__(self, model_name: str = MODEL_NAME, use_gpu: bool = False):
        self.model = YOLO(model_name)

        if use_gpu and torch.backends.mps.is_available():
            self.device = "mps"
        else:
            self.device = "cpu"
            if use_gpu:
                print("Warning: MPS (Metal GPU) not available, falling back to CPU.")

        print(f"Model loaded: {model_name} on {self.device}")

    def detect(self, frame: np.ndarray, confidence: float = CONFIDENCE_THRESHOLD) -> list[Detection]:
        results = self.model(frame, conf=confidence, device=self.device, verbose=False)
        detections = []

        for result in results:
            boxes = result.boxes
            if boxes is None:
                continue
            for i in range(len(boxes)):
                x1, y1, x2, y2 = boxes.xyxy[i].int().tolist()
                conf = float(boxes.conf[i])
                class_id = int(boxes.cls[i])
                label = self.model.names[class_id]
                detections.append(Detection(label=label, confidence=conf, bbox=(x1, y1, x2, y2)))

        return detections
