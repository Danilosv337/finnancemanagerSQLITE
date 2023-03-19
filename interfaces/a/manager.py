# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'finnanceRAqMHi.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import assets.resource_rc

class Ui_Manager(object):
    def setupUi(self, Manager):
        if not Manager.objectName():
            Manager.setObjectName(u"Manager")
        Manager.resize(774, 366)
        Manager.setStyleSheet(u"QLabel{\n"
"color: white;\n"
"}")
        self.centralwidget = QWidget(Manager)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setStyleSheet(u"QFrame#main_frame,QWidget#main_page,QWidget#main_page2{\n"
"border-radius: 30px;\n"
"border: .5px solid black;\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(53, 132, 228, 255), stop:1 rgba(26, 95, 180, 255));\n"
"}\n"
"")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.main_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.QStackedWidget = QStackedWidget(self.main_frame)
        self.QStackedWidget.setObjectName(u"QStackedWidget")
        self.QStackedWidget.setStyleSheet(u"border: none;")
        self.page_lucros = QWidget()
        self.page_lucros.setObjectName(u"page_lucros")
        self.horizontalLayout_7 = QHBoxLayout(self.page_lucros)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_11 = QFrame(self.page_lucros)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"QPushButton{\n"
"color: black;\n"
"background-color:white;\n"
"text-transform: uppercase;\n"
"min-width: 100px;\n"
"min-height: 30px;\n"
"border: 1px solid black;\n"
"border-radius: 8px;\n"
"}")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_11)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.Table_lucros = QTableWidget(self.frame_11)
        if (self.Table_lucros.columnCount() < 2):
            self.Table_lucros.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.Table_lucros.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.Table_lucros.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.Table_lucros.setObjectName(u"Table_lucros")

        self.gridLayout_9.addWidget(self.Table_lucros, 0, 0, 1, 1)

        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"QPushButton:hover{\n"
