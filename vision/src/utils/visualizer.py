import cv2


def draw_custom_pose(image, kpts, config):
    """Draw the skeleton on a crop."""
    annotated = image.copy()
    
    # Draw lines
    for p1_idx, p2_idx in config.CUSTOM_SKELETON:
        x1, y1, c1 = kpts[p1_idx]
        x2, y2, c2 = kpts[p2_idx]
        if c1 > config.POSE_CONF and c2 > config.POSE_CONF:
            cv2.line(annotated, (int(x1), int(y1)), (int(x2), int(y2)), 
                     config.LINE_COLOR, config.LINE_THICKNESS)

    # Draw points
    for idx in config.POINTS_TO_DRAW:
        kx, ky, conf = kpts[idx]
        if conf > config.POSE_CONF:
            cv2.circle(annotated, (int(kx), int(ky)), 
                       config.POINT_RADIUS, config.POINT_COLOR, -1)
    return annotated


def draw_global_pose(image, all_global_kpts, config):
    """Draw all player skeletons on the global image."""
    annotated = image.copy()
    for kpts in all_global_kpts:
        # Draw lines
        for p1_idx, p2_idx in config.CUSTOM_SKELETON:
            x1, y1, c1 = kpts[p1_idx]
            x2, y2, c2 = kpts[p2_idx]
            if c1 > config.POSE_CONF and c2 > config.POSE_CONF:
                cv2.line(annotated, (int(x1), int(y1)), (int(x2), int(y2)),
                         config.LINE_COLOR, config.GLOBAL_LINE_THICKNESS)
        # Draw points
        for idx in config.POINTS_TO_DRAW:
            kx, ky, conf = kpts[idx]
            if conf > config.POSE_CONF:
                cv2.circle(annotated, (int(kx), int(ky)),
                           config.GLOBAL_POINT_RADIUS, config.POINT_COLOR, -1)
    return annotated


def plot_global_frame(result, line_width=1):
    """Prepare the global frame."""
    original_names = result.names.copy()
    result.names = {k: "" for k in result.names} # Hide class names
    frame = result.plot(labels=True, conf=True, line_width=line_width)
    result.names = original_names
    return frame
