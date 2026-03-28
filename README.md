# Real-Time Object Detection

A Python app that uses your webcam and YOLOv8 to detect and label objects in real-time with bounding boxes.

## Setup

```bash
bash setup.sh
```

This creates a virtual environment and installs all dependencies. The first run will also download the YOLOv8 model (~6MB).

## Usage

```bash
source .venv/bin/activate
python -m src.main
```

### Options

| Flag | Default | Description |
|------|---------|-------------|
| `--camera 1` | `0` | Camera index (try 1, 2 if default doesn't work) |
| `--confidence 0.3` | `0.5` | Lower = more detections, higher = fewer but more accurate |
| `--gpu` | off | Enable Metal GPU acceleration (Apple Silicon) |
| `--model yolov8s.pt` | `yolov8n.pt` | Use a larger model for better accuracy |

### Controls

- Press **q** or **ESC** to quit

## Detectable Objects

The model recognizes 80 object classes including: person, phone, bottle, cup, book, laptop, keyboard, mouse, remote, scissors, clock, backpack, umbrella, handbag, chair, and many more.

## Troubleshooting

### Black/empty camera window
Go to **System Settings > Privacy & Security > Camera** and grant access to your terminal app (Terminal, iTerm2, etc.).

### Slow performance
- Use the default `yolov8n.pt` (Nano) model
- Try `--gpu` on Apple Silicon Macs
- Close other apps using the camera
