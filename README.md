# 🏆 **Biometric Face Recognition System**  

<p align="center">
  <img src="https://github.com/user-attachments/assets/sample-face-recognition.gif" alt="Face Recognition Demo" width="500"/>
</p>  

---

## 🌟 **About the Project**  
This **Biometric Face Recognition System** is a Python-based solution that captures, registers, and recognizes faces using **OpenCV and LBPH Face Recognizer**. It supports an **attendance system**, logging recognized users in a CSV file.  

Designed for **real-time applications**, it is lightweight, efficient, and can be extended to **access control, attendance tracking, or security systems**.  

---

## ✨ **Key Features**  
*   ✔ Face Registration: Capture and store user face images.
*   ✔ Model Training: Train a recognizer using stored images.
*   ✔ Real-time Face Recognition: Identify users in real time.
*   ✔ Attendance Logging: Automatically record recognized users.
*   ✔ Text-to-Speech Feedback: Announces recognized users.
---

## ⚙️ **Tech Stack**  
| **Technology**   | **Purpose**                            |  
|------------------|--------------------------------------|  
| **Python**       | Core programming language           |  
| **OpenCV**       | Face detection and recognition      |  
| **NumPy**        | Efficient array operations         |  
| **CSV**          | Attendance logging                  |  
| **pyttsx3**      | Text-to-speech engine               |  

---

## 📁 **Directory Structure**  
```bash
biometric_face_recognition/       # Root directory
│── dataset/                      # Stores user face images (auto-created)
│   ├── user1/                    # Folder for User1's images
│   │   ├── 0.jpg
│   │   ├── 1.jpg
│   │   ├── ...
│   ├── user2/                    # Folder for User2's images
│   │   ├── 0.jpg
│   │   ├── 1.jpg
│   │   ├── ...
│
│── face_model.yml                 # Trained LBPH face recognizer
│── labels.txt                      # Mapping of labels to user names
│── attendance.csv                   # Attendance log file
│
│── src/                            # Main source code directory
│   ├── face_registration.py        # Capture & store user face images
│   ├── train_model.py              # Train face recognition model
│   ├── face_recognition.py         # Real-time face recognition
│   ├── attendance_system.py        # Attendance tracking system
│
│── requirements.txt                # Required Python libraries

----------------

  
  



<h2>🛠️ Installation Steps:</h2>

<p>1. Install Dependencies</p>

```
pip install -r requirements.txt
```

<p>2. Face Registration : Run the script to capture and store face images</p>

```
python src/face_registration.py
```

<p>3. Train the Model : Train the facial recognition model</p>

```
python src/train_model.py
```

<p>4. Run Face Recognition - Start real-time face recognition</p>

<p>5. Attendance System - Launch the attendance logging system</p>

```
python src/attendance_system.py
```


<h2>🛡️ License:</h2>

This project is licensed under the MIT License
