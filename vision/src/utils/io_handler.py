import cv2
import shutil


def clean_dirs(*dirs):
    """Remove and recreate directories to start fresh."""
    for d in dirs:
        if d.exists():
            shutil.rmtree(d)
        d.mkdir(parents=True, exist_ok=True)


def save_img(image, path, filename):
    """Save image to disk."""
    full_path = path / filename
    cv2.imwrite(str(full_path), image)


