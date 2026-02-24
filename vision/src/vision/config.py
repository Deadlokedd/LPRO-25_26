import pathlib

# --- PATHS ---
ROOT_DIR = pathlib.Path(__file__).parent.parent
IMAGES_DIR = ROOT_DIR / "media" / "raw" / "images"
CROPS_OUT = ROOT_DIR / "media" / "results" / "crops_pose"
GLOBAL_OUT = ROOT_DIR / "media" / "results" / "global_detection"

# --- MODELS ---
DET_MODEL_PATH = "yolo26x.pt"
POSE_MODEL_PATH = "yolo26x-pose.pt"
DET_CONF = 0.25
POSE_CONF = 0.25

# --- DRAWING CONFIG ---
# BGR: Red (0,0,255), Blue (255,0,0)
POINT_COLOR = (0, 0, 255)   
LINE_COLOR = (255, 0, 0)    
POINT_RADIUS = 3
LINE_THICKNESS = 2

# COCO Points: Head (0-4), Shoulders (5-6), Hips (11-12), Knees (13-14), Ankles (15-16)
POINTS_TO_DRAW = {0, 1, 2, 3, 4, 5, 6, 11, 12, 13, 14, 15, 16}
CUSTOM_SKELETON = [
    (5, 6), (11, 12), (5, 11), (6, 12), # Trunk
    (11, 13), (13, 15),                 # Left leg
    (12, 14), (14, 16),                 # Right leg
    (0, 1), (0, 2), (1, 3), (2, 4)      # Head
]