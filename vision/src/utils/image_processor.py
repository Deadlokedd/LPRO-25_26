import numpy as np
import cv2


def get_crop(img, box_coords, pad):
    """Get a crop with padding. Returns (crop_image, clamped_coords)."""
    h, w, _ = img.shape
    x1, y1, x2, y2 = box_coords
    
    x1, y1 = max(0, x1 - pad), max(0, y1 - pad)
    x2, y2 = min(w, x2 + pad), min(h, y2 + pad)
    
    return img[y1:y2, x1:x2], (x1, y1, x2, y2)


def img_to_square(img, target_size=640):
    """Resize image to a square preserving aspect ratio.
    Returns (square_image, transform_params).
    transform_params = (scale, x_offset, y_offset)
    """
    h, w = img.shape[:2]
    scale = target_size / max(h, w)
    new_w, new_h = int(w * scale), int(h * scale)

    resized = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_CUBIC)

    img = np.full((target_size, target_size, 3), 128, dtype=np.uint8)
    x_offset = (target_size - new_w) // 2
    y_offset = (target_size - new_h) // 2
    img[y_offset:y_offset+new_h, x_offset:x_offset+new_w] = resized

    return img, (scale, x_offset, y_offset)


def map_kpts_to_global(kpts, sq_params, sr_scale, crop_origin):
    """Map keypoints from square-crop space back to global image coordinates.
    
    Args:
        kpts: (17, 3) array of keypoints [x, y, conf] in square-crop space.
        sq_params: (scale, x_offset, y_offset) from img_to_square.
        sr_scale: super-resolution upscale factor.
        crop_origin: (x1, y1) top-left corner of the crop in global image.
    
    Returns:
        (17, 3) array with x,y mapped to global coordinates, conf unchanged.
    """
    scale, x_off, y_off = sq_params
    cx, cy = crop_origin

    global_kpts = kpts.copy()
    global_kpts[:, 0] = (kpts[:, 0] - x_off) / scale / sr_scale + cx
    global_kpts[:, 1] = (kpts[:, 1] - y_off) / scale / sr_scale + cy
    return global_kpts
