# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginnVkFEC.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)
import assets.resource_rc

class Ui_login_window(object):
    def setupUi(self, login_window):
        if not login_window.objectName():
            login_window.setObjectName(u"login_window")
        login_window.setEnabled(True)
        login_window.resize(493, 351)
        login_window.setStyleSheet(u"QMainWindow{\n"
"	background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(53, 132, 228, 255), stop:1 rgba(26, 95, 180, 255));\n"
"}\n"
"QPushButton{\n"
"color: black;\n"
"height: 30px;\n"
"max-width: 120px;\n"
"background-color: white;\n"
"border-radius: 8px;\n"
"text-transform: uppercase;\n"
"font-weight:  bold;\n"
"}\n"
"QPushButton#btn_close,QPushButton#btn_minimize{\n"
"border: none;\n"
"height: 20px;\n"
"width: 40px;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(11,52,227,0.6);\n"
"color: white;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(11,52,200,0.4)\n"
"}\n"
"QLabel{\n"
"color: white;\n"
"}\n"
"QLabel#img_logo {\n"
"max-height: 80px;\n"
"max-width: 80px;\n"
"}\n"
"QLabel#Textedit_user,QLabel#Textedit_password{\n"
"font-size: 20px;\n"
"}\n"
"QLineEdit{\n"
"max-width: 200px;\n"
"background-color: rgb(25,25,25);\n"
"color: white;\n"
"}")
        self.centralwidget = QWidget(login_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget{\n"
"border-radius: 8px;\n"
"border: 1px solid black;\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(53, 132, 228, 255), stop:1 rgba(26, 95, 180, 255));\n"
"}")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.FRAME_INPUT = QFrame(self.centralwidget)
        self.FRAME_INPUT.setObjectName(u"FRAME_INPUT")
        self.FRAME_INPUT.setFrameShape(QFrame.NoFrame)
        self.FRAME_INPUT.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.FRAME_INPUT)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.Textinput_user = QLineEdit(self.FRAME_INPUT)
        self.Textinput_user.setObjectName(u"Textinput_user")

        self.gridLayout_3.addWidget(self.Textinput_user, 0, 3, 1, 1)

        self.label = QLabel(self.FRAME_INPUT)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/icons/3367825261557740377.svg"))

        self.gridLayout_3.addWidget(self.label, 0, 2, 1, 1)

        self.Textinput_password = QLineEdit(self.FRAME_INPUT)
        self.Textinput_password.setObjectName(u"Textinput_password")
        self.Textinput_password.setEchoMode(QLineEdit.Password)

        self.gridLayout_3.addWidget(self.Textinput_password, 1, 3, 1, 1)

        self.Textedit_user = QLabel(self.FRAME_INPUT)
        self.Textedit_user.setObjectName(u"Textedit_user")

        self.gridLayout_3.addWidget(self.Textedit_user, 0, 1, 1, 1)

        self.label_2 = QLabel(self.FRAME_INPUT)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u":/icons/13072964931556282345.svg"))

        self.gridLayout_3.addWidget(self.label_2, 1, 2, 1, 1)

        self.Textedit_password = QLabel(self.FRAME_INPUT)
        self.Textedit_password.setObjectName(u"Textedit_password")

        self.gridLayout_3.addWidget(self.Textedit_password, 1, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(80, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_6, 0, 4, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(80, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_5, 0, 0, 1, 1)

        self.Textinput_loginmessage = QLabel(self.FRAME_INPUT)
        self.Textinput_loginmessage.setObjectName(u"Textinput_loginmessage")
        font = QFont()
        font.setPointSize(12)
        self.Textinput_loginmessage.setFont(font)
        self.Textinput_loginmessage.setStyleSheet(u"")
        self.Textinput_loginmessage.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.Textinput_loginmessage, 2, 1, 1, 3)


        self.gridLayout_2.addWidget(self.FRAME_INPUT, 1, 0, 1, 1)

        self.LOGO = QFrame(self.centralwidget)
        self.LOGO.setObjectName(u"LOGO")
        self.LOGO.setFrameShape(QFrame.NoFrame)
        self.LOGO.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.LOGO)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_3 = QSpacerItem(80, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 2, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(80, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 0, 0, 1, 1)

        self.btn_close = QPushButton(self.LOGO)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_close.setStyleSheet(u"")

        self.gridLayout.addWidget(self.btn_close, 0, 4, 1, 1)

        self.btn_minimize = QPushButton(self.LOGO)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_minimize.setStyleSheet(u"font-size: 20px")

        self.gridLayout.addWidget(self.btn_minimize, 0, 3, 1, 1)

        self.verticalSpacer = QSpacerItem(0, 80, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 1, 4, 1, 1)

        self.img_logo = QLabel(self.LOGO)
        self.img_logo.setObjectName(u"img_logo")
        self.img_logo.setStyleSheet(u"")
        self.img_logo.setPixmap(QPixmap(u":/icons/Money_bag.ico"))
        self.img_logo.setScaledContents(True)

        self.gridLayout.addWidget(self.img_logo, 1, 1, 1, 1)


        self.gridLayout_2.addWidget(self.LOGO, 0, 0, 1, 1)

        self.FRAME_BUTTONS = QFrame(self.centralwidget)
        self.FRAME_BUTTONS.setObjectName(u"FRAME_BUTTONS")
        self.FRAME_BUTTONS.setFrameShape(QFrame.NoFrame)
        self.FRAME_BUTTONS.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.FRAME_BUTTONS)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.btn_login = QPushButton(self.FRAME_BUTTONS)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_4.addWidget(self.btn_login, 0, 0, 1, 1)

        self.btn_quit = QPushButton(self.FRAME_BUTTONS)
        self.btn_quit.setObjectName(u"btn_quit")
        self.btn_quit.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_4.addWidget(self.btn_quit, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.FRAME_BUTTONS, 2, 0, 1, 1)

        self.FRAME_FOOTER = QFrame(self.centralwidget)
        self.FRAME_FOOTER.setObjectName(u"FRAME_FOOTER")
        self.FRAME_FOOTER.setFrameShape(QFrame.NoFrame)
        self.FRAME_FOOTER.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.FRAME_FOOTER)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_4 = QLabel(self.FRAME_FOOTER)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.gridLayout_2.addWidget(self.FRAME_FOOTER, 3, 0, 1, 1)

        login_window.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_minimize, self.btn_close)
        QWidget.setTabOrder(self.btn_close, self.Textinput_user)
        QWidget.setTabOrder(self.Textinput_user, self.Textinput_password)
        QWidget.setTabOrder(self.Textinput_password, self.btn_login)
        QWidget.setTabOrder(self.btn_login, self.btn_quit)

        self.retranslateUi(login_window)

        QMetaObject.connectSlotsByName(login_window)
    # setupUi

    def retranslateUi(self, login_window):
        login_window.setWindowTitle(QCoreApplication.translate("login_window", u"MainWindow", None))
        self.label.setText("")
        self.Textedit_user.setText(QCoreApplication.translate("login_window", u"Usu\u00e1rio:", None))
        self.label_2.setText("")
        self.Textedit_password.setText(QCoreApplication.translate("login_window", u"Senha:", None))
        self.Textinput_loginmessage.setText("")
        self.btn_close.setText(QCoreApplication.translate("login_window", u"X", None))
        self.btn_minimize.setText(QCoreApplication.translate("login_window", u"-", None))
        self.img_logo.setText("")
        self.btn_login.setText(QCoreApplication.translate("login_window", u"Login", None))
        self.btn_quit.setText(QCoreApplication.translate("login_window", u"Sair", None))
        self.label_4.setText(QCoreApplication.translate("login_window", u"Finnance Manager V2 \u00a9 Danilosv337 -  2023", None))
    # retranslateUi

