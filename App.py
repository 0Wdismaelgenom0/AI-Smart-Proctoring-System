# App.py
# AI Smart Proctoring System 
# Developed by Mohammed Wad Ismail

import sys
import os
import time
import pickle
import numpy as np
import cv2
import cvzone
import face_recognition
from datetime import datetime

# Firebase Cloud Suite
import firebase_admin
from firebase_admin import credentials, db, storage, auth

# PySide2 GUI Core Framework
from PySide2 import QtCore
from PySide2.QtCore import QTimer, QTime, Qt, QThread, Signal
from PySide2.QtGui import QPixmap, QImage, QColor
from PySide2.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QVBoxLayout, QGraphicsDropShadowEffect, QMessageBox, QLCDNumber, QStackedWidget, QFileDialog

# ========================================================
# 🛠️ FIXED UI IMPORTS (Pointing correctly to 'ui' directory)
# ========================================================
from ui.ui_main_page import *
from ui.ui_exam_page import * 
from ui.ui_register import *
from ui.ui_about_us import *
from ui.ui_login_db import *
from ui.ui_splash_screen import *
from ui.ui_login import *
from ui.ui_dp_tool import *
from ui.ui_verfiy import *
from ui.ui_exam import *

# ========================================================
# LIVE FIREBASE SATELLITE INITIALIZATION
# ========================================================
try:
    cred = credentials.Certificate("serviceAccountKey.json") 
    firebase_admin.initialize_app(cred, {
        'databaseURL': "https://face-recognition-881e6-default-rtdb.asia-southeast1.firebasedatabase.app/",
        'storageBucket': "face-recognition-881e6.appspot.com",
        'authDomain': "face-recognition-881e6.appspot.com",
    })
    bucket = storage.bucket()
    print("[CLOUD INFO] Realtime Database & Storage Bucket synchronized successfully.")
except Exception as e:
    print(f"[CLOUD ERROR] Remote linking bypassed: {e}")

# Global Core State Initializers
d = 0
loger = 0
image_of_st = 0


# ========================================================
# ⚡ ASYNCHRONOUS BACKEND THREAD FOR FIREBASE UPLOAD (Optimization)
# ========================================================
class FirebaseUploadThread(QThread):
    finished_signal = Signal(str)

    def __init__(self, file_path, blob_path):
        super().__init__()
        self.file_path = file_path
        self.blob_path = blob_path

    def run(self):
        try:
            blob = bucket.blob(self.blob_path)
            blob.upload_from_filename(self.file_path)
            self.finished_signal.emit(f"[ASYNC SUCCESS] Uploaded: {self.blob_path}")
        except Exception as e:
            self.finished_signal.emit(f"[ASYNC ERROR] Failed to upload {self.blob_path}: {e}")


# ========================================================
# WIDGET 1: MAIN APPLICATION CONTROL BOARD
# ========================================================
class Main_c(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self)
        self.ui = Main_f()
        self.ui.setupUi(self)
        
        # Mapping Click Signals to Routing Methods
        self.ui.main_bt_exam.clicked.connect(self.goto_exam)
        self.ui.main_bt_db.clicked.connect(self.goto_db)
        self.ui.main_bt_abutus.clicked.connect(self.goto_abs)

    def goto_exam(self):
        login = exm_page_c()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def goto_db(self):
        login = db_tool_c()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def goto_abs(self):
        login = abutus_c()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)


