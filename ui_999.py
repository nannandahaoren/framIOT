# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '999bciXgz.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1361, 834)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"	color:#000;\n"
"	border:none;\n"
"	\n"
"}\n"
"\n"
"#centralWidget{\n"
"\n"
"	background-color: rgb(239, 249, 254);\n"
"}\n"
"\n"
"#QLineEdit{\n"
"	\n"
"	background: transparent;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leftMenu = QWidget(self.centralwidget)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setStyleSheet(u"background-color: rgb(107, 160, 200);")
        self.verticalLayout_2 = QVBoxLayout(self.leftMenu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.leftMenu)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(230, 0))
        self.frame.setMaximumSize(QSize(230, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, 0, -1)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 14, 0, 0)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(36, 36))
        self.label.setMaximumSize(QSize(36, 36))
        self.label.setPixmap(QPixmap(u":/pic/imag/icon.jpg"))
        self.label.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.label)

        self.horizontalSpacer_3 = QSpacerItem(6, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)

        self.widget_34 = QWidget(self.frame_2)
        self.widget_34.setObjectName(u"widget_34")
        self.verticalLayout_6 = QVBoxLayout(self.widget_34)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 15, 15, -1)
        self.label_3 = QLabel(self.widget_34)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(120, 26))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_3)

        self.label_4 = QLabel(self.widget_34)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(120, 26))
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_4)


        self.horizontalLayout_8.addWidget(self.widget_34)

        self.horizontalSpacer_4 = QSpacerItem(10, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, -1)
        self.verticalSpacer_10 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_10)

        self.btn1 = QPushButton(self.frame_4)
        self.btn1.setObjectName(u"btn1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn1.sizePolicy().hasHeightForWidth())
        self.btn1.setSizePolicy(sizePolicy1)
        self.btn1.setMinimumSize(QSize(120, 56))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.btn1.setFont(font1)
        self.btn1.setStyleSheet(u"\n"
"#btn1{\n"
"	background-color: #fefeff;\n"
"padding: 5px;\n"
"text-align: left;\n"
"border-top-left-radius: 10px ;\n"
"border-bottom-left-radius: 10px ;\n"
"\n"
"}\n"
"\n"
"#btn1:pressed {\n"
"	background-color: rgb(37, 150, 190);\n"
"	padding-top:3px;\n"
"	padding-left:3px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/pic/imag/garden.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn1.setIcon(icon)
        self.btn1.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.btn1)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.btn2 = QPushButton(self.frame_4)
        self.btn2.setObjectName(u"btn2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn2.sizePolicy().hasHeightForWidth())
        self.btn2.setSizePolicy(sizePolicy2)
        self.btn2.setMinimumSize(QSize(120, 56))
        self.btn2.setFont(font1)
        self.btn2.setStyleSheet(u"#btn2{\n"
"	background-color: #fefeff;\n"
"padding: 5px;\n"
"text-align: left;\n"
"border-top-left-radius: 10px ;\n"
"border-bottom-left-radius: 10px ;\n"
"\n"
"}\n"
"\n"
"\n"
"#btn2:pressed {\n"
"	background-color: rgb(37, 150, 190);\n"
"	padding-top:3px;\n"
"	padding-left:3px;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/pic/imag/hardware.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn2.setIcon(icon1)
        self.btn2.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.btn2)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_4)

        self.btn3 = QPushButton(self.frame_4)
        self.btn3.setObjectName(u"btn3")
        sizePolicy2.setHeightForWidth(self.btn3.sizePolicy().hasHeightForWidth())
        self.btn3.setSizePolicy(sizePolicy2)
        self.btn3.setMinimumSize(QSize(120, 56))
        self.btn3.setFont(font1)
        self.btn3.setStyleSheet(u"#btn3{\n"
"	background-color: #fefeff;\n"
"padding: 5px;\n"
"text-align: left;\n"
"border-top-left-radius: 10px ;\n"
"border-bottom-left-radius: 10px ;\n"
"\n"
"}\n"
"\n"
"\n"
"#btn3:pressed {\n"
"	background-color: rgb(37, 150, 190);\n"
"	padding-top:3px;\n"
"	padding-left:3px;\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/pic/imag/seting.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn3.setIcon(icon2)
        self.btn3.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.btn3)

        self.verticalSpacer_8 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_8)

        self.btn5 = QPushButton(self.frame_4)
        self.btn5.setObjectName(u"btn5")
        sizePolicy2.setHeightForWidth(self.btn5.sizePolicy().hasHeightForWidth())
        self.btn5.setSizePolicy(sizePolicy2)
        self.btn5.setMinimumSize(QSize(120, 56))
        self.btn5.setFont(font1)
        self.btn5.setStyleSheet(u"#btn5{\n"
"	background-color: #fefeff;\n"
"padding: 5px;\n"
"text-align: left;\n"
"\n"
"border-top-left-radius: 10px ;\n"
"border-bottom-left-radius: 10px ;\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"#btn5:pressed {\n"
"	background-color: rgb(37, 150, 190);\n"
"	padding-top:3px;\n"
"	padding-left:3px;\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/pic/imag/chongwu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn5.setIcon(icon3)
        self.btn5.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.btn5)

        self.verticalSpacer_9 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_9)

        self.btn4 = QPushButton(self.frame_4)
        self.btn4.setObjectName(u"btn4")
        sizePolicy2.setHeightForWidth(self.btn4.sizePolicy().hasHeightForWidth())
        self.btn4.setSizePolicy(sizePolicy2)
        self.btn4.setMinimumSize(QSize(120, 56))
        self.btn4.setFont(font1)
        self.btn4.setStyleSheet(u"#btn4{\n"
"	background-color: #fefeff;\n"
"padding: 5px;\n"
"text-align: left;\n"
"border-top-left-radius: 10px ;\n"
"border-bottom-left-radius: 10px ;\n"
"\n"
"}\n"
"\n"
"\n"
"#btn4:pressed {\n"
"	background-color: rgb(37, 150, 190);\n"
"	padding-top:3px;\n"
"	padding-left:3px;\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/pic/imag/wuren.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn4.setIcon(icon4)
        self.btn4.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.btn4)

        self.verticalSpacer_15 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_15)

        self.btn6 = QPushButton(self.frame_4)
        self.btn6.setObjectName(u"btn6")
        sizePolicy2.setHeightForWidth(self.btn6.sizePolicy().hasHeightForWidth())
        self.btn6.setSizePolicy(sizePolicy2)
        self.btn6.setMinimumSize(QSize(120, 56))
        self.btn6.setFont(font1)
        self.btn6.setStyleSheet(u"#btn6{\n"
"	background-color: #fefeff;\n"
"padding: 5px;\n"
"text-align: left;\n"
"border-top-left-radius: 10px ;\n"
"border-bottom-left-radius: 10px ;\n"
"\n"
"}\n"
"\n"
"\n"
"#btn6:pressed {\n"
"	background-color: rgb(37, 150, 190);\n"
"	padding-top:3px;\n"
"	padding-left:3px;\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/pic/imag/aboutus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn6.setIcon(icon5)
        self.btn6.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.btn6)


        self.verticalLayout_4.addWidget(self.frame_4)

        self.verticalSpacer = QSpacerItem(20, 60, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.verticalLayout_3.addWidget(self.frame_3)


        self.verticalLayout_2.addWidget(self.frame)


        self.horizontalLayout.addWidget(self.leftMenu)

        self.mainBody = QWidget(self.centralwidget)
        self.mainBody.setObjectName(u"mainBody")
        self.mainBody.setMinimumSize(QSize(120, 56))
        self.mainBody.setMaximumSize(QSize(16777207, 16777215))
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setWeight(75)
        self.mainBody.setFont(font2)
        self.mainBody.setStyleSheet(u"background-color: rgb(254, 254, 255);")
        self.verticalLayout = QVBoxLayout(self.mainBody)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.headerFrame = QWidget(self.mainBody)
        self.headerFrame.setObjectName(u"headerFrame")
        self.horizontalLayout_2 = QHBoxLayout(self.headerFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.headerFrame)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.horizontalLayout_2.addWidget(self.widget, 0, Qt.AlignLeft)

        self.widget_2 = QWidget(self.headerFrame)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(260, 0))
        self.widget_2.setMaximumSize(QSize(500, 16777215))
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.searchFrame = QFrame(self.widget_2)
        self.searchFrame.setObjectName(u"searchFrame")
        self.searchFrame.setMinimumSize(QSize(220, 50))
        self.searchFrame.setStyleSheet(u"#searchFrame{\n"
"\n"
"border-radius: 10px;\n"
"border: 2px solid #2596be;\n"
"\n"
"}\n"
"")
        self.searchFrame.setFrameShape(QFrame.StyledPanel)
        self.searchFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.searchFrame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.searchFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(30, 30))
        self.label_2.setMaximumSize(QSize(30, 30))
        self.label_2.setPixmap(QPixmap(u":/img/imag/blue/search.svg"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.searchFrame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(260, 46))
        self.lineEdit.setStyleSheet(u"#lineEdit{\n"
"	\n"
"	background: transparent;\n"
"}")

        self.horizontalLayout_5.addWidget(self.lineEdit)


        self.horizontalLayout_4.addWidget(self.searchFrame)


        self.horizontalLayout_2.addWidget(self.widget_2, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_7)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.B1 = QPushButton(self.headerFrame)
        self.B1.setObjectName(u"B1")
        self.B1.setMinimumSize(QSize(160, 50))
        font3 = QFont()
        font3.setPointSize(13)
        font3.setBold(True)
        font3.setWeight(75)
        self.B1.setFont(font3)
        self.B1.setStyleSheet(u"#B1{\n"
"	background-color: rgb(110, 209, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border:1px solid rgb(0,0,0);\n"
"	border-radius:10px;\n"
"	Width:60;\n"
"Height:36\n"
"}\n"
"#B1:hover {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"#B1:pressed {\n"
"	padding-top:3px;\n"
"	padding-left:3px;\n"
"}\n"
"\n"
"\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/pic/imag/time.png", QSize(), QIcon.Normal, QIcon.Off)
        self.B1.setIcon(icon6)
        self.B1.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.B1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.B2 = QPushButton(self.headerFrame)
        self.B2.setObjectName(u"B2")
        self.B2.setMinimumSize(QSize(160, 50))
        self.B2.setFont(font3)
        self.B2.setStyleSheet(u"#B2{\n"
"	background-color: rgb(110, 209, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border:1px solid rgb(0,0,0);\n"
"	border-radius:10px;\n"
"	Width:60;\n"
"Height:36\n"
"}\n"
"#B2:hover {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"#B2:pressed {\n"
"	padding-top:3px;\n"
"	padding-left:3px;\n"
"}\n"
"\n"
"\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/pic/imag/wether.png", QSize(), QIcon.Normal, QIcon.Off)
        self.B2.setIcon(icon7)
        self.B2.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.B2)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_9)

        self.B3 = QPushButton(self.headerFrame)
        self.B3.setObjectName(u"B3")
        self.B3.setMinimumSize(QSize(160, 50))
        self.B3.setFont(font3)
        self.B3.setStyleSheet(u"#B3{\n"
"	background-color: rgb(110, 209, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border:1px solid rgb(0,0,0);\n"
"	border-radius:10px;\n"
"	Width:60;\n"
"Height:36\n"
"}\n"
"#B3:hover {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"#B3:pressed {\n"
"	padding-top:3px;\n"
"	padding-left:3px;\n"
"}\n"
"\n"
"\n"
"")
        icon8 = QIcon()
        icon8.addFile(u":/pic/imag/7.png", QSize(), QIcon.Normal, QIcon.Off)
        self.B3.setIcon(icon8)
        self.B3.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.B3)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_10)

        self.B4 = QPushButton(self.headerFrame)
        self.B4.setObjectName(u"B4")
        self.B4.setMinimumSize(QSize(160, 50))
        self.B4.setFont(font3)
        self.B4.setStyleSheet(u"#B4{\n"
"	background-color: rgb(110, 209, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border:1px solid rgb(0,0,0);\n"
"	border-radius:10px;\n"
"	Width:60;\n"
"Height:36\n"
"}\n"
"#B4:hover {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"#B4:pressed {\n"
"	padding-top:3px;\n"
"	padding-left:3px;\n"
"}\n"
"\n"
"\n"
"")
        icon9 = QIcon()
        icon9.addFile(u":/pic/imag/pest.png", QSize(), QIcon.Normal, QIcon.Off)
        self.B4.setIcon(icon9)
        self.B4.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.B4)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_8)

        self.accountBtn = QPushButton(self.headerFrame)
        self.accountBtn.setObjectName(u"accountBtn")
        icon10 = QIcon()
        icon10.addFile(u":/pic/imag/user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.accountBtn.setIcon(icon10)
        self.accountBtn.setIconSize(QSize(36, 36))

        self.horizontalLayout_2.addWidget(self.accountBtn)

        self.label_5 = QLabel(self.headerFrame)
        self.label_5.setObjectName(u"label_5")
        font4 = QFont()
        font4.setPointSize(12)
        self.label_5.setFont(font4)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_11)

        self.horizontalSpacer_2 = QSpacerItem(13, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.widget_3 = QWidget(self.headerFrame)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_2.addWidget(self.widget_3, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.headerFrame, 0, Qt.AlignTop)

        self.mainFrame = QWidget(self.mainBody)
        self.mainFrame.setObjectName(u"mainFrame")
        self.horizontalLayout_7 = QHBoxLayout(self.mainFrame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.mainFrame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(200, 110))
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(True)
        font5.setWeight(75)
        self.tabWidget.setFont(font5)
        self.tabWidget.setCursor(QCursor(Qt.SizeAllCursor))
        self.tabWidget.setStyleSheet(u"/*\u8bbe\u7f6eTabWidget\u4e2dtab_1\u7684\u6837\u5f0f*/\n"
"#tabWidget{\n"
"	\n"
"	background-color: rgb(255, 252, 226);\n"
"}\n"
"\n"
"#tab1.QWidget{\n"
"	background-color: rgb(108, 117, 125);\n"
"	tab1.setAlignment(plain1, Qt::AlignCenter)\n"
"\n"
"}\n"
" \n"
"/*\u8bbe\u7f6eTabWidget\u4e2dtab_2\u7684\u6837\u5f0f*/\n"
"#tab2.QWidget{\n"
"	background-color: rgb(108, 117, 125);\n"
"}\n"
" \n"
"#tab3.QWidget{\n"
"	background-color: rgb(108, 117, 125);\n"
"}\n"
" \n"
"/*\u8bbe\u7f6eTabWidget\u4e2dtab_2\u7684\u6837\u5f0f*/\n"
"#tab4.QWidget{\n"
"	background-color: rgb(108, 117, 125);\n"
"}\n"
"/*\u8bbe\u7f6eTabWidget\u4e2dQTabBar\u7684\u6837\u5f0f*/\n"
"QTabBar::tab{\n"
"    width:160px;\n"
"	height::40px;\n"
"\n"
"	background-color: rgb(145, 205, 255);\n"
"	font-family:Consolas;    /*\u8bbe\u7f6etab\u4e2d\u7684\u6587\u672c\u7684\u5b57\u4f53*/\n"
"	font-size:12pt;\n"
"	    /*\u8bbe\u7f6etab\u4e2d\u7684\u6587\u672c\u7684\u989c\u8272*/\n"
"	color: rgb(0, 0, 0);\n"
"	border-top-left-radius: 10px;    /*\u8bbe\u7f6etab\u7684"
                        "\u8fb9\u6846\u7684\u5706\u89d2\uff08\u5de6\u4e0a\u5706\u89d2\uff09*/\n"
"	border-top-right-radius: 10px;    /*\u8bbe\u7f6etab\u7684\u8fb9\u6846\u7684\u5706\u89d2\uff08\u53f3\u4e0a\u5706\u89d2\uff09*/\n"
"	min-width: 5px;\n"
"	padding: 5px;\n"
"}\n"
" \n"
"/*\u8bbe\u7f6eTabWidget\u4e2dQTabBar\u7684tab\u88ab\u9009\u4e2d\u65f6\u7684\u6837\u5f0f*/\n"
"QTabBar::tab:selected{\n"
"	\n"
"	\n"
"	background-color: rgb(48, 172, 255);\n"
"}\n"
" \n"
"/*\u8bbe\u7f6eTabWidget\u4e2d\u9f20\u6807\u60ac\u6d6e\u5728QTabBar\u7684tab\u4e0a\uff0c\u4f46\u672a\u9009\u4e2d\u8be5Tab\u7684\u6837\u5f0f*/\n"
"\n"
"/*\n"
"QTabBar::tab:hover:!selected {\n"
"    background-color: rgb(178, 217, 125, 45);\n"
"}\n"
"*/\n"
"/*\u8bbe\u7f6eTabWidget\u7684\u8fb9\u6846\u7684\u6837\u5f0f*/\n"
"QTabWidget::pane {\n"
"    border: 1px solid rgb(108, 117, 125, 65);\n"
"}\n"
" \n"
"/*\u5f53\u6253\u5f00\u591a\u4e2atab\uff0c\u53f3\u4fa7\u51fa\u73b0\uff0c\u70b9\u51fb\u540e\uff0c\u53ef\u4ee5\u5411\u524d\u5411\u540e\u7684\u6309\u94ae\u7684\u6837\u5f0f*/\n"
"QT"
                        "abBar QToolButton {\n"
"    border: none;\n"
"	color: rgb(255, 206, 6);\n"
"    background-color: #0b0e11;\n"
"}\n"
" \n"
"QTabBar QToolButton:hover {\n"
"	background-color: #161a1e; \n"
"}")
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab1 = QWidget()
        self.tab1.setObjectName(u"tab1")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tab1.sizePolicy().hasHeightForWidth())
        self.tab1.setSizePolicy(sizePolicy3)
        self.horizontalLayout_9 = QHBoxLayout(self.tab1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.video = QLabel(self.tab1)
        self.video.setObjectName(u"video")
        self.video.setMinimumSize(QSize(600, 0))
        self.video.setMaximumSize(QSize(1800, 16777215))
        font6 = QFont()
        font6.setPointSize(17)
        self.video.setFont(font6)
        self.video.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.video)

        self.widget_6 = QWidget(self.tab1)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_8 = QVBoxLayout(self.widget_6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.quality = QLabel(self.widget_6)
        self.quality.setObjectName(u"quality")
        self.quality.setMinimumSize(QSize(120, 56))
        font7 = QFont()
        font7.setFamily(u"\u65b0\u5b8b\u4f53")
        font7.setPointSize(16)
        font7.setBold(True)
        font7.setWeight(75)
        self.quality.setFont(font7)
        self.quality.setStyleSheet(u"#quality{\n"
"	background-color: rgb(176, 230, 255);\n"
"	border-radius:10px;\n"
"\n"
"}")
        self.quality.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.quality)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_6)

        self.point = QPushButton(self.widget_6)
        self.point.setObjectName(u"point")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.point.sizePolicy().hasHeightForWidth())
        self.point.setSizePolicy(sizePolicy4)
        self.point.setMinimumSize(QSize(120, 56))
        self.point.setFont(font3)
        self.point.setStyleSheet(u"#point{\n"
"	background-color: rgb(110, 209, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border:1px solid rgb(0,0,0);\n"
"	border-radius:10px;\n"
"	Width:60;\n"
"Height:36\n"
"}\n"
"#point:hover {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"#point:pressed {\n"
"	padding-top:3px;\n"
"	padding-left:3px;\n"
"}\n"
"\n"
"\n"
"")
        icon11 = QIcon()
        icon11.addFile(u":/img/imag/analyse/3.png", QSize(), QIcon.Normal, QIcon.Off)
        self.point.setIcon(icon11)
        self.point.setIconSize(QSize(20, 20))

        self.verticalLayout_8.addWidget(self.point)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_11)

        self.help = QPushButton(self.widget_6)
        self.help.setObjectName(u"help")
        sizePolicy4.setHeightForWidth(self.help.sizePolicy().hasHeightForWidth())
        self.help.setSizePolicy(sizePolicy4)
        self.help.setMinimumSize(QSize(120, 56))
        self.help.setFont(font3)
        self.help.setStyleSheet(u"#help{\n"
"	background-color: rgb(110, 209, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border:1px solid rgb(0,0,0);\n"
"	border-radius:10px;\n"
"	Width:60;\n"
"Height:36\n"
"}\n"
"#help:hover {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"#help:pressed {\n"
"	padding-top:3px;\n"
"	padding-left:3px;\n"
"}\n"
"\n"
"\n"
"")
        icon12 = QIcon()
        icon12.addFile(u":/img/imag/help.png", QSize(), QIcon.Normal, QIcon.Off)
        self.help.setIcon(icon12)
        self.help.setIconSize(QSize(20, 20))

        self.verticalLayout_8.addWidget(self.help)

        self.verticalSpacer_42 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_42)

        self.number = QPushButton(self.widget_6)
        self.number.setObjectName(u"number")
        sizePolicy4.setHeightForWidth(self.number.sizePolicy().hasHeightForWidth())
        self.number.setSizePolicy(sizePolicy4)
        self.number.setMinimumSize(QSize(120, 56))
        self.number.setFont(font3)
        self.number.setStyleSheet(u"#number{\n"
"	background-color: rgb(110, 209, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border:1px solid rgb(0,0,0);\n"
"	border-radius:10px;\n"
"	Width:60;\n"
"Height:36\n"
"}\n"
"#number:hover {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"#number:pressed {\n"
"	padding-top:3px;\n"
"	padding-left:3px;\n"
"}\n"
"\n"
"\n"
"")
        self.number.setIcon(icon11)
        self.number.setIconSize(QSize(20, 20))

        self.verticalLayout_8.addWidget(self.number)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_14)

        self.angle_of_view = QLabel(self.widget_6)
        self.angle_of_view.setObjectName(u"angle_of_view")
        self.angle_of_view.setMinimumSize(QSize(120, 56))
        self.angle_of_view.setFont(font7)
        self.angle_of_view.setStyleSheet(u"#angle_of_view{\n"
"	background-color: rgb(176, 230, 255);\n"
"	border-radius:10px;\n"
"\n"
"}")
        self.angle_of_view.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.angle_of_view)

        self.verticalSpacer_20 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_20)

        self.synthetic = QPushButton(self.widget_6)
        self.synthetic.setObjectName(u"synthetic")
        sizePolicy4.setHeightForWidth(self.synthetic.sizePolicy().hasHeightForWidth())
        self.synthetic.setSizePolicy(sizePolicy4)
        self.synthetic.setMinimumSize(QSize(120, 56))
        self.synthetic.setFont(font3)
        self.synthetic.setStyleSheet(u"#synthetic{\n"
"	background-color: rgb(110, 209, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border:1px solid rgb(0,0,0);\n"
"	border-radius:10px;\n"
"	Width:60;\n"
"Height:36\n"
"}\n"
"#synthetic:hover {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"#synthetic:pressed {\n"
"	padding-top:3px;\n"
"	padding-left:3px;\n"
"}\n"
"\n"
"\n"
"")
        icon13 = QIcon()
        icon13.addFile(u":/img/imag/analyse/1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.synthetic.setIcon(icon13)
        self.synthetic.setIconSize(QSize(20, 20))

        self.verticalLayout_8.addWidget(self.synthetic)

        self.verticalSpacer_22 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_22)

        self.save1 = QPushButton(self.widget_6)
        self.save1.setObjectName(u"save1")
        sizePolicy4.setHeightForWidth(self.save1.sizePolicy().hasHeightForWidth())
        self.save1.setSizePolicy(sizePolicy4)
        self.save1.setMinimumSize(QSize(120, 56))
        self.save1.setFont(font3)
        self.save1.setStyleSheet(u"#save1{\n"
"	background-color: rgb(110, 209, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border:1px solid rgb(0,0,0);\n"
"	border-radius:10px;\n"
"	Width:60;\n"
"Height:36\n"
"}\n"
"#save1:hover {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"#save1:pressed {\n"
"	padding-top:3px;\n"
"	padding-left:3px;\n"
"}\n"
"\n"
"\n"
"")
        icon14 = QIcon()
        icon14.addFile(u":/img/imag/analyse/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.save1.setIcon(icon14)
        self.save1.setIconSize(QSize(20, 20))

        self.verticalLayout_8.addWidget(self.save1)

        self.verticalSpacer_23 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_23)

        self.verticalSpacer_24 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_24)

        self.widget_9 = QWidget(self.widget_6)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")

        self.verticalLayout_8.addWidget(self.widget_9)


        self.horizontalLayout_9.addWidget(self.widget_6)

        self.tabWidget.addTab(self.tab1, "")
        self.tab2 = QWidget()
        self.tab2.setObjectName(u"tab2")
        self.horizontalLayout_10 = QHBoxLayout(self.tab2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.plain2 = QPlainTextEdit(self.tab2)
        self.plain2.setObjectName(u"plain2")
        self.plain2.setFont(font4)
        self.plain2.setStyleSheet(u"background-color: rgb(255, 244, 205);")

        self.horizontalLayout_10.addWidget(self.plain2)

        self.widget_7 = QWidget(self.tab2)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_9 = QVBoxLayout(self.widget_7)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.ana2 = QLabel(self.widget_7)
        self.ana2.setObjectName(u"ana2")
        self.ana2.setMinimumSize(QSize(120, 56))
        font8 = QFont()
        font8.setFamily(u"\u65b0\u5b8b\u4f53")
        font8.setPointSize(16)
        font8.setBold(False)
        font8.setWeight(50)
        self.ana2.setFont(font8)
        self.ana2.setStyleSheet(u"#ana2{\n"
"	background-color: rgb(176, 230, 255);\n"
"	border-radius:10px;\n"
"\n"
"}")
        self.ana2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.ana2)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_7)

        self.nanpic = QPushButton(self.widget_7)
        self.nanpic.setObjectName(u"nanpic")
        sizePolicy4.setHeightForWidth(self.nanpic.sizePolicy().hasHeightForWidth())
        self.nanpic.setSizePolicy(sizePolicy4)
        self.nanpic.setMinimumSize(QSize(120, 56))
        self.nanpic.setFont(font3)
        self.nanpic.setStyleSheet(u"#nanpic{\n"
"		background-color: rgb(110, 209, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border:1px solid rgb(0,0,0);\n"
"	border-radius:10px;\n"
"	Width:60;\n"
"Height:36\n"
"}\n"
"#nanpic:hover {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"#nanpic:pressed {\n"
"	padding-top:3px;\n"
"	padding-left:3px;\n"
"}\n"
"\n"
"\n"
"")
        icon15 = QIcon()
        icon15.addFile(u":/img/imag/analyse/8.png", QSize(), QIcon.Normal, QIcon.Off)
        self.nanpic.setIcon(icon15)
        self.nanpic.setIconSize(QSize(20, 20))

        self.verticalLayout_9.addWidget(self.nanpic)

        self.verticalSpacer_25 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_25)

        self.yinyong = QPushButton(self.widget_7)
        self.yinyong.setObjectName(u"yinyong")
        sizePolicy4.setHeightForWidth(self.yinyong.sizePolicy().hasHeightForWidth())
        self.yinyong.setSizePolicy(sizePolicy4)
        self.yinyong.setMinimumSize(QSize(120, 56))
        self.yinyong.setFont(font3)
        self.yinyong.setStyleSheet(u"#yinyong{\n"
"	background-color: rgb(110, 209, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border:1px solid rgb(0,0,0);\n"
"	border-radius:10px;\n"
"	Width:60;\n"
"Height:36\n"
"}\n"
"#yinyong:hover {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"#yinyong:pressed {\n"
"	padding-top:3px;\n"
"	padding-left:3px;\n"
"}\n"
"\n"
"\n"
"")
        icon16 = QIcon()
        icon16.addFile(u":/img/imag/analyse/7.png", QSize(), QIcon.Normal, QIcon.Off)
        self.yinyong.setIcon(icon16)
        self.yinyong.setIconSize(QSize(20, 20))

        self.verticalLayout_9.addWidget(self.yinyong)

        self.verticalSpacer_26 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_26)

        self.point2 = QPushButton(self.widget_7)
        self.point2.setObjectName(u"point2")
        sizePolicy4.setHeightForWidth(self.point2.sizePolicy().hasHeightForWidth())
        self.point2.setSizePolicy(sizePolicy4)
        self.point2.setMinimumSize(QSize(120, 56))
        self.point2.setFont(font3)
        self.point2.setStyleSheet(u"#point2{\n"
"	background-color: rgb(110, 209, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border:1px solid rgb(0,0,0);\n"
"	border-radius:10px;\n"
"	Width:60;\n"
"Height:36\n"
"}\n"
"#point2:hover {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"#point2:pressed {\n"
"	padding-top:3px;\n"
"	padding-left:3px;\n"
"}\n"
"\n"
"\n"
"")
        self.point2.setIcon(icon11)
        self.point2.setIconSize(QSize(20, 20))

        self.verticalLayout_9.addWidget(self.point2)

        self.verticalSpacer_27 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_27)

        self.fertilize = QLabel(self.widget_7)
        self.fertilize.setObjectName(u"fertilize")
        self.fertilize.setMinimumSize(QSize(120, 56))
        self.fertilize.setFont(font8)
        self.fertilize.setStyleSheet(u"#fertilize{\n"
"	background-color: rgb(176, 230, 255);\n"
"	border-radius:10px;\n"
"\n"
"}")
        self.fertilize.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.fertilize)

        self.verticalSpacer_43 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_43)

        self.syn2 = QPushButton(self.widget_7)
        self.syn2.setObjectName(u"syn2")
        sizePolicy4.setHeightForWidth(self.syn2.sizePolicy().hasHeightForWidth())
        self.syn2.setSizePolicy(sizePolicy4)
        self.syn2.setMinimumSize(QSize(120, 56))
        self.syn2.setFont(font3)
        self.syn2.setStyleSheet(u"#syn2{\n"
"	background-color: rgb(110, 209, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border:1px solid rgb(0,0,0);\n"
"	border-radius:10px;\n"
"	Width:60;\n"
"Height:36\n"
"}\n"
"#syn2:hover {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"#syn2:pressed {\n"
"	padding-top:3px;\n"
"	padding-left:3px;\n"
"}\n"
"\n"
"\n"
"")
        self.syn2.setIcon(icon13)
        self.syn2.setIconSize(QSize(20, 20))

        self.verticalLayout_9.addWidget(self.syn2)

        self.verticalSpacer_29 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_29)

        self.save2 = QPushButton(self.widget_7)
        self.save2.setObjectName(u"save2")
        sizePolicy4.setHeightForWidth(self.save2.sizePolicy().hasHeightForWidth())
        self.save2.setSizePolicy(sizePolicy4)
        self.save2.setMinimumSize(QSize(120, 56))
        self.save2.setFont(font3)
        self.save2.setStyleSheet(u"#save2{\n"
"	background-color: rgb(110, 209, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border:1px solid rgb(0,0,0);\n"
"	border-radius:10px;\n"
"	Width:60;\n"
"Height:36\n"
"}\n"
"#save2:hover {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"#save2:pressed {\n"
"	padding-top:3px;\n"
"	padding-left:3px;\n"
"}\n"
"\n"
"\n"
"")
        self.save2.setIcon(icon14)
        self.save2.setIconSize(QSize(20, 20))

        self.verticalLayout_9.addWidget(self.save2)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_16)

        self.help1 = QPushButton(self.widget_7)
        self.help1.setObjectName(u"help1")
        sizePolicy4.setHeightForWidth(self.help1.sizePolicy().hasHeightForWidth())
        self.help1.setSizePolicy(sizePolicy4)
        self.help1.setMinimumSize(QSize(120, 56))
        self.help1.setFont(font3)
        self.help1.setStyleSheet(u"#help1{\n"
"	background-color: rgb(110, 209, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border:1px solid rgb(0,0,0);\n"
"	border-radius:10px;\n"
"	Width:60;\n"
"Height:36\n"
"}\n"
"#help1:hover {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"#help1:pressed {\n"
"	padding-top:3px;\n"
"	padding-left:3px;\n"
"}\n"
"\n"
"\n"
"")
        self.help1.setIcon(icon12)
        self.help1.setIconSize(QSize(20, 20))

        self.verticalLayout_9.addWidget(self.help1)

        self.verticalSpacer_30 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_30)

        self.verticalSpacer_31 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_31)

        self.widget_10 = QWidget(self.widget_7)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")

        self.verticalLayout_9.addWidget(self.widget_10)


        self.horizontalLayout_10.addWidget(self.widget_7)

        self.tabWidget.addTab(self.tab2, "")
        self.tab3 = QWidget()
        self.tab3.setObjectName(u"tab3")
        self.horizontalLayout_11 = QHBoxLayout(self.tab3)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.plain3 = QPlainTextEdit(self.tab3)
        self.plain3.setObjectName(u"plain3")
        self.plain3.setFont(font4)
        self.plain3.setStyleSheet(u"background-color: rgb(255, 244, 205);")

        self.horizontalLayout_11.addWidget(self.plain3)

        self.widget_11 = QWidget(self.tab3)
        self.widget_11.setObjectName(u"widget_11")
        self.verticalLayout_10 = QVBoxLayout(self.widget_11)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalSpacer_32 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_32)

        self.ana3 = QLabel(self.widget_11)
        self.ana3.setObjectName(u"ana3")
        self.ana3.setMinimumSize(QSize(120, 56))
        self.ana3.setFont(font2)
        self.ana3.setStyleSheet(u"#ana3{\n"
"	background-color: rgb(176, 230, 255);\n"
"	border-radius:10px;\n"
"\n"
"}")
        self.ana3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.ana3)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_5)

        self.fig = QPushButton(self.widget_11)
        self.fig.setObjectName(u"fig")
        sizePolicy4.setHeightForWidth(self.fig.sizePolicy().hasHeightForWidth())
        self.fig.setSizePolicy(sizePolicy4)
        self.fig.setMinimumSize(QSize(120, 56))
        self.fig.setFont(font3)
        self.fig.setStyleSheet(u"#fig{\n"
"		background-color: rgb(110, 209, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border:1px solid rgb(0,0,0);\n"
"	border-radius:10px;\n"
"	Width:60;\n"
"Height:36\n"
"}\n"
"#fig:hover {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"#fig:pressed {\n"
"	padding-top:3px;\n"
"	padding-left:3px;\n"
"}\n"
"\n"
"\n"
"")
        self.fig.setIcon(icon15)
        self.fig.setIconSize(QSize(20, 20))

        self.verticalLayout_10.addWidget(self.fig)

        self.verticalSpacer_33 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_33)

        self.yin3 = QPushButton(self.widget_11)
        self.yin3.setObjectName(u"yin3")
        sizePolicy4.setHeightForWidth(self.yin3.sizePolicy().hasHeightForWidth())
        self.yin3.setSizePolicy(sizePolicy4)
        self.yin3.setMinimumSize(QSize(120, 56))
        self.yin3.setFont(font3)
        self.yin3.setStyleSheet(u"#yin3{\n"
"	background-color: rgb(110, 209, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border:1px solid rgb(0,0,0);\n"
"	border-radius:10px;\n"
"	Width:60;\n"
"Height:36\n"
"}\n"
"#yin3:hover {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"#yin3:pressed {\n"
"	padding-top:3px;\n"
"	padding-left:3px;\n"
"}\n"
"\n"
"\n"
"")
        self.yin3.setIcon(icon16)
        self.yin3.setIconSize(QSize(20, 20))

        self.verticalLayout_10.addWidget(self.yin3)

        self.verticalSpacer_34 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_34)

        self.point3 = QPushButton(self.widget_11)
        self.point3.setObjectName(u"point3")
        sizePolicy4.setHeightForWidth(self.point3.sizePolicy().hasHeightForWidth())
        self.point3.setSizePolicy(sizePolicy4)
        self.point3.setMinimumSize(QSize(120, 56))
        self.point3.setFont(font3)
        self.point3.setStyleSheet(u"#point3{\n"
"	background-color: rgb(110, 209, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border:1px solid rgb(0,0,0);\n"
"	border-radius:10px;\n"
"	Width:60;\n"
"Height:36\n"
"}\n"
"#point3:hover {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"#point3:pressed {\n"
"	padding-top:3px;\n"
"	padding-left:3px;\n"
"}\n"
"\n"
"\n"
"")
        self.point3.setIcon(icon11)
        self.point3.setIconSize(QSize(20, 20))

        self.verticalLayout_10.addWidget(self.point3)

        self.verticalSpacer_35 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_35)

        self.pic3 = QPushButton(self.widget_11)
        self.pic3.setObjectName(u"pic3")
        sizePolicy4.setHeightForWidth(self.pic3.sizePolicy().hasHeightForWidth())
        self.pic3.setSizePolicy(sizePolicy4)
        self.pic3.setMinimumSize(QSize(120, 56))
        self.pic3.setFont(font3)
        self.pic3.setStyleSheet(u"#pic3{\n"
"	background-color: rgb(110, 209, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border:1px solid rgb(0,0,0);\n"
"	border-radius:10px;\n"
"	Width:60;\n"
"Height:36\n"
"}\n"
"#pic3:hover {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"#pic3:pressed {\n"
"	padding-top:3px;\n"
"	padding-left:3px;\n"
"}\n"
"\n"
"\n"
"")
        self.pic3.setIcon(icon11)
        self.pic3.setIconSize(QSize(20, 20))

        self.verticalLayout_10.addWidget(self.pic3)

        self.verticalSpacer_36 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_36)

        self.syn3 = QPushButton(self.widget_11)
        self.syn3.setObjectName(u"syn3")
        sizePolicy4.setHeightForWidth(self.syn3.sizePolicy().hasHeightForWidth())
        self.syn3.setSizePolicy(sizePolicy4)
        self.syn3.setMinimumSize(QSize(120, 56))
        self.syn3.setFont(font3)
        self.syn3.setStyleSheet(u"#syn3{\n"
"	background-color: rgb(110, 209, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border:1px solid rgb(0,0,0);\n"
"	border-radius:10px;\n"
"	Width:60;\n"
"Height:36\n"
"}\n"
"#syn3:hover {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"#syn3:pressed {\n"
"	padding-top:3px;\n"
"	padding-left:3px;\n"
"}\n"
"\n"
"\n"
"")
        self.syn3.setIcon(icon13)
        self.syn3.setIconSize(QSize(20, 20))

        self.verticalLayout_10.addWidget(self.syn3)

        self.verticalSpacer_37 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_37)

        self.save3 = QPushButton(self.widget_11)
        self.save3.setObjectName(u"save3")
        sizePolicy4.setHeightForWidth(self.save3.sizePolicy().hasHeightForWidth())
        self.save3.setSizePolicy(sizePolicy4)
        self.save3.setMinimumSize(QSize(120, 56))
        self.save3.setFont(font3)
        self.save3.setStyleSheet(u"#save3{\n"
"	background-color: rgb(110, 209, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border:1px solid rgb(0,0,0);\n"
"	border-radius:10px;\n"
"	Width:60;\n"
"Height:36\n"
"}\n"
"#save3:hover {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"#save3:pressed {\n"
"	padding-top:3px;\n"
"	padding-left:3px;\n"
"}\n"
"\n"
"\n"
"")
        self.save3.setIcon(icon14)
        self.save3.setIconSize(QSize(20, 20))

        self.verticalLayout_10.addWidget(self.save3)

        self.verticalSpacer_38 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_38)

        self.help3 = QPushButton(self.widget_11)
        self.help3.setObjectName(u"help3")
        sizePolicy4.setHeightForWidth(self.help3.sizePolicy().hasHeightForWidth())
        self.help3.setSizePolicy(sizePolicy4)
        self.help3.setMinimumSize(QSize(120, 56))
        self.help3.setFont(font3)
        self.help3.setStyleSheet(u"#help3{\n"
"	background-color: rgb(110, 209, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border:1px solid rgb(0,0,0);\n"
"	border-radius:10px;\n"
"	Width:60;\n"
"Height:36\n"
"}\n"
"#help3:hover {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"#help3:pressed {\n"
"	padding-top:3px;\n"
"	padding-left:3px;\n"
"}\n"
"\n"
"\n"
"")
        self.help3.setIcon(icon12)
        self.help3.setIconSize(QSize(20, 20))

        self.verticalLayout_10.addWidget(self.help3)

        self.verticalSpacer_39 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_39)

        self.widget_12 = QWidget(self.widget_11)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_16 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")

        self.verticalLayout_10.addWidget(self.widget_12)


        self.horizontalLayout_11.addWidget(self.widget_11)

        self.tabWidget.addTab(self.tab3, "")
        self.tab5 = QWidget()
        self.tab5.setObjectName(u"tab5")
        self.horizontalLayout_12 = QHBoxLayout(self.tab5)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.widget_4 = QWidget(self.tab5)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setStyleSheet(u"background-color: rgb(255, 244, 205);")

        self.horizontalLayout_12.addWidget(self.widget_4)

        self.tabWidget.addTab(self.tab5, "")
        self.tab4 = QWidget()
        self.tab4.setObjectName(u"tab4")
        self.horizontalLayout_13 = QHBoxLayout(self.tab4)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.plain4 = QPlainTextEdit(self.tab4)
        self.plain4.setObjectName(u"plain4")
        self.plain4.setFont(font4)
        self.plain4.setStyleSheet(u"background-color: rgb(255, 244, 205);")

        self.horizontalLayout_13.addWidget(self.plain4)

        self.widget_5 = QWidget(self.tab4)
        self.widget_5.setObjectName(u"widget_5")

        self.horizontalLayout_13.addWidget(self.widget_5)

        self.widget_13 = QWidget(self.tab4)
        self.widget_13.setObjectName(u"widget_13")
        self.verticalLayout_15 = QVBoxLayout(self.widget_13)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalSpacer_72 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_72)

        self.ana4 = QLabel(self.widget_13)
        self.ana4.setObjectName(u"ana4")
        self.ana4.setMinimumSize(QSize(120, 56))
        self.ana4.setFont(font2)
        self.ana4.setStyleSheet(u"#ana4{\n"
"	background-color: rgb(176, 230, 255);\n"
"	border-radius:10px;\n"
"\n"
"}")
        self.ana4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.ana4)

        self.verticalSpacer_73 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_73)

        self.point4 = QPushButton(self.widget_13)
        self.point4.setObjectName(u"point4")
        sizePolicy4.setHeightForWidth(self.point4.sizePolicy().hasHeightForWidth())
        self.point4.setSizePolicy(sizePolicy4)
        self.point4.setMinimumSize(QSize(120, 56))
        self.point4.setFont(font3)
        self.point4.setStyleSheet(u"#point4{\n"
"	background-color: rgb(110, 209, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border:1px solid rgb(0,0,0);\n"
"	border-radius:10px;\n"
"	Width:60;\n"
"Height:36\n"
"}\n"
"#point4:hover {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"#point4:pressed {\n"
"	padding-top:3px;\n"
"	padding-left:3px;\n"
"}\n"
"\n"
"\n"
"")
        self.point4.setIcon(icon11)
        self.point4.setIconSize(QSize(20, 20))

        self.verticalLayout_15.addWidget(self.point4)

        self.verticalSpacer_76 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_76)

        self.syn4 = QPushButton(self.widget_13)
        self.syn4.setObjectName(u"syn4")
        sizePolicy4.setHeightForWidth(self.syn4.sizePolicy().hasHeightForWidth())
        self.syn4.setSizePolicy(sizePolicy4)
        self.syn4.setMinimumSize(QSize(120, 56))
        self.syn4.setFont(font3)
        self.syn4.setStyleSheet(u"#syn4{\n"
"	background-color: rgb(110, 209, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border:1px solid rgb(0,0,0);\n"
"	border-radius:10px;\n"
"	Width:60;\n"
"	Height:36\n"
"}\n"
"#syn4:hover {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"#syn4:pressed {\n"
"	padding-top:3px;\n"
"	padding-left:3px;\n"
"}\n"
"\n"
"\n"
"")
        self.syn4.setIcon(icon13)
        self.syn4.setIconSize(QSize(20, 20))

        self.verticalLayout_15.addWidget(self.syn4)

        self.verticalSpacer_77 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_77)

        self.save4 = QPushButton(self.widget_13)
        self.save4.setObjectName(u"save4")
        sizePolicy4.setHeightForWidth(self.save4.sizePolicy().hasHeightForWidth())
        self.save4.setSizePolicy(sizePolicy4)
        self.save4.setMinimumSize(QSize(120, 56))
        self.save4.setFont(font3)
        self.save4.setStyleSheet(u"#save4{\n"
"	background-color: rgb(110, 209, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border:1px solid rgb(0,0,0);\n"
"	border-radius:10px;\n"
"	Width:60;\n"
"Height:36\n"
"}\n"
"#save4:hover {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"#save4:pressed {\n"
"	padding-top:3px;\n"
"	padding-left:3px;\n"
"}\n"
"\n"
"\n"
"")
        self.save4.setIcon(icon14)
        self.save4.setIconSize(QSize(20, 20))

        self.verticalLayout_15.addWidget(self.save4)

        self.verticalSpacer_78 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_78)

        self.help4 = QPushButton(self.widget_13)
        self.help4.setObjectName(u"help4")
        sizePolicy4.setHeightForWidth(self.help4.sizePolicy().hasHeightForWidth())
        self.help4.setSizePolicy(sizePolicy4)
        self.help4.setMinimumSize(QSize(120, 56))
        self.help4.setFont(font3)
        self.help4.setStyleSheet(u"#help4{\n"
"	background-color: rgb(110, 209, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border:1px solid rgb(0,0,0);\n"
"	border-radius:10px;\n"
"	Width:60;\n"
"Height:36\n"
"}\n"
"#help4:hover {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"#help4:pressed {\n"
"	padding-top:3px;\n"
"	padding-left:3px;\n"
"}\n"
"\n"
"\n"
"")
        self.help4.setIcon(icon12)
        self.help4.setIconSize(QSize(20, 20))

        self.verticalLayout_15.addWidget(self.help4)

        self.verticalSpacer_79 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_79)

        self.widget_22 = QWidget(self.widget_13)
        self.widget_22.setObjectName(u"widget_22")
        self.horizontalLayout_25 = QHBoxLayout(self.widget_22)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")

        self.verticalLayout_15.addWidget(self.widget_22)


        self.horizontalLayout_13.addWidget(self.widget_13)

        self.tabWidget.addTab(self.tab4, "")

        self.horizontalLayout_7.addWidget(self.tabWidget)


        self.verticalLayout.addWidget(self.mainFrame)


        self.horizontalLayout.addWidget(self.mainBody)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u667a\u6167\u8015\u8018", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5c81\u7a14\u5e74\u4e30", None))
        self.btn1.setText(QCoreApplication.translate("MainWindow", u"\u6211\u7684\u82b1\u56ed", None))
        self.btn2.setText(QCoreApplication.translate("MainWindow", u"\u786c\u4ef6\u7ba1\u7406", None))
        self.btn3.setText(QCoreApplication.translate("MainWindow", u"\u786c\u4ef6\u8bbe\u7f6e", None))
        self.btn5.setText(QCoreApplication.translate("MainWindow", u"\u5ba0\u7269\u7167\u7ba1", None))
        self.btn4.setText(QCoreApplication.translate("MainWindow", u"\u65e0\u4eba\u503c\u5b88", None))
        self.btn6.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e\u6211\u4eec", None))
        self.label_2.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"search something", None))
        self.B1.setText(QCoreApplication.translate("MainWindow", u"\u65f6\u95f4\u7ba1\u7406", None))
        self.B2.setText(QCoreApplication.translate("MainWindow", u"\u5929\u6c14\u9884\u62a5", None))
        self.B3.setText(QCoreApplication.translate("MainWindow", u"\u5f02\u5e38\u76d1\u63a7", None))
        self.B4.setText(QCoreApplication.translate("MainWindow", u"\u866b\u5bb3\u9632\u6cbb", None))
        self.accountBtn.setText("")
