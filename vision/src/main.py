"""CLI script to run the vision pipeline on local images."""
import cv2
from . import config
from .paths import IMAGES_DIR, FULL_FRAME_DET_OUT, PLAYER_CROPS_OUT, FULL_FRAME_POSE_OUT
from .pipeline import Pipeline
from .utils import visualizer, io_handler


def main():
    # Setup
    io_handler.clean_dirs(FULL_FRAME_DET_OUT, PLAYER_CROPS_OUT, FULL_FRAME_POSE_OUT)
    pipeline = Pipeline()

    image_files = sorted(list(IMAGES_DIR.glob("match*_0.jpg")))

    for img_path in image_files:
        img = cv2.imread(str(img_path))

        # Run pipeline
        result = pipeline.process_frame(img)

        # Save global detection frame
        global_frame = visualizer.plot_global_frame(result["det_result"])
        io_handler.save_img(global_frame, FULL_FRAME_DET_OUT, f"det_{img_path.name}")

        # Save player crops with pose
        match_subdir = io_handler.get_match_subdir(PLAYER_CROPS_OUT, img_path)
        all_global_kpts = []

        for player in result["players"]:
            crop = player["crop"]
            suffix = ""

            if player["keypoints"] is not None:
                crop = visualizer.draw_custom_pose(crop, player["keypoints"], config)
                all_global_kpts.append(player["global_keypoints"])
            else:
                suffix = "_NOPose"

            fname = f"{img_path.stem}_ID_{player['id']}{suffix}.jpg"
            io_handler.save_img(crop, match_subdir, fname)

        # Save global pose overlay
        if all_global_kpts:
            global_pose_img = visualizer.draw_global_pose(img, all_global_kpts, config)
            io_handler.save_img(global_pose_img, FULL_FRAME_POSE_OUT, f"pose_{img_path.name}")

        print(f"Image processed: {img_path.name}")


if __name__ == "__main__":
    main()
