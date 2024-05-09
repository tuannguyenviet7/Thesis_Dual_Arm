# Cài đặt PyQt5: pip3 install pyqt5
# Cài đặt PyOpenGL bằng Python packets: PyOpenGL
# Cài đặt numpy bằng Python packets: numpy

import sys
import math
import time

import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from PyQt5.QtCore import pyqtSignal, QPoint, QSize, Qt, QEvent
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QWidget, QOpenGLWidget
from Utils import *
from Camera import *
# from ikSolver import *
# from GUI_Receiver import *
#global variable
right_joint_vars = np.array([0, M_PI / 3, M_PI / 3, M_PI / 6, 0, 0])
left_joint_vars = np.array([[0, M_PI/3, M_PI/3, M_PI/6, 0, 0]])
best_left_q = np.asarray([-2.24553727, 2.94464527, 2.30306317, -3.00217117, 1.57079633, -0.89605538])
best_right_q = np.asarray([-2.24553727, 2.94464527, 2.30306317, -3.00217117, 1.57079633, -0.89605538])
class Window (QWidget):
    
    def __init__(self):
        super(Window, self).__init__()
        self.glWidget = GLWidget()
        mainLayout = QHBoxLayout()
        mainLayout.addWidget(self.glWidget, 100)
        self.setLayout(mainLayout)
        self.setWindowTitle('KLTN_2024_Dual_Arm_Kinematics')
        self.glWidget.installEventFilter(self)

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

    def update_joint_vars(self): 
        # Viết nội dung hàm truyền các góc khớp cho robot khi nhận được tín hiệu từ bạn iot

        # làm mới biến self.glWidget.right_joint_vars, self.glWidget.left.joint_vars
        # right_joint_vars = best_right_q
        # left_joint_vars = best_left_q
        # update glWidget để vẽ robot ở vị trí mới
        
        self.glWidget.update()

class GLWidget(QOpenGLWidget):

    def __init__(self, parent=None):
        super(GLWidget, self).__init__(parent)
        self.camera = Camera()
        self.camera.current_mouse = np.array([self.width()/2, self.height()/2])
        self.camera.last_mouse = self.camera.current_mouse
        self.setMouseTracking(True)
        self.setMinimumSize(800, 600)

    def sizeHint(self):
        return QSize(self.width(), self.height())

    def initializeGL(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)  # it's also possible.
        glColor(1, 1, 1, 1)

        # projection
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60, (self.width() / self.height()), 0.1, 1000.0)
        glEnable(GL_COLOR_MATERIAL)

    def init_camera(self):
        # modelview
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glViewport(0, 0, self.width(), self.height())
        glEnable(GL_DEPTH_TEST)
        self.camera.update()
    # def _display(self):     
    #     self.init_camera()
    #     draw_world_axes()
    #     draw_right_arm(best_right_q)
    #     draw_left_arm(best_left_q)

    def paintGL(self):
        # glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # # self.init_camera()
        # draw_world_axes()  # Gọi hàm draw_world_axes() ở đây
        # draw_right_arm(best_right_q)
        # draw_left_arm(best_left_q)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Draw axes
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

        # Thay thế giá trị mặc định bằng 20 cặp giá trị góc khớp mới
        for i in range(20):
            left_joints = np.random.uniform(-np.pi, np.pi, size=6)
            right_joints = np.random.uniform(-np.pi, np.pi, size=6)

            # Draw left arm joints and connect them
            glColor3f(1.0, 1.0, 1.0)  # White
            glPointSize(5)
            glBegin(GL_POINTS)
            for i in range(len(left_joints)):
                glVertex3f(np.cos(left_joints[i]), np.sin(left_joints[i]), 0)
            glEnd()

            glLineWidth(1)
            glBegin(GL_LINE_STRIP)
            for i in range(len(left_joints)):
                glVertex3f(np.cos(left_joints[i]), np.sin(left_joints[i]), 0)
            glEnd()

            # Draw right arm joints and connect them
            glColor3f(1.0, 1.0, 1.0)  # White
            glPointSize(5)
            glBegin(GL_POINTS)
            for i in range(len(right_joints)):
                glVertex3f(np.cos(right_joints[i]), np.sin(right_joints[i]), 0)
            glEnd()

            glLineWidth(1)
            glBegin(GL_LINE_STRIP)
            for i in range(len(right_joints)):
                glVertex3f(np.cos(right_joints[i]), np.sin(right_joints[i]), 0)
            glEnd()

        def resizeGL(self, w, h):
            # side = min(width, height)
            # if side < 0:
            #     return
            # glViewport((width - side) // 2, (height - side) // 2, side, side)
            #glViewport(0, 0, width, height)
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