"""I/O paths for local execution."""
import pathlib

# vision/ directory (paths.py -> src/ -> vision/)
_VISION_DIR = pathlib.Path(__file__).resolve().parent.parent

# Project root (vision/ -> LPRO-25_26/)
_PROJECT_ROOT = _VISION_DIR.parent

# Input
IMAGES_DIR = _PROJECT_ROOT / "data" / "raw" / "images"
VIDEOS_DIR = _PROJECT_ROOT / "data" / "raw" / "videos"

# Output
RESULTS_DIR = _PROJECT_ROOT / "data" / "results"
FULL_FRAME_POSE_OUT = RESULTS_DIR / "full_frame_pose"

