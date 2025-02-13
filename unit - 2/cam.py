from flask import Flask, Response
import cv2

# Initialize the Flask app
app = Flask(_name_)

# Initialize video capture (0 is the default camera)
camera = cv2.VideoCapture(0)


# Function to generate frames from the camera
def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


# Home route (optional)
@app.route('/')
def index():
    return "Welcome to the Video Stream! Go to <a href='/video_feed'>/video_feed</a> to view the stream."


# Route to stream the video
@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


# Favicon route (optional)
@app.route('/favicon.ico')
def favicon():
    return '', 204


# Run the Flask app
if _name_ == "_main_":
    app.run(host='0.0.0.0', port=5000)
