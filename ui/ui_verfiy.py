# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'verfiyLSXHmF.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class verfiy(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1001, 591)
        Form.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.92, y1:0, x2:0, y2:1, stop:0.0738636 rgba(0, 58, 84, 255), stop:0.261364 rgba(0, 92, 134, 255), stop:0.534091 rgba(0, 115, 169, 255), stop:0.721591 rgba(0, 194, 158, 255), stop:0.863636 rgba(66, 247, 255, 255), stop:1 rgba(50, 151, 255, 255));")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(700, 0, 301, 591))
        self.frame.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:1, cy:1, radius:0.5, fx:1, fy:0.977, stop:1 rgba(170, 41, 47, 0));\n"
"\n"
"border-radius:9px;\n"
"border:2px solid rgb(0, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.vr_image = QLabel(self.frame)
        self.vr_image.setObjectName(u"vr_image")
        self.vr_image.setGeometry(QRect(30, 10, 221, 191))
        self.vr_image.setStyleSheet(u"background-color: qradialgradient(spread:repeat, cx:1, cy:1, radius:0.5, fx:1, fy:1, stop:0 rgba(255, 0, 0, 0), stop:1 rgba(0, 0, 0, 0));")
        self.vr_image.setAlignment(Qt.AlignCenter)
        self.vr_name = QLabel(self.frame)
        self.vr_name.setObjectName(u"vr_name")
        self.vr_name.setGeometry(QRect(10, 220, 261, 41))
        self.vr_name.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.vr_name.setAlignment(Qt.AlignCenter)
        self.vr_patch = QLabel(self.frame)
        self.vr_patch.setObjectName(u"vr_patch")
        self.vr_patch.setGeometry(QRect(150, 280, 141, 41))
        self.vr_patch.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.vr_patch.setAlignment(Qt.AlignCenter)
        self.vr_spacil = QLabel(self.frame)
        self.vr_spacil.setObjectName(u"vr_spacil")
        self.vr_spacil.setGeometry(QRect(150, 340, 141, 41))
        self.vr_spacil.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.vr_spacil.setAlignment(Qt.AlignCenter)
        self.vr_total = QLabel(self.frame)
        self.vr_total.setObjectName(u"vr_total")
        self.vr_total.setGeometry(QRect(150, 400, 141, 41))
        self.vr_total.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.vr_total.setAlignment(Qt.AlignCenter)
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 280, 131, 41))
        self.label_7.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: qradialgradient(spread:repeat, cx:1, cy:1, radius:0.5, fx:1, fy:1, stop:0 rgba(255, 0, 0, 0), stop:1 rgba(0, 0, 0, 0));\n"
"color: rgb(255, 255, 255);\n"
"border:none;")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 340, 131, 41))
        self.label_8.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: qradialgradient(spread:repeat, cx:1, cy:1, radius:0.5, fx:1, fy:1, stop:0 rgba(255, 0, 0, 0), stop:1 rgba(0, 0, 0, 0));\n"
"color: rgb(255, 255, 255);\n"
"border:none;")
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(60, 460, 91, 41))
        self.label_11.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: qradialgradient(spread:repeat, cx:1, cy:1, radius:0.5, fx:1, fy:1, stop:0 rgba(255, 0, 0, 0), stop:1 rgba(0, 0, 0, 0));\n"
"color: rgb(255, 255, 255);\n"
"border:none;")
        self.label_11.setAlignment(Qt.AlignCenter)
        self.vr_id = QLabel(self.frame)
        self.vr_id.setObjectName(u"vr_id")
        self.vr_id.setGeometry(QRect(150, 460, 141, 41))
        self.vr_id.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.vr_id.setAlignment(Qt.AlignCenter)
        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(30, 400, 131, 41))
        self.label_9.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: qradialgradient(spread:repeat, cx:1, cy:1, radius:0.5, fx:1, fy:1, stop:0 rgba(255, 0, 0, 0), stop:1 rgba(0, 0, 0, 0));\n"
"color: rgb(255, 255, 255);\n"
"border:none;")
        self.label_9.setAlignment(Qt.AlignCenter)
        self.vr_webcam = QLabel(Form)
        self.vr_webcam.setObjectName(u"vr_webcam")
        self.vr_webcam.setGeometry(QRect(60, 50, 571, 391))
        self.vr_webcam.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:1, cy:1, radius:0.5, fx:1, fy:0.977, stop:1 rgba(170, 41, 47, 0));\n"
"\n"
"border:2px solid rgb(0, 255, 255);")
        self.vr_webcam.setAlignment(Qt.AlignCenter)
        self.vr_start_bt = QPushButton(Form)
        self.vr_start_bt.setObjectName(u"vr_start_bt")
        self.vr_start_bt.setGeometry(QRect(60, 480, 221, 41))
        self.vr_start_bt.setStyleSheet(u"alternate-background-color: qlineargradient(spread:pad, x1:0.602, y1:0.4945, x2:0, y2:0.5, stop:0.392045 rgba(221, 221, 221, 255), stop:0.863636 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:9px;\n"
"border:2px solid rgb(255, 255, 255);")
        self.vr_stop_bt = QPushButton(Form)
        self.vr_stop_bt.setObjectName(u"vr_stop_bt")
        self.vr_stop_bt.setGeometry(QRect(410, 480, 221, 41))
        self.vr_stop_bt.setStyleSheet(u"alternate-background-color: qlineargradient(spread:pad, x1:0.602, y1:0.4945, x2:0, y2:0.5, stop:0.392045 rgba(221, 221, 221, 255), stop:0.863636 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:9px;\n"
"border:2px solid rgb(0, 255, 255);")
        self.ver_back = QPushButton(Form)
        self.ver_back.setObjectName(u"ver_back")
        self.ver_back.setGeometry(QRect(0, 0, 80, 31))
        self.ver_back.setCursor(QCursor(Qt.PointingHandCursor))
        self.ver_back.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(76, 227, 227);\n"
"border-radius:9px;\n"
"border:2px solid rgb(255, 255, 255);")
        icon = QIcon()
        icon.addFile(u"icons/reply-all.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ver_back.setIcon(icon)
        self.ver_back.setIconSize(QSize(23, 31))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.vr_image.setText("")
        self.vr_name.setText("")
        self.vr_patch.setText("")
        self.vr_spacil.setText("")
        self.vr_total.setText("")
        self.label_7.setText(QCoreApplication.translate("Form", u"Patch Number >>", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Spacilist >>", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Id >>", None))
        self.vr_id.setText("")
        self.label_9.setText(QCoreApplication.translate("Form", u"Smister  >>", None))
        self.vr_webcam.setText("")
        self.vr_start_bt.setText(QCoreApplication.translate("Form", u"Start Test", None))
        self.vr_stop_bt.setText(QCoreApplication.translate("Form", u"Stop Test", None))
        self.ver_back.setText("")
    # retranslateUi

