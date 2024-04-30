from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QVBoxLayout, QTextEdit, QMessageBox
import numpy as np
from ikSolver import *

import math
from data import *
DH = {'theta': [0, 0, 0, 0, 0, 0],
      'd': [241, 173.5, -38, 0, 95, 45],
      'a': [0, 335, 294, 0, 0, 0],
      'alpha': [np.pi / 2, 0, 0, -np.pi / 2, np.pi / 2, 0],
      'offset': [0, 0, 20, 0, 0, 0]}
class Ui_MainWindow_4(object):
    def __init__(self):
        #Create variables in class
        self.x_left = None
        self.y_left = None
        self.z_left = None
        self.matrix_left = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]
        self.x_right = None
        self.y_right = None
        self.z_right = None
        self.matrix_right = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1309, 707)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrs_box_left = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrs_box_left.setGeometry(QtCore.QRect(860, 140, 421, 211))
        self.textBrs_box_left.setObjectName("textBrs_box_left")
        self.textBrs_box_right = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrs_box_right.setGeometry(QtCore.QRect(860, 430, 421, 231))
        self.textBrs_box_right.setObjectName("textBrs_box_right")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-120, 0, 1431, 81))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setGeometry(QtCore.QRect(120, 0, 91, 81))
        self.pushButton_4.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"border:1px solid rgb(255, 255, 255)")
        self.pushButton_4.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("sidebar_test/icon/1200px-Logo_HUET.svg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(580, 10, 501, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(500, 30, 671, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(540, 60, 161, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(750, 60, 81, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(900, 60, 211, 20))
        self.label_5.setObjectName("label_5")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(60, 100, 381, 481))
        self.groupBox.setStyleSheet("background-color: ;\n"
"color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"")
        self.groupBox.setObjectName("groupBox")
        self.textBrs_UX_left = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrs_UX_left.setGeometry(QtCore.QRect(20, 80, 91, 31))
        self.textBrs_UX_left.setObjectName("textBrs_UX_left")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 40, 93, 28))
        self.pushButton_5.setStyleSheet("background-color: #004580;\n"
"color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"\n"
"border:2px solid rgb(0,0,0);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_6.setGeometry(QtCore.QRect(130, 40, 93, 28))
        self.pushButton_6.setStyleSheet("background-color: #004580;\n"
"color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"\n"
"border:2px solid rgb(0,0,0);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_7.setGeometry(QtCore.QRect(240, 40, 93, 28))
        self.pushButton_7.setStyleSheet("background-color: #004580;\n"
"color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"\n"
"border:2px solid rgb(0,0,0);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_8.setGeometry(QtCore.QRect(20, 130, 93, 28))
        self.pushButton_8.setStyleSheet("background-color: #004580;\n"
"color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"\n"
"border:2px solid rgb(0,0,0);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_9.setGeometry(QtCore.QRect(130, 130, 93, 28))
        self.pushButton_9.setStyleSheet("background-color: #004580;\n"
"color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"\n"
"border:2px solid rgb(0,0,0);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_10.setGeometry(QtCore.QRect(240, 130, 93, 28))
        self.pushButton_10.setStyleSheet("background-color: #004580;\n"
"color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"\n"
"border:2px solid rgb(0,0,0);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.textBrs_VX_left = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrs_VX_left.setGeometry(QtCore.QRect(130, 80, 91, 31))
        self.textBrs_VX_left.setObjectName("textBrs_VX_left")
        self.textBrs_WX_left = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrs_WX_left.setGeometry(QtCore.QRect(240, 80, 91, 31))
        self.textBrs_WX_left.setObjectName("textBrs_WX_left")
        self.textBrs_WY_left = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrs_WY_left.setGeometry(QtCore.QRect(240, 170, 91, 31))
        self.textBrs_WY_left.setObjectName("textBrs_WY_left")
        self.textBrs_UY_left = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrs_UY_left.setGeometry(QtCore.QRect(20, 170, 91, 31))
        self.textBrs_UY_left.setObjectName("textBrs_UY_left")
        self.textBrs_VY_left = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrs_VY_left.setGeometry(QtCore.QRect(130, 170, 91, 31))
        self.textBrs_VY_left.setObjectName("textBrs_VY_left")
        self.pushButton_22 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_22.setGeometry(QtCore.QRect(240, 220, 93, 28))
        self.pushButton_22.setStyleSheet("background-color: #004580;\n"
"color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"\n"
"border:2px solid rgb(0,0,0);")
        self.pushButton_22.setObjectName("pushButton_22")
        self.textBrs_PX_left = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrs_PX_left.setGeometry(QtCore.QRect(20, 350, 91, 31))
        self.textBrs_PX_left.setObjectName("textBrs_PX_left")
        self.textBrs_WZ_left = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrs_WZ_left.setGeometry(QtCore.QRect(240, 260, 91, 31))
        self.textBrs_WZ_left.setObjectName("textBrs_WZ_left")
        self.pushButton_23 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_23.setGeometry(QtCore.QRect(130, 220, 93, 28))
        self.pushButton_23.setStyleSheet("background-color: #004580;\n"
"color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"\n"
"border:2px solid rgb(0,0,0);")
        self.pushButton_23.setObjectName("pushButton_23")
        self.textBrs_UZ_left = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrs_UZ_left.setGeometry(QtCore.QRect(20, 260, 91, 31))
        self.textBrs_UZ_left.setObjectName("textBrs_UZ_left")
        self.textBrs_PY_left = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrs_PY_left.setGeometry(QtCore.QRect(130, 350, 91, 31))
        self.textBrs_PY_left.setObjectName("textBrs_PY_left")
        self.pushButton_24 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_24.setGeometry(QtCore.QRect(130, 310, 93, 28))
        self.pushButton_24.setStyleSheet("background-color: #004580;\n"
"color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"\n"
"border:2px solid rgb(0,0,0);")
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_25 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_25.setGeometry(QtCore.QRect(240, 310, 93, 28))
        self.pushButton_25.setStyleSheet("background-color: #004580;\n"
"color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"\n"
"border:2px solid rgb(0,0,0);")
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_26 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_26.setGeometry(QtCore.QRect(20, 220, 93, 28))
        self.pushButton_26.setStyleSheet("background-color: #004580;\n"
"color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"\n"
"border:2px solid rgb(0,0,0);")
        self.pushButton_26.setObjectName("pushButton_26")
        self.textBrs_VZ_left = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrs_VZ_left.setGeometry(QtCore.QRect(130, 260, 91, 31))
        self.textBrs_VZ_left.setObjectName("textBrs_VZ_left")
        self.textBrs_PZ_left = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrs_PZ_left.setGeometry(QtCore.QRect(240, 350, 91, 31))
        self.textBrs_PZ_left.setObjectName("textBrs_PZ_left")
        self.pushButton_27 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_27.setGeometry(QtCore.QRect(20, 310, 93, 28))
        self.pushButton_27.setStyleSheet("background-color: #004580;\n"
"color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"\n"
"border:2px solid rgb(0,0,0);")
        self.pushButton_27.setObjectName("pushButton_27")
        self.textBrs_Height_left = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrs_Height_left.setGeometry(QtCore.QRect(240, 440, 91, 31))
        self.textBrs_Height_left.setObjectName("textBrs_Height_left")
        self.pushButton_28 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_28.setGeometry(QtCore.QRect(130, 400, 93, 28))
        self.pushButton_28.setStyleSheet("background-color: #004580;\n"
"color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"\n"
"border:2px solid rgb(0,0,0);")
        self.pushButton_28.setObjectName("pushButton_28")
        self.textBrs_Width_left = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrs_Width_left.setGeometry(QtCore.QRect(130, 440, 91, 31))
        self.textBrs_Width_left.setObjectName("textBrs_Width_left")
        self.pushButton_29 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_29.setGeometry(QtCore.QRect(240, 400, 93, 28))
        self.pushButton_29.setStyleSheet("background-color: #004580;\n"
"color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"\n"
"border:2px solid rgb(0,0,0);")
        self.pushButton_29.setObjectName("pushButton_29")
        self.pushButton_30 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_30.setGeometry(QtCore.QRect(20, 400, 93, 28))
        self.pushButton_30.setStyleSheet("background-color: #004580;\n"
"color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"\n"
"border:2px solid rgb(0,0,0);")
        self.pushButton_30.setObjectName("pushButton_30")
        self.textBrs_Length_left = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrs_Length_left.setGeometry(QtCore.QRect(20, 440, 91, 31))
        self.textBrs_Length_left.setObjectName("textBrs_Length_left")
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(860, 110, 93, 28))
        self.pushButton_17.setStyleSheet("background-color: #004580;\n"
"color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"\n"
"border:2px solid rgb(0,0,0);")
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(860, 400, 93, 28))
        self.pushButton_18.setStyleSheet("background-color: #004580;\n"
"color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"\n"
"border:2px solid rgb(0,0,0);")
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_Receive = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Receive.setGeometry(QtCore.QRect(290, 600, 93, 28))
        self.pushButton_Receive.setStyleSheet("background-color: #004580;\n"
"color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"\n"
"border:2px solid rgb(0,0,0);")
        self.pushButton_Receive.setObjectName("pushButton_Receive")
        self.pushButton_Solve = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Solve.setGeometry(QtCore.QRect(420, 600, 93, 28))
        self.pushButton_Solve.setStyleSheet("background-color: #004580;\n"
"color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"\n"
"border:2px solid rgb(0,0,0);")
        self.pushButton_Solve.setObjectName("pushButton_Solve")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(450, 100, 381, 481))
        self.groupBox_2.setStyleSheet("background-color: ;\n"
"color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"")
        self.groupBox_2.setObjectName("groupBox_2")
        self.textBrs_UX_right = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrs_UX_right.setGeometry(QtCore.QRect(20, 80, 91, 31))
        self.textBrs_UX_right.setObjectName("textBrs_UX_right")
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_11.setGeometry(QtCore.QRect(20, 40, 93, 28))
        self.pushButton_11.setStyleSheet("background-color: #004580;\n"
"color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"\n"
"border:2px solid rgb(0,0,0);")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_12.setGeometry(QtCore.QRect(130, 40, 93, 28))
        self.pushButton_12.setStyleSheet("background-color: #004580;\n"
"color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"\n"
"border:2px solid rgb(0,0,0);")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_13.setGeometry(QtCore.QRect(240, 40, 93, 28))
        self.pushButton_13.setStyleSheet("background-color: #004580;\n"
"color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"\n"
"border:2px solid rgb(0,0,0);")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_14.setGeometry(QtCore.QRect(20, 130, 93, 28))
        self.pushButton_14.setStyleSheet("background-color: #004580;\n"
"color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"\n"
"border:2px solid rgb(0,0,0);")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_15.setGeometry(QtCore.QRect(130, 130, 93, 28))
        self.pushButton_15.setStyleSheet("background-color: #004580;\n"
"color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"\n"
"border:2px solid rgb(0,0,0);")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_16.setGeometry(QtCore.QRect(240, 130, 93, 28))
        self.pushButton_16.setStyleSheet("background-color: #004580;\n"
"color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"\n"
"border:2px solid rgb(0,0,0);")
        self.pushButton_16.setObjectName("pushButton_16")
        self.textBrs_VX_right = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrs_VX_right.setGeometry(QtCore.QRect(130, 80, 91, 31))
        self.textBrs_VX_right.setObjectName("textBrs_VX_right")
        self.textBrs_WX_right = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrs_WX_right.setGeometry(QtCore.QRect(240, 80, 91, 31))
        self.textBrs_WX_right.setObjectName("textBrs_WX_right")
        self.textBrs_WY_right = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrs_WY_right.setGeometry(QtCore.QRect(240, 170, 91, 31))
        self.textBrs_WY_right.setObjectName("textBrs_WY_right")
        self.textBrs_UY_right = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrs_UY_right.setGeometry(QtCore.QRect(20, 170, 91, 31))
        self.textBrs_UY_right.setObjectName("textBrs_UY_right")
        self.textBrs_VY_right = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrs_VY_right.setGeometry(QtCore.QRect(130, 170, 91, 31))
        self.textBrs_VY_right.setObjectName("textBrs_VY_right")
        self.pushButton_31 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_31.setGeometry(QtCore.QRect(240, 220, 93, 28))
        self.pushButton_31.setStyleSheet("background-color: #004580;\n"
"color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"\n"
"border:2px solid rgb(0,0,0);")
        self.pushButton_31.setObjectName("pushButton_31")
        self.textBrs_PX_right = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrs_PX_right.setGeometry(QtCore.QRect(20, 350, 91, 31))
        self.textBrs_PX_right.setObjectName("textBrs_PX_right")
        self.textBrs_WZ_right = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrs_WZ_right.setGeometry(QtCore.QRect(240, 260, 91, 31))
        self.textBrs_WZ_right.setObjectName("textBrs_WZ_right")
        self.pushButton_32 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_32.setGeometry(QtCore.QRect(130, 220, 93, 28))
        self.pushButton_32.setStyleSheet("background-color: #004580;\n"
"color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"\n"
"border:2px solid rgb(0,0,0);")
        self.pushButton_32.setObjectName("pushButton_32")
        self.textBrs_UZ_right = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrs_UZ_right.setGeometry(QtCore.QRect(20, 260, 91, 31))
        self.textBrs_UZ_right.setObjectName("textBrs_UZ_right")
        self.textBrs_PY_right = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrs_PY_right.setGeometry(QtCore.QRect(130, 350, 91, 31))
        self.textBrs_PY_right.setObjectName("textBrowser_27")
        self.pushButton_33 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_33.setGeometry(QtCore.QRect(130, 310, 93, 28))
        self.pushButton_33.setStyleSheet("background-color: #004580;\n"
"color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"\n"
"border:2px solid rgb(0,0,0);")
        self.pushButton_33.setObjectName("pushButton_33")
        self.pushButton_34 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_34.setGeometry(QtCore.QRect(240, 310, 93, 28))
        self.pushButton_34.setStyleSheet("background-color: #004580;\n"
"color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"\n"
"border:2px solid rgb(0,0,0);")
        self.pushButton_34.setObjectName("pushButton_34")
        self.pushButton_35 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_35.setGeometry(QtCore.QRect(20, 220, 93, 28))
        self.pushButton_35.setStyleSheet("background-color: #004580;\n"
"color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"\n"
"border:2px solid rgb(0,0,0);")
        self.pushButton_35.setObjectName("pushButton_35")
        self.textBrs_VZ_right = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrs_VZ_right.setGeometry(QtCore.QRect(130, 260, 91, 31))
        self.textBrs_VZ_right.setObjectName("textBrowser_28")
        self.textBrs_PZ_right = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrs_PZ_right.setGeometry(QtCore.QRect(240, 350, 91, 31))
        self.textBrs_PZ_right.setObjectName("textBrs_PZ_right")
        self.pushButton_36 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_36.setGeometry(QtCore.QRect(20, 310, 93, 28))
        self.pushButton_36.setStyleSheet("background-color: #004580;\n"
"color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"\n"
"border:2px solid rgb(0,0,0);")
        self.pushButton_36.setObjectName("pushButton_36")
        self.textBrs_Height_right = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrs_Height_right.setGeometry(QtCore.QRect(240, 440, 91, 31))
        self.textBrs_Height_right.setObjectName("textBrs_Height_right")
        self.pushButton_37 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_37.setGeometry(QtCore.QRect(130, 400, 93, 28))
        self.pushButton_37.setStyleSheet("background-color: #004580;\n"
"color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"\n"
"border:2px solid rgb(0,0,0);")
        self.pushButton_37.setObjectName("pushButton_37")
        self.textBrs_Width_right = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrs_Width_right.setGeometry(QtCore.QRect(130, 440, 91, 31))
        self.textBrs_Width_right.setObjectName("textBrs_Width_right")
        self.pushButton_38 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_38.setGeometry(QtCore.QRect(240, 400, 93, 28))
        self.pushButton_38.setStyleSheet("background-color: #004580;\n"
"color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"\n"
"border:2px solid rgb(0,0,0);")
        self.pushButton_38.setObjectName("pushButton_38")
        self.pushButton_39 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_39.setGeometry(QtCore.QRect(20, 400, 93, 28))
        self.pushButton_39.setStyleSheet("background-color: #004580;\n"
"color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"\n"
"border:2px solid rgb(0,0,0);")
        self.pushButton_39.setObjectName("pushButton_39")
        self.textBrs_Length_right = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrs_Length_right.setGeometry(QtCore.QRect(20, 440, 91, 31))
        self.textBrs_Length_right.setObjectName("textBrs_Length_right")
        self.pushButton_Online = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Online.setGeometry(QtCore.QRect(550, 600, 93, 28))
        self.pushButton_Online.setStyleSheet("background-color: #004580;\n"
"color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"\n"
"border:2px solid rgb(0,0,0);")
        self.pushButton_Online.setObjectName("pushButton_Online")
        MainWindow.setCentralWidget(self.centralwidget)

        self.pushButton_Receive.clicked.connect(self.receive_button_clicked)
        self.pushButton_Solve.clicked.connect(self.solve_button_clicked)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">UNIVERSITY OF ENGINEERING AND TECHNOLOGY</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">BUILD ALGORITHMS OF HUMAN MANIPULATION FOR DUAL ARM ROBOTICS </span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>Student: Nguyen Viet Tuan</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "ID: 20021206"))
        self.label_5.setText(_translate("MainWindow", "Instructor: PhD. Do Tran Thang"))
        self.groupBox.setTitle(_translate("MainWindow", "Left Arm"))
        self.pushButton_5.setText(_translate("MainWindow", "U(X)"))
        self.pushButton_6.setText(_translate("MainWindow", "V(X)"))
        self.pushButton_7.setText(_translate("MainWindow", "W(X)"))
        self.pushButton_8.setText(_translate("MainWindow", "U(Y)"))
        self.pushButton_9.setText(_translate("MainWindow", "V(Y)"))
        self.pushButton_10.setText(_translate("MainWindow", "W(Y)"))
        self.pushButton_22.setText(_translate("MainWindow", "W(Z)"))
        self.pushButton_23.setText(_translate("MainWindow", "V(Z)"))
        self.pushButton_24.setText(_translate("MainWindow", "P(Y)"))
        self.pushButton_25.setText(_translate("MainWindow", "P(Z)"))
        self.pushButton_26.setText(_translate("MainWindow", "U(Z)"))
        self.pushButton_27.setText(_translate("MainWindow", "P(X)"))
        self.pushButton_28.setText(_translate("MainWindow", "Width"))
        self.pushButton_29.setText(_translate("MainWindow", "Height"))
        self.pushButton_30.setText(_translate("MainWindow", "Length"))
        self.pushButton_17.setText(_translate("MainWindow", "Left Arm"))
        self.pushButton_18.setText(_translate("MainWindow", "Right Arm"))
        self.pushButton_Receive.setText(_translate("MainWindow", "Receive"))
        self.pushButton_Solve.setText(_translate("MainWindow", "Solve"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Right Arm"))
        self.pushButton_11.setText(_translate("MainWindow", "U(X)"))
        self.pushButton_12.setText(_translate("MainWindow", "V(X)"))
        self.pushButton_13.setText(_translate("MainWindow", "W(X)"))
        self.pushButton_14.setText(_translate("MainWindow", "U(Y)"))
        self.pushButton_15.setText(_translate("MainWindow", "V(Y)"))
        self.pushButton_16.setText(_translate("MainWindow", "W(Y)"))
        self.pushButton_31.setText(_translate("MainWindow", "W(Z)"))
        self.pushButton_32.setText(_translate("MainWindow", "V(Z)"))
        self.pushButton_33.setText(_translate("MainWindow", "P(Y)"))
        self.pushButton_34.setText(_translate("MainWindow", "P(Z)"))
        self.pushButton_35.setText(_translate("MainWindow", "U(Z)"))
        self.pushButton_36.setText(_translate("MainWindow", "P(X)"))
        self.pushButton_37.setText(_translate("MainWindow", "Width"))
        self.pushButton_38.setText(_translate("MainWindow", "Height"))
        self.pushButton_39.setText(_translate("MainWindow", "Length"))
        self.pushButton_Online.setText(_translate("MainWindow", "Online"))
    def receive_button_clicked(self):
        # Assigning values from arrays to variables for left arm
        self.x_left = position_receive[0]
        self.y_left = position_receive[1]
        self.z_left = position_receive[2]
        
        for i in range(len(orientation_matrix_receive)):
            for j in range(len(orientation_matrix_receive[0])):
                self.matrix_left[i][j] = orientation_matrix_receive[i][j]
        # Assigning values from arrays to variables for right arm
        self.x_right = position_receive[0]
        self.y_right = position_receive[1]
        self.z_right = position_receive[2]
        for i in range(len(orientation_matrix_receive)):
            for j in range(len(orientation_matrix_receive[0])):
                self.matrix_right[i][j] = orientation_matrix_receive[i][j]
        #Display data of left arm
        self.textBrs_PX_left.setText(str(self.x_left))
        self.textBrs_PY_left.setText(str(self.y_left))
        self.textBrs_PZ_left.setText(str(self.z_left))
        self.textBrs_UX_left.setText(str(self.matrix_left[0][0]))
        self.textBrs_VX_left.setText(str(self.matrix_left[0][1]))
        self.textBrs_WX_left.setText(str(self.matrix_left[0][2]))
        self.textBrs_UY_left.setText(str(self.matrix_left[1][0]))
        self.textBrs_VY_left.setText(str(self.matrix_left[1][1]))
        self.textBrs_WY_left.setText(str(self.matrix_left[1][2]))
        self.textBrs_UZ_left.setText(str(self.matrix_left[2][0]))
        self.textBrs_VZ_left.setText(str(self.matrix_left[2][1]))
        self.textBrs_WZ_left.setText(str(self.matrix_left[2][2]))

        #Display data of right
        self.textBrs_PX_right.setText(str(self.x_right))
        self.textBrs_PY_right.setText(str(self.y_right))
        self.textBrs_PZ_right.setText(str(self.z_right))
        self.textBrs_UX_right.setText(str(self.matrix_right[0][0]))
        self.textBrs_VX_right.setText(str(self.matrix_right[0][1]))
        self.textBrs_WX_right.setText(str(self.matrix_right[0][2]))
        self.textBrs_UY_right.setText(str(self.matrix_right[1][0]))
        self.textBrs_VY_right.setText(str(self.matrix_right[1][1]))
        self.textBrs_WY_right.setText(str(self.matrix_right[1][2]))
        self.textBrs_UZ_right.setText(str(self.matrix_right[2][0]))
        self.textBrs_VZ_right.setText(str(self.matrix_right[2][1]))
        self.textBrs_WZ_right.setText(str(self.matrix_right[2][2]))
    def solve_button_clicked(self):
        if any(v is None for v in [self.x_left, self.y_left, self.z_left,
                            self.matrix_left,
                            self.x_right, self.y_right, self.z_right,
                            self.matrix_right]):
        # Show a message box indicating that data needs to be received first
            QMessageBox.warning(None, "Warning", "Please receive data first.")
            return
        position_left_arm = [
            self.x_left,
            self.y_left,
            self.z_left
        ]
        orientation_left_arm = matrix_to_ur_euler(np.array(self.matrix_left))
        position_right_arm = [
            self.x_right,
            self.y_right,
            self.z_right
        ]
        orientation_right_arm = matrix_to_ur_euler(np.array(self.matrix_right))
        left_result, right_result = self.execute_IK(position_left_arm, orientation_left_arm, position_right_arm, orientation_right_arm, DH)
        self.textBrs_box_left.setText("Left Arm Result:\n" + str(left_result))
        self.textBrs_box_right.setText("Right Arm Result:\n" + str(right_result))
    def execute_IK(self, position_left, orientation_left, position_right, orientation_right,DH):
        left_arm_solver = ikSolver(DH)
        right_arm_solver = ikSolver(DH)  

        # Convert data of left arm  
        position_left_arm = np.array(position_left)
        orientation_left_arm = np.array(orientation_left)
        left_arm_T06 = left_arm_solver.create_Transformation_Matrix(position_left_arm, orientation_left_arm,DH['offset'])

        # Convert data of right arm
        position_right_arm = np.array(position_right)
        orientation_right_arm = np.array(orientation_right)
        right_arm_T06 = right_arm_solver.create_Transformation_Matrix(position_right_arm, orientation_right_arm,DH['offset'])
 
        # Create combined IK solver
        combined_solver = CombinedIKSolver(DH)

        # Solve inverse kinematics for both arms simultaneously
        left_q, right_q = combined_solver.solveIK(left_arm_T06, right_arm_T06)
        if np.any(np.isnan(left_q)) or np.any(np.isnan(right_q)):
            left_result = "Flag = 1"
            right_result = "Flag = 1"
            return left_result, right_result
        else:
            left_result = f"Left Arm IK Solution:\nJoint Angles (q): {left_q}\n"
            right_result = f"\nRight Arm IK Solution:\nJoint Angles (q): {right_q}\n"
            # print(left_result + right_result)
            return left_result, right_result

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_4()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
