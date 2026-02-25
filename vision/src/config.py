"""Model and visualization parameters for the vision module.

This module contains portable configuration.
For file paths, see paths.py.
"""
import pathlib

# vision/ directory (config.py -> src/ -> vision/)
_VISION_DIR = pathlib.Path(__file__).resolve().parent.parent

# --- MODELS ---
_MODELS_DIR = _VISION_DIR / "models"
MMPOSE_POSE2D_MODEL = 'wholebody'
MMPOSE_CONF = 0.10

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

# Pose keypoints for offsides
OFFSIDE_KEYPOINTS = {
    0: 'nose', 1: 'left_eye', 2: 'right_eye', 3: 'left_ear', 4: 'right_ear',
    5: 'left_shoulder', 6: 'right_shoulder',
    11: 'left_hip', 12: 'right_hip',
    13: 'left_knee', 14: 'right_knee',
    15: 'left_ankle', 16: 'right_ankle',
    17: 'left_big_toe', 18: 'left_small_toe', 19: 'left_heel',
    20: 'right_big_toe', 21: 'right_small_toe', 22: 'right_heel'
}

OFFSIDE_SKELETON = [
    (0, 1), (0, 2), (1, 3), (2, 4),           # Face
    (5, 6), (11, 12), (5, 11), (6, 12),       # Trunk
    (11, 13), (13, 15),                       # Left leg
    (12, 14), (14, 16),                       # Right leg
    (15, 17), (15, 18), (15, 19),             # Left foot
    (16, 20), (16, 21), (16, 22)              # Right foot
]
