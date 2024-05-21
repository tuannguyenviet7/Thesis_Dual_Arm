import sys
import time
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PyQt5.QtWidgets import QOpenGLWidget
from OpenGL.GL import *
from OpenGL.GLU import *
from sympy import symbols, cos, sin, pi, simplify, pprint, tan, expand_trig, sqrt, trigsimp, atan2
from sympy.matrices import Matrix

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import time
import numpy as np
import math
from IkSolver import *



class OpenGLWidget(QOpenGLWidget):
    def __init__(self):
        super().__init__()
        self.last_x = 0
        self.last_y = 0
        self.rot_x = 0
        self.rot_y = 0
        self.mouse_pressed = False

        self.right_arms = [[], [], []]
        self.left_arms = [[], [], []]

    def initializeGL(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClearDepth(1.0)
        glEnable(GL_DEPTH_TEST)

    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60, w / h, 0.01, 100.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(0, 0, 10, 0, 0, 0, 0, 100, 0)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -10.0)
        glRotatef(self.rot_x, 1.0, 0.0, 0.0)
        glRotatef(self.rot_y, 0.0, 1.0, 0.0)

        self.draw_axes()
        self.draw_arm(self.right_arms)
        self.draw_arm(self.left_arms)

    def draw_arm(self, arm):
        if len(arm[0]) > 1:
            glPointSize(15)
            glColor3f(1.0, 0.0, 1.0)  # Color of points: white
            glBegin(GL_POINTS)
            for i in range(8):
                glVertex3f(arm[0][i], arm[1][i], arm[2][i])
            glEnd()

            glColor3f(0.5, 0.5, 0.5)  # Color of lines: white
            for i in range(7):
                glBegin(GL_LINES)
                glVertex3f(arm[0][i], arm[1][i], arm[2][i])
                glVertex3f(arm[0][i+1], arm[1][i+1], arm[2][i+1])
                glEnd()

    def draw_axes(self):
        glLineWidth(2)
        glBegin(GL_LINES)
        glColor3f(1.0, 0.0, 0.0)  # X axis in red
        glVertex3f(-10, 0, 0)
        glVertex3f(10, 0, 0)

        glColor3f(0.0, 1.0, 0.0)  # Y axis in green
        glVertex3f(0, -10, 0)
        glVertex3f(0, 10, 0)

        glColor3f(0.0, 0.0, 1.0)  # Z axis in blue
        glVertex3f(0, 0, -10)
        glVertex3f(0, 0, 10)
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

    def add_arm(self, x, y, z, one_arm):
        if one_arm == 'right':
            self.right_arms = [[], [], []]
            self.right_arms[0] = x
            self.right_arms[1] = y
            self.right_arms[2] = z
        elif one_arm == 'left':
            self.left_arms = [[], [], []]
            self.left_arms[0] = x
            self.left_arms[1] = y
            self.left_arms[2] = z
        self.update()

class MainPage(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("OpenGL Example")
        self.setGeometry(100, 100, 1200, 800)

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        layout = QVBoxLayout()
        centralWidget.setLayout(layout)

        self.glWidget = OpenGLWidget()
        layout.addWidget(self.glWidget)

        self.q2_r = 0
        self.x_ttt = 0
        self.y_ttt = 2.18629015972879
        self.z_ttt =   -0.5400000000000003
        self.corn = 0
        self.check_status = False
        self.last_q_both = None
        self.timer = QTimer()
        self.timer.timeout.connect(lambda: self.update_q(1))
        self.timer.start(50)  # 500 milliseconds interval

    def update_q(self, i):
        # q_increment = 0.01 # Increment for q1
        # if i == 1:
        #     self.q2_r += q_increment  # Increment q1
        
        self.x_ttt += 0.01
        self.y_ttt += 0.02
        self.z_ttt -= 0.01
        self.corn += 0.1
        #Check 1st time joints of dual arm
        if self.check_status == False:
            theta1 = [3.609999999999967, 1.741630831000581, 0.5, -2.346298499492475, 1.1974120573295397, -2.395804252567312]
            theta2 = [2.5510380735426352, 1.2500000000000009, 0, -0.24583699638560927, 0, 0.06415578974597116]
            self.check_status = True
            
        # q1_r,q2_r,q3_r,q4_r,q5_r,q6_r = best_right_q[0],best_right_q[1],best_right_q[2],best_right_q[3],best_right_q[4],best_right_q[5]
        else:
            # q1_l,q2_l,q3_l,q4_l,q5_l,q6_l = best_left_q[0],best_left_q[1],best_left_q[2],best_left_q[3],best_left_q[4],best_left_q[5]
            #right arm

            #left
            left_position = np.array([0.04, 0.18, 0.18])  # Example position for left arm
            orientation_matrix = np.array([[0.847, -0.117, 0.56],
                                        [0.49, 0.958, -0.704],
                                        [-0.207, 0.261, 0.437]])
            ori_array = matrix_to_ur_euler(orientation_matrix)
            T = ik.create_Transformation_Matrix(left_position,ori_array)
            
            if(self.check_status == True):
                q, qs = ik.solveIK(T,np.array(theta1))
                self.check_status == 2
            else:
                q,qs = ik.solveIK(T,q)
                theta1 = [q[0],q[1],q[2],q[3],q[4],q[5]]
        self.last_q_both = np.array([theta1,theta2])
        end_effector_position1 = FK(dh_params, theta1, initial_translation=(1, 0, 0))  # Right arm starts at (1, 0, 0)
        end_effector_position2 = FK(dh_params, theta2, initial_translation=(-1, 0, 0))  # Left arm starts at (0, 0, 0)

        self.glWidget.add_arm(end_effector_position1[0], end_effector_position1[1], end_effector_position1[2], 'right')
        self.glWidget.add_arm(end_effector_position2[0], end_effector_position2[1], end_effector_position2[2], 'left')
        self.glWidget.update()

if __name__ == "__main__":
    app = QApplication([])
    window = MainPage()
    window.show()
    sys.exit(app.exec_())
