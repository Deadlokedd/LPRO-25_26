"""Vision pipeline: core detection + pose logic."""
from ultralytics import YOLO
from .utils import image_processor, super_resolution
from . import config


class Pipeline:
    """Player detection and top-down pose estimation pipeline."""

    def __init__(self):
        self.det_model = YOLO(config.DET_MODEL_PATH)
        self.pose_model = YOLO(config.POSE_MODEL_PATH)
        self.sr_model = super_resolution.init_upscaler()

    def process_frame(self, img):
        """Process a frame and return detections + keypoints.

        Args:
            img: BGR numpy array of the frame to process.

        Returns:
            dict with:
                - "det_result": raw detection result object
                - "players": list of dicts {id, bbox, crop, keypoints, global_keypoints}
        """
        # --- GLOBAL DETECTION ---
        results_det = self.det_model.track(
            img, classes=0, conf=config.DET_CONF, persist=False
        )

        boxes = results_det[0].boxes
        players = []

        if boxes is not None and boxes.id is not None:
            ids = boxes.id.cpu().numpy().astype(int)
            bboxes = boxes.xyxy.cpu().numpy().astype(int)

            for player_id, coords in zip(ids, bboxes):
                player_data = self._process_player(img, int(player_id), coords)
                players.append(player_data)

        return {
            "det_result": results_det[0],
            "players": players,
        }

    def _process_player(self, img, player_id, coords):
        """Process an individual player: crop -> SR -> pose.

        Returns:
            dict with id, bbox, crop, keypoints (or None), global_keypoints (or None)
        """
        # Crop
        person_crop, crop_coords = image_processor.get_crop(img, coords, pad=10)
        crop_origin = (crop_coords[0], crop_coords[1])

        # Super-Resolution
        person_crop = super_resolution.upscale(person_crop, self.sr_model)

        # Resize to square
        sq_person_crop, sq_params = image_processor.img_to_square(person_crop)

        # Pose estimation
        results_pose = self.pose_model.predict(
            sq_person_crop, conf=config.POSE_CONF, verbose=False
        )

        kpts = None
        global_kpts = None

        for r_pose in results_pose:
            if r_pose.keypoints is not None and len(r_pose.keypoints.data) > 0:
                kpts = r_pose.keypoints.data[0].cpu().numpy()
                global_kpts = image_processor.map_kpts_to_global(
                    kpts, sq_params, self.sr_model.scale, crop_origin
                )

        return {
            "id": player_id,
            "bbox": coords.tolist(),
            "crop": sq_person_crop,
            "keypoints": kpts,
            "global_keypoints": global_kpts,
        }
