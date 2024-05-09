from OpenGL.GLU import *
from math import *
import numpy as np

class Camera:
    def __init__(self):
        self.eye = np.array([0.0, 0.0, 0.0])
        self.up = np.array([0.0, 1.0, 0.0])
        self.right = np.array([1.0, 0.0, 0.0])
        self.forward = np.array([0.0, 0.0, 1.0])
        self.look = self.eye + self.forward
        self.yaw = -90
        self.pitch = 0
        self.last_mouse = np.array([0, 0])
        self.current_mouse = self.last_mouse
        self.mouse_sensitivityX = 0.05
        self.mouse_sensitivityY = 0.05
        self.key_sensitivity = 0.1

    def rotate(self, yaw, pitch):
        self.yaw += yaw
        self.pitch += pitch
        if self.pitch > 89.0:
            self.pitch = 89
        if self.pitch < -89.0:
            self.pitch = -89
        self.forward[0] = cos(radians(self.yaw)) * cos(radians(self.pitch))
        self.forward[1] = sin(radians(self.pitch))
        self.forward[2] = sin(radians(self.yaw)) * cos(radians(self.pitch))
        self.forward = self.forward/np.linalg.norm(self.forward)
        vector_cross = np.cross(self.forward, np.array([0.0, 1.0, 0.0]))
        self.right = vector_cross/np.linalg.norm(vector_cross)
        vector_cross = np.cross(self.right, self.forward)
        self.up = vector_cross/np.linalg.norm(vector_cross)

    def update(self):
        mouse_change = self.last_mouse - self.current_mouse
        self.last_mouse = self.current_mouse
        self.rotate(-mouse_change[0] * self.mouse_sensitivityX, mouse_change[1] * self.mouse_sensitivityY)
        self.look = self.eye + self.forward
        gluLookAt(self.eye[0], self.eye[1], self.eye[2],
                  self.look[0], self.look[1], self.look[2],
                  self.up[0], self.up[1], self.up[2])