#if QT_CONFIG(shortcut)
        self.accountBtn.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"kingipr", None))
        self.video.setText(QCoreApplication.translate("MainWindow", u"-----------------------------\u89c6\u9891\u663e\u793a\u533a\u57df-------------------------------", None))
        self.quality.setText(QCoreApplication.translate("MainWindow", u"\u753b\u8d28\u5207\u6362", None))
        self.point.setText(QCoreApplication.translate("MainWindow", u"720P", None))
        self.help.setText(QCoreApplication.translate("MainWindow", u"1080P", None))
        self.number.setText(QCoreApplication.translate("MainWindow", u"4K", None))
        self.angle_of_view.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u89d2\u5207\u6362", None))
        self.synthetic.setText(QCoreApplication.translate("MainWindow", u"\u5b9a\u70b9", None))
        self.save1.setText(QCoreApplication.translate("MainWindow", u"\u5de1\u89c6", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), QCoreApplication.translate("MainWindow", u"\u5b9e\u65f6\u76d1\u63a7", None))
        self.plain2.setPlaceholderText("")
        self.ana2.setText(QCoreApplication.translate("MainWindow", u"\u6d47\u6c34", None))
        self.nanpic.setText(QCoreApplication.translate("MainWindow", u"\u8282\u6c34\u6a21\u5f0f", None))
        self.yinyong.setText(QCoreApplication.translate("MainWindow", u"\u704c\u6e89\u6a21\u5f0f", None))
        self.point2.setText(QCoreApplication.translate("MainWindow", u"\u96fe\u5316\u6a21\u5f0f", None))
        self.fertilize.setText(QCoreApplication.translate("MainWindow", u"\u65bd\u80a5", None))
        self.syn2.setText(QCoreApplication.translate("MainWindow", u"\u7efc\u5408", None))
        self.save2.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.help1.setText(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), QCoreApplication.translate("MainWindow", u"\u6d47\u6c34\u65bd\u80a5", None))
        self.plain3.setPlaceholderText("")
        self.ana3.setText(QCoreApplication.translate("MainWindow", u"\u5206\u6790\u5de5\u5177", None))
        self.fig.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u53f7", None))
        self.yin3.setText(QCoreApplication.translate("MainWindow", u"\u5f15\u7528", None))
        self.point3.setText(QCoreApplication.translate("MainWindow", u"\u6807\u70b9", None))
        self.pic3.setText(QCoreApplication.translate("MainWindow", u"\u9644\u56fe", None))
        self.syn3.setText(QCoreApplication.translate("MainWindow", u"\u7efc\u5408", None))
        self.save3.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.help3.setText(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), QCoreApplication.translate("MainWindow", u"\u677e\u571f\u79cd\u83dc", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab5), QCoreApplication.translate("MainWindow", u"\u6536\u83b7\u852c\u83dc", None))
        self.plain4.setPlaceholderText("")
        self.ana4.setText(QCoreApplication.translate("MainWindow", u"\u5206\u6790\u5de5\u5177", None))
        self.point4.setText(QCoreApplication.translate("MainWindow", u"\u6807\u70b9", None))
        self.syn4.setText(QCoreApplication.translate("MainWindow", u"\u7efc\u5408", None))
        self.save4.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.help4.setText(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab4), QCoreApplication.translate("MainWindow", u"\u82b1\u56ed\u8bbe\u8ba1", None))
    # retranslateUi

