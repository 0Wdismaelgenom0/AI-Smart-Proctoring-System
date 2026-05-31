# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registerfnKMNn.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class register(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(1050, 630)
        palette = QPalette()
        gradient = QLinearGradient(0.92, 0, 0, 1)
        gradient.setSpread(QGradient.PadSpread)
        gradient.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0738636, QColor(0, 58, 84, 255))
        gradient.setColorAt(0.261364, QColor(0, 92, 134, 255))
        gradient.setColorAt(0.534091, QColor(0, 115, 169, 255))
        gradient.setColorAt(0.721591, QColor(0, 194, 158, 255))
        gradient.setColorAt(0.863636, QColor(66, 247, 255, 255))
        gradient.setColorAt(1, QColor(50, 151, 255, 255))
        brush = QBrush(gradient)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        gradient1 = QLinearGradient(0.92, 0, 0, 1)
        gradient1.setSpread(QGradient.PadSpread)
        gradient1.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient1.setColorAt(0.0738636, QColor(0, 58, 84, 255))
        gradient1.setColorAt(0.261364, QColor(0, 92, 134, 255))
        gradient1.setColorAt(0.534091, QColor(0, 115, 169, 255))
        gradient1.setColorAt(0.721591, QColor(0, 194, 158, 255))
        gradient1.setColorAt(0.863636, QColor(66, 247, 255, 255))
        gradient1.setColorAt(1, QColor(50, 151, 255, 255))
        brush1 = QBrush(gradient1)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        gradient2 = QLinearGradient(0.92, 0, 0, 1)
        gradient2.setSpread(QGradient.PadSpread)
        gradient2.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient2.setColorAt(0.0738636, QColor(0, 58, 84, 255))
        gradient2.setColorAt(0.261364, QColor(0, 92, 134, 255))
        gradient2.setColorAt(0.534091, QColor(0, 115, 169, 255))
        gradient2.setColorAt(0.721591, QColor(0, 194, 158, 255))
        gradient2.setColorAt(0.863636, QColor(66, 247, 255, 255))
        gradient2.setColorAt(1, QColor(50, 151, 255, 255))
        brush2 = QBrush(gradient2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush2)
        brush3 = QBrush(QColor(255, 176, 187, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        gradient3 = QLinearGradient(0.92, 0, 0, 1)
        gradient3.setSpread(QGradient.PadSpread)
        gradient3.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient3.setColorAt(0.0738636, QColor(0, 58, 84, 255))
        gradient3.setColorAt(0.261364, QColor(0, 92, 134, 255))
        gradient3.setColorAt(0.534091, QColor(0, 115, 169, 255))
        gradient3.setColorAt(0.721591, QColor(0, 194, 158, 255))
        gradient3.setColorAt(0.863636, QColor(66, 247, 255, 255))
        gradient3.setColorAt(1, QColor(50, 151, 255, 255))
        brush4 = QBrush(gradient3)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        gradient4 = QLinearGradient(0.92, 0, 0, 1)
        gradient4.setSpread(QGradient.PadSpread)
        gradient4.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient4.setColorAt(0.0738636, QColor(0, 58, 84, 255))
        gradient4.setColorAt(0.261364, QColor(0, 92, 134, 255))
        gradient4.setColorAt(0.534091, QColor(0, 115, 169, 255))
        gradient4.setColorAt(0.721591, QColor(0, 194, 158, 255))
        gradient4.setColorAt(0.863636, QColor(66, 247, 255, 255))
        gradient4.setColorAt(1, QColor(50, 151, 255, 255))
        brush5 = QBrush(gradient4)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        gradient5 = QLinearGradient(0.92, 0, 0, 1)
        gradient5.setSpread(QGradient.PadSpread)
        gradient5.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient5.setColorAt(0.0738636, QColor(0, 58, 84, 255))
        gradient5.setColorAt(0.261364, QColor(0, 92, 134, 255))
        gradient5.setColorAt(0.534091, QColor(0, 115, 169, 255))
        gradient5.setColorAt(0.721591, QColor(0, 194, 158, 255))
        gradient5.setColorAt(0.863636, QColor(66, 247, 255, 255))
        gradient5.setColorAt(1, QColor(50, 151, 255, 255))
        brush6 = QBrush(gradient5)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        gradient6 = QLinearGradient(0.92, 0, 0, 1)
        gradient6.setSpread(QGradient.PadSpread)
        gradient6.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient6.setColorAt(0.0738636, QColor(0, 58, 84, 255))
        gradient6.setColorAt(0.261364, QColor(0, 92, 134, 255))
        gradient6.setColorAt(0.534091, QColor(0, 115, 169, 255))
        gradient6.setColorAt(0.721591, QColor(0, 194, 158, 255))
        gradient6.setColorAt(0.863636, QColor(66, 247, 255, 255))
        gradient6.setColorAt(1, QColor(50, 151, 255, 255))
        brush7 = QBrush(gradient6)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        gradient7 = QLinearGradient(0.92, 0, 0, 1)
        gradient7.setSpread(QGradient.PadSpread)
        gradient7.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient7.setColorAt(0.0738636, QColor(0, 58, 84, 255))
        gradient7.setColorAt(0.261364, QColor(0, 92, 134, 255))
        gradient7.setColorAt(0.534091, QColor(0, 115, 169, 255))
        gradient7.setColorAt(0.721591, QColor(0, 194, 158, 255))
        gradient7.setColorAt(0.863636, QColor(66, 247, 255, 255))
        gradient7.setColorAt(1, QColor(50, 151, 255, 255))
        brush8 = QBrush(gradient7)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        gradient8 = QLinearGradient(0.92, 0, 0, 1)
        gradient8.setSpread(QGradient.PadSpread)
        gradient8.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient8.setColorAt(0.0738636, QColor(0, 58, 84, 255))
        gradient8.setColorAt(0.261364, QColor(0, 92, 134, 255))
        gradient8.setColorAt(0.534091, QColor(0, 115, 169, 255))
        gradient8.setColorAt(0.721591, QColor(0, 194, 158, 255))
        gradient8.setColorAt(0.863636, QColor(66, 247, 255, 255))
        gradient8.setColorAt(1, QColor(50, 151, 255, 255))
        brush9 = QBrush(gradient8)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush3)
        mainWindow.setPalette(palette)
        mainWindow.setCursor(QCursor(Qt.ArrowCursor))
        mainWindow.setContextMenuPolicy(Qt.DefaultContextMenu)
        mainWindow.setAutoFillBackground(False)
        mainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.92, y1:0, x2:0, y2:1, stop:0.0738636 rgba(0, 58, 84, 255), stop:0.261364 rgba(0, 92, 134, 255), stop:0.534091 rgba(0, 115, 169, 255), stop:0.721591 rgba(0, 194, 158, 255), stop:0.863636 rgba(66, 247, 255, 255), stop:1 rgba(50, 151, 255, 255));\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(183, 36, 80, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        mainWindow.setTabShape(QTabWidget.Rounded)
        mainWindow.setDockOptions(QMainWindow.AllowNestedDocks|QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        mainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.webcam_l = QLabel(self.centralwidget)
        self.webcam_l.setObjectName(u"webcam_l")
        self.webcam_l.setGeometry(QRect(20, 60, 461, 301))
        self.webcam_l.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:1, cy:1, radius:0.5, fx:1, fy:0.977, stop:1 rgba(170, 41, 47, 0));\n"
"\n"
"border:2px solid rgb(0, 255, 255);")
        self.webcam_l.setScaledContents(False)
        self.webcam_l.setAlignment(Qt.AlignCenter)
        self.webcam_l.setWordWrap(False)
        self.slect_img_bt = QToolButton(self.centralwidget)
        self.slect_img_bt.setObjectName(u"slect_img_bt")
        self.slect_img_bt.setGeometry(QRect(680, 450, 81, 31))
        self.slect_img_bt.setCursor(QCursor(Qt.PointingHandCursor))
        self.slect_img_bt.setStyleSheet(u"alternate-background-color: qlineargradient(spread:pad, x1:0.602, y1:0.4945, x2:0, y2:0.5, stop:0.392045 rgba(221, 221, 221, 255), stop:0.863636 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:9px;\n"
"border:2px solid rgb(0, 255, 255);\n"
"")
        self.captur = QPushButton(self.centralwidget)
        self.captur.setObjectName(u"captur")
        self.captur.setGeometry(QRect(230, 390, 121, 51))
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.captur.setFont(font)
        self.captur.setCursor(QCursor(Qt.PointingHandCursor))
        self.captur.setMouseTracking(True)
        self.captur.setAutoFillBackground(False)
        self.captur.setStyleSheet(u"alternate-background-color: qlineargradient(spread:pad, x1:0.602, y1:0.4945, x2:0, y2:0.5, stop:0.392045 rgba(221, 221, 221, 255), stop:0.863636 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:9px;\n"
"border:2px solid rgb(0, 255, 255);\n"
"")
        self.captur.setCheckable(False)
        self.captur.setAutoDefault(False)
        self.captur.setFlat(False)
        self.egister_bot = QPushButton(self.centralwidget)
        self.egister_bot.setObjectName(u"egister_bot")
        self.egister_bot.setGeometry(QRect(390, 530, 221, 41))
        self.egister_bot.setFont(font)
        self.egister_bot.setCursor(QCursor(Qt.PointingHandCursor))
        self.egister_bot.setMouseTracking(True)
        self.egister_bot.setAutoFillBackground(False)
        self.egister_bot.setStyleSheet(u"background-color: rgb(32, 221, 127);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:9px;\n"
"border:2px solid rgb(0, 255, 255);\n"
"")
        self.egister_bot.setCheckable(False)
        self.egister_bot.setAutoDefault(False)
        self.egister_bot.setFlat(False)
        self.showimg_register = QLabel(self.centralwidget)
        self.showimg_register.setObjectName(u"showimg_register")
        self.showimg_register.setGeometry(QRect(790, 200, 231, 201))
        self.showimg_register.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(204, 34, 51, 0));")
        self.showimg_register.setTextFormat(Qt.AutoText)
        self.showimg_register.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(525, 120, 171, 81))
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(204, 34, 51, 0));\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.ghos_text = QLabel(self.centralwidget)
        self.ghos_text.setObjectName(u"ghos_text")
        self.ghos_text.setGeometry(QRect(440, 450, 231, 31))
        self.ghos_text.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(204, 34, 51, 0));\n"
