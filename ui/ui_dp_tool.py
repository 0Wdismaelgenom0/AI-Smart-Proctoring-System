# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dp_toolsHvaXe.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class db_tool(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1050, 630)
        Form.setMinimumSize(QSize(1050, 630))
        Form.setMaximumSize(QSize(1100, 650))
        Form.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.92, y1:0, x2:0, y2:1, stop:0.0738636 rgba(0, 58, 84, 255), stop:0.261364 rgba(0, 92, 134, 255), stop:0.534091 rgba(0, 115, 169, 255), stop:0.721591 rgba(0, 194, 158, 255), stop:0.863636 rgba(66, 247, 255, 255), stop:1 rgba(50, 151, 255, 255));")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 400, 631))
        self.frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 99), stop:1 rgba(255, 255, 255, 255));\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"gridline-color: rgb(255, 255, 255);\n"
"border-radius:9px;\n"
"border:2px solid rgb(0, 255, 255);")
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.db_Trin = QPushButton(self.frame)
        self.db_Trin.setObjectName(u"db_Trin")
        self.db_Trin.setGeometry(QRect(20, 250, 161, 51))
        self.db_Trin.setCursor(QCursor(Qt.PointingHandCursor))
        self.db_Trin.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0.92, y1:0, x2:0, y2:1, stop:0.0738636 rgba(0, 58, 84, 255), stop:0.261364 rgba(0, 92, 134, 255), stop:0.534091 rgba(0, 115, 169, 255), stop:0.721591 rgba(0, 194, 158, 255), stop:0.863636 rgba(66, 247, 255, 255), stop:1 rgba(50, 151, 255, 255));")
        self.db_insert_new = QPushButton(self.frame)
        self.db_insert_new.setObjectName(u"db_insert_new")
        self.db_insert_new.setGeometry(QRect(210, 250, 171, 51))
        self.db_insert_new.setCursor(QCursor(Qt.PointingHandCursor))
        self.db_insert_new.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0.92, y1:0, x2:0, y2:1, stop:0.0738636 rgba(0, 58, 84, 255), stop:0.261364 rgba(0, 92, 134, 255), stop:0.534091 rgba(0, 115, 169, 255), stop:0.721591 rgba(0, 194, 158, 255), stop:0.863636 rgba(66, 247, 255, 255), stop:1 rgba(50, 151, 255, 255));")
        self.db_back = QPushButton(self.frame)
        self.db_back.setObjectName(u"db_back")
        self.db_back.setGeometry(QRect(0, 0, 80, 31))
        self.db_back.setCursor(QCursor(Qt.PointingHandCursor))
        self.db_back.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(76, 227, 227);\n"
"border-radius:9px;\n"
"border:2px solid rgb(255, 255, 255);")
        icon = QIcon()
        icon.addFile(u"icons/reply-all.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.db_back.setIcon(icon)
        self.db_back.setIconSize(QSize(23, 31))
        self.db_delet = QPushButton(self.frame)
        self.db_delet.setObjectName(u"db_delet")
        self.db_delet.setGeometry(QRect(130, 380, 131, 61))
        self.db_delet.setCursor(QCursor(Qt.PointingHandCursor))
        self.db_delet.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0.92, y1:0, x2:0, y2:1, stop:0.0738636 rgba(0, 58, 84, 255), stop:0.261364 rgba(0, 92, 134, 255), stop:0.534091 rgba(0, 115, 169, 255), stop:0.721591 rgba(0, 194, 158, 255), stop:0.863636 rgba(66, 247, 255, 255), stop:1 rgba(50, 151, 255, 255));")
        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(400, 0, 648, 627))
        self.frame_2.setStyleSheet(u"\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"gridline-color: rgb(255, 255, 255);\n"
"border-radius:9px;\n"
"border:2px solid rgb(0, 255, 255);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.db_lineEdit_id = QLineEdit(self.frame_2)
        self.db_lineEdit_id.setObjectName(u"db_lineEdit_id")
        self.db_lineEdit_id.setGeometry(QRect(70, 20, 181, 41))
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.db_lineEdit_id.setFont(font)
        self.db_lineEdit_id.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 99), stop:1 rgba(255, 255, 255, 255));\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"gridline-color: rgb(255, 255, 255);\n"
"border-radius:9px;\n"
"border:2px solid rgb(0, 255, 255)")
        self.db_lineEdit_id.setInputMethodHints(Qt.ImhPreferNumbers)
        self.db_lineEdit_id.setReadOnly(False)
        self.db_show_bt = QPushButton(self.frame_2)
        self.db_show_bt.setObjectName(u"db_show_bt")
        self.db_show_bt.setGeometry(QRect(70, 90, 181, 56))
        self.db_show_bt.setCursor(QCursor(Qt.PointingHandCursor))
        self.db_show_bt.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.92, y1:0, x2:0, y2:1, stop:0.0738636 rgba(0, 58, 84, 255), stop:0.261364 rgba(0, 92, 134, 255), stop:0.534091 rgba(0, 115, 169, 255), stop:0.721591 rgba(0, 194, 158, 255), stop:0.863636 rgba(66, 247, 255, 255), stop:1 rgba(50, 151, 255, 255));")
        self.db_image = QLabel(self.frame_2)
        self.db_image.setObjectName(u"db_image")
        self.db_image.setGeometry(QRect(340, 10, 261, 161))
        self.db_image.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:1, cy:1, radius:0.5, fx:1, fy:0.977, stop:1 rgba(170, 41, 47, 0));\n"
