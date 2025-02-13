import cv
from ultralytics import YOLO

# Initialize YOLO model
model = YOLO('yolov8s.pt')  # Path to the YOLOv8 model weights file

# Open video file
cap = cv.VideoCapture('video.mp4')  # Replace with the path to your video file

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Perform YOLO inference
    results = model.predict(frame)

    # Extract and process results
    for result in results:
        boxes = result.boxes
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = box.conf[0]
            cls = int(box.cls[0])
            
            # Check if detected class is 'person' (usually index 0 in COCO dataset)
            if cls == 0:
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                cv2.putText(frame, 'person', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

    # Display the frame
    cv.imshow('Detection', frame)
    if cv.waitKey(1) & 0xFF == 27:  # ESC key to exit
        break

# Release resources
cap.release()
cv.destroyAllWindows()
