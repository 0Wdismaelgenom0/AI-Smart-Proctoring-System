# AI Smart Proctoring System 🛡️🤖

An advanced, automated desktop proctoring application driven by real-time facial recognition and seamlessly synchronized with the Firebase Cloud Suite. Developed with **Python** and **PySide2**, featuring a multi-threaded architecture optimized to sustain high-performance execution without blocking the graphical user interface.

---

## 📁 Repository Structure

The project follows a clean, modular object-oriented structural architecture:

* **App.py** - Main application driver & routing control.
* **ui/** - Sub-package containing UI interface structures.
* **icons/** - Central repository for visual assets and icons.

---

## 🚀 Key Features

* **Asynchronous Multi-Threading (QThread):** Heavy operations (such as uploading captured images to Firebase Storage) are offloaded to dedicated background worker threads. This guarantees that the live video feed runs smoothly at a strict 30 FPS without experiencing UI freezing or frame drops.
* **Smart Local Caching First:** Optimized image loading protocols verify local file paths before attempting cloud database handshakes. This architectural choice dramatically cuts latency times down to milliseconds.
* **Security Proctoring Engine:** Real-time facial identification checks students against trained local models, logs continuous updates, and reports anomalies to both local CSV logs and cloud references.
* **Desktop Fluidity on Any Hardware:** Structured entirely using QStackedWidget for clean memory-efficient view routing.

---

## 🛠️ Prerequisites & Installation

### 1. Clone the Repository
```bash
git clone [https://github.com/0Wdismaelgenom0/AI-Smart-Proctoring-System.git](https://github.com/0Wdismaelgenom0/AI-Smart-Proctoring-System.git)
cd AI-Smart-Proctoring-System
