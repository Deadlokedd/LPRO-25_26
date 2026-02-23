import pathlib
from ultralytics import YOLO

ROOT_DIR = pathlib.Path(__file__).parent.parent.parent
IMAGES_DIR = ROOT_DIR / "media" / "raw" / "images"
CROPS_OUT = ROOT_DIR / "media" / "results" / "global_pose"
CROPS_OUT.mkdir(parents=True, exist_ok=True)

pose_model = YOLO("yolo26x-pose.pt") 

image_files = sorted(list(IMAGES_DIR.glob("match*_0.jpg")))
print(f"Found {len(image_files)} images.")

results_pose = pose_model.predict(source=image_files, conf=0.25, device=0)

for r in results_pose:
    original_filename = pathlib.Path(r.path).name 
    save_path = CROPS_OUT / f"pose_{original_filename}"
    r.save(filename=str(save_path))
