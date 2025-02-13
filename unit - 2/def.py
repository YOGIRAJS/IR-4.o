from flask import Flask, Response, render_template, jsonify
import cv2
import geocoder
import threading
import time
from ultralytics import YOLO

# Initialize Flask app
app = Flask(__name__)

# Initialize webcam
cap = cv2.VideoCapture(0)

# YOLO model setup
model = YOLO('yolov10l.pt')

# Variables for location and detection
current_location = {"latitude": None, "longitude": None}
detected_objects = []

# Function to update location every 2 seconds
def update_location():
    global current_location
    while True:
        g = geocoder.ip('me')
        location = g.latlng
        if location:
            current_location = {"latitude": location[0], "longitude": location[1]}
        time.sleep(2)

# Start location update thread
location_thread = threading.Thread(target=update_location, daemon=True)
location_thread.start()

# Function to generate video frames with detection and location overlay
def generate_frames():
    global detected_objects
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model.predict(frame)
        detected_objects = []

        for result in results:
            boxes = result.boxes.xyxy.cpu().numpy()
            confidences = result.boxes.conf.cpu().numpy()
            classes = result.boxes.cls.cpu().numpy()

            for box, confidence, cls in zip(boxes, confidences, classes):
                x1, y1, x2, y2 = map(int, box)
                class_name = model.names[int(cls)]
                detected_objects.append({"name": class_name, "confidence": float(confidence)})

                # Draw bounding boxes
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, f"{class_name} {confidence:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

        # Add location overlay
        location_text = f"Lat: {current_location['latitude']}, Lon: {current_location['longitude']}"
        cv2.putText(frame, location_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        # Encode frame for streaming
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# Flask routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/get_location')
def get_location():
    return jsonify(current_location)

@app.route('/get_detections')
def get_detections():
    return jsonify(detected_objects)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
