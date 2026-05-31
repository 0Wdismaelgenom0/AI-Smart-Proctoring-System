# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'examtsynNN.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *



class exam(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1050, 630)
        Form.setCursor(QCursor(Qt.ArrowCursor))
        Form.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.92, y1:0, x2:0, y2:1, stop:0.0738636 rgba(0, 58, 84, 255), stop:0.261364 rgba(0, 92, 134, 255), stop:0.534091 rgba(0, 115, 169, 255), stop:0.721591 rgba(0, 194, 158, 255), stop:0.863636 rgba(66, 247, 255, 255), stop:1 rgba(50, 151, 255, 255));")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(900, 10, 151, 181))
        self.frame.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:1, cy:1, radius:0.5, fx:1, fy:0.977, stop:1 rgba(170, 41, 47, 0));")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.ex_camera = QLabel(self.frame)
        self.ex_camera.setObjectName(u"ex_camera")
        self.ex_camera.setGeometry(QRect(10, 0, 131, 121))
        self.ex_camera.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:1, cy:1, radius:0.5, fx:1, fy:0.977, stop:1 rgba(170, 41, 47, 0));\n"
"\n"
"\n"
"border-radius:6px;\n"
"border:2px solid rgb(0, 255, 255);\n"
"")
        self.ex_camera.setAlignment(Qt.AlignCenter)
        self.ex_id = QLabel(self.frame)
        self.ex_id.setObjectName(u"ex_id")
        self.ex_id.setGeometry(QRect(50, 140, 91, 31))
        self.ex_id.setStyleSheet(u"alternate-background-color: qlineargradient(spread:pad, x1:0.602, y1:0.4945, x2:0, y2:0.5, stop:0.392045 rgba(221, 221, 221, 255), stop:0.863636 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(255, 255, 255);\n"
"border-radius:9px;\n"
"border:2px solid rgb(0, 255, 255);\n"
"")
        self.ex_id.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 140, 47, 31))
        self.label_2.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:1, cy:1, radius:0.5, fx:1, fy:0.977, stop:1 rgba(170, 41, 47, 0));\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 0, 901, 51))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.ex_out_bt = QPushButton(self.frame_2)
        self.ex_out_bt.setObjectName(u"ex_out_bt")
        self.ex_out_bt.setGeometry(QRect(810, 10, 75, 31))
        self.ex_out_bt.setCursor(QCursor(Qt.PointingHandCursor))
        self.ex_out_bt.setStyleSheet(u"background-color: rgb(170, 0, 0);\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:9px;\n"
"border:2px solid rgb(0, 255, 255);\n"
"")
        self._enter = QLCDNumber(self.frame_2)
        self._enter.setObjectName(u"_enter")
        self._enter.setGeometry(QRect(400, 0, 201, 51))
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(250, 0, 141, 41))
        self.label.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:1, cy:1, radius:0.5, fx:1, fy:0.977, stop:1 rgba(170, 41, 47, 0));\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(700, 0, 101, 51))
        self.label_4.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:1, cy:1, radius:0.5, fx:1, fy:0.977, stop:1 rgba(170, 41, 47, 0));\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 2, 141, 41))
        self.label_3.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:1, cy:1, radius:0.5, fx:1, fy:0.977, stop:1 rgba(170, 41, 47, 0));\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.ex_strt = QPushButton(self.frame_2)
        self.ex_strt.setObjectName(u"ex_strt")
        self.ex_strt.setGeometry(QRect(160, 10, 75, 23))
        self.ex_strt.setStyleSheet(u"background-color: rgb(0, 170, 0);\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:9px;\n"
"border:2px solid rgb(0, 255, 255);\n"
"")
        self.ex_exame_show = QLabel(Form)
        self.ex_exame_show.setObjectName(u"ex_exame_show")
        self.ex_exame_show.setGeometry(QRect(0, 50, 901, 581))
        self.ex_exame_show.setStyleSheet(u"border-right: 3px solid  rgb(0, 255, 255);\n"
"background-image: url(icons/exame_tem.jpg);\n"
"\n"
"")
        self.ex_exame_show.setAlignment(Qt.AlignCenter)
        self.ex_lcdNumber_test = QLCDNumber(Form)
        self.ex_lcdNumber_test.setObjectName(u"ex_lcdNumber_test")
        self.ex_lcdNumber_test.setGeometry(QRect(920, 210, 121, 61))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.ex_camera.setText("")
        self.ex_id.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"id", None))
        self.ex_out_bt.setText(QCoreApplication.translate("Form", u"Exit", None))
        self.label.setText(QCoreApplication.translate("Form", u"Time you Entered :", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Loge Out >>", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Start Exam :", None))
        self.ex_strt.setText(QCoreApplication.translate("Form", u"Start", None))
        self.ex_exame_show.setText("")
    # retranslateUi

