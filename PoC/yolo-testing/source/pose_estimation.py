from ultralytics import YOLO

model = YOLO("yolo26n-pose.pt")

results = model.track(
    source="../media/football_match.mp4",
    conf=0.25,
    show=True,  # shows window in real time
    device="cpu",  # GPU acceleration ----- Nvidia => 0 // cpu = 'cpu'
    show_labels=False,
    show_boxes=False,
)
