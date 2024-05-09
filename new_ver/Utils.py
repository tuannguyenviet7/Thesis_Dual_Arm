import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *

M_PI = 3.14

DH = DH = {'theta': [0, 0, 0, 0, 0, 0],
               'd': [241, 173.5, -38, 0, 95, 45],
               'a': [0, 335, 294, 0, 0, 0],
           'alpha': [M_PI / 2, 0, 0, -M_PI / 2, M_PI / 2, 0],
          'offset': [0, 0, 20, 0, 0, 0]}

def map_value(current_min, current_max, new_min, new_max, value):
    current_range = current_max - current_min
    new_range = new_max - new_min
    return new_min + new_range * ((value - current_min)/current_range)

def x_rotation(vector, theta):
    new_vector = np.array([[1,             0,              0],
                           [0, np.cos(theta), -np.sin(theta)],
                           [0, np.sin(theta),  np.cos(theta)]])
    return np.dot(new_vector, vector)

def y_rotation(vector, theta):
    new_vector = np.array([[ np.cos(theta), 0, np.sin(theta)],
                           [             0, 1,             0],
                           [-np.sin(theta), 0, np.cos(theta)]])
    return np.dot(new_vector, vector)

def z_rotation(vector, theta):
    new_vector = np.array([[np.cos(theta), -np.sin(theta), 0],
                           [np.sin(theta),  np.cos(theta), 0],
                           [            0,              0, 1]])
    return np.dot(new_vector, vector)

def draw_world_axes():
    # glLineWidth(2)

    # glBegin(GL_LINES)
    # glColor(1, 0, 0)
    # glVertex3f(-3, 0, 0)
    # glVertex3f(3, 0, 0)
    # glEnd()
    # conex = gluNewQuadric()
    # glPushMatrix()
    # glTranslated(3, 0, 0)
    # glRotated(90, 0, 1, 0)
    # gluCylinder(conex, 0.2, 0, 0.5, 100, 100)
    # glPopMatrix()

    # glBegin(GL_LINES)
    # glColor(0, 1, 0)
    # glVertex3f(0, -6, 0)
    # glVertex3f(0, 6, 0)
    # glEnd()
    # coney = gluNewQuadric()
    # glPushMatrix()
    # glTranslated(0, 6, 0)
    # glRotated(-90, 1, 0, 0)
    # gluCylinder(coney, 0.2, 0, 0.5, 100, 100)
    # glPopMatrix()

    # glBegin(GL_LINES)
    # glColor(0, 0, 1)
    # glVertex3f(0, 0, -5)
    # glVertex3f(0, 0, 5)
    # glEnd()
    # conez = gluNewQuadric()
    # glPushMatrix()
    # glTranslated(0, 0, 5)
    # gluCylinder(conez, 0.2, 0, 0.5, 100, 100)
    # glPopMatrix()

    # sphere = gluNewQuadric()
    # # glPushMatrix()
    # # glTranslated(0,0,0)
    # gluSphere(sphere, 0.05, 100, 100)
    # # glPopMatrix()

    # glLineWidth(1)
    # glColor(1, 1, 1)
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

def draw_world_axes_left():
    glLineWidth(2)

    glBegin(GL_LINES)
    glColor(1, 0, 0)
    glVertex3f(-3, 0, 0)
    glVertex3f(3, 0, 0)
    glEnd()

    conex = gluNewQuadric()
    glPushMatrix()
    glTranslated(3, 0, 0)
    glRotated(90, 0, 1, 0)
    gluCylinder(conex, 0.2, 0, 0.5, 100, 100)
    glPopMatrix()

    glBegin(GL_LINES)
    glColor(0, 1, 0)
    glVertex3f(0, -6, 0)
    glVertex3f(0, 6, 0)
    glEnd()

    coney = gluNewQuadric()
    glPushMatrix()
    glTranslated(0, 6, 0)
    glRotated(-90, 1, 0, 0)
    gluCylinder(coney, 0.2, 0, 0.5, 100, 100)
    glPopMatrix()

    glBegin(GL_LINES)
    glColor(0, 0, 1)
    glVertex3f(0, 0, -5)
    glVertex3f(0, 0, 5)
    glEnd()

    conez = gluNewQuadric()
    glPushMatrix()
    glTranslated(0, 0, 5)
    gluCylinder(conez, 0.2, 0, 0.5, 100, 100)
    glPopMatrix()

    glLineWidth(1)
    glColor(1, 1, 1)

def draw_right_arm(joints):


    # Draw joints and connect them
    glColor3f(1.0, 1.0, 1.0)  # White
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

def draw_left_arm(joints):


    # Draw joints and connect them
    glColor3f(1.0, 1.0, 1.0)  # White
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





