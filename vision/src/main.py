"""CLI script to run the vision pipeline on local images."""
import cv2
from .paths import IMAGES_DIR, FULL_FRAME_POSE_OUT
from .pipeline import Pipeline
from .utils import io_handler


def main():
    # Setup
    io_handler.clean_dirs(FULL_FRAME_POSE_OUT)
    pipeline = Pipeline()

    image_files = sorted(list(IMAGES_DIR.glob("match*_0.jpg")))

    for img_path in image_files:
        img = cv2.imread(str(img_path))

        result = pipeline.process_frame(img)

        # Save image after processing
        if result is not None:
            io_handler.save_img(result, FULL_FRAME_POSE_OUT, f"pose_{img_path.name}")

        print(f"Image processed: {img_path.name}")


if __name__ == "__main__":
    main()
