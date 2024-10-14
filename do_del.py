# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'do_del.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QWidget)
import res_rc

class Ui_Del(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(204, 64)
        Dialog.setMaximumSize(QSize(204, 64))
        icon = QIcon()
        icon.addFile(u":/icons/icon3.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(u"QWidget {\n"
"    background-color: #1E1E1E; /* \u041e\u0441\u043d\u043e\u0432\u043d\u043e\u0439 \u0444\u043e\u043d */\n"
"    color: #FFFFFF; /* \u0422\u0435\u043a\u0441\u0442 */\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #3A3A3A; /* \u041a\u043d\u043e\u043f\u043a\u0430 */\n"
"	border: 2px solid rgba(255, 255, 255, 70); /* \u0413\u0440\u0430\u043d\u0438\u0446\u0430 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #3A3A3A; /* \u041a\u043d\u043e\u043f\u043a\u0430 */\n"
"	border: 2px solid rgba(255, 255, 255, 150); /* \u0413\u0440\u0430\u043d\u0438\u0446\u0430 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1E1E1E; /* \u0424\u043e\u043d \u043a\u043d\u043e\u043f\u043a\u0438 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"	border: 2px solid rgb(255, 255, 255); /* \u0413\u0440\u0430\u043d\u0438\u0446\u0430 \u043a\u043d\u043e"
                        "\u043f\u043a\u0438 */\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	border: 2px solid rgba(255, 255, 255, 70);\n"
"	color: white;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgba(255, 255, 255, 150);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPlainTextEdit {\n"
"	border: 2px solid rgba(255, 255, 255, 70);\n"
"	color: white;\n"
"}\n"
"\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgba(255, 255, 255, 150);\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"}\n"
"\n"
"QTableView {\n"
"	font-size: 12px;\n"
"	border: none;\n"
"	gridline-color: rgba(255, 255, 255, 70);\n"
"	selection-color: rgb(253, 252, 76);\n"
"	selection-background-color: rgb(255, 145, 132);\n"
"}\n"
"\n"
"QTableWiew:section {\n"
"	border: none;\n"
"	padding-bottom: 5px;\n"
"	padding-top: 5px;\n"
"}\n"
"\n"
"QTableWiew:item {\n"
"	border-style: none;\n"
"}\n"
"\n"
"QTimeEdit {\n"
"	border: 2px solid rgba(255, 255, 255, 70);\n"
"	color: whit"
                        "e;\n"
"}\n"
"\n"
"QTimeEdit:hover {\n"
"	border: 2px solid rgba(255, 255, 255, 150);\n"
"}\n"
"\n"
"QTimeEdit:focus {\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"}")
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0423\u0434\u0430\u043b\u0435\u043d\u0438\u0435", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u044e \u0438\u0437 \u0433\u0440\u0430\u0444\u0438\u043a\u0430?", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\u041d\u0435\u0442", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430", None))
    # retranslateUi

