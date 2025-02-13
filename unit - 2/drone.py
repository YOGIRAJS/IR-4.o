import cv2
import matplotlib.pyplot as plt

face_cascade = cv2.CascadeClassifier('c:/Users/pushkraj/Downloads/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(frame, "Person: 1", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    # Use matplotlib to display the image
    plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show(block=False)
    plt.pause(0.01)
    plt.close()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