"font: 13pt \"MS Shell Dlg 2\";")
        self.ghos_text.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(530, 40, 151, 81))
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(204, 34, 51, 0));\n"
"")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.start_webcam = QPushButton(self.centralwidget)
        self.start_webcam.setObjectName(u"start_webcam")
        self.start_webcam.setGeometry(QRect(90, 390, 111, 51))
        self.start_webcam.setCursor(QCursor(Qt.PointingHandCursor))
        self.start_webcam.setStyleSheet(u"alternate-background-color: qlineargradient(spread:pad, x1:0.602, y1:0.4945, x2:0, y2:0.5, stop:0.392045 rgba(221, 221, 221, 255), stop:0.863636 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:9px;\n"
"border:2px solid rgb(200, 255, 255);\n"
"")
        icon = QIcon()
        icon.addFile(u"icons/camera.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.start_webcam.setIcon(icon)
        self.start_webcam.setIconSize(QSize(32, 32))
        self.start_webcam.setAutoDefault(False)
        self.enter_name = QLineEdit(self.centralwidget)
        self.enter_name.setObjectName(u"enter_name")
        self.enter_name.setGeometry(QRect(679, 60, 231, 41))
        self.enter_name.setFont(font)
        self.enter_name.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 99), stop:1 rgba(255, 255, 255, 255));\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"gridline-color: rgb(255, 255, 255);\n"
