"""Experiment: object tracking in video (people + ball)."""
import pathlib
from ultralytics import YOLO

_VISION_DIR = pathlib.Path(__file__).resolve().parent.parent
_PROJECT_ROOT = _VISION_DIR.parent
VIDEOS_DIR = _PROJECT_ROOT / "data" / "raw" / "videos"
video_path = VIDEOS_DIR / "match1.mp4"

model = YOLO(str(_VISION_DIR / "models" / "yolo26x.pt"))

results = model.track(
    source=video_path,
    conf=0.25,    
    show=True,                  # shows window in real time
    device=0,                   # GPU acceleration
    classes=[0, 32],            # 0: person, 32: sports_ball
    persist=True,               # keeps ID between frames
    tracker="botsort.yaml",     # tracking algorithm
    show_labels=False,          
    line_width=2
)
