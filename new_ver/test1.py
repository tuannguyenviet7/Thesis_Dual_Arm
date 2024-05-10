import sys
import math
import time

import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from PyQt5.QtCore import pyqtSignal, QThread
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QOpenGLWidget,QMessageBox
from PyQt5.QtCore import Qt
from ikSolver import *
from GUI_Receiver import *


class KinematicsThread(QThread):
    updated = pyqtSignal(np.ndarray, np.ndarray)  # Signal to emit updated joint angles

    def __init__(self, parent=None):
        super(KinematicsThread, self).__init__(parent)
        self.running = False

    def run(self):
        self.running = True
        while self.running:
            # Khởi tạo các góc khớp ngẫu nhiên cho cánh tay trái và phải
            left_joints = np.asarray([-2.03444394 , 2.98909208 , 2.28503782 , 3.04349935  ,1.57079633 ,-1.10714872]) # Ngẫu nhiên từ -pi đến pi
            right_joints = np.random.rand(6) * 2 * np.pi - np.pi  # Ngẫu nhiên từ -pi đến pi
            # Gửi tín hiệu với các góc khớp đã khởi tạo
            self.updated.emit(left_joints, right_joints)
            time.sleep(0.5)  # Độ trễ 0.5s giữa các lần cập nhật


    def stop(self):
        self.running = False
        self.wait()

class OpenGLWidget(QOpenGLWidget):
    def __init__(self):
        super().__init__()
        self.last_x = 0
        self.last_y = 0
        self.rot_x = 0
        self.rot_y = 0
        self.mouse_pressed = False

    def initializeGL(self):
        # Khởi tạo các thiết lập ban đầu
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClearDepth(1.0)
        glEnable(GL_DEPTH_TEST)

    def resizeGL(self, w, h):
        # Cài đặt viewport
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, w/h, 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(0, 0, 10, 0, 0, 0, 0, 1, 0)

    def paintGL(self):
        # Xóa buffer màu và buffer độ sâu
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Đặt ma trận modelview để thực hiện phép biến đổi
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -10.0)
        glRotatef(self.rot_x, 1.0, 0.0, 0.0)
        glRotatef(self.rot_y, 0.0, 1.0, 0.0)

        # Vẽ các trục
        self.draw_axes()

        # Vẽ các khớp của cánh tay trái và phải
        if hasattr(self, 'left_joints') and hasattr(self, 'right_joints'):
            self.draw_arm(self.left_joints, (0.0, 1.0, 0.0))  # Cánh tay trái màu xanh lá
            self.draw_arm(self.right_joints, (1.0, 0.0, 0.0))  # Cánh tay phải màu đỏ

    def draw_axes(self):
        # Vẽ các trục tọa độ
        glLineWidth(2)
        glBegin(GL_LINES)
        glColor3f(1.0, 0.0, 0.0)  # Trục x màu đỏ
        glVertex3f(-10, 0, 0)
        glVertex3f(10, 0, 0)

        glColor3f(0.0, 1.0, 0.0)  # Trục y màu xanh lá
        glVertex3f(0, -10, 0)
        glVertex3f(0, 10, 0)

        glColor3f(0.0, 0.0, 1.0)  # Trục z màu xanh dương
        glVertex3f(0, 0, -10)
        glVertex3f(0, 0, 10)
        glEnd()

    def draw_arm(self, joints, color):
        glColor3f(*color)
        glPointSize(5)
        glBegin(GL_POINTS)
        for i in range(len(joints)):
            glVertex3f(np.cos(joints[i]), np.sin(joints[i]), 0)
        glEnd()

        glLineWidth(1)
        glBegin(GL_LINE_STRIP)
        for i in range(len(joints)):
            glVertex3f(np.cos(joints[i]), np.sin(joints[i]), 0)
        glEnd()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mouse_pressed = True
            self.last_x = event.x()
            self.last_y = event.y()

    def mouseMoveEvent(self, event):
        if self.mouse_pressed:
            dx = event.x() - self.last_x
            dy = event.y() - self.last_y
            self.last_x = event.x()
            self.last_y = event.y()
            self.rot_x += dy * 0.1
            self.rot_y += dx * 0.1
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mouse_pressed = False

    def update_joint_vars(self, left_joints, right_joints):
        # Cập nhật góc khớp và vẽ lại
        self.left_joints = left_joints
        self.right_joints = right_joints
        self.update()

    def update_joint_vars(self, left_joints, right_joints):
        # Cập nhật góc khớp và vẽ lại
        self.left_joints = left_joints
        self.right_joints = right_joints
        self.update()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("OpenGL Example")
        self.setGeometry(100, 100, 800, 600)

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        layout = QVBoxLayout()
        centralWidget.setLayout(layout)

        self.glWidget = OpenGLWidget()
        layout.addWidget(self.glWidget)

        # Tạo và khởi chạy luồng kinematics
        self.kinematics_thread = KinematicsThread()
        self.kinematics_thread.updated.connect(self.glWidget.update_joint_vars)
        self.kinematics_thread.start()

    def closeEvent(self, event):
        # Khi cửa sổ đóng, dừng luồng
        self.kinematics_thread.stop()
        event.accept()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())