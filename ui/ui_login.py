# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginZuHBAO.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class login(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1050, 630)
        Form.setStyleSheet(u"")
        self.log_frame = QFrame(Form)
        self.log_frame.setObjectName(u"log_frame")
        self.log_frame.setGeometry(QRect(257, 52, 501, 471))
        self.log_frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.92, y1:0, x2:0, y2:1, stop:0.0738636 rgba(0, 117, 169, 255), stop:0.261364 rgba(0, 131, 190, 255), stop:0.534091 rgba(0, 174, 255, 255), stop:0.721591 rgba(1, 201, 210, 255), stop:0.863636 rgba(66, 247, 255, 255), stop:1 rgba(50, 151, 255, 255));\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"gridline-color: rgb(255, 255, 255);\n"
"border-radius:9px;\n"
"border:2px solid rgb(0, 255, 255);")
        self.log_frame.setFrameShape(QFrame.StyledPanel)
        self.log_frame.setFrameShadow(QFrame.Raised)
        self.pt_login = QPushButton(self.log_frame)
        self.pt_login.setObjectName(u"pt_login")
        self.pt_login.setGeometry(QRect(181, 310, 135, 51))
        self.pt_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.pt_login.setStyleSheet(u"background-color: rgb(85, 170, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:9px;\n"
"border:2px solid rgb(255, 255, 255);")
        self.siginew = QPushButton(self.log_frame)
        self.siginew.setObjectName(u"siginew")
        self.siginew.setGeometry(QRect(183, 380, 131, 50))
        self.siginew.setCursor(QCursor(Qt.PointingHandCursor))
        self.siginew.setStyleSheet(u"background-color: rgb(0, 85, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:9px;\n"
"border:2px solid rgb(255, 255, 255);")
        self.log_img = QLabel(self.log_frame)
        self.log_img.setObjectName(u"log_img")
        self.log_img.setGeometry(QRect(105, 50, 291, 191))
        self.log_img.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 99), stop:1 rgba(255, 255, 255, 255));\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"gridline-color: rgb(255, 255, 255);\n"
"border-radius:9px;\n"
"border:2px solid rgb(0, 255, 255);")
        self.log_img.setAlignment(Qt.AlignCenter)
        self.log_message = QLabel(self.log_frame)
        self.log_message.setObjectName(u"log_message")
        self.log_message.setGeometry(QRect(40, 250, 431, 31))
        self.log_message.setCursor(QCursor(Qt.IBeamCursor))
        self.log_message.setFocusPolicy(Qt.TabFocus)
        self.log_message.setStyleSheet(u"border:none;\n"
"color: rgb(255, 0, 0);\n"
"background-color: qradialgradient(spread:pad, cx:1, cy:1, radius:0.5, fx:1, fy:0.977, stop:1 rgba(170, 41, 47, 0));")
        self.log_message.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pt_login.setText(QCoreApplication.translate("Form", u"login", None))
        self.siginew.setText(QCoreApplication.translate("Form", u"sign new", None))
        self.log_img.setText("")
        self.log_message.setText(QCoreApplication.translate("Form", u"!!you not IN System Pleas Rigester Or CaLL The admin!!", None))
    # retranslateUi

