# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about_usygUhUl.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Abutus(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1050, 630)
        Form.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.92, y1:0, x2:0, y2:1, stop:0.0738636 rgba(0, 58, 84, 255), stop:0.261364 rgba(0, 92, 134, 255), stop:0.534091 rgba(0, 115, 169, 255), stop:0.721591 rgba(0, 194, 158, 255), stop:0.863636 rgba(66, 247, 255, 255), stop:1 rgba(50, 151, 255, 255));")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(37, 46, 980, 333))
        self.frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 99), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"border-radius:9px;\n"
"border:2px solid rgb(0, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-1, 10, 980, 61))
        self.label.setStyleSheet(u"color: rgb(170, 255, 255);\n"
"background-color: qradialgradient(spread:pad, cx:1, cy:1, radius:0.5, fx:1, fy:0.977, stop:1 rgba(170, 41, 47, 0));\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"border:none;\n"
"border-bottom:4px solid  rgb(0, 170, 255);")
        self.label.setAlignment(Qt.AlignCenter)
        self.textBrowser = QTextBrowser(self.frame)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(21, 80, 939, 241))
        self.textBrowser.setStyleSheet(u"\n"
"color: rgb(170, 255, 255);")
        self.abut_chrom = QPushButton(Form)
        self.abut_chrom.setObjectName(u"abut_chrom")
        self.abut_chrom.setGeometry(QRect(240, 420, 111, 101))
        self.abut_chrom.setCursor(QCursor(Qt.PointingHandCursor))
        self.abut_chrom.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 255, 255);\n"
"border-radius:50%;\n"
"border:2px solid rgb(255, 255, 255);")
        icon_crm = QIcon()
        icon_crm.addFile(u"icons/chrome.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.abut_chrom.setIcon(icon_crm)
        self.abut_chrom.setIconSize(QSize(50, 50))
        self.abut_twiter = QPushButton(Form)
        self.abut_twiter.setObjectName(u"abut_twiter")
        self.abut_twiter.setGeometry(QRect(450, 420, 111, 101))
        self.abut_twiter.setCursor(QCursor(Qt.PointingHandCursor))
        self.abut_twiter.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 255, 255);\n"
"border-radius:50%;\n"
"border:2px solid rgb(255, 255, 255);")
        icon_twt = QIcon()
        icon_twt.addFile(u"icons/twitter.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.abut_twiter.setIcon(icon_twt)
        self.abut_twiter.setIconSize(QSize(50, 50))
        self.abut_facebook = QPushButton(Form)
        self.abut_facebook.setObjectName(u"abut_facebook")
        self.abut_facebook.setGeometry(QRect(660, 420, 111, 101))
        self.abut_facebook.setCursor(QCursor(Qt.PointingHandCursor))
        self.abut_facebook.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 255, 255);\n"
"border-radius:50%;\n"
"border:2px solid rgb(255, 255, 255);")
        icon_fc = QIcon()
        icon_fc.addFile(u"icons/facebook.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.abut_facebook.setIcon(icon_fc)
        self.abut_facebook.setIconSize(QSize(50, 50))
        self.abut_back = QPushButton(Form)
        self.abut_back.setObjectName(u"abut_back")
        self.abut_back.setGeometry(QRect(0, 0, 80, 31))
        self.abut_back.setCursor(QCursor(Qt.PointingHandCursor))
        self.abut_back.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(76, 227, 227);\n"
"border-radius:9px;\n"
"border:2px solid rgb(255, 255, 255);")
        icon = QIcon()
        icon.addFile(u"icons/reply-all.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.abut_back.setIcon(icon)
        self.abut_back.setIconSize(QSize(23, 31))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"About us.", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">exam monitaring Is Disktope System That devolope py</span></p>\n"
"<p align=\"center\""
                        " style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">AAU Sudan Universty student To Make The Online Examing Ezey and usefuly .......</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;\"><br /></p></body></html>", None))
        self.abut_chrom.setText("")
        self.abut_twiter.setText("")
        self.abut_facebook.setText("")
        self.abut_back.setText("")
    # retranslateUi

