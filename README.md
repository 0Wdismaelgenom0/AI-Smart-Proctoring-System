# AI Smart Proctoring System 🛡️🤖

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org)
[![Framework](https://img.shields.io/badge/UI_Framework-PySide2-green.svg)](https://pyside.org)
[![Database](https://img.shields.io/badge/Cloud-Firebase-orange.svg)](https://firebase.google.com)
[![Optimized FPS](https://img.shields.io/badge/Performance-30_FPS-red.svg)](#-key-features)

An advanced, automated desktop proctoring application driven by real-time facial recognition and seamlessly synchronized with the Firebase Cloud Suite. Developed with **Python** and **PySide2**, featuring a multi-threaded architecture optimized to sustain high-performance execution without blocking the graphical user interface.

---

## 📁 Repository Structure

The project follows a clean, modular object-oriented structural architecture:

```text
Smart-Proctoring-System/
│
├── App.py                      # Main application driver & routing control
├── serviceAccountKey.json      # Firebase Admin SDK private key credentials
├── EncodeFile.p                # Pickled face binary encodings data
├── moniter.csv                 # Local tracking sheet logging proctoring marks
├── requirements.txt            # System dependencies list
│
├── ui/                         # Sub-package containing UI interface structures
│   ├── __init__.py             # Makes 'ui' an importable Python package
│   ├── ui_main_page.py
│   ├── ui_exam_page.py
│   └── [Other compiled UI views...]
│
└── icons/                      # Central repository for visual assets and icons
 
##🚀 Key Features
​⚡ Asynchronous Multi-Threading (QThread): Heavy operations (such as uploading captured images to Firebase Storage) are offloaded to dedicated background worker threads. This guarantees that the live video feed runs smoothly at a strict 30 FPS without experiencing UI freezing or frame drops.
​🔍 Smart Local Caching First: Optimized image loading protocols verify local file paths before attempting cloud database handshakes. This architectural choice dramatically cuts latency times down to milliseconds.
​🛡️ Security Proctoring Engine: Real-time facial identification checks students against trained local models, logs continuous updates, and reports anomalies (unknown users/impersonation tokens) to both local CSV logs and cloud references.
​📱 Desktop Fluidity on Any Hardware: Structured entirely using QStackedWidget for clean memory-efficient view routing.
​##🛠️ Prerequisites & Installation
​1. Clone the repository
git clone [https://github.com/0Wdismaelgenom0/AI-Smart-Proctoring-System.git](https://github.com/0Wdismaelgenom0/AI-Smart-Proctoring-System.git)
cd AI-Smart-Proctoring-System
2. Install Dependencies
​Make sure you have CMake and Python installed on your environment, then run:
pip install -r requirements.txt
3. Firebase Configuration Setup
​Before initiating the application tracking suite, place your Firebase private key configuration file named serviceAccountKey.json inside the root directory.

##​💻 Tech Stack & Core Libraries
Component Library Used Purpose
Core Language Python System Development
GUI Framework PySide2 (Qt for Python) Desktop UI Elements & Event Routing
Computer Vision OpenCV & CVZone Video Capture & Frame Blitting
Deep Learning Face Recognition (dlib backend) Vector Encodings & Face Matching
Cloud Backend Firebase Admin SDK Realtime DB, Auth, and Cloud Storage

##👨‍💻 Developer
​Mohammed Wad Ismail - Core System Architect & Lead Developer - 0Wdismaelgenom0 
