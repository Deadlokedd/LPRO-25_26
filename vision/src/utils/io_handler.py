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


def get_match_subdir(base_path, img_path):
    """Generate and create the subdirectory based on the match name."""
    match_name = img_path.stem.split('_')[0]
    match_dir = base_path / match_name
    match_dir.mkdir(parents=True, exist_ok=True)
    return match_dir
