import cv2
from mmpose.apis import MMPoseInferencer
import numpy as np
from . import config


class Pipeline:
    """Top-down player detection and pose estimation pipeline."""

    def __init__(self) -> None:
        self.pose_model = MMPoseInferencer(pose2d=config.MMPOSE_POSE2D_MODEL)

    def process_frame(self, img: np.ndarray) -> np.ndarray:
        """Process a frame and return detections + keypoints.
        Args:
            img: BGR numpy array of the frame to process.
        Returns:
            np.ndarray: The pose-annotated image.
        """

        # Detection + Pose Estimation
        generator = self.pose_model(
            img, 
            return_vis=True,
            draw_bbox=True
        )
        
        result = next(generator)
        pose_annotated_img = cv2.cvtColor(result['visualization'][0], cv2.COLOR_RGB2BGR)
        
        return pose_annotated_img