"background-color: rgba(11,52,227,0.6);\n"
"color: white;\n"
"}")
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_7)

        self.btn_add_page_lucros = QPushButton(self.frame_12)
        self.btn_add_page_lucros.setObjectName(u"btn_add_page_lucros")
        self.btn_add_page_lucros.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_8.addWidget(self.btn_add_page_lucros)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_11)

        self.btn_remove_page_lucros = QPushButton(self.frame_12)
        self.btn_remove_page_lucros.setObjectName(u"btn_remove_page_lucros")
        self.btn_remove_page_lucros.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_8.addWidget(self.btn_remove_page_lucros)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_12)


        self.gridLayout_9.addWidget(self.frame_12, 1, 0, 1, 1)


        self.horizontalLayout_7.addWidget(self.frame_11)

        self.QStackedWidget.addWidget(self.page_lucros)
        self.page_edit_lucros = QWidget()
        self.page_edit_lucros.setObjectName(u"page_edit_lucros")
        self.verticalLayout_5 = QVBoxLayout(self.page_edit_lucros)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_22 = QFrame(self.page_edit_lucros)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_22)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_23 = QFrame(self.frame_22)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setStyleSheet(u"background-color: rgb(25,25,25);\n"
"border-radius: 7px;")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_23 = QLabel(self.frame_23)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"max-height: 80px;\n"
"max-width: 80px;")
        self.label_23.setPixmap(QPixmap(u":/icons/aumentar.png"))
        self.label_23.setScaledContents(True)

        self.horizontalLayout_17.addWidget(self.label_23)


        self.verticalLayout_6.addWidget(self.frame_23)

        self.frame_24 = QFrame(self.frame_22)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setStyleSheet(u"QLineEdit{\n"
"min-width: 150px;\n"
"min-height: 25px;\n"
"color: black;\n"
"background-color: white;\n"
"border-radius: 5px;\n"
"}\n"
"QLabel{\n"
"font-size: 20px\n"
"}")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalSpacer_31 = QSpacerItem(45, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_31)

        self.label_21 = QLabel(self.frame_24)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_16.addWidget(self.label_21)

        self.EditText_desc_editlucro = QLineEdit(self.frame_24)
        self.EditText_desc_editlucro.setObjectName(u"EditText_desc_editlucro")

        self.horizontalLayout_16.addWidget(self.EditText_desc_editlucro)

        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_33)

        self.label_22 = QLabel(self.frame_24)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_16.addWidget(self.label_22)

        self.EditText_value_editlucro = QLineEdit(self.frame_24)
        self.EditText_value_editlucro.setObjectName(u"EditText_value_editlucro")

        self.horizontalLayout_16.addWidget(self.EditText_value_editlucro)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_32)


        self.verticalLayout_6.addWidget(self.frame_24)

        self.frame_26 = QFrame(self.frame_22)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.EditText_info_lucro = QLabel(self.frame_26)
        self.EditText_info_lucro.setObjectName(u"EditText_info_lucro")
        self.EditText_info_lucro.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.EditText_info_lucro)


        self.verticalLayout_6.addWidget(self.frame_26)

        self.frame_25 = QFrame(self.frame_22)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setStyleSheet(u"QPushButton{\n"
"background-color: white;\n"
"color: black;\n"
"text-transform: uppercase;\n"
"min-width: 100px;\n"
"min-height: 25px;\n"
"border: 2px solid black;\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(11,52,227,0.6);\n"
"color: white;\n"
"}\n"
"QFrame{\n"
"background-color: transparent;\n"
"}")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_25 = QSpacerItem(187, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_25)

        self.btn_update_page_editlucro = QPushButton(self.frame_25)
        self.btn_update_page_editlucro.setObjectName(u"btn_update_page_editlucro")
        self.btn_update_page_editlucro.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_14.addWidget(self.btn_update_page_editlucro)

        self.horizontalSpacer_26 = QSpacerItem(188, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_26)

        self.btn_return_page_editlucro = QPushButton(self.frame_25)
        self.btn_return_page_editlucro.setObjectName(u"btn_return_page_editlucro")
        self.btn_return_page_editlucro.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_14.addWidget(self.btn_return_page_editlucro)

        self.horizontalSpacer_27 = QSpacerItem(187, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_27)


        self.verticalLayout_6.addWidget(self.frame_25)


        self.verticalLayout_5.addWidget(self.frame_22)

        self.QStackedWidget.addWidget(self.page_edit_lucros)
        self.page_edit_gastos = QWidget()
        self.page_edit_gastos.setObjectName(u"page_edit_gastos")
        self.horizontalLayout_12 = QHBoxLayout(self.page_edit_gastos)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.frame_18 = QFrame(self.page_edit_gastos)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_18)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_19 = QFrame(self.frame_18)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setStyleSheet(u"background-color: rgb(25,25,25);\n"
"border-radius: 7px;")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_24 = QLabel(self.frame_19)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"max-height: 80px;\n"
"max-width: 80px;")
        self.label_24.setPixmap(QPixmap(u":/icons/financas.png"))
        self.label_24.setScaledContents(True)

        self.horizontalLayout_18.addWidget(self.label_24)


        self.verticalLayout_4.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.frame_18)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setStyleSheet(u"QLineEdit{\n"
"min-width: 150px;\n"
"min-height: 25px;\n"
"color: black;\n"
"background-color: white;\n"
"border-radius: 5px;\n"
"}\n"
"QLabel{\n"
"font-size: 20px\n"
"}")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_29)

        self.label_19 = QLabel(self.frame_20)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_15.addWidget(self.label_19)

        self.EditText_desc_editgasto = QLineEdit(self.frame_20)
        self.EditText_desc_editgasto.setObjectName(u"EditText_desc_editgasto")

        self.horizontalLayout_15.addWidget(self.EditText_desc_editgasto)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_28)

        self.label_20 = QLabel(self.frame_20)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_15.addWidget(self.label_20)

        self.EditText_value_editgasto = QLineEdit(self.frame_20)
        self.EditText_value_editgasto.setObjectName(u"EditText_value_editgasto")

        self.horizontalLayout_15.addWidget(self.EditText_value_editgasto)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_30)


        self.verticalLayout_4.addWidget(self.frame_20)

        self.frame_27 = QFrame(self.frame_18)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.EditText_info_gasto = QLabel(self.frame_27)
        self.EditText_info_gasto.setObjectName(u"EditText_info_gasto")
        self.EditText_info_gasto.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.EditText_info_gasto)


        self.verticalLayout_4.addWidget(self.frame_27)

        self.frame_21 = QFrame(self.frame_18)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setStyleSheet(u"QPushButton{\n"
"background-color: white;\n"
"color: black;\n"
"text-transform: uppercase;\n"
"min-width: 100px;\n"
"min-height: 25px;\n"
"border: 2px solid black;\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(11,52,227,0.6);\n"
"color: white;\n"
"}\n"
"QFrame{\n"
"background-color: transparent;\n"
"}")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_22 = QSpacerItem(187, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_22)

        self.btn_update_page_editgasto = QPushButton(self.frame_21)
        self.btn_update_page_editgasto.setObjectName(u"btn_update_page_editgasto")
        self.btn_update_page_editgasto.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_13.addWidget(self.btn_update_page_editgasto)

        self.horizontalSpacer_23 = QSpacerItem(188, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_23)

        self.btn_return_page_editgasto = QPushButton(self.frame_21)
        self.btn_return_page_editgasto.setObjectName(u"btn_return_page_editgasto")
        self.btn_return_page_editgasto.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_13.addWidget(self.btn_return_page_editgasto)

        self.horizontalSpacer_24 = QSpacerItem(187, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_24)


        self.verticalLayout_4.addWidget(self.frame_21)


        self.horizontalLayout_12.addWidget(self.frame_18)

        self.QStackedWidget.addWidget(self.page_edit_gastos)
        self.page_edit_salario = QWidget()
        self.page_edit_salario.setObjectName(u"page_edit_salario")
        self.page_edit_salario.setStyleSheet(u"color: white;")
        self.verticalLayout_2 = QVBoxLayout(self.page_edit_salario)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_14 = QFrame(self.page_edit_salario)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setStyleSheet(u"border: none;\n"
"")
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_3 = QVBoxLayout(self.frame_14)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"background-color: rgb(25,25,25);\n"
"border-radius: 10px;\n"
"color: green;")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_15 = QLabel(self.frame_15)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"max-width: 60px;\n"
"max-height: 60px;")
        self.label_15.setPixmap(QPixmap(u":/icons/carteira.png"))
        self.label_15.setScaledContents(True)

        self.horizontalLayout_9.addWidget(self.label_15)

        self.label_16 = QLabel(self.frame_15)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"font-size: 35px;\n"
