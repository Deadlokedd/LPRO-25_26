from ultralytics import YOLO

model = YOLO("yolo26n.pt")

results = model.track(
    source="../media/football_match.mp4",
    conf=0.25,
    show=True,  # shows window in real time
    device="cpu",  # GPU acceleration ----- Nvidia => 0 // cpu = 'cpu'
    classes=[0, 32],  # 0: person, 32: sports_ball
    persist=True,  # keeps ID between frames
    tracker="botsort.yaml",  # tracking algorithm
    show_labels=False,
    line_width=2,
)
