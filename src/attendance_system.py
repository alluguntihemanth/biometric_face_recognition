import cv2
import numpy as np
import csv
import datetime
import pyttsx3  # Text-to-Speech library

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 150)  # Adjust speaking speed (Optional)

# Load recognizer and labels
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("./face_model.yml")

label_dict = {}
with open("./labels.txt", "r") as f:
    for line in f:
        key, value = line.strip().split(",")
        label_dict[int(key)] = value

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

attendance_file = "./attendance.csv"

# Set to store names that are already logged in the current session
logged_names = set()

with open(attendance_file, "a", newline="") as f:
    writer = csv.writer(f)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            face_img = gray[y:y+h, x:x+w]
            label, confidence = recognizer.predict(face_img)

            if confidence < 70:
                name = label_dict[label]
                color = (0, 255, 0)

                # Log attendance & speak name only if the person is seen for the first time in this session
                if name not in logged_names:
                    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    writer.writerow([name, timestamp])
                    logged_names.add(name)  # Mark as logged for this session
                    
                    # Speak welcome message
                    engine.say(f"Welcome, {name}!")
                    engine.runAndWait()

            else:
                name = "Unknown"
                color = (0, 0, 255)

            cv2.putText(frame, name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)

        cv2.imshow("Attendance System", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
print("Attendance log updated successfully!")
