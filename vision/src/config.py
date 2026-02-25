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
