import pathlib
ROOT_DIR = pathlib.Path(__file__).parent.parent.parent
MEDIA_DIR = ROOT_DIR / "media"
VIDEOS_DIR = MEDIA_DIR / "raw" / "videos"
video_path = VIDEOS_DIR / "match1.mp4"

from ultralytics import YOLO

model = YOLO('yolo26x-pose.pt') 

results = model.track(
    source=video_path,  
    conf=0.25,                  
    show=True,                  # shows window in real time
    device=0,                   # GPU acceleration
    show_labels=False,          
    show_boxes=False
)
