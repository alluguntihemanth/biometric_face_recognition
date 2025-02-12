# biometric_face_recognition
A Deep Learning model for advanced Face Recognition.


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
- **Face Registration**: Capture and store user face images for training.  
- **Model Training**: Train a face recognition model using LBPH.  
- **Real-Time Recognition**: Identify faces from a live webcam feed.  
- **Attendance Tracking**: Logs recognized users' names and timestamps.  
- **Text-to-Speech**: Announces recognized users with an audio welcome.  

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


🚀 Installation & Setup
1️⃣ Prerequisites
Ensure you have Python 3.8+ installed.

Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
2️⃣ Run Face Registration
bash
Copy
Edit
python src/face_registration.py
This will capture 30 images per user for training.
3️⃣ Train the Model
bash
Copy
Edit
python src/train_model.py
This will create face_model.yml and labels.txt for recognition.
4️⃣ Run Face Recognition
bash
Copy
Edit
python src/face_recognition.py
The system will recognize registered users and display their names.
5️⃣ Run the Attendance System
bash
Copy
Edit
python src/attendance_system.py
Recognized users will be logged in attendance.csv with timestamps.
📸 Visual Demo
Face Registration
<p align="center"> <img src="https://github.com/user-attachments/assets/sample-registration.png" alt="Face Registration" width="400"/> </p>
Real-Time Recognition
<p align="center"> <img src="https://github.com/user-attachments/assets/sample-recognition.png" alt="Face Recognition" width="400"/> </p>
Attendance Logging
<p align="center"> <img src="https://github.com/user-attachments/assets/sample-attendance.png" alt="Attendance Log" width="400"/> </p>
🔧 Configuration
Modify the confidence threshold in face_recognition.py and attendance_system.py for accuracy tuning:

python
Copy
Edit
if confidence < 70:  # Adjust this threshold
🤝 Contributing
We welcome contributions! 🚀

Steps to Contribute:
Fork this repository.
Clone your forked repo:
bash
Copy
Edit
git clone https://github.com/your-username/biometric_face_recognition.git
Create a feature branch:
bash
Copy
Edit
git checkout -b feature-name
Commit your changes:
bash
Copy
Edit
git commit -m "Added new feature"
Push the branch:
bash
Copy
Edit
git push origin feature-name
Create a Pull Request on GitHub.
📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

📧 Contact
For any queries, reach out to:
Email: hemanthallugunti@gmail.com
LinkedIn: Hemanth Reddy Allugunti

Enjoy using the Biometric Face Recognition System! 😊

vbnet
Copy
Edit

This keeps **everything inside a single code block** as per your request. 🚀  

Let me know if you need any **tweaks or additions**!
