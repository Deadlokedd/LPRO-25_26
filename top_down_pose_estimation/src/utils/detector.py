import numpy as np

def get_crop(img, box_coords, pad):
    """Get a crop with padding."""
    h, w, _ = img.shape
    x1, y1, x2, y2 = box_coords
    
    x1, y1 = max(0, x1 - pad), max(0, y1 - pad)
    x2, y2 = min(w, x2 + pad), min(h, y2 + pad)
    
    return img[y1:y2, x1:x2]