"font-weight: bold ;")

        self.horizontalLayout_9.addWidget(self.label_16)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_15)

        self.EditText_current_salario2 = QLabel(self.frame_15)
        self.EditText_current_salario2.setObjectName(u"EditText_current_salario2")
        self.EditText_current_salario2.setStyleSheet(u"font-size: 30px;")

        self.horizontalLayout_9.addWidget(self.EditText_current_salario2)


        self.verticalLayout_3.addWidget(self.frame_15)

        self.frame_17 = QFrame(self.frame_14)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_16)

        self.label_18 = QLabel(self.frame_17)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"font-size: 25px;")

        self.horizontalLayout_10.addWidget(self.label_18)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_17)

        self.EditText_salario_update = QLineEdit(self.frame_17)
        self.EditText_salario_update.setObjectName(u"EditText_salario_update")
        self.EditText_salario_update.setStyleSheet(u"min-width: 150px;\n"
"min-height: 25px;\n"
"color: black;\n"
"background-color: white;\n"
"border-radius: 5px;")
        self.EditText_salario_update.setAlignment(Qt.AlignCenter)
        self.EditText_salario_update.setReadOnly(False)

        self.horizontalLayout_10.addWidget(self.EditText_salario_update)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_18)


        self.verticalLayout_3.addWidget(self.frame_17)

        self.frame_16 = QFrame(self.frame_14)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"QPushButton{\n"
