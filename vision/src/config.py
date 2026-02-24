"""Model and visualization parameters for the vision module.

This module contains portable configuration.
For file paths, see paths.py.
"""
import pathlib

# vision/ directory (config.py -> src/ -> vision/)
_VISION_DIR = pathlib.Path(__file__).resolve().parent.parent

# --- MODELS ---
_MODELS_DIR = _VISION_DIR / "models"
DET_MODEL_PATH = str(_MODELS_DIR / "yolo26x.pt")
POSE_MODEL_PATH = str(_MODELS_DIR / "yolo26x-pose.pt")
DET_CONF = 0.25
POSE_CONF = 0.10

SR_MODEL_URLS = {
    'RealESRGAN_x2plus': 'https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.1/RealESRGAN_x2plus.pth',
    'RealESRGAN_x4plus': 'https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth',
}

# --- DRAWING CONFIG ---
# BGR: Red (0,0,255), Blue (255,0,0)
POINT_COLOR = (0, 0, 255)   
LINE_COLOR = (255, 0, 0)    
POINT_RADIUS = 2
LINE_THICKNESS = 2

# Global overlay drawing params
GLOBAL_POINT_RADIUS = 3
GLOBAL_LINE_THICKNESS = 2

# Pose keypoints: Head (0-4), Shoulders (5-6), Hips (11-12), Knees (13-14), Ankles (15-16)
POINTS_TO_DRAW = {0, 1, 2, 3, 4, 5, 6, 11, 12, 13, 14, 15, 16}
CUSTOM_SKELETON = [
    (5, 6), (11, 12), (5, 11), (6, 12), # Trunk
    (11, 13), (13, 15),                 # Left leg
    (12, 14), (14, 16),                 # Right leg
    (0, 1), (0, 2), (1, 3), (2, 4)      # Head
]