"border-radius:3px;\n"
"border:2px solid rgb(0, 255, 255);")
        self.db_image.setAlignment(Qt.AlignCenter)
        self.db_name = QLabel(self.frame_2)
        self.db_name.setObjectName(u"db_name")
        self.db_name.setGeometry(QRect(340, 190, 261, 41))
        self.db_name.setCursor(QCursor(Qt.IBeamCursor))
        self.db_name.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 99), stop:1 rgba(255, 255, 255, 255));\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"gridline-color: rgb(255, 255, 255);\n"
"border-radius:9px;\n"
"border:2px solid rgb(0, 255, 255)")
        self.db_name.setAlignment(Qt.AlignCenter)
        self.db_path = QLabel(self.frame_2)
        self.db_path.setObjectName(u"db_path")
        self.db_path.setGeometry(QRect(341, 250, 261, 41))
        self.db_path.setCursor(QCursor(Qt.IBeamCursor))
        self.db_path.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 99), stop:1 rgba(255, 255, 255, 255));\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"gridline-color: rgb(255, 255, 255);\n"
"border-radius:9px;\n"
"border:2px solid rgb(0, 255, 255)")
        self.db_path.setAlignment(Qt.AlignCenter)
        self.db_smester = QLabel(self.frame_2)
        self.db_smester.setObjectName(u"db_smester")
        self.db_smester.setGeometry(QRect(342, 315, 261, 41))
        self.db_smester.setCursor(QCursor(Qt.IBeamCursor))
        self.db_smester.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 99), stop:1 rgba(255, 255, 255, 255));\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"gridline-color: rgb(255, 255, 255);\n"
"border-radius:9px;\n"
"border:2px solid rgb(0, 255, 255)")
        self.db_smester.setAlignment(Qt.AlignCenter)
        self.db_deprt = QLabel(self.frame_2)
        self.db_deprt.setObjectName(u"db_deprt")
        self.db_deprt.setGeometry(QRect(343, 380, 262, 41))
        self.db_deprt.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 99), stop:1 rgba(255, 255, 255, 255));\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"gridline-color: rgb(255, 255, 255);\n"
"border-radius:9px;\n"
"border:2px solid rgb(0, 255, 255)")
        self.db_deprt.setAlignment(Qt.AlignCenter)
        self.db_lastchek = QLabel(self.frame_2)
        self.db_lastchek.setObjectName(u"db_lastchek")
        self.db_lastchek.setGeometry(QRect(342, 440, 264, 41))
        self.db_lastchek.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 99), stop:1 rgba(255, 255, 255, 255));\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"gridline-color: rgb(255, 255, 255);\n"
"border-radius:9px;\n"
"border:2px solid rgb(0, 255, 255)")
        self.db_lastchek.setAlignment(Qt.AlignCenter)
        self.db_Intgrit = QLabel(self.frame_2)
        self.db_Intgrit.setObjectName(u"db_Intgrit")
        self.db_Intgrit.setGeometry(QRect(410, 550, 131, 71))
        self.db_Intgrit.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 99), stop:1 rgba(255, 255, 255, 255));\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"gridline-color: rgb(255, 255, 255);\n"
"border-radius:9px;\n"
"border:2px solid rgb(0, 255, 255)")
        self.db_Intgrit.setAlignment(Qt.AlignCenter)
        self.db_total = QLabel(self.frame_2)
        self.db_total.setObjectName(u"db_total")
        self.db_total.setGeometry(QRect(344, 500, 264, 41))
        self.db_total.setCursor(QCursor(Qt.IBeamCursor))
        self.db_total.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 99), stop:1 rgba(255, 255, 255, 255));\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"gridline-color: rgb(255, 255, 255);\n"
"border-radius:9px;\n"
"border:2px solid rgb(0, 255, 255)")
        self.db_total.setAlignment(Qt.AlignCenter)
        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(210, 240, 111, 61))
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(204, 34, 51, 0));\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"border:none;")
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(235, 177, 81, 61))
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(204, 34, 51, 0));\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"border:none;")
        self.label_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(154, 428, 171, 61))
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(204, 34, 51, 0));\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"border:none;")
        self.label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(183, 300, 141, 61))
        self.label_11.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(204, 34, 51, 0));\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"border:none;")
        self.label_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(177, 489, 151, 61))
        self.label_12.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(204, 34, 51, 0));\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"border:none;")
        self.label_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(184, 366, 141, 61))
        self.label_13.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(204, 34, 51, 0));\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"border:none;")
        self.label_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_14 = QLabel(self.frame_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(230, 560, 141, 61))
        self.label_14.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(204, 34, 51, 0));\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"border:none;")
        self.label_14.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.db_Trin.setText(QCoreApplication.translate("Form", u"Train data", None))
        self.db_insert_new.setText(QCoreApplication.translate("Form", u"Insert new", None))
        self.db_back.setText("")
        self.db_delet.setText(QCoreApplication.translate("Form", u"Delete", None))
        self.db_lineEdit_id.setInputMask("")
        self.db_lineEdit_id.setText("")
        self.db_lineEdit_id.setPlaceholderText(QCoreApplication.translate("Form", u"     enter studant id", None))
        self.db_show_bt.setText(QCoreApplication.translate("Form", u"Show Student record", None))
        self.db_image.setText("")
        self.db_name.setText("")
        self.db_path.setText("")
        self.db_smester.setText("")
        self.db_deprt.setText("")
        self.db_lastchek.setText("")
        self.db_Intgrit.setText("")
        self.db_total.setText("")
        self.label_8.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"right\">Patch No :</p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"right\">Name :</p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"right\">Last Time Check :</p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"right\">Semester :</p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"right\">Total Of Check:</p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"right\">Department :</p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"right\">Intgrite%:</p></body></html>", None))
    # retranslateUi

