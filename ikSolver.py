import numpy as np
from scipy.spatial.transform import Rotation as R
from sympy import symbols, cos, sin, pi, simplify, pprint, tan, expand_trig, sqrt, trigsimp, atan2
# Inverse kinematic solver for a UR robot
# Based on Kinematics of a UR5, by Rasmus Skovgaard Andersen
# http://rasmusan.blog.aau.dk/files/ur5_kinematics.pdf

class ikSolver():
    def __init__(self, a, d, alpha):

        # Initialize the DH parameters of the robot
        self.a = a
        self.d = d
        self.alpha = alpha

    def create_Transformation_Matrix(self, position, orientation):
        """

        :param position: 3x1 numpy array of the position, xyz
        :param orientation: 3x1 numpy array of the orientation in euler angles xyz
        :return: homogenous transformation matrix
        """
        T = np.eye(4)
        rot = R.from_euler('xyz', orientation)
        T[0:3, 0:3] = rot.as_matrix()
        T[0:3, 3] = position
        return T

    def DHLink(self, alpha, a, d, angle):
        T = np.array([[np.cos(angle),                 -np.sin(angle),                0,              a],
                     [np.sin(angle) * np.cos(alpha), np.cos(angle) * np.cos(alpha), -np.sin(alpha), -np.sin(alpha)*d],
                     [np.sin(angle) * np.sin(alpha), np.cos(angle) * np.sin(alpha), np.cos(alpha),  np.cos(alpha)*d],
                     [0,                             0,                             0,              1]])
        return T

    def nearestQ(self, q_list, last_q):
        """
        Function that computes the distance from every new configuration to the previous
        :param q_list: list of configurations
        :param last_q: previous configuration
        :return: closest configuration to the previous
        """
        weights = np.array([6, 5, 4, 3, 2, 1])
        best_q = np.zeros(6)
        bestConfDist = np.inf
        for q in q_list:
            confDist = np.sum(((q - last_q) * weights)**2)
            if confDist < bestConfDist:
                bestConfDist = confDist
                best_q = q
        return np.asarray(best_q)

    def solveIK(self, T06, *last_q):
        """
        Inverse Kinematics Solver
        :param T06: Homogenous transformation matrix of the TCP frame
        :param last_q: previous configuration of the robot
        :return: q: Closest IK Solution, theta: Every IK solution
        """
        theta = np.zeros([8,6])

        # ---------- Theta 1 ----------
        P05 = (T06 @ np.array([0,0,-self.d[5], 1]))[0:3]
        phi1 = np.arctan2(P05[1],P05[0])
        phi2 = np.array([np.arccos(self.d[3]/np.linalg.norm(P05[0:2])), -np.arccos(self.d[3]/np.linalg.norm(P05[0:2]))])

        for i in range(4):
            theta[i,0] = phi1 + phi2[0] + np.pi/2
            theta[i+4,0] = phi1 + phi2[1] + np.pi/2

        for i in range(8):
            if theta[i,0] <= np.pi:
                theta[i,0] += 2*np.pi
            if theta[i,0] > np.pi:
                theta[i,0] -= 2*np.pi
        
        # ---------- Theta 5 ----------
        P06 = T06[0:3,3]
        for i in range(8):
            theta[i,4] = np.arccos((P06[0]*np.sin(theta[i,0])-P06[1]*np.cos(theta[i,0])-self.d[3])/self.d[5])
            if np.isin(i, [2,3,6,7]):
                theta[i,4] = -theta[i,4]

        # ---------- Theta 6 ----------
        T60 = np.linalg.inv(T06)
        X60 = T60[0:3,0]
        Y60 = T60[0:3,1]

        for i in range(8):
            theta[i,5] = np.arctan2((-X60[1]*np.sin(theta[i,0])+Y60[1]*np.cos(theta[i,0]))/np.sin(theta[i,4]),
                                    ( X60[0]*np.sin(theta[i,0])-Y60[0]*np.cos(theta[i,0]))/np.sin(theta[i,4]))

        # ------- Theta 3 and 2 -------

        for i in range(8):
            T01 = self.DHLink(self.alpha[0],self.a[0],self.d[0], theta[i,0])
            T45 = self.DHLink(self.alpha[4],self.a[4],self.d[4], theta[i,4])
            T56 = self.DHLink(self.alpha[5],self.a[5],self.d[5], theta[i,5])

            T14 = np.linalg.inv(T01)@T06@np.linalg.inv(T45@T56)
            P14xz = np.array([T14[0,3], T14[2,3]])

            theta[i,2] = np.arccos((np.linalg.norm(P14xz)**2-self.a[1]**2-self.a[2]**2)/(2*self.a[1]*self.a[2]))

            if i % 2 != 0:
                theta[i,2] = -theta[i,2]

            theta[i,1] = np.arctan2(-P14xz[1], -P14xz[0]) - np.arcsin(-self.a[2]*np.sin(theta[i,2])/np.linalg.norm(P14xz))

        # ---------- Theta 4 ----------

        for i in range(8):
            T01 = self.DHLink(self.alpha[0],self.a[0],self.d[0], theta[i,0])
            T12 = self.DHLink(self.alpha[1],self.a[1],self.d[1], theta[i,1])
            T23 = self.DHLink(self.alpha[2],self.a[2],self.d[2], theta[i,2])
            T45 = self.DHLink(self.alpha[4],self.a[4],self.d[4], theta[i,4])
            T56 = self.DHLink(self.alpha[5],self.a[5],self.d[5], theta[i,5])

            T34 = np.linalg.inv(T01@T12@T23)@T06@np.linalg.inv(T45@T56)

            theta[i,3] = np.arctan2(T34[1,0], T34[0,0])

        if last_q:
            q = self.nearestQ(theta, last_q)
            return q, theta
        else:
            return theta