"background-color: white;\n"
"color: black;\n"
"text-transform: uppercase;\n"
"min-width: 100px;\n"
"min-height: 25px;\n"
"border: 2px solid black;\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(11,52,227,0.6);\n"
"color: white;\n"
"}\n"
"QFrame{\n"
"background-color: transparent;\n"
"}")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_19)

        self.btn_update_page_editsalario = QPushButton(self.frame_16)
        self.btn_update_page_editsalario.setObjectName(u"btn_update_page_editsalario")
        self.btn_update_page_editsalario.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_11.addWidget(self.btn_update_page_editsalario)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_20)

        self.btn_return_page_editsalario = QPushButton(self.frame_16)
        self.btn_return_page_editsalario.setObjectName(u"btn_return_page_editsalario")
        self.btn_return_page_editsalario.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_11.addWidget(self.btn_return_page_editsalario)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_21)


        self.verticalLayout_3.addWidget(self.frame_16)


        self.verticalLayout_2.addWidget(self.frame_14)

        self.QStackedWidget.addWidget(self.page_edit_salario)
        self.main_page = QWidget()
        self.main_page.setObjectName(u"main_page")
        self.main_page.setStyleSheet(u"border:none")
        self.gridLayout_2 = QGridLayout(self.main_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_8 = QFrame(self.main_page)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"border: none;")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_8)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_10 = QFrame(self.frame_8)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"QPushButton{\n"
"background-color: white;\n"
"color: black;\n"
"text-transform: uppercase;\n"
"min-width: 100px;\n"
"min-height: 25px;\n"
"border: 2px solid black;\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(11,52,227,0.6);\n"
"color: white;\n"
"}\n"
"")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.btn_refresh_page_home = QPushButton(self.frame_10)
        self.btn_refresh_page_home.setObjectName(u"btn_refresh_page_home")
        self.btn_refresh_page_home.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_5.addWidget(self.btn_refresh_page_home)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.btn_quit_main_home = QPushButton(self.frame_10)
        self.btn_quit_main_home.setObjectName(u"btn_quit_main_home")
        self.btn_quit_main_home.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_5.addWidget(self.btn_quit_main_home)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)


        self.gridLayout_3.addWidget(self.frame_10, 1, 0, 1, 3)

        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_5 = QFrame(self.frame_9)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: rgb(25, 25, 25);\n"
"color: green;\n"
"border-radius: 10px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-size: 20px;\n"
"font-weight: bold ;")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label, 1, 0, 1, 3)

        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setCursor(QCursor(Qt.CrossCursor))
        self.label_2.setStyleSheet(u"max-height: 40px;\n"
"max-width: 40px")
        self.label_2.setPixmap(QPixmap(u":/icons/carteira.png"))
        self.label_2.setScaledContents(True)

        self.gridLayout_4.addWidget(self.label_2, 2, 0, 1, 1)

        self.EditText_current_salario_home = QLabel(self.frame_5)
        self.EditText_current_salario_home.setObjectName(u"EditText_current_salario_home")
        self.EditText_current_salario_home.setStyleSheet(u"font-size: 15px")

        self.gridLayout_4.addWidget(self.EditText_current_salario_home, 2, 2, 1, 1)


        self.horizontalLayout_3.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_9)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color: rgb(25, 25, 25);\n"
