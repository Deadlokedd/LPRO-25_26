"""Experiment: direct global pose estimation on images."""
import pathlib
from ultralytics import YOLO
from src.paths import IMAGES_DIR

_PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
_VISION_DIR = _PROJECT_ROOT / "vision"
CROPS_OUT = _PROJECT_ROOT / "data" / "results" / "exp_full_frame_pose"
CROPS_OUT.mkdir(parents=True, exist_ok=True)

pose_model = YOLO(str(_VISION_DIR / "models" / "yolo26x-pose.pt"))

image_files = sorted(list(IMAGES_DIR.glob("match*_0.jpg")))

results_pose = pose_model.predict(source=image_files, conf=0.25, device=0)

for r in results_pose:
    original_filename = pathlib.Path(r.path).name 
    save_path = CROPS_OUT / f"exp_pose_{original_filename}"
    r.save(filename=str(save_path))