"border-radius:9px;\n"
"border:2px solid rgb(0, 255, 255);\n"
"\n"
"")
        self.enter_name.setInputMethodHints(Qt.ImhNone)
        self.enter_name.setMaxLength(20)
        self.enter_name.setClearButtonEnabled(True)
        self.enter_id = QLineEdit(self.centralwidget)
        self.enter_id.setObjectName(u"enter_id")
        self.enter_id.setGeometry(QRect(680, 140, 231, 40))
        self.enter_id.setFont(font)
        self.enter_id.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 99), stop:1 rgba(255, 255, 255, 255));\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"gridline-color: rgb(255, 255, 255);\n"
"border-radius:9px;\n"
"border:2px solid rgb(0, 255, 255);\n"
"")
        self.enter_id.setInputMethodHints(Qt.ImhDigitsOnly)
        self.enter_id.setMaxLength(6)
        self.enter_id.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.enter_id.setClearButtonEnabled(True)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(570, 200, 101, 61))
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(204, 34, 51, 0));\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(552, 270, 121, 61))
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(204, 34, 51, 0));\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.rej_back = QPushButton(self.centralwidget)
        self.rej_back.setObjectName(u"rej_back")
        self.rej_back.setGeometry(QRect(0, 0, 80, 31))
        self.rej_back.setCursor(QCursor(Qt.PointingHandCursor))
        self.rej_back.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(76, 227, 227);\n"