# ========================================================
# WIDGET 2: DATABASE INSTITUTIONAL TOOLKIT
# ========================================================
class db_tool_c(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self)
        self.ui = db_tool()
        self.ui.setupUi(self)
        
        self.ui.db_show_bt.clicked.connect(self.getImage_lable)
        self.ui.db_insert_new.clicked.connect(self.goto_register)
        self.ui.db_back.clicked.connect(self.backe)
        self.ui.db_Trin.clicked.connect(self.trin)
        
        # Hiding baseline UI elements
        self.ui.db_Intgrit.setVisible(False)
        self.ui.db_delet.setVisible(False)
        self.ui.label_14.setVisible(False)
    
    def goto_register(self):
        # استدعاء الكلاس الموحد وتحديد مسار العودة لصفحة قاعدة البيانات
        login = StudentRegister(target_route="db")
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def backe(self):
        login = Main_c()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1) 

    def trin(self):
        folderPath = 'Images'
        if not os.path.exists(folderPath):
            os.mkdir(folderPath)
        pathList = os.listdir(folderPath)
        imgList = []
        studentIds = []
        
        for path in pathList:
            imgList.append(cv2.imread(os.path.join(folderPath, path)))
            studentIds.append(os.path.splitext(path)[0])
            fileName = f'{folderPath}/{path}'
            
            # تشغيل خيط خلفي لرفع الصور أثناء التدريب دون تجميد الواجهة
            self.upload_thread = FirebaseUploadThread(fileName, fileName)
            self.upload_thread.start()

        def findEncodings(imagesList):
            encodeList = []
            for img in imagesList:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                encodes = face_recognition.face_encodings(img)
                if encodes:
                    encodeList.append(encodes[0])
            return encodeList

        print("Encoding Started ...")
        encodeListKnown = findEncodings(imgList)
        encodeListKnownWithIds = [encodeListKnown, studentIds]
        print("Encoding Complete")

        file = open("EncodeFile.p", 'wb')
        pickle.dump(encodeListKnownWithIds, file)
        file.close()
        print("File Saved Successfully.")

    def getImage_lable(self):
        id = self.ui.db_lineEdit_id.text()
        local_path = f'Images/{id}.png'
        
        # تحسين: التحقق محلياً أولاً قبل التحميل السحابي لتسريع الأداء
        if os.path.exists(local_path):
            pixmap = QPixmap(local_path)
            self.ui.db_image.setPixmap(pixmap)
            self.ui.db_image.setScaledContents(True)
        else:
            try:
                blob = bucket.blob(f'Images/{id}.png')
                img = blob.download_as_bytes()
                self.ui.db_image.setScaledContents(True)
                pixmap = QPixmap()
                pixmap.loadFromData(img)
                self.ui.db_image.setPixmap(pixmap)
            except Exception as e:
                print(f"Error getting image: {e}")
        
        studentInfo = db.reference(f'Students/{id}').get()
        if studentInfo:
            self.ui.db_lastchek.setText(str(studentInfo.get('last_check_time', '-')))
            self.ui.db_smester.setText(str(studentInfo.get('smester', '-')))
            self.ui.db_name.setText(str(studentInfo.get('name', '-')))
            self.ui.db_path.setText(str(studentInfo.get('patch', '-')))
            self.ui.db_deprt.setText(str(studentInfo.get('Departmant', '-')))
            self.ui.db_total.setText(str(studentInfo.get('total_check', '-')))


