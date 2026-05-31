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
 
