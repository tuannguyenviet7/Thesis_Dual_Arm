from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QVBoxLayout, QTextEdit, QMessageBox
import numpy as np
from ikSolver import ikSolver, CombinedIKSolver
import math
from data import *
DH = {'theta': [0, 0, 0, 0, 0, 0],
      'd': [241, 173.5, -38, 0, 95, 45],
      'a': [0, 335, 294, 0, 0, 0],
      'alpha': [np.pi / 2, 0, 0, -np.pi / 2, np.pi / 2, 0],
      'offset': [0, 0, 20, 0, 0, 0]}
class ResultWindow(QMainWindow):
    def __init__(self, left_result, right_result):
        super().__init__()
        self.setWindowTitle("IK Results")
        self.setGeometry(100, 100, 400, 300)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.left_result_text = QTextEdit()
        self.left_result_text.setPlainText(left_result)
        self.left_result_text.setReadOnly(True)

        self.right_result_text = QTextEdit()
        self.right_result_text.setPlainText(right_result)
        self.right_result_text.setReadOnly(True)

        layout.addWidget(self.left_result_text)
        layout.addWidget(self.right_result_text)
class Ui_MainWindow_4(object):
    def __init__(self):
        #Create a global variable in class
        self.x_left = None
        self.y_left = None
        self.z_left = None
        self.roll_left = None
        self.pitch_left = None
        self.Yaw_left = None
        self.x_right = None
        self.y_right = None
        self.z_right = None
        self.roll_right = None
        self.pitch_right = None
        self.Yaw_right = None
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 110, 55, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 210, 55, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 160, 55, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(120, 250, 55, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(120, 310, 55, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(120, 360, 55, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(450, 360, 55, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(450, 210, 55, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(450, 250, 55, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(450, 110, 55, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(450, 160, 55, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(450, 310, 55, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(110, 60, 181, 31))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(440, 60, 181, 31))
        self.label_14.setObjectName("label_14")
        #Set up Button 
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 430, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(270, 430, 93, 28))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 430, 93, 28 ))
        self.pushButton_2.setObjectName("pushButton_2")
        #Set up Spin Box 
        self.doubleSpinBox_1 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_1.setGeometry(QtCore.QRect(190, 100, 71, 31))
        self.doubleSpinBox_1.setObjectName("doubleSpinBox")
        self.doubleSpinBox_1.setSingleStep(0.1)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(190, 150, 71, 31))
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.doubleSpinBox_2.setSingleStep(0.1)
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_3.setGeometry(QtCore.QRect(190, 200, 71, 31))
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.doubleSpinBox_3.setSingleStep(0.1)
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_4.setGeometry(QtCore.QRect(190, 250, 71, 31))
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.doubleSpinBox_4.setSingleStep(0.1)
        self.doubleSpinBox_5 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_5.setGeometry(QtCore.QRect(190, 300, 71, 31))
        self.doubleSpinBox_5.setObjectName("doubleSpinBox_5")
        self.doubleSpinBox_5.setSingleStep(0.1)
        self.doubleSpinBox_6 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_6.setGeometry(QtCore.QRect(190, 350, 71, 31))
        self.doubleSpinBox_6.setObjectName("doubleSpinBox_6")
        self.doubleSpinBox_6.setSingleStep(0.1)
        self.doubleSpinBox_7 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_7.setGeometry(QtCore.QRect(520, 300, 71, 31))
        self.doubleSpinBox_7.setObjectName("doubleSpinBox_7")
        self.doubleSpinBox_7.setSingleStep(0.1)
        self.doubleSpinBox_8 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_8.setGeometry(QtCore.QRect(520, 100, 71, 31))
        self.doubleSpinBox_8.setObjectName("doubleSpinBox_8")
        self.doubleSpinBox_8.setSingleStep(0.1)
        self.doubleSpinBox_9 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_9.setGeometry(QtCore.QRect(520, 150, 71, 31))
        self.doubleSpinBox_9.setObjectName("doubleSpinBox_9")
        self.doubleSpinBox_9.setSingleStep(0.1)
        self.doubleSpinBox_10 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_10.setGeometry(QtCore.QRect(520, 200, 71, 31))
        self.doubleSpinBox_10.setObjectName("doubleSpinBox_10")
        self.doubleSpinBox_10.setSingleStep(0.1)
        self.doubleSpinBox_11 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_11.setGeometry(QtCore.QRect(520, 250, 71, 31))
        self.doubleSpinBox_11.setObjectName("doubleSpinBox_11")
        self.doubleSpinBox_11.setSingleStep(0.1)
        self.doubleSpinBox_12 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_12.setGeometry(QtCore.QRect(520, 350, 71, 31))
        self.doubleSpinBox_12.setObjectName("doubleSpinBox_12")
        self.doubleSpinBox_12.setSingleStep(0.1)
        #Set up Label to show data
        self.textBrowser_1 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_1.setGeometry(QtCore.QRect(270, 100, 51, 31))
        self.textBrowser_1.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(270, 150, 51, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(270, 200, 51, 31))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(270, 250, 51, 31))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_5.setGeometry(QtCore.QRect(270, 300, 51, 31))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_6.setGeometry(QtCore.QRect(270, 350, 51, 31))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_7.setGeometry(QtCore.QRect(600, 100, 51, 31))
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_8.setGeometry(QtCore.QRect(600, 150, 51, 31))
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.textBrowser_9 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_9.setGeometry(QtCore.QRect(600, 300, 51, 31))
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.textBrowser_10 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_10.setGeometry(QtCore.QRect(600, 250, 51, 31))
        self.textBrowser_10.setObjectName("textBrowser_10")
        self.textBrowser_11 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_11.setGeometry(QtCore.QRect(600, 350, 51, 31))
        self.textBrowser_11.setObjectName("textBrowser_11")
        self.textBrowser_12 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_12.setGeometry(QtCore.QRect(600, 200, 51, 31))
        self.textBrowser_12.setObjectName("textBrowser_12")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMenu.menuAction())

        #Assign button to function
        self.pushButton.clicked.connect(self.receive_button_clicked)
        self.pushButton_1.clicked.connect(self.solve_1_button_clicked)
        self.pushButton_2.clicked.connect(self.solve_2_button_clicked)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "X"))
        self.label_2.setText(_translate("MainWindow", "Z"))
        self.label_3.setText(_translate("MainWindow", "Y"))
        self.label_4.setText(_translate("MainWindow", "Roll"))
        self.label_5.setText(_translate("MainWindow", "Pitch"))
        self.label_6.setText(_translate("MainWindow", "Yaw"))
        self.label_7.setText(_translate("MainWindow", "Yaw"))
        self.label_8.setText(_translate("MainWindow", "Z"))
        self.label_9.setText(_translate("MainWindow", "Roll"))
        self.label_10.setText(_translate("MainWindow", "X"))
        self.label_11.setText(_translate("MainWindow", "Y"))
        self.label_12.setText(_translate("MainWindow", "Pitch"))
        self.label_13.setText(_translate("MainWindow", "Left Arm"))
        self.label_14.setText(_translate("MainWindow", "Right Arm"))
        self.pushButton.setText(_translate("MainWindow", "Reiceve"))
        self.pushButton_1.setText(_translate("MainWindow", "Solve_1"))
        self.pushButton_2.setText(_translate("MainWindow", "Solve_2"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
    def receive_button_clicked(self):
        # Assigning values from arrays to variables for left arm
        self.x_left = left_position_receive[0]
        self.y_left = left_position_receive[1]
        self.z_left = left_position_receive[2]
        self.roll_left = left_orientation_receive[0]
        self.pitch_left = left_orientation_receive[1]
        self.Yaw_left = left_orientation_receive[2]
        
        # Assigning values from arrays to variables for right arm
        self.x_right = right_position_receive[0]
        self.y_right = right_position_receive[1]
        self.z_right = right_position_receive[2]
        self.roll_right = right_orientation_receive[0]
        self.pitch_right = right_orientation_receive[1]
        self.Yaw_right = right_orientation_receive[2]
        # For left arm
        self.textBrowser_1.setText(str(self.x_left))
        self.textBrowser_2.setText(str(self.y_left))
        self.textBrowser_3.setText(str(self.z_left))
        self.textBrowser_4.setText(str(self.roll_left))
        self.textBrowser_5.setText(str(self.pitch_left))
        self.textBrowser_6.setText(str(self.Yaw_left))

        # For right arm
        self.textBrowser_7.setText(str(self.x_right))
        self.textBrowser_8.setText(str(self.y_right))
        self.textBrowser_9.setText(str(self.z_right))
        self.textBrowser_10.setText(str(self.roll_right))
        self.textBrowser_11.setText(str(self.pitch_right))
        self.textBrowser_12.setText(str(self.Yaw_right))
    def solve_1_button_clicked(self):
        position_left_arm = [
            self.doubleSpinBox_1.value(),
            self.doubleSpinBox_2.value(),
            self.doubleSpinBox_3.value()
        ]
        orientation_left_arm = [
            self.doubleSpinBox_4.value(),
            self.doubleSpinBox_5.value(),
            self.doubleSpinBox_6.value()
        ]
        position_right_arm = [
            self.doubleSpinBox_7.value(),
            self.doubleSpinBox_8.value(),
            self.doubleSpinBox_9.value()
        ]
        orientation_right_arm = [
            self.doubleSpinBox_10.value(),
            self.doubleSpinBox_11.value(),
            self.doubleSpinBox_12.value()
        ]
        left_result, right_result = self.execute_IK(position_left_arm,orientation_left_arm,position_right_arm,orientation_right_arm,DH)
        self.show_result_window(left_result, right_result)
    def solve_2_button_clicked(self):
        if any(v is None for v in [self.x_left, self.y_left, self.z_left,
                            self.roll_left, self.pitch_left, self.Yaw_left,
                            self.x_right, self.y_right, self.z_right,
                            self.roll_right, self.pitch_right, self.Yaw_right]):
        # Show a message box indicating that data needs to be received first
            QMessageBox.warning(None, "Warning", "Please receive data first.")
            return
        position_left_arm_2 = [
            self.x_left,
            self.y_left,
            self.z_left
        ]
        orientation_left_arm_2 = [
            self.roll_left,
            self.pitch_left,
            self.Yaw_left
        ]
        position_right_arm_2 = [
            self.x_right,
            self.y_right,
            self.z_right
        ]
        orientation_right_arm_2 = [
            self.roll_right,
            self.pitch_right,
            self.Yaw_right
        ]
        left_result, right_result = self.execute_IK(position_left_arm_2, orientation_left_arm_2, position_right_arm_2, orientation_right_arm_2, DH)
        self.show_result_window(left_result, right_result)
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
    def show_result_window(self, left_result, right_result):
        self.result_window = ResultWindow(left_result, right_result)
        self.result_window.show()    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_4()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
