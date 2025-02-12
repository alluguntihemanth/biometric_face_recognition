# Biometric Face Recognition System  

## Overview  
This project implements a biometric face recognition system using OpenCV and the LBPH (Local Binary Patterns Histograms) algorithm. The system allows users to register their faces, train a recognition model, and identify individuals in real time. Additionally, it includes an attendance tracking system that logs recognized individuals into a CSV file.

---

## Process Overview  

1. **Face Registration**  
   - Captures and stores multiple images of a user's face.  
   - Saves images under a dataset folder, categorized by user name.  

2. **Model Training**  
   - Trains a face recognition model using the collected images.  
   - Generates and saves a trained model (`face_model.yml`) and label mappings (`labels.txt`).  

3. **Real-time Face Recognition**  
   - Uses the trained model to recognize faces in a live video feed.  
   - Displays recognized names and confidence levels.  

4. **Attendance System**  
   - Logs recognized users along with a timestamp into `attendance.csv`.  
   - Uses text-to-speech (TTS) to announce recognized individuals.  

---

## Prerequisites  
- Python 3.8 or later  
- OpenCV (`cv2`)  
- NumPy  
- Pyttsx3 (for text-to-speech)  

---

## Setup Instructions  

### Step 1: Clone the Repository  
```bash
git clone https://github.com/yourusername/biometric_face_recognition.git
cd biometric_face_recognition
```

### Step 2: Create a Virtual Environment  
#### Using `venv`  
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```
#### Using `conda`  
```bash
conda create --name face_recognition_env python=3.8
conda activate face_recognition_env
```

### Step 3: Install Dependencies  
```bash
pip install -r requirements.txt
```

### Step 4: Run the Face Registration Script  
```bash
python src/face_registration.py
```
Follow the prompts to enter a user name and capture face images.

### Step 5: Train the Face Recognition Model  
```bash
python src/train_model.py
```
This will save `face_model.yml` and `labels.txt`.

### Step 6: Start Real-time Face Recognition  
```bash
python src/face_recognition.py
```

### Step 7: Run the Attendance System  
```bash
python src/attendance_system.py
```

---

## Project Structure  
```
biometric_face_recognition/
│── dataset/                      # Stores user face images (auto-created)
│   ├── user1/                    # Folder for User1's images
│   ├── user2/                    # Folder for User2's images
│
├── face_model.yml                 # Trained LBPH face recognizer
├── labels.txt                      # Mapping of labels to user names
├── attendance.csv                  # Attendance log file
│
│── src/                            # Main source code directory
│   ├── face_registration.py        # Captures & stores user face images
│   ├── train_model.py              # Trains the face recognition model
│   ├── face_recognition.py         # Runs real-time face recognition
│   ├── attendance_system.py        # Logs recognized faces with timestamps
│
│── requirements.txt                 # List of required dependencies
```

---

## Notes  
- Ensure your webcam is properly connected.  
- The system recognizes faces with a confidence threshold of **70%**.  
- Attendance is logged only once per session to avoid duplicate entries.  

---

## Future Enhancements  
- Improve model accuracy with deep learning-based face recognition.  
- Implement a web-based interface for registration and recognition.  
- Enhance security by adding face anti-spoofing mechanisms.  

---
