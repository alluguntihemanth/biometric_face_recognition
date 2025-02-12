import cv2
import numpy as np
import os

dataset_path = "dataset"
recognizer = cv2.face.LBPHFaceRecognizer_create()
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

faces = []
labels = []
label_dict = {}
label_count = 0

for user in os.listdir(dataset_path):
    user_path = os.path.join(dataset_path, user)
    if not os.path.isdir(user_path):
        continue
    
    label_dict[label_count] = user  # Assign numeric label
    for file in os.listdir(user_path):
        img_path = os.path.join(user_path, file)
        image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        
        faces.append(image)
        labels.append(label_count)

    label_count += 1

faces = np.array(faces, dtype='object')
labels = np.array(labels)

# Train the model
recognizer.train(faces, labels)
recognizer.save("face_model.yml")

# Save label mappings
with open("labels.txt", "w") as f:
    for key, value in label_dict.items():
        f.write(f"{key},{value}\n")

print("Model trained successfully and saved!")
