# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main pagezZCjky.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Main_f(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1080, 605)
        Form.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.92, y1:0, x2:0, y2:1, stop:0.0738636 rgba(0, 58, 84, 255), stop:0.261364 rgba(0, 92, 134, 255), stop:0.534091 rgba(0, 115, 169, 255), stop:0.721591 rgba(0, 194, 158, 255), stop:0.863636 rgba(66, 247, 255, 255), stop:1 rgba(50, 151, 255, 255));")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 1091, 311))
        self.frame.setStyleSheet(u"background-image: url(icons/face2.webp);\n"
"border-bottom:4px solid  rgb(0, 170, 255);\n"
"border-radius:15px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(70, 230, 331, 61))
        self.label_12.setStyleSheet(u"color: rgb(170, 255, 255);\n"
"background-color: qradialgradient(spread:pad, cx:1, cy:1, radius:0.5, fx:1, fy:0.977, stop:1 rgba(170, 41, 47, 0));\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"border:none;")
        self.label_12.setAlignment(Qt.AlignCenter)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(124, 10, 221, 181))
        self.frame_2.setStyleSheet(u"image: url(icons/logo1 (1).png);\n"
"border:none;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.main_bt_exam = QPushButton(Form)
        self.main_bt_exam.setObjectName(u"main_bt_exam")
        self.main_bt_exam.setGeometry(QRect(120, 370, 161, 119))
        self.main_bt_exam.setCursor(QCursor(Qt.PointingHandCursor))
        self.main_bt_exam.setAutoFillBackground(False)
        self.main_bt_exam.setStyleSheet(u"alternate-background-color: qlineargradient(spread:pad, x1:0.602, y1:0.4945, x2:0, y2:0.5, stop:0.392045 rgba(221, 221, 221, 255), stop:0.863636 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:9px;\n"
"border:2px solid rgb(255, 255, 255);\n"
"")
        icon = QIcon()
        icon.addFile(u"icons/edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.main_bt_exam.setIcon(icon)
        self.main_bt_exam.setIconSize(QSize(65, 71))
        self.main_bt_exam.setCheckable(True)
        self.main_bt_exam.setAutoDefault(True)
        self.main_bt_exam.setFlat(False)
        self.main_bt_db = QPushButton(Form)
        self.main_bt_db.setObjectName(u"main_bt_db")
        self.main_bt_db.setGeometry(QRect(470, 370, 151, 121))
        self.main_bt_db.setCursor(QCursor(Qt.PointingHandCursor))
        self.main_bt_db.setStyleSheet(u"alternate-background-color: qlineargradient(spread:pad, x1:0.602, y1:0.4945, x2:0, y2:0.5, stop:0.392045 rgba(221, 221, 221, 255), stop:0.863636 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:9px;\n"
"border:2px solid rgb(255, 255, 255);")
        icon1 = QIcon()
        icon1.addFile(u"icons/database.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.main_bt_db.setIcon(icon1)
        self.main_bt_db.setIconSize(QSize(66, 76))
        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(110, 510, 181, 41))
        self.label_8.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:1, cy:1, radius:0.5, fx:1, fy:0.977, stop:1 rgba(170, 41, 47, 0));\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(464, 512, 161, 41))
        self.label_10.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:1, cy:1, radius:0.5, fx:1, fy:0.977, stop:1 rgba(170, 41, 47, 0));\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.label_10.setAlignment(Qt.AlignCenter)
        self.main_bt_abutus = QPushButton(Form)
        self.main_bt_abutus.setObjectName(u"main_bt_abutus")
        self.main_bt_abutus.setGeometry(QRect(800, 370, 151, 121))
        self.main_bt_abutus.setCursor(QCursor(Qt.PointingHandCursor))
        self.main_bt_abutus.setStyleSheet(u"alternate-background-color: qlineargradient(spread:pad, x1:0.602, y1:0.4945, x2:0, y2:0.5, stop:0.392045 rgba(221, 221, 221, 255), stop:0.863636 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:9px;\n"
"border:2px solid rgb(255, 255, 255);")
        icon2 = QIcon()
        icon2.addFile(u"icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.main_bt_abutus.setIcon(icon2)
        self.main_bt_abutus.setIconSize(QSize(66, 76))
        self.label_11 = QLabel(Form)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(790, 510, 161, 41))
        self.label_11.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:1, cy:1, radius:0.5, fx:1, fy:0.977, stop:1 rgba(170, 41, 47, 0));\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_12.setText(QCoreApplication.translate("Form", u" EXAM MONITER SYSTEM ", None))
        self.main_bt_exam.setText("")
        self.main_bt_db.setText("")
        self.label_8.setText(QCoreApplication.translate("Form", u"Enter Exam Side", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Database side", None))
        self.main_bt_abutus.setText("")
        self.label_11.setText(QCoreApplication.translate("Form", u"Aboute As", None))
    # retranslateUi