# ========================================================
# WIDGET 3: CLOUD DATABASE ACCESS PORTAL (LOGIN)
# ========================================================
class login_db(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.log = login_DB()
        self.log.setupUi(self)
        self.log.log_message.setVisible(False)
        self.log.pt_login.clicked.connect(self.startVideo_log)

    def startVideo_log(self):
        self.capture_v = cv2.VideoCapture(0)
        self.timer = QTimer(self)
        print("Loading Encode File ...")
        if os.path.exists('EncodeFile.p'):
            file = open('EncodeFile.p', 'rb')
            encodeListKnownWithIds = pickle.load(file)
            file.close()
            self.encodeListKnown, self.studentIds = encodeListKnownWithIds
        else:
            self.encodeListKnown, self.studentIds = [], []
        
        self.timer.timeout.connect(self.update_frame_log)
        self.timer.start(33) 

    def face_rec_log(self, frame, encodeListKnown, studentIds):
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        
        faceCurFrame = face_recognition.face_locations(rgb_small_frame)
        encodeCurFrame = face_recognition.face_encodings(rgb_small_frame, faceCurFrame)
        
        if faceCurFrame:
            for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
                if len(encodeListKnown) > 0:
                    matches = face_recognition.compare_faces(encodeListKnown, encodeFace, tolerance=0.4)
                    faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
                    matchIndex = np.argmin(faceDis)
                    
                    if matches[matchIndex]:
                        global loger
                        id = studentIds[matchIndex].upper()
                        loger = id
                        
                        main = db_tool_c()
                        widget.addWidget(main)
                        widget.setCurrentIndex(widget.currentIndex() + 1)
                        self.timer.stop()
                        self.capture_v.release()
                        return frame
            
            self.log.log_message.setText('You do not have permission to log')
            self.log.log_message.setVisible(True)
        return frame

    def update_frame_log(self):
        ret, self.image = self.capture_v.read()
        if ret:
            self.displayImage_log(self.image, self.encodeListKnown, self.studentIds, 1)

    def displayImage_log(self, image, encodeListKnown, studentIds, window=1):
        image = self.face_rec_log(image, encodeListKnown, studentIds)
        qformat = QImage.Format_RGB888 if len(image.shape) == 3 else QImage.Format_Indexed8
        outImage = QImage(image, image.shape[1], image.shape[0], image.strides[0], qformat).rgbSwapped()
        self.log.log_img.setPixmap(QPixmap.fromImage(outImage))
        self.log.log_img.setScaledContents(True)


# ========================================================
# 🔐 UNIFIED STUDENT ENROLLMENT FRAMEWORK 
# ========================================================
class StudentRegister(QMainWindow):
    def __init__(self, target_route="db", parent=None):
        """
        target_route: "db" للعودة لصفحة قاعدة البيانات، أو "login" للعودة لصفحة تسجيل الدخول
        """
        QMainWindow.__init__(self, parent)
        self.ui = register()
        self.ui.setupUi(self)
        
        # تحديد مسار العودة ديناميكياً
        self.target_route = target_route
        
        # ربط الأزرار بالوظائف
        self.ui.egister_bot.clicked.connect(self.add_to_firebase)
        self.ui.rej_back.clicked.connect(self.backe)
        self.ui.start_webcam.clicked.connect(self.webcme)
        self.ui.captur.clicked.connect(self.stop)
        self.ui.slect_img_bt.clicked.connect(self.uplod_img)

    def message_ex(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Successful Insertion")
        msgBox.setInformativeText("Student records appended to cloud database.")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()

    def backe(self):
        # تنظيف الذاكرة وإغلاق الكاميرا فوراً عند العودة لمنع تسريب الموارد
        if hasattr(self, 'timer_r') and self.timer_r.isActive():
            self.timer_r.stop()
        if hasattr(self, 'capture') and self.capture.isOpened():
            self.capture.release()

        # التوجيه النظيف بناءً على مكان الاستدعاء
        if self.target_route == "login":
            next_page = login_c()
        else:
            next_page = db_tool_c()
            
        widget.addWidget(next_page)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def webcme(self):
        self.capture = cv2.VideoCapture(0)
        self.timer_r = QTimer(self) 
        self.timer_r.timeout.connect(self.update_frame)
        self.timer_r.start(33)
  
    def update_frame(self):
        ret, self.image = self.capture.read()
        if ret:
            self.displayImage(self.image, 1)
   
    def displayImage(self, img, window=1):
        qformat = QImage.Format_RGB888 if len(img.shape) == 3 else QImage.Format_Indexed8
        self.outimage = QImage(img, img.shape[1], img.shape[0], img.strides[0], qformat).rgbSwapped()
        if window == 1:
            self.ui.webcam_l.setPixmap(QPixmap.fromImage(self.outimage))
            self.ui.webcam_l.setScaledContents(True)

    def stop(self):
        if hasattr(self, 'timer_r'):
            self.timer_r.stop()
        if hasattr(self, 'outimage'):
            self.ui.showimg_register.setPixmap(QPixmap.fromImage(self.outimage))
            self.ui.showimg_register.setScaledContents(True)
        if hasattr(self, 'capture'):
            self.capture.release()

    def uplod_img(self):
        filename = QFileDialog.getOpenFileName(self, 'Select Image', os.getcwd(), 'Png File (*.png)')
        if filename[0]:
            pixmap = QPixmap(filename[0])
            self.ui.showimg_register.setPixmap(pixmap)
            self.ui.showimg_register.setScaledContents(True)
            self.image = cv2.imread(filename[0])
            return filename[0]

    def add_to_firebase(self):
        ref = db.reference('Students')
        id = self.ui.enter_id.text()
        name = self.ui.enter_name.text()
        patch = self.ui.rg_cm_patch.currentText()
        Departmant = self.ui.rg_cm_spaf.currentText()
        smester = self.ui.rg_cm_smis.currentText()

        if not id or not name:
            QMessageBox.warning(self, "Warning", "Please enter ID and Name.")
            return

        student_data = {
            "name": f"{name}",
            "patch": patch,
            "Departmant": f"{Departmant}",
            "total_check": 0,
            "smester": smester,
            "last_check_time": "2026/01/01 00:00:00"
        }
        
        # تحسين: الإدخال المباشر بدون حلقات التكرار غير الضرورية
        ref.child(id).set(student_data)
            
        if not os.path.exists('Images'):
            os.mkdir('Images')
            
        if hasattr(self, 'image'):
            cv2.imwrite(f'Images/{id}.png', self.image)
            fileName = f'Images/{id}.png'
            
            # الرفع السحابي في الخلفية (30 FPS دون أي تأثير على الأداء)
            self.upload_thread = FirebaseUploadThread(fileName, fileName)
            self.upload_thread.start()
        
        self.message_ex()


# ========================================================
# WIDGET 5: EXAM VERIFICATION PORTAL (IDENTITY CHECKS)
# ========================================================
class verfie_c(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self)
        self.ver = verfiy()
        self.ver.setupUi(self)
        self.ver.vr_start_bt.clicked.connect(self.startVideo_v)
        self.ver.ver_back.clicked.connect(self.backe_v)
        self.ver.vr_stop_bt.clicked.connect(self.stop_v)
    
    def startVideo_v(self):
        self.capture_v = cv2.VideoCapture(0)
        self.timer = QTimer(self)
        print("Loading Encode File ...")
        if os.path.exists('EncodeFile.p'):
            file = open('EncodeFile.p', 'rb')
            encodeListKnownWithIds = pickle.load(file)
            file.close()
            self.encodeListKnown, self.studentIds = encodeListKnownWithIds
        else:
            self.encodeListKnown, self.studentIds = [], []
        
        self.timer.timeout.connect(self.update_frame_v)
        self.timer.start(33) 
    
    def getImage_lable(self, id):
        local_path = f'Images/{id}.png'
        # تحسين: فحص وجود الصورة محلياً لمنع توقف الكاميرا أثناء المراقبة الحية
        if os.path.exists(local_path):
            pixmap = QPixmap(local_path)
            self.ver.vr_image.setPixmap(pixmap)
            self.ver.vr_image.setScaledContents(True)
        else:
            try:
                blob = bucket.blob(local_path)
                img = blob.download_as_bytes()
                pixmap = QPixmap()
                pixmap.loadFromData(img)
                self.ver.vr_image.setPixmap(pixmap)
                self.ver.vr_image.setScaledContents(True)
            except Exception as e:
                print(f'Cannot find image snapshot: {e}')

    def face_rec_v(self, frame, encodeListKnown, studentIds):
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        
        faceCurFrame = face_recognition.face_locations(rgb_small_frame)
        encodeCurFrame = face_recognition.face_encodings(rgb_small_frame, faceCurFrame)
        
        id = "unknown"
        if faceCurFrame:
            for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
                if len(encodeListKnown) > 0:
                    matches = face_recognition.compare_faces(encodeListKnown, encodeFace, tolerance=0.3)
                    faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
                    matchIndex = np.argmin(faceDis)
                    
                    if matches[matchIndex]:
                        id = studentIds[matchIndex].upper()
                        self.getImage_lable(id)
                        self.ver.vr_image.setVisible(True)
                            
                        studentInfo = db.reference(f'Students/{id}').get()
                        if studentInfo:
                            self.ver.vr_id.setText(str(id))
                            self.ver.vr_name.setText(str(studentInfo.get('name', '-')))
                            self.ver.vr_patch.setText(str(studentInfo.get('patch', '-')))
                            self.ver.vr_spacil.setText(str(studentInfo.get('Departmant', '-')))
                            self.ver.vr_total.setText(str(studentInfo.get('smester', '-')))

            if id == "unknown":
                self.ver.vr_id.setText("-")
                self.ver.vr_name.setText("-")
                self.ver.vr_patch.setText("-")
                self.ver.vr_spacil.setText("-")
                self.ver.vr_total.setText("-")
                self.ver.vr_image.setVisible(False)
                
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, id, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
        return frame 
    
    def update_frame_v(self):
        ret, self.image = self.capture_v.read()
        if ret:
            self.displayImage_v(self.image, self.encodeListKnown, self.studentIds, 1)

    def displayImage_v(self, image, encodeListKnown, studentIds, window=1):
        image = self.face_rec_v(image, encodeListKnown, studentIds)
        qformat = QImage.Format_RGB888 if len(image.shape) == 3 else QImage.Format_Indexed8
        outImage = QImage(image, image.shape[1], image.shape[0], image.strides[0], qformat).rgbSwapped()
        if window == 1:
            self.ver.vr_webcam.setPixmap(QPixmap.fromImage(outImage))
            self.ver.vr_webcam.setScaledContents(True)
    
    def stop_v(self):
        self.timer.stop()
        self.capture_v.release()

    def backe_v(self):
        login = exm_page_c()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)


# ========================================================
# WIDGET 6: INSTITUTIONAL SECURITY GATEWAY (LOGIN)
# ========================================================
class login_c(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.log = login()
        self.log.setupUi(self)
        self.log.log_message.setVisible(False)
        self.log.pt_login.clicked.connect(self.startVideo_log)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.log.log_frame.setGraphicsEffect(self.shadow)
        self.log.siginew.clicked.connect(self.gotoregister)

    def gotoregister(self):
        # استدعاء الكلاس الموحد وتحديد مسار العودة لصفحة تسجيل الدخول
        reg = StudentRegister(target_route="login")
        widget.addWidget(reg)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def startVideo_log(self):
        self.capture_v = cv2.VideoCapture(0)
        self.timer = QTimer(self)
        if os.path.exists('EncodeFile.p'):
            file = open('EncodeFile.p', 'rb')
            encodeListKnownWithIds = pickle.load(file)
            file.close()
            self.encodeListKnown, self.studentIds = encodeListKnownWithIds
        else:
            self.encodeListKnown, self.studentIds = [], []
        
        self.timer.timeout.connect(self.update_frame_log)
        self.timer.start(33)

    def face_rec_log(self, frame, encodeListKnown, studentIds):
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        
        faceCurFrame = face_recognition.face_locations(rgb_small_frame)
        encodeCurFrame = face_recognition.face_encodings(rgb_small_frame, faceCurFrame)
        
        if faceCurFrame:
            for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
                if len(encodeListKnown) > 0:
                    matches = face_recognition.compare_faces(encodeListKnown, encodeFace, tolerance=0.3)
                    faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
                    matchIndex = np.argmin(faceDis)
                    
                    if matches[matchIndex]:
                        global loger
                        id = studentIds[matchIndex].upper()
                        loger = id
            
                        main = Main_c()
                        widget.addWidget(main)
                        widget.setCurrentIndex(widget.currentIndex() + 1)
                        self.timer.stop()
                        self.capture_v.release()
                        return frame
            self.log.log_message.setVisible(True)
        return frame 

    def update_frame_log(self):
        ret, self.image = self.capture_v.read()
        if ret:
            self.displayImage_log(self.image, self.encodeListKnown, self.studentIds, 1)

    def displayImage_log(self, image, encodeListKnown, studentIds, window=1):
        image = self.face_rec_log(image, encodeListKnown, studentIds)
        qformat = QImage.Format_RGB888 if len(image.shape) == 3 else QImage.Format_Indexed8
        outImage = QImage(image, image.shape[1], image.shape[0], image.strides[0], qformat).rgbSwapped()
        self.log.log_img.setPixmap(QPixmap.fromImage(outImage))
        self.log.log_img.setScaledContents(True)
    
    def stop_log(self):
        self.timer.stop()


# ========================================================
# WIDGET 7: CORE AI PROCTORING ENGINE (THE EXAM CAMERA)
# ========================================================
class Exame_c(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self)
        self.exm = exam()
        self.exm.setupUi(self)
        self.exm.ex_strt.clicked.connect(self.startVideo)
        self.exm.ex_out_bt.clicked.connect(self.backe_ex)
        
        # تفعيل مؤقت الـ LCD ليعمل بشكل دوري مستمر لتحديث الوقت ثانية بثانية
        self.lcd_timer = QTimer(self)
        self.lcd_timer.timeout.connect(self.lcd_number)
        self.lcd_timer.start(1000)
        
        self.exm._enter.setDigitCount(12)
        self.exm._enter.setSegmentStyle(QLCDNumber.Flat)
        self.lcd_number() # استدعاء أولي فوري لمنع تأخير شاشة الـ LCD
        
        self.exm.ex_exame_show.setVisible(False)
        self.exm.ex_lcdNumber_test.setVisible(False)

    def lcd_number(self):
        self.timef = datetime.now().strftime("%I:%M:%S %p")
        self.exm._enter.display(self.timef)
        self.exm.ex_lcdNumber_test.setDigitCount(12)
        self.exm.ex_lcdNumber_test.setSegmentStyle(QLCDNumber.Flat)
        self.exm.ex_lcdNumber_test.display(self.timef)

    def startVideo(self):
        path = f'loger-{loger}'
        if not os.path.exists(path):
            os.mkdir(path)

        self.capture = cv2.VideoCapture(0)
        self.timer = QTimer(self)
        print("Loading Encode File ...")
        if os.path.exists('EncodeFile.p'):
            file = open('EncodeFile.p', 'rb')
            encodeListKnownWithIds = pickle.load(file)
            file.close()
            self.encodeListKnown, self.studentIds = encodeListKnownWithIds
        else:
            self.encodeListKnown, self.studentIds = [], []
            
        self.timer.timeout.connect(self.update_frame_ex)
        self.timer.start(33) 
        
    def moniter(self, id, loger, datetimeopject, marke):
        with open('moniter.csv', 'a') as f:
            f.writelines(f'\n{id},{loger} {datetimeopject}, {marke}')
    
    def face_rec_ex(self, frame, encodeListKnown, studentIds):
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        
        faceCurFrame = face_recognition.face_locations(rgb_small_frame)
        encodeCurFrame = face_recognition.face_encodings(rgb_small_frame, faceCurFrame)
        
        self.counter = 0
        self.modeType = 0
        id = "unknown"
        
        if faceCurFrame:
            for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
                if len(encodeListKnown) > 0:
                    matches = face_recognition.compare_faces(encodeListKnown, encodeFace, tolerance=0.5)
                    faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
                    matchIndex = np.argmin(faceDis)
                    
                    if matches[matchIndex]:
                        id = studentIds[matchIndex].upper()
                        self.exm.ex_exame_show.setVisible(True)
                        
                        if self.counter == 0:
                            self.counter = 1
                            self.modeType = 1
                             
                        if self.counter != 0:
                            if self.counter == 1:
                                studentInfo = db.reference(f'Students/{id}').get()
                                if studentInfo:
                                    datetimeObject = datetime.strptime(studentInfo['last_check_time'], '%Y/%m/%d %H:%M:%S')
                                    secondsElapsed = (datetime.now() - datetimeObject).total_seconds()
                                    if secondsElapsed > 30:
                                        ref = db.reference(f'Students/{id}')
                                        studentInfo['total_check'] += 1
                                        ref.child('total_check').set(studentInfo['total_check'])
                                        ref.child('last_check_time').set(datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
                                        datetimeObjectn = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
                                        marke = 1
                                        self.moniter(id, loger, datetimeObjectn, marke)
                                    else:
                                        self.counter = 0
                            
                            if self.counter <= 10:
                                self.exm.ex_id.setText(str(id))
                            self.counter += 1
                            if self.counter >= 20:
                                self.counter = 0
                                self.modeType = 0

            if id == 'unknown':
                marke = 0
                datetimeObject = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
                self.moniter(id, loger, datetimeObject, marke)

            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, id, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
            self.exm.ex_id.setText(str(id))
            
            global d
            d += 1
            path_dir = f'loger-{loger}'
            if not os.path.exists(path_dir):
                os.mkdir(path_dir)
            
            cv2.imwrite(f'{path_dir}/{d}.png', frame)
            fileName = f'{path_dir}/{d}.png'
            
            # 🔥 أداء 30 FPS: الرفع السحابي يتم في الخلفية دون تعطيل الإطارات الحية
            self.upload_thread = FirebaseUploadThread(fileName, fileName)
            self.upload_thread.start()
            
        else:
            self.counter = 0
        return frame 
        
    def update_frame_ex(self):
        ret, self.image = self.capture.read()
        if ret:
            self.displayImage_ex(self.image, self.encodeListKnown, self.studentIds)

    def displayImage_ex(self, image, encodeListKnown, studentIds):
        image = self.face_rec_ex(image, encodeListKnown, studentIds)
        qformat = QImage.Format_RGB888 if len(image.shape) == 3 else QImage.Format_Indexed8
        outImage = QImage(image, image.shape[1], image.shape[0], image.strides[0], qformat).rgbSwapped()
        self.exm.ex_camera.setPixmap(QPixmap.fromImage(outImage))
        self.exm.ex_camera.setScaledContents(True)

    def backe_ex(self):
        self.timer.stop()
        self.lcd_timer.stop() # إيقاف مؤقت الـ LCD لتجنب أي تسريب للذاكرة
        self.capture.release()
        login = Main_c()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1) 


# ========================================================
# WIDGET 8: ABOUT US SCREEN
# ========================================================
class abutus_c(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self)
        self.abu = Abutus()
        self.abu.setupUi(self)
        self.abu.abut_back.clicked.connect(self.backe)

    def backe(self):
        login = Main_c()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)


# ========================================================
# WIDGET 9: APPLICATION ROUTING ROUTINE
# ========================================================
class exm_page_c(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self)
        self.ex_pg = exam_page()
        self.ex_pg.setupUi(self)
        self.ex_pg.exm_pg_back.clicked.connect(self.backe)
        self.ex_pg.exm_pg_ver_bt.clicked.connect(self.goto_ver)
        self.ex_pg.exm_pg_goexam_bt.clicked.connect(self.goto_exam) 

    def backe(self):
        login = Main_c()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)
     
    def goto_exam(self):
        login = Exame_c()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1) 

    def goto_ver(self):
        login = verfie_c()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)


# ========================================================
# WIDGET 10: CUSTOM PRODUCTION STARTUP SPLASH SCREEN
# ========================================================
counter = 0
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(50)

        self.ui.label_description.setText("<strong>WELCOME</strong> TO MY APPLICATION")
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>LOADING</strong> DATABASE"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>LOADING</strong> USER INTERFACE"))
        self.show()

    def progress(self):
        global counter
        self.ui.progressBar.setValue(counter)

        if counter > 100:
            self.timer.stop()
            log = login_c()
            widget.addWidget(log)
            widget.show()
            self.close()
        counter += 1

# ========================================================
# CORE SYSTEM EXECUTION TRACE
# ========================================================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    windo = SplashScreen()
    widget = QStackedWidget()
    
    widget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.92, y1:0, x2:0, y2:1, stop:0.0738636 rgba(0, 58, 84, 255), stop:0.261364 rgba(0, 92, 134, 255), stop:0.534091 rgba(0, 115, 169, 255), stop:0.721591 rgba(0, 194, 158, 255), stop:0.863636 rgba(66, 247, 255, 255), stop:1 rgba(50, 151, 255, 255));")
    widget.setFixedSize(1050, 630)
    
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting UI Architecture Application Cleanly.")
