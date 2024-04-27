# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sidebar.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(950, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.search_tool = QtWidgets.QWidget(self.widget_3)
        self.search_tool.setMinimumSize(QtCore.QSize(0, 40))
        self.search_tool.setObjectName("search_tool")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.search_tool)
        self.horizontalLayout_4.setContentsMargins(0, 0, 9, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.change_btn = QtWidgets.QPushButton(self.search_tool)
        self.change_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../sidebar_test/icon/icon/menu-4-32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.change_btn.setIcon(icon)
        self.change_btn.setIconSize(QtCore.QSize(14, 14))
        self.change_btn.setCheckable(True)
        self.change_btn.setObjectName("change_btn")
        self.horizontalLayout_4.addWidget(self.change_btn)
        spacerItem = QtWidgets.QSpacerItem(236, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.search_input = QtWidgets.QLineEdit(self.search_tool)
        self.search_input.setObjectName("search_input")
        self.horizontalLayout.addWidget(self.search_input)
        self.search_btn = QtWidgets.QPushButton(self.search_tool)
        self.search_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../#010_sidebar/icon/icon/search-13-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_btn.setIcon(icon1)
        self.search_btn.setObjectName("search_btn")
        self.horizontalLayout.addWidget(self.search_btn)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(236, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.user_btn = QtWidgets.QPushButton(self.search_tool)
        self.user_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../#010_sidebar/icon/icon/user-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.user_btn.setIcon(icon2)
        self.user_btn.setObjectName("user_btn")
        self.horizontalLayout_4.addWidget(self.user_btn)
        self.verticalLayout_5.addWidget(self.search_tool)
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget_3)
        self.stackedWidget.setObjectName("stackedWidget")
        self.homepage = QtWidgets.QWidget()
        self.homepage.setObjectName("homepage")
        self.homepage_label = QtWidgets.QLabel(self.homepage)
        self.homepage_label.setGeometry(QtCore.QRect(311, 9, 136, 33))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.homepage_label.setFont(font)
        self.homepage_label.setAlignment(QtCore.Qt.AlignCenter)
        self.homepage_label.setObjectName("homepage_label")
        self.stackedWidget.addWidget(self.homepage)
        self.senddatapage = QtWidgets.QWidget()
        self.senddatapage.setObjectName("senddatapage")
        self.senddata_label_2 = QtWidgets.QLabel(self.senddatapage)
        self.senddata_label_2.setGeometry(QtCore.QRect(311, 9, 171, 33))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.senddata_label_2.setFont(font)
        self.senddata_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.senddata_label_2.setObjectName("senddata_label_2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.senddatapage)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(160, 90, 451, 311))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.vy_entry = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.vy_entry.setObjectName("vy_entry")
        self.gridLayout_2.addWidget(self.vy_entry, 3, 1, 1, 1)
        self.wx_entry = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.wx_entry.setObjectName("wx_entry")
        self.gridLayout_2.addWidget(self.wx_entry, 1, 2, 1, 1)
        self.height_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.height_label.setAlignment(QtCore.Qt.AlignCenter)
        self.height_label.setObjectName("height_label")
        self.gridLayout_2.addWidget(self.height_label, 8, 2, 1, 1)
        self.py_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.py_label.setAlignment(QtCore.Qt.AlignCenter)
        self.py_label.setObjectName("py_label")
        self.gridLayout_2.addWidget(self.py_label, 6, 1, 1, 1)
        self.pz_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.pz_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pz_label.setObjectName("pz_label")
        self.gridLayout_2.addWidget(self.pz_label, 6, 2, 1, 1)
        self.length_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.length_label.setAlignment(QtCore.Qt.AlignCenter)
        self.length_label.setObjectName("length_label")
        self.gridLayout_2.addWidget(self.length_label, 8, 0, 1, 1)
        self.px_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.px_label.setAlignment(QtCore.Qt.AlignCenter)
        self.px_label.setObjectName("px_label")
        self.gridLayout_2.addWidget(self.px_label, 6, 0, 1, 1)
        self.ux_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.ux_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ux_label.setObjectName("ux_label")
        self.gridLayout_2.addWidget(self.ux_label, 0, 0, 1, 1)
        self.vx_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.vx_label.setAlignment(QtCore.Qt.AlignCenter)
        self.vx_label.setObjectName("vx_label")
        self.gridLayout_2.addWidget(self.vx_label, 0, 1, 1, 1)
        self.wx_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.wx_label.setAlignment(QtCore.Qt.AlignCenter)
        self.wx_label.setObjectName("wx_label")
        self.gridLayout_2.addWidget(self.wx_label, 0, 2, 1, 1)
        self.uy_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.uy_label.setAlignment(QtCore.Qt.AlignCenter)
        self.uy_label.setObjectName("uy_label")
        self.gridLayout_2.addWidget(self.uy_label, 2, 0, 1, 1)
        self.vy_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.vy_label.setAlignment(QtCore.Qt.AlignCenter)
        self.vy_label.setObjectName("vy_label")
        self.gridLayout_2.addWidget(self.vy_label, 2, 1, 1, 1)
        self.wy_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.wy_label.setAlignment(QtCore.Qt.AlignCenter)
        self.wy_label.setObjectName("wy_label")
        self.gridLayout_2.addWidget(self.wy_label, 2, 2, 1, 1)
        self.uz_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.uz_label.setAlignment(QtCore.Qt.AlignCenter)
        self.uz_label.setObjectName("uz_label")
        self.gridLayout_2.addWidget(self.uz_label, 4, 0, 1, 1)
        self.vz_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.vz_label.setAlignment(QtCore.Qt.AlignCenter)
        self.vz_label.setObjectName("vz_label")
        self.gridLayout_2.addWidget(self.vz_label, 4, 1, 1, 1)
        self.wz_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.wz_label.setAlignment(QtCore.Qt.AlignCenter)
        self.wz_label.setObjectName("wz_label")
        self.gridLayout_2.addWidget(self.wz_label, 4, 2, 1, 1)
        self.wy_entry = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.wy_entry.setObjectName("wy_entry")
        self.gridLayout_2.addWidget(self.wy_entry, 3, 2, 1, 1)
        self.width_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.width_label.setAlignment(QtCore.Qt.AlignCenter)
        self.width_label.setObjectName("width_label")
        self.gridLayout_2.addWidget(self.width_label, 8, 1, 1, 1)
        self.uz_entry = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.uz_entry.setObjectName("uz_entry")
        self.gridLayout_2.addWidget(self.uz_entry, 5, 0, 1, 1)
        self.vz_entry = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.vz_entry.setObjectName("vz_entry")
        self.gridLayout_2.addWidget(self.vz_entry, 5, 1, 1, 1)
        self.wz_entry = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.wz_entry.setObjectName("wz_entry")
        self.gridLayout_2.addWidget(self.wz_entry, 5, 2, 1, 1)
        self.pz_entry = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.pz_entry.setObjectName("pz_entry")
        self.gridLayout_2.addWidget(self.pz_entry, 7, 2, 1, 1)
        self.px_entry = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.px_entry.setObjectName("px_entry")
        self.gridLayout_2.addWidget(self.px_entry, 7, 0, 1, 1)
        self.py_entry = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.py_entry.setObjectName("py_entry")
        self.gridLayout_2.addWidget(self.py_entry, 7, 1, 1, 1)
        self.length_entry = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.length_entry.setObjectName("length_entry")
        self.gridLayout_2.addWidget(self.length_entry, 9, 0, 1, 1)
        self.width_entry = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.width_entry.setObjectName("width_entry")
        self.gridLayout_2.addWidget(self.width_entry, 9, 1, 1, 1)
        self.height_entry = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.height_entry.setObjectName("height_entry")
        self.gridLayout_2.addWidget(self.height_entry, 9, 2, 1, 1)
        self.ux_entry = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.ux_entry.setObjectName("ux_entry")
        self.gridLayout_2.addWidget(self.ux_entry, 1, 0, 1, 1)
        self.uy_entry = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.uy_entry.setObjectName("uy_entry")
        self.gridLayout_2.addWidget(self.uy_entry, 3, 0, 1, 1)
        self.vx_entry = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.vx_entry.setObjectName("vx_entry")
        self.gridLayout_2.addWidget(self.vx_entry, 1, 1, 1, 1)
        self.sendata_button = QtWidgets.QPushButton(self.senddatapage)
        self.sendata_button.setGeometry(QtCore.QRect(340, 420, 81, 31))
        self.sendata_button.setObjectName("sendata_button")
        self.stackedWidget.addWidget(self.senddatapage)
        self.getdatapage = QtWidgets.QWidget()
        self.getdatapage.setObjectName("getdatapage")
        self.getdata_button = QtWidgets.QPushButton(self.getdatapage)
        self.getdata_button.setGeometry(QtCore.QRect(430, 420, 91, 31))
        self.getdata_button.setObjectName("getdata_button")
        self.choose_button = QtWidgets.QPushButton(self.getdatapage)
        self.choose_button.setGeometry(QtCore.QRect(240, 420, 91, 31))
        self.choose_button.setObjectName("choose_button")
        self.choose_label = QtWidgets.QLabel(self.getdatapage)
        self.choose_label.setGeometry(QtCore.QRect(310, 460, 101, 20))
        self.choose_label.setAlignment(QtCore.Qt.AlignCenter)
        self.choose_label.setObjectName("choose_label")
        self.layoutWidget = QtWidgets.QWidget(self.getdatapage)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 90, 761, 311))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.vy_entry_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.vy_entry_2.setObjectName("vy_entry_2")
        self.gridLayout_3.addWidget(self.vy_entry_2, 3, 1, 1, 1)
        self.wx_entry_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.wx_entry_2.setObjectName("wx_entry_2")
        self.gridLayout_3.addWidget(self.wx_entry_2, 1, 2, 1, 1)
        self.height_label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.height_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.height_label_2.setObjectName("height_label_2")
        self.gridLayout_3.addWidget(self.height_label_2, 8, 2, 1, 1)
        self.py_label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.py_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.py_label_2.setObjectName("py_label_2")
        self.gridLayout_3.addWidget(self.py_label_2, 6, 1, 1, 1)
        self.pz_label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.pz_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.pz_label_2.setObjectName("pz_label_2")
        self.gridLayout_3.addWidget(self.pz_label_2, 6, 2, 1, 1)
        self.length_label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.length_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.length_label_2.setObjectName("length_label_2")
        self.gridLayout_3.addWidget(self.length_label_2, 8, 0, 1, 1)
        self.px_label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.px_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.px_label_2.setObjectName("px_label_2")
        self.gridLayout_3.addWidget(self.px_label_2, 6, 0, 1, 1)
        self.ux_label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.ux_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.ux_label_2.setObjectName("ux_label_2")
        self.gridLayout_3.addWidget(self.ux_label_2, 0, 0, 1, 1)
        self.vx_label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.vx_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.vx_label_2.setObjectName("vx_label_2")
        self.gridLayout_3.addWidget(self.vx_label_2, 0, 1, 1, 1)
        self.wx_label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.wx_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.wx_label_2.setObjectName("wx_label_2")
        self.gridLayout_3.addWidget(self.wx_label_2, 0, 2, 1, 1)
        self.uy_label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.uy_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.uy_label_2.setObjectName("uy_label_2")
        self.gridLayout_3.addWidget(self.uy_label_2, 2, 0, 1, 1)
        self.vy_label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.vy_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.vy_label_2.setObjectName("vy_label_2")
        self.gridLayout_3.addWidget(self.vy_label_2, 2, 1, 1, 1)
        self.wy_label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.wy_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.wy_label_2.setObjectName("wy_label_2")
        self.gridLayout_3.addWidget(self.wy_label_2, 2, 2, 1, 1)
        self.uz_label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.uz_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.uz_label_2.setObjectName("uz_label_2")
        self.gridLayout_3.addWidget(self.uz_label_2, 4, 0, 1, 1)
        self.vz_label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.vz_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.vz_label_2.setObjectName("vz_label_2")
        self.gridLayout_3.addWidget(self.vz_label_2, 4, 1, 1, 1)
        self.wz_label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.wz_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.wz_label_2.setObjectName("wz_label_2")
        self.gridLayout_3.addWidget(self.wz_label_2, 4, 2, 1, 1)
        self.wy_entry_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.wy_entry_2.setObjectName("wy_entry_2")
        self.gridLayout_3.addWidget(self.wy_entry_2, 3, 2, 1, 1)
        self.width_label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.width_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.width_label_2.setObjectName("width_label_2")
        self.gridLayout_3.addWidget(self.width_label_2, 8, 1, 1, 1)
        self.uz_entry_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.uz_entry_2.setObjectName("uz_entry_2")
        self.gridLayout_3.addWidget(self.uz_entry_2, 5, 0, 1, 1)
        self.vz_entry_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.vz_entry_2.setObjectName("vz_entry_2")
        self.gridLayout_3.addWidget(self.vz_entry_2, 5, 1, 1, 1)
        self.wz_entry_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.wz_entry_2.setObjectName("wz_entry_2")
        self.gridLayout_3.addWidget(self.wz_entry_2, 5, 2, 1, 1)
        self.pz_entry_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.pz_entry_2.setObjectName("pz_entry_2")
        self.gridLayout_3.addWidget(self.pz_entry_2, 7, 2, 1, 1)
        self.px_entry_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.px_entry_2.setObjectName("px_entry_2")
        self.gridLayout_3.addWidget(self.px_entry_2, 7, 0, 1, 1)
        self.py_entry_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.py_entry_2.setObjectName("py_entry_2")
        self.gridLayout_3.addWidget(self.py_entry_2, 7, 1, 1, 1)
        self.length_entry_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.length_entry_2.setObjectName("length_entry_2")
        self.gridLayout_3.addWidget(self.length_entry_2, 9, 0, 1, 1)
        self.width_entry_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.width_entry_2.setObjectName("width_entry_2")
        self.gridLayout_3.addWidget(self.width_entry_2, 9, 1, 1, 1)
        self.height_entry_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.height_entry_2.setObjectName("height_entry_2")
        self.gridLayout_3.addWidget(self.height_entry_2, 9, 2, 1, 1)
        self.ux_entry_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.ux_entry_2.setObjectName("ux_entry_2")
        self.gridLayout_3.addWidget(self.ux_entry_2, 1, 0, 1, 1)
        self.uy_entry_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.uy_entry_2.setObjectName("uy_entry_2")
        self.gridLayout_3.addWidget(self.uy_entry_2, 3, 0, 1, 1)
        self.vx_entry_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.vx_entry_2.setObjectName("vx_entry_2")
        self.gridLayout_3.addWidget(self.vx_entry_2, 1, 1, 1, 1)
        self.horizontalLayout_6.addLayout(self.gridLayout_3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.layoutWidget1 = QtWidgets.QWidget(self.getdatapage)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 20, 761, 35))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.getdata_label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.getdata_label.setFont(font)
        self.getdata_label.setAlignment(QtCore.Qt.AlignCenter)
        self.getdata_label.setObjectName("getdata_label")
        self.horizontalLayout_7.addWidget(self.getdata_label)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.passdata_button = QtWidgets.QPushButton(self.getdatapage)
        self.passdata_button.setGeometry(QtCore.QRect(320, 510, 91, 23))
        self.passdata_button.setObjectName("passdata_button")
        self.stackedWidget.addWidget(self.getdatapage)
        self.tablepage = QtWidgets.QWidget()
        self.tablepage.setObjectName("tablepage")
        self.table_label = QtWidgets.QLabel(self.tablepage)
        self.table_label.setGeometry(QtCore.QRect(311, 9, 148, 33))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.table_label.setFont(font)
        self.table_label.setAlignment(QtCore.Qt.AlignCenter)
        self.table_label.setObjectName("table_label")
        self.stackedWidget.addWidget(self.tablepage)
        self.chatpage = QtWidgets.QWidget()
        self.chatpage.setObjectName("chatpage")
        self.link_entry = QtWidgets.QLineEdit(self.chatpage)
        self.link_entry.setGeometry(QtCore.QRect(160, 250, 391, 20))
        self.link_entry.setObjectName("link_entry")
        self.browser_button = QtWidgets.QPushButton(self.chatpage)
        self.browser_button.setGeometry(QtCore.QRect(560, 250, 31, 23))
        self.browser_button.setObjectName("browser_button")
        self.sendfile_button = QtWidgets.QPushButton(self.chatpage)
        self.sendfile_button.setGeometry(QtCore.QRect(600, 250, 75, 23))
        self.sendfile_button.setObjectName("sendfile_button")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.chatpage)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(80, 10, 611, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.chat_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.chat_label.setFont(font)
        self.chat_label.setAlignment(QtCore.Qt.AlignCenter)
        self.chat_label.setObjectName("chat_label")
        self.horizontalLayout_5.addWidget(self.chat_label)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.stackedWidget.addWidget(self.chatpage)
        self.searchpage = QtWidgets.QWidget()
        self.searchpage.setObjectName("searchpage")
        self.search_label = QtWidgets.QLabel(self.searchpage)
        self.search_label.setGeometry(QtCore.QRect(311, 9, 146, 33))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.search_label.setFont(font)
        self.search_label.setAlignment(QtCore.Qt.AlignCenter)
        self.search_label.setObjectName("search_label")
        self.stackedWidget.addWidget(self.searchpage)
        self.userpage = QtWidgets.QWidget()
        self.userpage.setObjectName("userpage")
        self.user_label = QtWidgets.QLabel(self.userpage)
        self.user_label.setGeometry(QtCore.QRect(311, 9, 120, 33))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.user_label.setFont(font)
        self.user_label.setAlignment(QtCore.Qt.AlignCenter)
        self.user_label.setObjectName("user_label")
        self.stackedWidget.addWidget(self.userpage)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.gridLayout.addWidget(self.widget_3, 0, 2, 1, 1)
        self.icon_only_widget = QtWidgets.QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName("icon_only_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.logo_label_1 = QtWidgets.QLabel(self.icon_only_widget)
        self.logo_label_1.setMinimumSize(QtCore.QSize(50, 50))
        self.logo_label_1.setMaximumSize(QtCore.QSize(50, 50))
        self.logo_label_1.setText("")
        self.logo_label_1.setPixmap(QtGui.QPixmap("../sidebar_test/icon/1200px-Logo_HUET.svg.png"))
        self.logo_label_1.setScaledContents(True)
        self.logo_label_1.setObjectName("logo_label_1")
        self.horizontalLayout_3.addWidget(self.logo_label_1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.home_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.home_btn_1.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../#010_sidebar/icon/icon/home-4-32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap("../#010_sidebar/icon/icon/home-4-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.home_btn_1.setIcon(icon3)
        self.home_btn_1.setIconSize(QtCore.QSize(20, 20))
        self.home_btn_1.setCheckable(True)
        self.home_btn_1.setAutoExclusive(True)
        self.home_btn_1.setObjectName("home_btn_1")
        self.verticalLayout.addWidget(self.home_btn_1)
        self.dashborad_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.dashborad_btn_1.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../#010_sidebar/icon/icon/dashboard-5-32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap("../#010_sidebar/icon/icon/dashboard-5-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.dashborad_btn_1.setIcon(icon4)
        self.dashborad_btn_1.setIconSize(QtCore.QSize(20, 20))
        self.dashborad_btn_1.setCheckable(True)
        self.dashborad_btn_1.setAutoExclusive(True)
        self.dashborad_btn_1.setObjectName("dashborad_btn_1")
        self.verticalLayout.addWidget(self.dashborad_btn_1)
        self.orders_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.orders_btn_1.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../#010_sidebar/icon/icon/activity-feed-32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon5.addPixmap(QtGui.QPixmap("../#010_sidebar/icon/icon/activity-feed-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.orders_btn_1.setIcon(icon5)
        self.orders_btn_1.setIconSize(QtCore.QSize(20, 20))
        self.orders_btn_1.setCheckable(True)
        self.orders_btn_1.setAutoExclusive(True)
        self.orders_btn_1.setObjectName("orders_btn_1")
        self.verticalLayout.addWidget(self.orders_btn_1)
        self.products_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.products_btn_1.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../#010_sidebar/icon/icon/product-32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon6.addPixmap(QtGui.QPixmap("../#010_sidebar/icon/icon/product-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.products_btn_1.setIcon(icon6)
        self.products_btn_1.setIconSize(QtCore.QSize(20, 20))
        self.products_btn_1.setCheckable(True)
        self.products_btn_1.setAutoExclusive(True)
        self.products_btn_1.setObjectName("products_btn_1")
        self.verticalLayout.addWidget(self.products_btn_1)
        self.customers_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.customers_btn_1.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../#010_sidebar/icon/icon/group-32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.customers_btn_1.setIcon(icon7)
        self.customers_btn_1.setIconSize(QtCore.QSize(20, 20))
        self.customers_btn_1.setCheckable(True)
        self.customers_btn_1.setAutoExclusive(True)
        self.customers_btn_1.setObjectName("customers_btn_1")
        self.verticalLayout.addWidget(self.customers_btn_1)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        spacerItem8 = QtWidgets.QSpacerItem(20, 375, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem8)
        self.exit_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.exit_btn_1.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icon/icon/close-window-64.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_btn_1.setIcon(icon8)
        self.exit_btn_1.setIconSize(QtCore.QSize(20, 20))
        self.exit_btn_1.setObjectName("exit_btn_1")
        self.verticalLayout_3.addWidget(self.exit_btn_1)
        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)
        self.full_menu_widget = QtWidgets.QWidget(self.centralwidget)
        self.full_menu_widget.setObjectName("full_menu_widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.full_menu_widget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.logo_label_2 = QtWidgets.QLabel(self.full_menu_widget)
        self.logo_label_2.setMinimumSize(QtCore.QSize(40, 40))
        self.logo_label_2.setMaximumSize(QtCore.QSize(40, 40))
        self.logo_label_2.setText("")
        self.logo_label_2.setPixmap(QtGui.QPixmap("sidebar_test/icon/1200px-Logo_HUET.svg.png"))
        self.logo_label_2.setScaledContents(True)
        self.logo_label_2.setObjectName("logo_label_2")
        self.horizontalLayout_2.addWidget(self.logo_label_2)
        self.logo_label_3 = QtWidgets.QLabel(self.full_menu_widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.logo_label_3.setFont(font)
        self.logo_label_3.setObjectName("logo_label_3")
        self.horizontalLayout_2.addWidget(self.logo_label_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.home_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        self.home_btn_2.setIcon(icon3)
        self.home_btn_2.setIconSize(QtCore.QSize(14, 14))
        self.home_btn_2.setCheckable(True)
        self.home_btn_2.setAutoExclusive(True)
        self.home_btn_2.setObjectName("home_btn_2")
        self.verticalLayout_2.addWidget(self.home_btn_2)
        self.dashborad_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        self.dashborad_btn_2.setIcon(icon4)
        self.dashborad_btn_2.setIconSize(QtCore.QSize(14, 14))
        self.dashborad_btn_2.setCheckable(True)
        self.dashborad_btn_2.setAutoExclusive(True)
        self.dashborad_btn_2.setObjectName("dashborad_btn_2")
        self.verticalLayout_2.addWidget(self.dashborad_btn_2)
        self.orders_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        self.orders_btn_2.setIcon(icon5)
        self.orders_btn_2.setIconSize(QtCore.QSize(14, 14))
        self.orders_btn_2.setCheckable(True)
        self.orders_btn_2.setAutoExclusive(True)
        self.orders_btn_2.setObjectName("orders_btn_2")
        self.verticalLayout_2.addWidget(self.orders_btn_2)
        self.products_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        self.products_btn_2.setIcon(icon6)
        self.products_btn_2.setIconSize(QtCore.QSize(14, 14))
        self.products_btn_2.setCheckable(True)
        self.products_btn_2.setAutoExclusive(True)
        self.products_btn_2.setObjectName("products_btn_2")
        self.verticalLayout_2.addWidget(self.products_btn_2)
        self.customers_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("../#010_sidebar/icon/icon/group-32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon9.addPixmap(QtGui.QPixmap("../#010_sidebar/icon/icon/group-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.customers_btn_2.setIcon(icon9)
        self.customers_btn_2.setIconSize(QtCore.QSize(14, 14))
        self.customers_btn_2.setCheckable(True)
        self.customers_btn_2.setAutoExclusive(True)
        self.customers_btn_2.setObjectName("customers_btn_2")
        self.verticalLayout_2.addWidget(self.customers_btn_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem9 = QtWidgets.QSpacerItem(20, 373, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem9)
        self.exit_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        self.exit_btn_2.setIcon(icon8)
        self.exit_btn_2.setIconSize(QtCore.QSize(14, 14))
        self.exit_btn_2.setObjectName("exit_btn_2")
        self.verticalLayout_4.addWidget(self.exit_btn_2)
        self.gridLayout.addWidget(self.full_menu_widget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        self.change_btn.toggled['bool'].connect(self.icon_only_widget.setVisible)
        self.change_btn.toggled['bool'].connect(self.full_menu_widget.setHidden)
        self.home_btn_1.toggled['bool'].connect(self.home_btn_2.setChecked)
        self.dashborad_btn_1.toggled['bool'].connect(self.dashborad_btn_2.setChecked)
        self.orders_btn_1.toggled['bool'].connect(self.orders_btn_2.setChecked)
        self.products_btn_1.toggled['bool'].connect(self.products_btn_2.setChecked)
        self.customers_btn_1.toggled['bool'].connect(self.customers_btn_2.setChecked)
        self.home_btn_2.toggled['bool'].connect(self.home_btn_1.setChecked)
        self.dashborad_btn_2.toggled['bool'].connect(self.dashborad_btn_1.setChecked)
        self.orders_btn_2.toggled['bool'].connect(self.orders_btn_1.setChecked)
        self.products_btn_2.toggled['bool'].connect(self.products_btn_1.setChecked)
        self.customers_btn_2.toggled['bool'].connect(self.customers_btn_1.setChecked)
        self.exit_btn_2.clicked.connect(MainWindow.close)
        self.exit_btn_1.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.search_input.setPlaceholderText(_translate("MainWindow", "Search..."))
        self.homepage_label.setText(_translate("MainWindow", "Home Page"))
        self.senddata_label_2.setText(_translate("MainWindow", "Sendata page"))
        self.height_label.setText(_translate("MainWindow", "Height"))
        self.py_label.setText(_translate("MainWindow", "P(Y)"))
        self.pz_label.setText(_translate("MainWindow", "P(Z)"))
        self.length_label.setText(_translate("MainWindow", "Length"))
        self.px_label.setText(_translate("MainWindow", "P(X)"))
        self.ux_label.setText(_translate("MainWindow", "U(X)"))
        self.vx_label.setText(_translate("MainWindow", "V(X)"))
        self.wx_label.setText(_translate("MainWindow", "W(X)"))
        self.uy_label.setText(_translate("MainWindow", "U(Y)"))
        self.vy_label.setText(_translate("MainWindow", "V(Y)"))
        self.wy_label.setText(_translate("MainWindow", "W(Y)"))
        self.uz_label.setText(_translate("MainWindow", "U(Z)"))
        self.vz_label.setText(_translate("MainWindow", "V(Z)"))
        self.wz_label.setText(_translate("MainWindow", "W(Z)"))
        self.width_label.setText(_translate("MainWindow", "Width"))
        self.sendata_button.setText(_translate("MainWindow", "Send"))
        self.getdata_button.setText(_translate("MainWindow", "Get data"))
        self.choose_button.setText(_translate("MainWindow", "Choose"))
        self.choose_label.setText(_translate("MainWindow", "You choose row: "))
        self.height_label_2.setText(_translate("MainWindow", "Height"))
        self.py_label_2.setText(_translate("MainWindow", "P(Y)"))
        self.pz_label_2.setText(_translate("MainWindow", "P(Z)"))
        self.length_label_2.setText(_translate("MainWindow", "Length"))
        self.px_label_2.setText(_translate("MainWindow", "P(X)"))
        self.ux_label_2.setText(_translate("MainWindow", "U(X)"))
        self.vx_label_2.setText(_translate("MainWindow", "V(X)"))
        self.wx_label_2.setText(_translate("MainWindow", "W(X)"))
        self.uy_label_2.setText(_translate("MainWindow", "U(Y)"))
        self.vy_label_2.setText(_translate("MainWindow", "V(Y)"))
        self.wy_label_2.setText(_translate("MainWindow", "W(Y)"))
        self.uz_label_2.setText(_translate("MainWindow", "U(Z)"))
        self.vz_label_2.setText(_translate("MainWindow", "V(Z)"))
        self.wz_label_2.setText(_translate("MainWindow", "W(Z)"))
        self.width_label_2.setText(_translate("MainWindow", "Width"))
        self.getdata_label.setText(_translate("MainWindow", "Getdata Page"))
        self.passdata_button.setText(_translate("MainWindow", "Pass Data"))
        self.table_label.setText(_translate("MainWindow", "Table Page"))
        self.browser_button.setText(_translate("MainWindow", "..."))
        self.sendfile_button.setText(_translate("MainWindow", "Send"))
        self.chat_label.setText(_translate("MainWindow", "Chat Page"))
        self.search_label.setText(_translate("MainWindow", "Search Page"))
        self.user_label.setText(_translate("MainWindow", "User Page"))
        self.logo_label_3.setText(_translate("MainWindow", "Sidebar"))
        self.home_btn_2.setText(_translate("MainWindow", "Home"))
        self.dashborad_btn_2.setText(_translate("MainWindow", "Send data"))
        self.orders_btn_2.setText(_translate("MainWindow", "Get data"))
        self.products_btn_2.setText(_translate("MainWindow", "Table"))
        self.customers_btn_2.setText(_translate("MainWindow", "Chat"))
        self.exit_btn_2.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
