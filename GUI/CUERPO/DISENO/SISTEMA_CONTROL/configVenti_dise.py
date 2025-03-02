# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'configVenti_dise.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.resize(371, 264)
        Dialog.setMouseTracking(False)
        Dialog.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/SISTEMA_CONTROL/IMAGENES/SISTEMA_CONTROL/IoT_domotica.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setWindowOpacity(1.0)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("background-color: #d8d8d8;\n"
"")
        Dialog.setWindowFilePath("")
        Dialog.setInputMethodHints(QtCore.Qt.ImhNone)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setMinimumSize(QtCore.QSize(0, 50))
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("TamilSangamMN")
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("  font-family: TamilSangamMN;\n"
"  font-size: 20px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setMinimumSize(QtCore.QSize(50, 50))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.dSB_tempActVenti = QtWidgets.QDoubleSpinBox(Dialog)
        self.dSB_tempActVenti.setMinimumSize(QtCore.QSize(90, 40))
        self.dSB_tempActVenti.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dSB_tempActVenti.setFont(font)
        self.dSB_tempActVenti.setStyleSheet("      QDoubleSpinBox {\n"
"            padding-right: 15px; /* make room for the arrows */\n"
"            border-image: url(:/PYQT5/IMAGENES/pyqt5/frame.png) 4;\n"
"            border-width: 3;\n"
"        }\n"
"        QDoubleSpinBox::up-button {\n"
"            subcontrol-origin: border;\n"
"            subcontrol-position: top right; /* position at the top right corner */\n"
"            width: 16px; /* 16 + 2*1px border-width = 15px padding + 3px parent border */\n"
"            border-image: url(:/PYQT5/IMAGENES/pyqt5/spinup.png) 1;\n"
"            border-width: 1px;\n"
"        }\n"
"        QDoubleSpinBox::up-button:hover {\n"
"            border-image: url(:/PYQT5/IMAGENES/pyqt5/spinup_hover.png) 1;\n"
"        }\n"
"        QDoubleSpinBox::up-button:pressed {\n"
"            border-image: url(:/PYQT5/IMAGENES/pyqt5/spinup_pressed.png) 1;\n"
"        }\n"
"        QDoubleSpinBox::up-arrow {\n"
"            image: url(:/PYQT5/IMAGENES/pyqt5/up_arrow.png);\n"
"            width: 7px;\n"
"            height: 7px;\n"
"        }\n"
"        QDoubleSpinBox::up-arrow:disabled, QSpinBox::up-arrow:off { /* off state when value is max */\n"
"        image: url(:/PYQT5/IMAGENES/pyqt5/up_arrow_disabled.png);\n"
"        }\n"
"        QDoubleSpinBox::down-button {\n"
"            subcontrol-origin: border;\n"
"            subcontrol-position: bottom right; /* position at bottom right corner */\n"
"            width: 16px;\n"
"            border-image: url(:/PYQT5/IMAGENES/pyqt5/spindown.png) 1;\n"
"            border-width: 1px;\n"
"            border-top-width: 0;\n"
"        }\n"
"        QDoubleSpinBox::down-button:hover {\n"
"            border-image: url(:/PYQT5/IMAGENES/pyqt5spindown_hover.png) 1;\n"
"        }\n"
"        QDoubleSpinBox::down-button:pressed {\n"
"            border-image: url(:/PYQT5/IMAGENES/pyqt5/spindown_pressed.png) 1;\n"
"        }\n"
"        QDoubleSpinBox::down-arrow {\n"
"            image: url(:/PYQT5/IMAGENES/pyqt5/down_arrow.png);\n"
"            width: 7px;\n"
"            height: 7px;\n"
"        }\n"
"        QDoubleSpinBox::down-arrow:disabled,QSpinBox::down-arrow:off { /* off state when value in min */\n"
"        image: url(:/images/down_arrow_disabled.png);\n"
"        }")
        self.dSB_tempActVenti.setAlignment(QtCore.Qt.AlignCenter)
        self.dSB_tempActVenti.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.dSB_tempActVenti.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.dSB_tempActVenti.setKeyboardTracking(True)
        self.dSB_tempActVenti.setProperty("showGroupSeparator", False)
        self.dSB_tempActVenti.setDecimals(1)
        self.dSB_tempActVenti.setProperty("value", 70.0)
        self.dSB_tempActVenti.setObjectName("dSB_tempActVenti")
        self.horizontalLayout.addWidget(self.dSB_tempActVenti)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setMinimumSize(QtCore.QSize(50, 50))
        self.label_2.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setMinimumSize(QtCore.QSize(70, 50))
        self.label_4.setMaximumSize(QtCore.QSize(100, 80))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setStyleSheet("border-image: url(:/SISTEMA_CONTROL/IMAGENES/SISTEMA_CONTROL/termo.png);")
        self.label_4.setText("")
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setMinimumSize(QtCore.QSize(50, 50))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setMinimumSize(QtCore.QSize(0, 10))
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setMinimumSize(QtCore.QSize(50, 50))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.btn_guardarSalir = QtWidgets.QPushButton(Dialog)
        self.btn_guardarSalir.setMinimumSize(QtCore.QSize(110, 40))
        self.btn_guardarSalir.setMaximumSize(QtCore.QSize(150, 50))
        self.btn_guardarSalir.setStyleSheet("QPushButton:hover {\n"
"    background-color: #DDE8E8; \n"
"    border: 1px solid #DAE7E7;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #DDE8E8; \n"
"    border: 1px solid #B1BCBC;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:#B8C0C0;\n"
"    border: 1px solid #B8C0C0;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(170, 170, 127)\n"
"}")
        self.btn_guardarSalir.setObjectName("btn_guardarSalir")
        self.horizontalLayout_2.addWidget(self.btn_guardarSalir)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setMinimumSize(QtCore.QSize(50, 50))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "RoniHernandez99/IoT_domotica "))
        self.label.setText(_translate("Dialog", "Prender ventilador a partir de los:"))
        self.label_2.setText(_translate("Dialog", "°[C]"))
        self.btn_guardarSalir.setText(_translate("Dialog", "GUARDAR"))

import IMAG_rc
