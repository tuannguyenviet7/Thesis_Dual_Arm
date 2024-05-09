import sys
import math
import time

import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from PyQt5.QtCore import pyqtSignal, QPoint, QSize, Qt, QEvent, QThread
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QWidget, QOpenGLWidget

from Camera import *

class KinematicsThread(QThread):
    updated = pyqtSignal(list, list)  # Signal to emit updated joint angles

    def __init__(self, parent=None):
        super(KinematicsThread, self).__init__(parent)
        self.running = False

    def run(self):
        self.running = True
        while self.running:
            # Trong vòng lặp này, bạn có thể lấy dữ liệu từ góc khớp và gửi nó đến đối tượng GLWidget
            left_joints = [-2.24553727, 2.94464527, 2.30306317, -3.00217117, 1.57079633, -0.89605538]
            right_joints = [-2.24553727, 2.94464527, 2.30306317, -3.00217117, 1.57079633, -0.89605538]
            self.updated.emit(left_joints, right_joints)
            time.sleep(0.5)  # Thời gian chờ giữa các lần cập nhật

    def stop(self):
        self.running = False
        self.wait()

class Window(QWidget):
    
    def __init__(self):
        super(Window, self).__init__()
        self.glWidget = GLWidget()
        mainLayout = QHBoxLayout()
        mainLayout.addWidget(self.glWidget)
        self.setLayout(mainLayout)
        self.setWindowTitle('KLTN_2024_Dual_Arm_Kinematics')
        self.glWidget.installEventFilter(self)

        # Tạo và khởi chạy luồng kinematics
        self.kinematics_thread = KinematicsThread()
        self.kinematics_thread.updated.connect(self.glWidget.update_joint_vars)
        self.kinematics_thread.start()

    def closeEvent(self, event):
        # Khi cửa sổ đóng, dừng luồng
        self.kinematics_thread.stop()
        event.accept()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Down:
            self.glWidget.camera.eye -= self.glWidget.camera.forward * self.glWidget.camera.key_sensitivity
        if event.key() == Qt.Key_Up:
            self.glWidget.camera.eye += self.glWidget.camera.forward * self.glWidget.camera.key_sensitivity
        if event.key() == Qt.Key_Right:
            self.glWidget.camera.eye += self.glWidget.camera.right * self.glWidget.camera.key_sensitivity
        if event.key() == Qt.Key_Left:
            self.glWidget.camera.eye -= self.glWidget.camera.right * self.glWidget.camera.key_sensitivity
        self.glWidget.update()

    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseMove:
            self.glWidget.camera.current_mouse = np.array([event.x(), event.y()])
        self.glWidget.update()
        return super().eventFilter(obj, event)

class GLWidget(QOpenGLWidget):

    def __init__(self, parent=None):
        super(GLWidget, self).__init__(parent)
        self.camera = Camera()
        self.camera.current_mouse = np.array([self.width()/2, self.height()/2])
        self.camera.last_mouse = self.camera.current_mouse
        self.setMouseTracking(True)
        self.setMinimumSize(800, 600)

    def update_joint_vars(self, left_joints, right_joints): 
        # Cập nhật dữ liệu góc khớp và vẽ lại
        self.left_joints = left_joints
        self.right_joints = right_joints
        self.update()

    def paintGL(self):
        # Xóa màn hình
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Vẽ các trục tọa độ
        self.draw_axes()

        # Vẽ cánh tay
        if hasattr(self, 'left_joints') and hasattr(self, 'right_joints'):
            self.draw_arms()

    def draw_axes(self):
        glLineWidth(2)
        glBegin(GL_LINES)
        glColor3f(1.0, 0.0, 0.0)  # Red
        glVertex3f(-10, 0, 0)
        glVertex3f(10, 0, 0)

        glColor3f(0.0, 1.0, 0.0)  # Green
        glVertex3f(0, -10, 0)
        glVertex3f(0, 10, 0)

        glColor3f(0.0, 0.0, 1.0)  # Blue
        glVertex3f(0, 0, -10)
        glVertex3f(0, 0, 10)
        glEnd()

    def draw_arms(self):
        if hasattr(self, 'left_joints') and hasattr(self, 'right_joints'):
            for left_joints, right_joints in zip(self.left_joints, self.right_joints):
                num_left_joints = 5
                num_right_joints = 5

                glPointSize(5)
                glBegin(GL_POINTS)
                for i in range(num_left_joints):
                    glColor3f(1.0, 0.0, 0.0)  # Red
                    glVertex3f(np.cos(left_joints[i]), np.sin(left_joints[i]), -i * 2)
                glEnd()

                glLineWidth(1)
                glBegin(GL_LINE_STRIP)
                for i in range(num_left_joints):
                    glColor3f(1.0, 0.0, 0.0)  # Red
                    glVertex3f(np.cos(left_joints[i]), np.sin(left_joints[i]), -i * 2)
                glEnd()

                glPointSize(5)
                glBegin(GL_POINTS)
                for i in range(num_right_joints):
                    glColor3f(0.0, 0.0, 1.0)  # Blue
                    glVertex3f(np.cos(right_joints[i]), np.sin(right_joints[i]), -i * 2)
                glEnd()

                glLineWidth(1)
                glBegin(GL_LINE_STRIP)
                for i in range(num_right_joints):
                    glColor3f(0.0, 0.0, 1.0)  # Blue
                    glVertex3f(np.cos(right_joints[i]), np.sin(right_joints[i]), -i * 2)
                glEnd()



    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, w/h, 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(0, 0, 10, 0, 0, 0, 0, 1, 0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
