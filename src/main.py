import argparse
import time

import cv2

from .camera import Camera
from .config import CONFIDENCE_THRESHOLD, WINDOW_NAME
from .detector import Detector
from .renderer import draw_detections


def parse_args():
    parser = argparse.ArgumentParser(description="Real-time object detection using YOLOv8")
    parser.add_argument("--camera", type=int, default=0, help="Camera index (default: 0)")
    parser.add_argument("--confidence", type=float, default=CONFIDENCE_THRESHOLD, help="Detection confidence threshold (default: 0.5)")
    parser.add_argument("--gpu", action="store_true", help="Enable MPS (Metal) GPU acceleration")
    parser.add_argument("--model", type=str, default="yolov8n.pt", help="YOLOv8 model variant (default: yolov8n.pt)")
    return parser.parse_args()


def main():
    args = parse_args()

    print("Starting Object Detection...")
    print(f"  Model: {args.model}")
    print(f"  Confidence: {args.confidence}")
    print(f"  Camera: {args.camera}")
    print(f"  GPU: {'enabled' if args.gpu else 'disabled'}")
    print()

    detector = Detector(model_name=args.model, use_gpu=args.gpu)

    with Camera(camera_index=args.camera) as camera:
        # Check if camera works on first frame
        success, test_frame = camera.read()
        if not success:
            print(
                "\nError: Camera returned empty frames.\n"
                "On macOS, go to System Settings > Privacy & Security > Camera\n"
                "and grant access to your terminal application."
            )
            return

        print("Camera opened. Press 'q' or ESC to quit.\n")
        prev_time = time.time()

        while True:
            success, frame = camera.read()
            if not success:
                print("Lost camera feed.")
                break

            # Run detection
            detections = detector.detect(frame, confidence=args.confidence)

            # Calculate FPS
            current_time = time.time()
            fps = 1.0 / (current_time - prev_time) if (current_time - prev_time) > 0 else 0
            prev_time = current_time

            # Draw results
            draw_detections(frame, detections, fps)

            # Display
            cv2.imshow(WINDOW_NAME, frame)

            # Check for quit
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q") or key == 27:  # q or ESC
                break

    cv2.destroyAllWindows()
    print("Done.")


if __name__ == "__main__":
    main()
