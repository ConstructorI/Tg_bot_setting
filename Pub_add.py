# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Pub_add.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QDialog,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTimeEdit, QVBoxLayout, QWidget)

class Ui_Pub_add(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(470, 350)
        Dialog.setMinimumSize(QSize(470, 350))
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
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pushButton_3 = QPushButton(Dialog)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMaximumSize(QSize(120, 16777215))

        self.verticalLayout.addWidget(self.pushButton_3)


        self.gridLayout.addLayout(self.verticalLayout, 2, 5, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_2.addWidget(self.lineEdit_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 20))

        self.verticalLayout_3.addWidget(self.label_4)

        self.plainTextEdit = QPlainTextEdit(Dialog)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(0, 80))

        self.verticalLayout_3.addWidget(self.plainTextEdit)

        self.checkBox = QCheckBox(Dialog)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMinimumSize(QSize(0, 20))

        self.verticalLayout_3.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(Dialog)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setMinimumSize(QSize(0, 20))

        self.verticalLayout_3.addWidget(self.checkBox_2)


        self.verticalLayout_2.addLayout(self.verticalLayout_3)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 3, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(120, 22))

        self.verticalLayout_6.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(120, 22))
        self.pushButton_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.verticalLayout_6.addWidget(self.pushButton_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 2, -1, -1)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.timeEdit = QTimeEdit(Dialog)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setMinimumSize(QSize(40, 0))
        self.timeEdit.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)

        self.verticalLayout_5.addWidget(self.timeEdit)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)


        self.gridLayout.addLayout(self.verticalLayout_6, 0, 5, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 3, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u041f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u044f", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u0430\u043d\u0430\u043b\u0430:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"ID:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u043e\u043c\u043f\u0442 \u0434\u043b\u044f \u0442\u0435\u043a\u0441\u0442\u0430:", None))
        self.checkBox.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0432\u043d\u0430\u0447\u0430\u043b\u0435 \u0440\u0430\u043d\u0434\u043e\u043c\u043d\u044b\u0439 \u0442\u0435\u043a\u0441\u0442", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0443", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0432\u0440\u0435\u043c\u044f", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0432\u0440\u0435\u043c\u044f", None))
    # retranslateUi

