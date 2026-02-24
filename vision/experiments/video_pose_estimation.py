"""Experiment: pose estimation in video."""
import pathlib
from ultralytics import YOLO

_VISION_DIR = pathlib.Path(__file__).resolve().parent.parent
_PROJECT_ROOT = _VISION_DIR.parent
VIDEOS_DIR = _PROJECT_ROOT / "data" / "raw" / "videos"
video_path = VIDEOS_DIR / "match1.mp4"

model = YOLO(str(_VISION_DIR / "models" / "yolo26x-pose.pt"))

results = model.track(
    source=video_path,  
    conf=0.25,                  
    show=True,                  # shows window in real time
    device=0,                   # GPU acceleration
    show_labels=False,          
    show_boxes=False
)