def matrix_to_ur_euler(matrix):
    roll = np.arctan2(matrix[1, 0], matrix[0, 0])
    pitch = np.arctan2(-matrix[2, 0], np.sqrt(matrix[2, 1]**2 + matrix[2, 2]**2))
    yaw = np.arctan2(matrix[2, 1], matrix[2, 2])
    array = ([roll, pitch, yaw])
    return array      
#Foward Solver
def HTM(dh_params, i, theta):
    theta_i = theta[i]
    a_i = dh_params['a'][i]
    d_i = dh_params['d'][i]
    alpha_i = dh_params['alpha'][i]

    HTM = [[cos(theta_i), -sin(theta_i)*cos(alpha_i),  sin(theta_i)*sin(alpha_i), a_i*cos(theta_i)],
           [sin(theta_i),  cos(theta_i)*cos(alpha_i), -cos(theta_i)*sin(alpha_i), a_i*sin(theta_i)],
           [0,             sin(alpha_i),               cos(alpha_i),              d_i],
           [0,             0,                          0,                         1]]
    return HTM

def FK(dh_params, theta, initial_translation=(0, 0, 0)):
    T = np.eye(4)
    T[0][3] = initial_translation[0]
    T[1][3] = initial_translation[1]
    T[2][3] = initial_translation[2]

    positions = [[], [], []]
    x = T[0][3]
    y = T[1][3]
    z = T[2][3]
    positions[0].append(x)
    positions[1].append(y)
    positions[2].append(z)

    for i in range(7):
        if i <= 5:
            T = T @ HTM(dh_params, i, theta)
            x = T[0][3]
            y = T[1][3]
            z = T[2][3]
            positions[0].append(x)
            positions[1].append(y)
            positions[2].append(z)
        if i > 5:
            Tend = np.eye(4)
            Tend[2][3] = dh_params['offset'][2]
            end_effector_position = T @ Tend
       
            x = end_effector_position[0][3]
            y = end_effector_position[1][3]
            z = end_effector_position[2][3]
            positions[0].append(x)
            positions[1].append(y)
            positions[2].append(z)
    
    return positions
#DH table
dh_params = {'a': [0, 3.35, 2.94, 0, 0, 0],
             'alpha': [np.pi / 2, 0, 0, -np.pi / 2, np.pi / 2, 0],
             'd': [2.41, 1.735, -0.38, 0, 0.95, 0.45],
             'offset': [0, 0, 0.2, 0, 0, 0]}
#example for position and orientation

left_position = np.array([0.04, 0.18, 0.18])  # Example position for left arm
orientation_matrix = np.array([[0.847, -0.117, 0.56],
                               [0.49, 0.958, -0.704],
                               [-0.207, 0.261, 0.437]])
ori_array = matrix_to_ur_euler(orientation_matrix)
last_q = np.array([3.6,1.74,0.5,-2.34,1.19,-2.395])
a = np.array([0, 3.35, 2.94, 0, 0, 0])
d = np.array([2.41, 1.735, -0.38, 0, 0.95, 0.45])
alpha = np.array( [np.pi / 2, 0, 0, -np.pi / 2, np.pi / 2, 0])

ik = ikSolver(a, d, alpha)
T = ik.create_Transformation_Matrix(left_position,ori_array)



    
