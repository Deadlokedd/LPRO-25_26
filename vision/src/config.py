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