"color: green;\n"
"border-radius: 10px;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"max-height: 40px;\n"
"max-width: 40px")
        self.label_5.setPixmap(QPixmap(u":/icons/aumentar.png"))
        self.label_5.setScaledContents(True)

        self.gridLayout_6.addWidget(self.label_5, 3, 0, 1, 1)

        self.EditText_current_lucros_home = QLabel(self.frame_6)
        self.EditText_current_lucros_home.setObjectName(u"EditText_current_lucros_home")
        self.EditText_current_lucros_home.setStyleSheet(u"font-size: 15px")

        self.gridLayout_6.addWidget(self.EditText_current_lucros_home, 3, 2, 1, 1)

        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font-size: 20px;\n"
"font-weight: bold;")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_4, 2, 0, 1, 3)


        self.horizontalLayout_3.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_9)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"background-color: rgb(25, 25, 25);\n"
"color: red;\n"
"border-radius: 10px;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_7)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.EditText_current_gasto_home = QLabel(self.frame_7)
        self.EditText_current_gasto_home.setObjectName(u"EditText_current_gasto_home")
        self.EditText_current_gasto_home.setStyleSheet(u"font-size: 15px")

        self.gridLayout_5.addWidget(self.EditText_current_gasto_home, 2, 2, 1, 1)

        self.label_7 = QLabel(self.frame_7)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"font-size: 20px;\n"
"font-weight: bold;")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_7, 1, 0, 1, 3)

        self.label_8 = QLabel(self.frame_7)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"max-height: 40px;\n"
"max-width: 40px")
        self.label_8.setPixmap(QPixmap(u":/icons/financas.png"))
        self.label_8.setScaledContents(True)

        self.gridLayout_5.addWidget(self.label_8, 2, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.frame_7)

        self.frame_13 = QFrame(self.frame_9)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"background-color: rgb(25, 25, 25);\n"
"color: green;\n"
"border-radius: 10px;")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_13)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_11 = QLabel(self.frame_13)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"font-size: 20px;\n"
"font-weight: bold;")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_11, 0, 0, 1, 3)

        self.EditText_current_credit_home = QLabel(self.frame_13)
        self.EditText_current_credit_home.setObjectName(u"EditText_current_credit_home")
        self.EditText_current_credit_home.setStyleSheet(u"font-size: 15px")

        self.gridLayout_10.addWidget(self.EditText_current_credit_home, 1, 2, 1, 1)

        self.label_12 = QLabel(self.frame_13)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"max-height: 40px;\n"
