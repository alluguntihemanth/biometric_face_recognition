import cv2
import os

# Create dataset directory if it doesn't exist
dataset_path = "dataset"
if not os.path.exists(dataset_path):
    os.makedirs(dataset_path)

# Get user name
user_name = input("Enter your name: ")
user_path = os.path.join(dataset_path, user_name)

if not os.path.exists(user_path):
    os.makedirs(user_path)

# Initialize webcam
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

count = 0
print("Capturing images... Press 'q' to exit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face_img = gray[y:y+h, x:x+w]
        file_name = os.path.join(user_path, f"{count}.jpg")
        cv2.imwrite(file_name, face_img)
        count += 1
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Face Registration", frame)
    if cv2.waitKey(1) & 0xFF == ord('q') or count >= 30:  # Capture 30 images per user
        break

cap.release()
cv2.destroyAllWindows()
print(f"Face registration complete. Images saved in {user_path}")