"border-radius:9px;\n"
"border:2px solid rgb(255, 255, 255);")
        icon1 = QIcon()
        icon1.addFile(u"icons/reply-all.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.rej_back.setIcon(icon1)
        self.rej_back.setIconSize(QSize(23, 31))
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(551, 343, 121, 61))
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(204, 34, 51, 0));\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.label_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.rg_cm_patch = QComboBox(self.centralwidget)
        self.rg_cm_patch.addItem("")
        self.rg_cm_patch.addItem("")
        self.rg_cm_patch.addItem("")
        self.rg_cm_patch.addItem("")
        self.rg_cm_patch.addItem("")
        self.rg_cm_patch.addItem("")
        self.rg_cm_patch.addItem("")
        self.rg_cm_patch.addItem("")
        self.rg_cm_patch.addItem("")
        self.rg_cm_patch.setObjectName(u"rg_cm_patch")
        self.rg_cm_patch.setGeometry(QRect(690, 220, 69, 26))
        self.rg_cm_patch.setCursor(QCursor(Qt.PointingHandCursor))
        self.rg_cm_patch.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border:2px solid rgb(0, 255, 255);")
        self.rg_cm_spaf = QComboBox(self.centralwidget)
        self.rg_cm_spaf.addItem("")
        self.rg_cm_spaf.addItem("")
        self.rg_cm_spaf.addItem("")
        self.rg_cm_spaf.setObjectName(u"rg_cm_spaf")
        self.rg_cm_spaf.setGeometry(QRect(690, 290, 69, 26))
        self.rg_cm_spaf.setCursor(QCursor(Qt.PointingHandCursor))
        self.rg_cm_spaf.setStyleSheet(u"\n"
"background-color: rgb(255, 255, 255);\n"
"border:2px solid rgb(0, 255, 255);")
        self.rg_cm_smis = QComboBox(self.centralwidget)
        self.rg_cm_smis.addItem("")
        self.rg_cm_smis.addItem("")
        self.rg_cm_smis.addItem("")
        self.rg_cm_smis.addItem("")
        self.rg_cm_smis.addItem("")
        self.rg_cm_smis.addItem("")
        self.rg_cm_smis.addItem("")
        self.rg_cm_smis.addItem("")
        self.rg_cm_smis.addItem("")
        self.rg_cm_smis.addItem("")
        self.rg_cm_smis.addItem("")
        self.rg_cm_smis.addItem("")
        self.rg_cm_smis.setObjectName(u"rg_cm_smis")
        self.rg_cm_smis.setGeometry(QRect(692, 363, 69, 26))
        self.rg_cm_smis.setCursor(QCursor(Qt.PointingHandCursor))
        self.rg_cm_smis.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border:2px solid rgb(0, 255, 255);\n"
