# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QTableView, QVBoxLayout,
    QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(737, 228)
        icon = QIcon()
        icon.addFile(u":/icons/icon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
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
"	font-size: 14px;\n"
"	border: 1px solid rgba(255, 255, 255, 70);\n"
"	gridline-color: rgba(255, 255, 255, 70);\n"
"	selection-color: white;\n"
"	selection-background-color: #3A3A3A;\n"
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
"	color"
                        ": white;\n"
"}\n"
"\n"
"QTimeEdit:hover {\n"
"	border: 2px solid rgba(255, 255, 255, 150);\n"
"}\n"
"\n"
"QTimeEdit:focus {\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_3.addWidget(self.pushButton_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableView.setDragDropOverwriteMode(True)
        self.tableView.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableView.horizontalHeader().setVisible(False)
        self.tableView.verticalHeader().setVisible(False)

        self.verticalLayout_3.addWidget(self.tableView)


        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Tg bot settings", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0439:", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u044e", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0441\u0442\u0438 \u0442\u043e\u043a\u0435\u043d", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0438\u043a\u0447\u0430 \u0431\u043e\u0442\u0430", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0431\u043e\u0442\u0430", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0439\u0442\u0438", None))
    # retranslateUi

