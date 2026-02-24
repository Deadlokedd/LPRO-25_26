from ultralytics import YOLO
import cv2
import config
from utils import visualizer, io_handler, detector

def main():
    # Setup
    io_handler.create_dirs(config.GLOBAL_OUT, config.CROPS_OUT)
    det_model = YOLO(config.DET_MODEL_PATH)
    pose_model = YOLO(config.POSE_MODEL_PATH)
    
    image_files = sorted(list(config.IMAGES_DIR.glob("match*_0.jpg")))

    for img_path in image_files:
        img = cv2.imread(str(img_path))
        if img is None: continue 

        # Global detection
        results_det = det_model.track(img, classes=0, conf=config.DET_CONF, persist=False)
        
        # Save global frame
        global_frame = visualizer.plot_global_frame(results_det[0])
        io_handler.save_img(global_frame, config.GLOBAL_OUT, f"det_{img_path.name}")

        # Player detection
        boxes = results_det[0].boxes
        if boxes is not None and boxes.id is not None:
            ids = boxes.id.cpu().numpy().astype(int)
            match_subdir = io_handler.get_match_subdir(config.CROPS_OUT, img_path)

            for i, det in enumerate(list(boxes)):
                player_id = ids[i]
                coords = det.xyxy[0].cpu().numpy().astype(int)
                
                # Crop
                person_crop = detector.get_crop(img, coords, pad=10)
                
                # Pose
                results_pose = pose_model.predict(person_crop, conf=config.POSE_CONF, verbose=False)
                
                for r_pose in results_pose:
                    suffix = ""
                    final_image = person_crop.copy()

                    if (r_pose.keypoints is not None and len(r_pose.keypoints.data) > 0):
                        kpts = r_pose.keypoints.data[0].cpu().numpy()
                        final_image = visualizer.draw_custom_pose(person_crop, kpts, config)
                    else:
                        suffix = "_NOPose"

                    # Save player pose
                    fname = f"{img_path.stem}_ID_{player_id}{suffix}.jpg"
                    io_handler.save_img(final_image, match_subdir, fname)

        print(f"Finalizada: {img_path.name}")

if __name__ == "__main__":
    main()