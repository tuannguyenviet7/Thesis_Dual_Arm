import numpy as np
from scipy.spatial.transform import Rotation as R



class ikSolver():
    def __init__(self,DH):

        # Initialize the DH parameters of the robot
        self.theta = DH['theta']
        self.d = DH['d']
        self.a = DH['a']
        self.alpha = DH['alpha']
        self.offset = DH['offset']
    def create_Transformation_Matrix(self, position, orientation,offset):
        """
        :param position: 3x1 numpy array of the position, xyz
        :param orientation: 3x1 numpy array of the orientation in euler angles xyz
        :param offset: 3x1 numpy array representing the offset from the TCP to the end effector frame
        :return: homogeneous transformation matrix
        """
        T = np.eye(4)
        rot = R.from_euler('xyz', orientation)
        T[0:3, 0:3] = rot.as_matrix()
        offset_array = np.array(self.offset)[:3]  # Lấy chỉ 3 phần tử đầu của offset
        T[0:3, 3] = position + offset_array 
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
class CombinedIKSolver():
    def __init__(self,DH):
        self.left_solver = ikSolver(DH)
        self.right_solver = ikSolver(DH)

    def solveIK(self, left_T06, right_T06, *last_q):
        left_q = self.left_solver.solveIK(left_T06)
        right_q = self.right_solver.solveIK(right_T06)
        if last_q:
            left_q = self.left_solver.nearestQ(left_q, last_q[0])
            right_q = self.right_solver.nearestQ(right_q, last_q[1])
        return left_q, right_q
def matrix_to_ur_euler(matrix):
    roll = np.arctan2(matrix[1, 0], matrix[0, 0])
    pitch = np.arctan2(-matrix[2, 0], np.sqrt(matrix[2, 1]**2 + matrix[2, 2]**2))
    yaw = np.arctan2(matrix[2, 1], matrix[2, 2])
    array = ([roll, pitch, yaw])
    return array
  
    
# # # Define DH parameters for each arm
# # # For simplicity, assuming both arms have the same parameters
# # a = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
# # d = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
# # alpha = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
DH = {'theta': [0, 0, 0, 0, 0, 0],
      'd': [241, 173.5, -38, 0, 95, 45],
      'a': [0, 335, 294, 0, 0, 0],
      'alpha': [np.pi / 2, 0, 0, -np.pi / 2, np.pi / 2, 0],
      'offset': [0, 0, 20, 0, 0, 0]}
# Create instances of the ikSolver class for each arm
left_arm_solver = ikSolver(DH)
right_arm_solver = ikSolver(DH)



# # Example position and orientation for left arm end effector
# left_position = np.array([0.1, 0.2, 0.3])  # Example position for left arm
# orientation_matrix = np.array([[12, 0, 0],
#                                [0, 0, 11],
#                                [0, 13, 0]])
# left_oirentaion = matrix_to_ur_euler(orientation_matrix)
# left_arm_T06 = left_arm_solver.create_Transformation_Matrix(left_position,left_oirentaion ,DH['offset'])

# # Example position and orientation for right arm end effector
# right_position = np.array([0.4, 0.5, 0.6])  # Example position for right arm
# right_orientation = np.array([0.0, 0.0, 0.0])  # Example orientation for right arm
# right_arm_T06 = right_arm_solver.create_Transformation_Matrix(right_position, left_oirentaion,DH['offset'])

# # Create combined IK solver
# combined_solver = CombinedIKSolver(DH)

# # Solve inverse kinematics for both arms simultaneously
# left_q, right_q = combined_solver.solveIK(left_arm_T06, right_arm_T06)

# # Print the results
# print("Left Arm IK Solution:")
# print("Joint Angles (q):", left_q)

# print("\nRight Arm IK Solution:")
# print("Joint Angles (q):", right_q)



