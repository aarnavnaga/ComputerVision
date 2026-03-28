import cv2
import numpy as np

from .detector import Detection
from .config import (
    BOX_COLOR,
    BOX_THICKNESS,
    LABEL_COLOR,
    LABEL_BG_COLOR,
    LABEL_FONT_SCALE,
    LABEL_THICKNESS,
)


def draw_detections(frame: np.ndarray, detections: list[Detection], fps: float = 0.0) -> np.ndarray:
    for det in detections:
        x1, y1, x2, y2 = det.bbox

        # Draw bounding box
        cv2.rectangle(frame, (x1, y1), (x2, y2), BOX_COLOR, BOX_THICKNESS)

        # Prepare label text
        label_text = f"{det.label} {det.confidence:.0%}"
        (text_w, text_h), baseline = cv2.getTextSize(
            label_text, cv2.FONT_HERSHEY_SIMPLEX, LABEL_FONT_SCALE, LABEL_THICKNESS
        )

        # Draw filled rectangle behind label
        cv2.rectangle(
            frame,
            (x1, y1 - text_h - baseline - 4),
            (x1 + text_w, y1),
            LABEL_BG_COLOR,
            cv2.FILLED,
        )

        # Draw label text
        cv2.putText(
            frame,
            label_text,
            (x1, y1 - baseline - 2),
            cv2.FONT_HERSHEY_SIMPLEX,
            LABEL_FONT_SCALE,
            LABEL_COLOR,
            LABEL_THICKNESS,
        )

    # Draw FPS counter
    fps_text = f"FPS: {fps:.1f}"
    cv2.putText(frame, fps_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

    return frame