"max-width: 40px")
        self.label_12.setPixmap(QPixmap(u":/icons/Money_bag.ico"))
        self.label_12.setScaledContents(True)

        self.gridLayout_10.addWidget(self.label_12, 1, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.frame_13)


        self.gridLayout_3.addWidget(self.frame_9, 0, 0, 1, 3)


        self.gridLayout_2.addWidget(self.frame_8, 0, 0, 1, 1)

        self.QStackedWidget.addWidget(self.main_page)
        self.page_gastos = QWidget()
        self.page_gastos.setObjectName(u"page_gastos")
        self.gridLayout_7 = QGridLayout(self.page_gastos)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.frame = QFrame(self.page_gastos)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.table_gastos = QTableWidget(self.frame)
        if (self.table_gastos.columnCount() < 2):
            self.table_gastos.setColumnCount(2)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_gastos.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_gastos.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        self.table_gastos.setObjectName(u"table_gastos")
        self.table_gastos.setLayoutDirection(Qt.LeftToRight)
        self.table_gastos.setAutoFillBackground(False)
        self.table_gastos.setFrameShape(QFrame.NoFrame)
        self.table_gastos.setFrameShadow(QFrame.Sunken)
        self.table_gastos.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.table_gastos.setSelectionMode(QAbstractItemView.NoSelection)
        self.table_gastos.setTextElideMode(Qt.ElideRight)
        self.table_gastos.setShowGrid(True)
        self.table_gastos.setGridStyle(Qt.SolidLine)
        self.table_gastos.verticalHeader().setStretchLastSection(False)

        self.gridLayout_8.addWidget(self.table_gastos, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.page_gastos)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QPushButton{\n"
"color: black;\n"
"background-color:white;\n"
"text-transform: uppercase;\n"
"min-width: 100px;\n"
"min-height: 30px;\n"
"border: 1px solid black;\n"
"border-radius: 8px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(11,52,227,0.6);\n"
"color: white;\n"
"}")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_9)

        self.btn_add_page_gastos = QPushButton(self.frame_2)
        self.btn_add_page_gastos.setObjectName(u"btn_add_page_gastos")
        self.btn_add_page_gastos.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_6.addWidget(self.btn_add_page_gastos)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_10)

        self.btn_remove_page_gastos = QPushButton(self.frame_2)
        self.btn_remove_page_gastos.setObjectName(u"btn_remove_page_gastos")
        self.btn_remove_page_gastos.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_6.addWidget(self.btn_remove_page_gastos)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_8)


        self.gridLayout_7.addWidget(self.frame_2, 1, 0, 1, 1)

        self.QStackedWidget.addWidget(self.page_gastos)

        self.gridLayout.addWidget(self.QStackedWidget, 1, 1, 1, 1)

        self.frame_3 = QFrame(self.main_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QFrame{\n"
"max-height:40px;\n"
"min-height: 40px;\n"
"\n"
"}\n"
"QPushButton{\n"
"min-height: 20px;\n"
"max-height: 20px;\n"
"background-color: white;\n"
"color: rgb(0, 0, 0);\n"
"font-size:20px\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(11,52,227,0.6);\n"
"color: white;\n"
"}")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_14)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_13)

        self.EditText_welcome = QLabel(self.frame_3)
        self.EditText_welcome.setObjectName(u"EditText_welcome")
        font = QFont()
        font.setFamilies([u"Serif"])
        font.setPointSize(13)
        font.setBold(False)
        font.setUnderline(False)
        self.EditText_welcome.setFont(font)

        self.horizontalLayout_2.addWidget(self.EditText_welcome)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_minimize = QPushButton(self.frame_3)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btn_minimize)

        self.btn_quit = QPushButton(self.frame_3)
        self.btn_quit.setObjectName(u"btn_quit")
        self.btn_quit.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btn_quit)


        self.gridLayout.addWidget(self.frame_3, 0, 1, 1, 1)

        self.frame_4 = QFrame(self.main_frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QFrame{\n"
"min-height: 40px;\n"
"max-height: 40px;\n"
"}\n"
"QLabel{\n"
"font-size: 15px;\n"
"}")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.label_10 = QLabel(self.frame_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.label_10)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.gridLayout.addWidget(self.frame_4, 2, 1, 1, 1)

        self.sidebar = QFrame(self.main_frame)
        self.sidebar.setObjectName(u"sidebar")
        self.sidebar.setStyleSheet(u"QFrame{\n"
"\n"
"background-color: rgb(25,25,25);\n"
"border-top-left-radius: 30px;\n"
"border-bottom-left-radius: 30px;\n"
"}\n"
"QPushButton{\n"
"border: none;\n"
"background-color: rgb(25,25,25);\n"
"min-width: 100%;\n"
"min-height: 60px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(53, 132, 228);\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"\n"
"}")
        self.sidebar.setFrameShape(QFrame.StyledPanel)
        self.sidebar.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.sidebar)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_home = QPushButton(self.sidebar)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/botao-home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home.setIcon(icon1)
        self.btn_home.setIconSize(QSize(25, 25))

        self.verticalLayout.addWidget(self.btn_home)

        self.btn_page_salario = QPushButton(self.sidebar)
        self.btn_page_salario.setObjectName(u"btn_page_salario")
        self.btn_page_salario.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_page_salario.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/carteira.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_page_salario.setIcon(icon2)
        self.btn_page_salario.setIconSize(QSize(25, 25))

        self.verticalLayout.addWidget(self.btn_page_salario)

        self.btn_page_lucros = QPushButton(self.sidebar)
        self.btn_page_lucros.setObjectName(u"btn_page_lucros")
        self.btn_page_lucros.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/aumentar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_page_lucros.setIcon(icon3)
        self.btn_page_lucros.setIconSize(QSize(25, 25))

        self.verticalLayout.addWidget(self.btn_page_lucros)

        self.btn_page_gastos = QPushButton(self.sidebar)
        self.btn_page_gastos.setObjectName(u"btn_page_gastos")
        self.btn_page_gastos.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/financas.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_page_gastos.setIcon(icon4)
        self.btn_page_gastos.setIconSize(QSize(25, 25))

        self.verticalLayout.addWidget(self.btn_page_gastos)


        self.gridLayout.addWidget(self.sidebar, 0, 0, 3, 1)


        self.horizontalLayout.addWidget(self.main_frame)

        Manager.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_home, self.btn_page_salario)
        QWidget.setTabOrder(self.btn_page_salario, self.btn_page_lucros)
        QWidget.setTabOrder(self.btn_page_lucros, self.btn_page_gastos)
        QWidget.setTabOrder(self.btn_page_gastos, self.pushButton)
        QWidget.setTabOrder(self.pushButton, self.btn_minimize)
        QWidget.setTabOrder(self.btn_minimize, self.btn_quit)
        QWidget.setTabOrder(self.btn_quit, self.btn_refresh_page_home)
        QWidget.setTabOrder(self.btn_refresh_page_home, self.btn_quit_main_home)
        QWidget.setTabOrder(self.btn_quit_main_home, self.Table_lucros)
        QWidget.setTabOrder(self.Table_lucros, self.btn_add_page_lucros)
        QWidget.setTabOrder(self.btn_add_page_lucros, self.btn_remove_page_lucros)
        QWidget.setTabOrder(self.btn_remove_page_lucros, self.table_gastos)
        QWidget.setTabOrder(self.table_gastos, self.btn_add_page_gastos)
        QWidget.setTabOrder(self.btn_add_page_gastos, self.btn_remove_page_gastos)
        QWidget.setTabOrder(self.btn_remove_page_gastos, self.EditText_salario_update)
        QWidget.setTabOrder(self.EditText_salario_update, self.EditText_desc_editlucro)
        QWidget.setTabOrder(self.EditText_desc_editlucro, self.EditText_value_editlucro)
        QWidget.setTabOrder(self.EditText_value_editlucro, self.btn_update_page_editlucro)
        QWidget.setTabOrder(self.btn_update_page_editlucro, self.btn_return_page_editlucro)
        QWidget.setTabOrder(self.btn_return_page_editlucro, self.EditText_desc_editgasto)
        QWidget.setTabOrder(self.EditText_desc_editgasto, self.EditText_value_editgasto)
        QWidget.setTabOrder(self.EditText_value_editgasto, self.btn_update_page_editgasto)
        QWidget.setTabOrder(self.btn_update_page_editgasto, self.btn_return_page_editgasto)
        QWidget.setTabOrder(self.btn_return_page_editgasto, self.btn_update_page_editsalario)
        QWidget.setTabOrder(self.btn_update_page_editsalario, self.btn_return_page_editsalario)

        self.retranslateUi(Manager)
        self.btn_quit.clicked.connect(Manager.close)
        self.btn_minimize.clicked.connect(Manager.showMinimized)

        self.QStackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Manager)
    # setupUi

    def retranslateUi(self, Manager):
        Manager.setWindowTitle(QCoreApplication.translate("Manager", u"MainWindow", None))
        ___qtablewidgetitem = self.Table_lucros.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Manager", u"Desc Lucro", None));
        ___qtablewidgetitem1 = self.Table_lucros.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Manager", u"Lucro", None));
        self.btn_add_page_lucros.setText(QCoreApplication.translate("Manager", u"Adicionar", None))
        self.btn_remove_page_lucros.setText(QCoreApplication.translate("Manager", u"Remover", None))
        self.label_23.setText("")
        self.label_21.setText(QCoreApplication.translate("Manager", u"Desc Lucro: ", None))
        self.label_22.setText(QCoreApplication.translate("Manager", u"Valor Lucro: ", None))
        self.EditText_info_lucro.setText("")
        self.btn_update_page_editlucro.setText(QCoreApplication.translate("Manager", u"Adicionar", None))
        self.btn_return_page_editlucro.setText(QCoreApplication.translate("Manager", u"Voltar", None))
        self.label_24.setText("")
        self.label_19.setText(QCoreApplication.translate("Manager", u"Desc Gasto: ", None))
        self.label_20.setText(QCoreApplication.translate("Manager", u"Valor Gasto:", None))
        self.EditText_info_gasto.setText("")
        self.btn_update_page_editgasto.setText(QCoreApplication.translate("Manager", u"Adicionar", None))
        self.btn_return_page_editgasto.setText(QCoreApplication.translate("Manager", u"Voltar", None))
        self.label_15.setText("")
        self.label_16.setText(QCoreApplication.translate("Manager", u"Sal\u00e1rio Atual:", None))
        self.EditText_current_salario2.setText(QCoreApplication.translate("Manager", u"R$ 00,00", None))
        self.label_18.setText(QCoreApplication.translate("Manager", u"Atualizar Sal\u00e1rio:", None))
        self.EditText_salario_update.setPlaceholderText(QCoreApplication.translate("Manager", u"00,00", None))
        self.btn_update_page_editsalario.setText(QCoreApplication.translate("Manager", u"Atualizar", None))
        self.btn_return_page_editsalario.setText(QCoreApplication.translate("Manager", u"Voltar", None))
        self.btn_refresh_page_home.setText(QCoreApplication.translate("Manager", u"Atualizar", None))
        self.btn_quit_main_home.setText(QCoreApplication.translate("Manager", u"Sair", None))
        self.label.setText(QCoreApplication.translate("Manager", u"Sal\u00e1rio", None))
        self.label_2.setText("")
        self.EditText_current_salario_home.setText(QCoreApplication.translate("Manager", u"R$ 00,00", None))
        self.label_5.setText("")
        self.EditText_current_lucros_home.setText(QCoreApplication.translate("Manager", u"R$ 00,00", None))
        self.label_4.setText(QCoreApplication.translate("Manager", u"Lucros", None))
        self.EditText_current_gasto_home.setText(QCoreApplication.translate("Manager", u"R$ 00,00", None))
        self.label_7.setText(QCoreApplication.translate("Manager", u"Gastos", None))
        self.label_8.setText("")
        self.label_11.setText(QCoreApplication.translate("Manager", u"Saldo Total", None))
        self.EditText_current_credit_home.setText(QCoreApplication.translate("Manager", u"R$ 00,00", None))
        self.label_12.setText("")
        ___qtablewidgetitem2 = self.table_gastos.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Manager", u"Descri\u00e7\u00e3o Gasto", None));
        ___qtablewidgetitem3 = self.table_gastos.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Manager", u"Valor Gasto", None));
        self.btn_add_page_gastos.setText(QCoreApplication.translate("Manager", u"Adicionar", None))
        self.btn_remove_page_gastos.setText(QCoreApplication.translate("Manager", u"Remover", None))
        self.pushButton.setText("")
        self.EditText_welcome.setText(QCoreApplication.translate("Manager", u"Seja Bem Vindo!, #User5284176#", None))
        self.btn_minimize.setText(QCoreApplication.translate("Manager", u"-", None))
        self.btn_quit.setText(QCoreApplication.translate("Manager", u"x", None))
        self.label_10.setText(QCoreApplication.translate("Manager", u"Finnance Manager V2 \u00a9 Danilosv337 -  2023", None))
        self.btn_home.setText("")
        self.btn_page_salario.setText("")
        self.btn_page_lucros.setText("")
        self.btn_page_gastos.setText("")
    # retranslateUi

