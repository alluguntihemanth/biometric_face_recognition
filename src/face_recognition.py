import cv2
import numpy as np

# Load trained recognizer and label mappings
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("face_model.yml")

label_dict = {}
with open("labels.txt", "r") as f:
    for line in f:
        key, value = line.strip().split(",")
        label_dict[int(key)] = value

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

print("Starting face recognition... Press 'q' to exit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face_img = gray[y:y+h, x:x+w]
        label, confidence = recognizer.predict(face_img)

        if confidence < 70:  # Threshold for recognition
            name = label_dict[label]
            color = (0, 255, 0)  # Green for recognized
        else:
            name = "Unknown"
            color = (0, 0, 255)  # Red for unknown

        cv2.putText(frame, name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)

    cv2.imshow("Face Recognition", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
