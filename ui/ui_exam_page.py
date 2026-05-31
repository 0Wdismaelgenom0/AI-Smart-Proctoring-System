# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'exam_pageugnwkY.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class exam_page(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1043, 560)
        Form.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.92, y1:0, x2:0, y2:1, stop:0.0738636 rgba(0, 58, 84, 255), stop:0.261364 rgba(0, 92, 134, 255), stop:0.534091 rgba(0, 115, 169, 255), stop:0.721591 rgba(0, 194, 158, 255), stop:0.863636 rgba(66, 247, 255, 255), stop:1 rgba(50, 151, 255, 255));")
        self.exm_pg_goexam_bt = QPushButton(Form)
        self.exm_pg_goexam_bt.setObjectName(u"exm_pg_goexam_bt")
        self.exm_pg_goexam_bt.setGeometry(QRect(700, 220, 188, 101))
        self.exm_pg_goexam_bt.setCursor(QCursor(Qt.PointingHandCursor))
        self.exm_pg_goexam_bt.setStyleSheet(u"border-radius:9px;\n"
"border:2px solid rgb(0, 255, 255);")
        icon = QIcon()
        icon.addFile(u"icons/file-signature.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.exm_pg_goexam_bt.setIcon(icon)
        self.exm_pg_goexam_bt.setIconSize(QSize(59, 73))
        self.exm_pg_ver_bt = QPushButton(Form)
        self.exm_pg_ver_bt.setObjectName(u"exm_pg_ver_bt")
        self.exm_pg_ver_bt.setGeometry(QRect(400, 220, 190, 104))
        self.exm_pg_ver_bt.setCursor(QCursor(Qt.PointingHandCursor))
        self.exm_pg_ver_bt.setStyleSheet(u"border-radius:9px;\n"
"border:2px solid rgb(0, 255, 255);")
        icon1 = QIcon()
        icon1.addFile(u"icons/sliders-h.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.exm_pg_ver_bt.setIcon(icon1)
        self.exm_pg_ver_bt.setIconSize(QSize(55, 53))
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(8, 41, 291, 511))
        self.frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 99), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"border-radius:9px;\n"
"border:2px solid rgb(0, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-1, 10, 292, 61))
        self.label.setStyleSheet(u"color: rgb(170, 255, 255);\n"
"background-color: qradialgradient(spread:pad, cx:1, cy:1, radius:0.5, fx:1, fy:0.977, stop:1 rgba(170, 41, 47, 0));\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"border:none;\n"
"border-bottom:4px solid  rgb(0, 170, 255);")
        self.label.setAlignment(Qt.AlignCenter)
        self.textBrowser = QTextBrowser(self.frame)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(15, 150, 256, 221))
        self.textBrowser.setStyleSheet(u"\n"
"color: rgb(170, 255, 255);")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 90, 71, 51))
        self.label_4.setStyleSheet(u"font: 18pt \"MS Shell Dlg 2\";\n"
"background-color: qradialgradient(spread:repeat, cx:1, cy:1, radius:0.5, fx:1, fy:1, stop:0 rgba(255, 0, 0, 0), stop:1 rgba(0, 0, 0, 0));\n"
"color: rgb(255, 255, 0);\n"
"border:none;")
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.exm_pg_back = QPushButton(Form)
        self.exm_pg_back.setObjectName(u"exm_pg_back")
        self.exm_pg_back.setGeometry(QRect(0, 0, 80, 31))
        self.exm_pg_back.setCursor(QCursor(Qt.PointingHandCursor))
        self.exm_pg_back.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(76, 227, 227);\n"
"border-radius:9px;\n"
"border:2px solid rgb(255, 255, 255);")
        icon2 = QIcon()
        icon2.addFile(u"icons/reply-all.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.exm_pg_back.setIcon(icon2)
        self.exm_pg_back.setIconSize(QSize(23, 31))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(700, 340, 191, 51))
        self.label_2.setStyleSheet(u"font: 18pt \"MS Shell Dlg 2\";\n"
"background-color: qradialgradient(spread:repeat, cx:1, cy:1, radius:0.5, fx:1, fy:1, stop:0 rgba(255, 0, 0, 0), stop:1 rgba(0, 0, 0, 0));\n"
"color: rgb(255, 255, 255);\n"
"border:none;")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(340, 340, 301, 51))
        self.label_3.setStyleSheet(u"font: 15pt \"MS Shell Dlg 2\";\n"
"background-color: qradialgradient(spread:repeat, cx:1, cy:1, radius:0.5, fx:1, fy:1, stop:0 rgba(255, 0, 0, 0), stop:1 rgba(0, 0, 0, 0));\n"
"color: rgb(255, 255, 255);\n"
"border:none;")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.exm_pg_goexam_bt.setText("")
        self.exm_pg_ver_bt.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"wlcome to exam page", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">- !! Make Sure Of Your LIGHT AND Position Of Your WEBCAME</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; marg"
                        "in-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">-!! You Cane Checke Your Camere And Internet By Prass CHICKe button</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-le"
                        "ft:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">-!!  GOOD LUCK </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Hint !!!", None))
        self.exm_pg_back.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"Enter The Exam", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Chicke Connect with database ", None))
    # retranslateUi