"")
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)

        self.captur.setDefault(False)
        self.egister_bot.setDefault(False)


        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"register", None))
        self.webcam_l.setText("")
        self.slect_img_bt.setText(QCoreApplication.translate("mainWindow", u"...", None))
        self.captur.setText(QCoreApplication.translate("mainWindow", u"Captur", None))
        self.egister_bot.setText(QCoreApplication.translate("mainWindow", u"Register", None))
        self.showimg_register.setText("")
        self.label_4.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">ID Number :</span></p></body></html>", None))
        self.ghos_text.setText(QCoreApplication.translate("mainWindow", u"Or chose Image From File >>", None))
        self.label_6.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>Enter Name :</p></body></html>", None))
        self.start_webcam.setText("")
        self.enter_name.setPlaceholderText(QCoreApplication.translate("mainWindow", u"           enter name", None))
        self.enter_id.setPlaceholderText(QCoreApplication.translate("mainWindow", u"         enter id of studant", None))
        self.label_7.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"right\">Patch No :</p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"right\">Departmant :</p></body></html>", None))
        self.rej_back.setText("")
        self.label_9.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"right\">Semster :</p></body></html>", None))
        self.rg_cm_patch.setItemText(0, QCoreApplication.translate("mainWindow", u"23", None))
        self.rg_cm_patch.setItemText(1, QCoreApplication.translate("mainWindow", u"24", None))
        self.rg_cm_patch.setItemText(2, QCoreApplication.translate("mainWindow", u"25", None))
        self.rg_cm_patch.setItemText(3, QCoreApplication.translate("mainWindow", u"26", None))
        self.rg_cm_patch.setItemText(4, QCoreApplication.translate("mainWindow", u"27", None))
        self.rg_cm_patch.setItemText(5, QCoreApplication.translate("mainWindow", u"28", None))
        self.rg_cm_patch.setItemText(6, QCoreApplication.translate("mainWindow", u"29", None))
        self.rg_cm_patch.setItemText(7, QCoreApplication.translate("mainWindow", u"30", None))
        self.rg_cm_patch.setItemText(8, QCoreApplication.translate("mainWindow", u"31", None))

        self.rg_cm_spaf.setItemText(0, QCoreApplication.translate("mainWindow", u"CS", None))
        self.rg_cm_spaf.setItemText(1, QCoreApplication.translate("mainWindow", u"SI", None))
        self.rg_cm_spaf.setItemText(2, QCoreApplication.translate("mainWindow", u"IT", None))

        self.rg_cm_smis.setItemText(0, QCoreApplication.translate("mainWindow", u"1", None))
        self.rg_cm_smis.setItemText(1, QCoreApplication.translate("mainWindow", u"2", None))
        self.rg_cm_smis.setItemText(2, QCoreApplication.translate("mainWindow", u"3", None))
        self.rg_cm_smis.setItemText(3, QCoreApplication.translate("mainWindow", u"4", None))
        self.rg_cm_smis.setItemText(4, QCoreApplication.translate("mainWindow", u"5", None))
        self.rg_cm_smis.setItemText(5, QCoreApplication.translate("mainWindow", u"6", None))
        self.rg_cm_smis.setItemText(6, QCoreApplication.translate("mainWindow", u"7", None))
        self.rg_cm_smis.setItemText(7, QCoreApplication.translate("mainWindow", u"8", None))
        self.rg_cm_smis.setItemText(8, QCoreApplication.translate("mainWindow", u"9", None))
        self.rg_cm_smis.setItemText(9, QCoreApplication.translate("mainWindow", u"10", None))
        self.rg_cm_smis.setItemText(10, QCoreApplication.translate("mainWindow", u"11", None))
        self.rg_cm_smis.setItemText(11, QCoreApplication.translate("mainWindow", u"12", None))

    # retranslateUi

