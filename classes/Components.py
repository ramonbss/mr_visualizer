'''
Created on Feb 23, 2019

@author: ramon
'''

import numpy as np
from math import cos, sin
import math
from modern_robotics.core import ScrewToAxis, VecTose3, MatrixExp6

LINK_TYPE_REV = 0
LINK_TYPE_PRI = 1

FRAME_S = 0
FRAME_B = 1

screw_matrix = None

DEGREE = 57.2958
world_root = np.array([ 0, 0 ])


class Components(object):
    '''
    classdocs
    '''
    Type = ''
    Qframe = None
    def __init__(self, params):
        '''
        Constructor
        '''
        
    def set_Qframe(self, frame):
        self.Qframe = frame

"""
# Created by: Aditya Dua
# 1 June, 2017
# Got from robopy package ( https://github.com/adityadua24/robopy )
"""
class Transforms():

    @classmethod
    def __RxRyRz(cls, theta, unit):
        import math
        if type(theta) is float or type(theta) is int:
            theta = [theta]
        if type(theta) is list:
            if unit == 'deg':
                theta = [(each * math.pi / 180) for each in theta]
                return theta
            else:
                return theta
        else:
            raise AttributeError("\nInvalid argument type.\n"
                                 "theta must be of type: \n"
                                 "float, \n"
                                 "int, or \n"
                                 "list of float or int")
    
    
    @classmethod
    def Rx(cls, theta, unit="rad"):
        theta = cls.__RxRyRz(theta, unit)
        rot = [ cls.rotx(each) for each in theta]
        #return cls(null=True).__fill(rot)
        return rot
    
    @classmethod
    def Ry(cls, theta, unit="rad"):
        theta = cls.__RxRyRz(theta, unit)
        rot = [cls.roty(each) for each in theta]
        #return cls(null=True).__fill(rot)
        return rot
    
    @classmethod
    def Rz(cls, theta, unit="rad"):
        theta = cls.__RxRyRz(theta, unit)
        #print(theta)
        rot = [cls.rotz(each) for each in theta]
        #return cls().__fill(rot)
        return rot
    
    def __fill(self, data):
        for each in data:
            self._list.append(each)
        return self
    
    # ---------------------------------------------------------------------------------------#
    @classmethod
    def rotx(cls,theta, unit="rad"):
        """
        ROTX gives rotation about X axis
    
        :param theta: angle for rotation matrix
        :param unit: unit of input passed. 'rad' or 'deg'
        :return: rotation matrix
    
        rotx(THETA) is an SO(3) rotation matrix (3x3) representing a rotation
        of THETA radians about the x-axis
        rotx(THETA, "deg") as above but THETA is in degrees
        """
        
        if unit == "deg":
            theta = theta * math.pi / 180
        ct = math.cos(theta)
        st = math.sin(theta)
        mat = np.matrix([[1, 0, 0], [0, ct, -st], [0, st, ct]])
        mat = np.asmatrix(mat.round(15))
        return mat
    
    
    # ---------------------------------------------------------------------------------------#
    @classmethod
    def roty(cls,theta, unit="rad"):
        """
        ROTY Rotation about Y axis
    
        :param theta: angle for rotation matrix
        :param unit: unit of input passed. 'rad' or 'deg'
        :return: rotation matrix
    
        roty(THETA) is an SO(3) rotation matrix (3x3) representing a rotation
        of THETA radians about the y-axis
        roty(THETA, "deg") as above but THETA is in degrees
        """
        if unit == "deg":
            theta = theta * math.pi / 180
        ct = math.cos(theta)
        st = math.sin(theta)
        mat = np.matrix([[ct, 0, st], [0, 1, 0], [-st, 0, ct]])
        mat = np.asmatrix(mat.round(15))
        return mat
    
    
    # ---------------------------------------------------------------------------------------#
    @classmethod
    def rotz(cls,theta, unit="rad"):
        """
        ROTZ Rotation about Z axis
    
        :param theta: angle for rotation matrix
        :param unit: unit of input passed. 'rad' or 'deg'
        :return: rotation matrix
    
        rotz(THETA) is an SO(3) rotation matrix (3x3) representing a rotation
        of THETA radians about the z-axis
        rotz(THETA, "deg") as above but THETA is in degrees
        """
        #print(theta)
        if unit == "deg":
            theta = theta * math.pi / 180
        #print(theta)
        ct = math.cos(theta)
        st = math.sin(theta)
        mat = np.matrix([[ct, -st, 0], [st, ct, 0], [0, 0, 1]])
        mat = np.asmatrix(mat.round(15))
        #print(mat)
        return mat
    
    @classmethod
    def trotx(cls,theta, unit="rad", xyz=[0, 0, 0]):
        """
        TROTX Rotation about X axis
    
        :param theta: rotation in radians or degrees
        :param unit: "rad" or "deg" to indicate unit being used
        :param xyz: the xyz translation, if blank defaults to [0,0,0]
        :return: homogeneous transform matrix
    
        trotx(THETA) is a homogeneous transformation (4x4) representing a rotation
        of THETA radians about the x-axis.
        trotx(THETA, 'deg') as above but THETA is in degrees
        trotx(THETA, 'rad', [x,y,z]) as above with translation of [x,y,z]
        """
        tm = cls.rotx(theta, unit)
        tm = np.r_[tm, np.zeros((1, 3))]
        mat = np.c_[tm, np.array([[xyz[0]], [xyz[1]], [xyz[2]], [1]])]
        mat = np.asmatrix(mat.round(15))
        return mat
    
    @classmethod
    def troty(cls, theta, unit="rad", xyz=[0, 0, 0]):
        """
        TROTY Rotation about Y axis
    
        :param theta: rotation in radians or degrees
        :param unit: "rad" or "deg" to indicate unit being used
        :param xyz: the xyz translation, if blank defaults to [0,0,0]
        :return: homogeneous transform matrix
    
        troty(THETA) is a homogeneous transformation (4x4) representing a rotation
        of THETA radians about the y-axis.
        troty(THETA, 'deg') as above but THETA is in degrees
        troty(THETA, 'rad', [x,y,z]) as above with translation of [x,y,z]
        """
        tm = cls.roty(theta, unit)
        tm = np.r_[tm, np.zeros((1, 3))]
        mat = np.c_[tm, np.array([[xyz[0]], [xyz[1]], [xyz[2]], [1]])]
        mat = np.asmatrix(mat.round(15))
        return mat
    
    
    @classmethod
    def trotz(cls, theta, unit="rad", xyz=[0, 0, 0]):
        """
        TROTZ Rotation about Z axis
    
        :param theta: rotation in radians or degrees
        :param unit: "rad" or "deg" to indicate unit being used
        :param xyz: the xyz translation, if blank defaults to [0,0,0]
        :return: homogeneous transform matrix
    
        trotz(THETA) is a homogeneous transformation (4x4) representing a rotation
        of THETA radians about the z-axis.
        trotz(THETA, 'deg') as above but THETA is in degrees
        trotz(THETA, 'rad', [x,y,z]) as above with translation of [x,y,z]
        """
        tm = cls.rotz(theta, unit)
        tm = np.r_[tm, np.zeros((1, 3))]
        mat = np.c_[tm, np.array([[xyz[0]], [xyz[1]], [xyz[2]], [1]])]
        mat = np.asmatrix(mat.round(15))
        return mat
    
    @classmethod
    def transl( cls, x=None, y=None, z=None ):
        """
        TRANSL Create or unpack an SE(3) translational homogeneous transform
    
        :param x: translation along x axes, homogeneous transform or a list of translations
        :param y: translation along y axes
        :param z: translation along z axes
        :return: homogeneous transform with pure translation
    
        Create a translational SE(3) matrix::
    
        T = TRANSL(X, Y, Z) is an SE(3) homogeneous transform (4x4) representing a
        pure translation of X, Y and Z.
    
        T = TRANSL(P) is an SE(3) homogeneous transform (4x4) representing a
        translation of P=[X,Y,Z]. If P (Mx3) it represents a sequence and T (4x4xM)
        is a sequence of homogeneous transforms such that T(:,:,i) corresponds to
        the i'th row of P.
    
        Extract the translational part of an SE(3) matrix::
    
        P = TRANSL(T) is the translational part of a homogeneous transform T as a
        3-element column vector.  If T (4x4xM) is a homogeneous transform sequence
        the rows of P (Mx3) are the translational component of the corresponding
        transform in the sequence.
    
        [X,Y,Z] = TRANSL(T) is the translational part of a homogeneous transform
        T as three components.  If T (4x4xM) is a homogeneous transform sequence
        then X,Y,Z (1xM) are the translational components of the corresponding
        transform in the sequence.
       """
        if type(x) is np.matrix:
            if cls.ishomog(x, [4, 4]):
                return x[:3, 2]
        elif type(x) is list:
            if len(x) == 3:
                temp = np.matrix([[x[0]], [x[1]], [x[2]]])
                temp = np.concatenate((np.eye(3), temp), axis=1)
                return np.concatenate((temp, np.matrix([[0, 0, 0, 1]])), axis=0)
        # todo trajectory case
        elif x is not None and y is not None and z is not None:
            t = np.matrix([[x], [y], [z]])
            return cls.rt2tr(np.eye(3), t)
        else:
            raise AttributeError("Invalid arguments")
        
    @classmethod
    def rt2tr(cls,r, t):
        """
        RT2TR Convert rotation and translation to homogeneous transform
    
        :param r: rotation matrix
        :param t: translation
        :return: homogeneous transform
    
        RT2TR(R, t) is a homogeneous transformation matrix (N+1xN+1) formed from an
        orthonormal rotation matrix R (NxN) and a translation vector t
        (Nx1).  Works for R in SO(2) or SO(3):
        - If R is 2x2 and t is 2x1, then TR is 3x3
        - If R is 3x3 and t is 3x1, then TR is 4x4
        """
        if r.shape == (2, 2):
            if r.shape[0] != r.shape[1]:
                raise AttributeError("R must be square")
            if r.shape[0] != t.shape[0]:
                raise AttributeError("R and t must have the same number of rows")
            tr = np.concatenate((r, t), axis=1)
            tr = np.concatenate((tr, np.matrix([[0, 0, 1]])), axis=0)
            return tr
        else:
            if r.shape[0] != r.shape[1]:
                raise AttributeError("R must be square")
            if r.shape[0] != t.shape[0]:
                raise AttributeError("R and t must have the same number of rows")
            tr = np.concatenate((r, t), axis=1)
            tr = np.concatenate((tr, np.matrix([[0, 0, 0, 1]])), axis=0)
            return tr
    
    
    @classmethod
    def rpy2r(cls, thetas, unit='rad'):
        """
        RPY2R Roll-pitch-yaw angles to rotation matrix
    
        :param thetas: list of angles
        :param order: 'xyz', 'zyx' or 'yxz'
        :param unit: 'rad' or 'deg'
        :return: rotation matrix
    
        RPY2R(ROLL, PITCH, YAW, OPTIONS) is an SO(3) orthonormal rotation matrix
        (3x3) equivalent to the specified roll, pitch, yaw angles angles.
        These correspond to rotations about the Z, Y, X axes respectively. If ROLL,
        PITCH, YAW are column vectors (Nx1) then they are assumed to represent a
        trajectory and R is a three-dimensional matrix (3x3xN), where the last index
        corresponds to rows of ROLL, PITCH, YAW.
    
        R = RPY2R(RPY, OPTIONS) as above but the roll, pitch, yaw angles are taken
        from the vector (1x3) RPY=[ROLL,PITCH,YAW]. If RPY is a matrix(Nx3) then R
        is a three-dimensional matrix (3x3xN), where the last index corresponds to
        rows of RPY which are assumed to be [ROLL,PITCH,YAW].
    
        Options::
            'deg'   Compute angles in degrees (radians default)
            'xyz'   Rotations about X, Y, Z axes (for a robot gripper)
            'yxz'   Rotations about Y, X, Z axes (for a camera)
    
        Note::
        - Toolbox rel 8-9 has the reverse angle sequence as default.
        - ZYX order is appropriate for vehicles with direction of travel in the X
        direction.  XYZ order is appropriate if direction of travel is in the Z direction.
        """
        if type(thetas[0]) is float or type(thetas[0]) is int:
            # TODO
            # enforce if one element is list.
            # All are list. OR one element is int or float then all are either int or float
            thetas = [thetas]  # Put list in a list
    
        if unit == 'deg':
            thetas = [[(angles * math.pi / 180) for angles in each_rpy] for each_rpy in thetas]
        if type(thetas[0]) is list:
            roll = [theta[0] for theta in thetas]
            pitch = [theta[1] for theta in thetas]
            yaw = [theta[2] for theta in thetas]
    
        
            x = [cls.rotx(theta) for theta in yaw]
            y = [cls.roty(theta) for theta in pitch]
            z = [cls.rotz(theta) for theta in roll]
            xyz = [(x[i] * y[i] * z[i]) for i in range(len(thetas))]
            xyz = [np.asmatrix(each.round(15)) for each in xyz]
            if len(xyz) == 1:
                return xyz[0]
            else:
                return xyz

        else:
            raise TypeError('thetas must be a list of roll pitch yaw angles\n'
                            'OR a list of list of roll pitch yaw angles.')
    
    @classmethod    
    def r2t(cls, rmat):
        """
        R2T Convert rotation matrix to a homogeneous transform
    
        :param rmat: rotation matrix
        :return: homogeneous transformation
    
        R2T(rmat) is an SE(2) or SE(3) homogeneous transform equivalent to an
        SO(2) or SO(3) orthonormal rotation matrix rmat with a zero translational
        component. Works for T in either SE(2) or SE(3):
        if rmat is 2x2 then return is 3x3, or
        if rmat is 3x3 then return is 4x4.
    
        Translational component is zero.
        """
        assert isinstance(rmat, np.matrix)
        dim = rmat.shape
        if dim[0] != dim[1]:
            raise ValueError(' Matrix Must be square ')
        elif dim[0] == 2:
            tmp = np.r_[rmat, np.zeros((1, 2))]
            mat = np.c_[tmp, np.array([[0], [0], [1]])]
            mat = np.asmatrix(mat.round(15))
            return mat
        elif dim[0] == 3:
            tmp = np.r_[rmat, np.zeros((1, 3))]
            mat = np.c_[tmp, np.array([[0], [0], [0], [1]])]
            mat = np.asmatrix(mat.round(15))
            return mat
        else:
            raise ValueError(' Value must be a rotation matrix ')
    
    @classmethod   
    def rotationMatrixToEulerAngles(cls, R) :
 
        #assert(isRotationMatrix(R))
         
        sy = math.sqrt(R[0,0] * R[0,0] +  R[1,0] * R[1,0])
         
        singular = sy < 1e-6
     
        if  not singular :
            x = math.atan2(R[2,1] , R[2,2])
            y = math.atan2(-R[2,0], sy)
            z = math.atan2(R[1,0], R[0,0])
        else :
            x = math.atan2(-R[1,2], R[1,1])
            y = math.atan2(-R[2,0], sy)
            z = 0
     
        return np.array([x, y, z])
        
    @classmethod
    def ishomog(cls,tr, dim, rtest=''):
        """ISHOMOG Test if SE(3) homogeneous transformation matrix.
        ISHOMOG(T) is true if the argument T is of dimension 4x4 or 4x4xN, else false.
        ISHOMOG(T, 'valid') as above, but also checks the validity of the rotation sub-matrix.
        See Also: isrot, ishomog2, isvec"""
        try:
            assert type(tr) is np.matrix, "Argument should be a numpy matrix"
            assert dim == (3, 3) or dim == (4, 4)
        except AssertionError:
            return False
        is_valid = None
        if rtest == 'valid':
            is_valid = lambda matrix: abs(np.linalg.det(matrix) - 1) < np.spacing([1])[0]
        flag = True
        if cls.is_mat_list(tr):
            for matrix in tr:
                if not (matrix.shape[0] == dim[0] and matrix.shape[1] == dim[0]):
                    flag = False
            # if rtest = 'valid'
            if flag and rtest == 'valid':
                flag = is_valid(tr[0])  # As in matlab code only first matrix is passed for validity test
                # TODO-Do we need to test all matrices in list for validity of rotation submatrix -- Yes
        elif isinstance(tr, np.matrix):
            if tr.shape[0] == dim[0] and tr.shape[1] == dim[0]:
                if flag and rtest == 'valid':
                    flag = is_valid(tr)
            else:
                flag = False
        else:
            raise ValueError('Invalid data type passed to common.ishomog()')
        return flag
    
    @classmethod
    def is_mat_list(cls,list_matrices):
        """is_mat_list checks(arg1) checks if arg1
        is a list containing numpy matrix data type elements or not.
        If not, False is returned."""
        flag = True
        if isinstance(list_matrices, list):
            for matrix in list_matrices:
                if not isinstance(matrix, np.matrix):
                    flag = False
                    # TODO Check for matrix dimensions?
        else:
            flag = False
        return flag
    

class Link(object):
    '''
    classdocs
    '''
    parent = None
    child = None
    link_length = 0
    
    # End point of the segment
    b = np.array([0,0,0])
    seg_parent = None
    
    theta = 0
    
    link_type = LINK_TYPE_REV
    
    class link_settings():
        def __init__(self):
            self.size = 1
            self.paralllel_to = 'X'
            self.frame_x_angle = 0
            self.frame_y_angle = 0
            self.frame_z_angle = 0

    
    # If root
    def __init__(self):
        '''
        Constructor
        '''
        self.color = (255,0,0)
    
    def create(self, x, y, z, len_, theta):
        '''
        Constructor
        '''
        self.a = Transforms.trotx( 0 , unit='deg' )
        self.theta = theta / DEGREE # Convert to degrees
        self.len = len_
        self.b = Transforms.transl(self.len, 0, 0)
        
        return self
    
    def create_by_parent(self, parent, len_, angle):
        
        self.parent = parent
        self.len = len_
        self.angle = angle / DEGREE
        
        # Ensure b vector is updated
        parent.update()
        self.a = np.copy( parent.b )
        
        return self
    
    def update(self):
        self.calculateB()
    
    # Calculate segment's end point
    def calculateB(self):
        # If element has a parent updates its root to parent end
        #if self.parent != None:
            #self.a = self.parent.b.copy()
        
        # If link is Prismatic, it will follow the orientation from its parent
        if self.link_type == LINK_TYPE_PRI and self.parent != None:
            self.angle = self.parent.angle
            
            
        len = self.len
            
        if self.link_type == LINK_TYPE_PRI:
            links_scale_factor = 1
            len = self.len + self.theta * links_scale_factor
        
        # Remove the '-' to make angles increase in clockwise
        dx = len * cos( -self.angle )
        dy = len * sin( -self.angle )
        self.b.set( self.a.x + dx, self.a.y + dy)
        
        if self.child != None:
            self.child.a = np.copy( self.b )
    
    
    # Drawn segment
    def show(self, img):
        self.a.make_int()
        self.b.make_int()
        #cv2.line(img,(self.a.x,self.a.y),(self.b.x,self.b.y), self.color ,5)
        #cv2.circle( img, (self.a.x,self.a.y), 4, (0,255,0), -1 )
        #cv2.circle( img, (self.b.x,self.b.y), 4, (0,0,255), -1 )
        
        #if self.link_type == LINK_TYPE_REV:
        #     cv2.circle( img, (self.a.x,self.a.y), 8, (0,255,0), 1 )
        # else:
        #     cv2.rectangle( img, (self.a.x-4,self.a.y-4), (self.a.x+4,self.a.y+4), (0,255,0), -1 )
        
        return img

    
class Frame_Template( Components ):
    origin = np.array( [0.,0.,0.], dtype=np.float )
    
    # Frame Transformation/Rotation Homogenius matrix
    T = []
    
    # Axes lines references
    x_plot = None
    y_plot = None
    z_plot = None
    text_plot = None
    
    x_axis = np.array( [ origin[0], len ] ), np.array( [ origin[1], len ] ), np.array( [ origin[2], len ] )
    x_color = 'r'
    
    y_axis = np.array( [ origin[0], len ] ), np.array( [ origin[1], len ] ), np.array( [ origin[2], len ] )
    y_color = 'g'
    
    z_axis = np.array( [ origin[0], len ] ), np.array( [ origin[1], len ] ), np.array( [ origin[2], len ] )
    z_color = 'b'
    
    len = 4
    
    """
        Set axis label
    """
    def set_axe_label(self, label):
        self.axe_label = label
        
    """
        Clear plot from matplot canvas
    """
    def rem_plot(self, plot):
        if plot != None:
            try:
                plot.remove()
            # Plot not in the list exception
            except ValueError:
                pass

class Robot( Frame_Template ):
    def __init__(self, plotCanvas):
        '''
        Constructor
        '''
        self.PlotCanvas = plotCanvas

class W_Hat( Frame_Template ):
    
    
    w_color = 'yellow'
    
    def __init__(self, plotCanvas):
        '''
        Constructor
        '''
        self.PlotCanvas = plotCanvas
        
        self.origin = np.array( [0.,0.,0.], dtype=np.float )
        
        self.w = np.array( [0.,0.,0.], dtype=np.float )
        self.theta = .0
    
        self.w_plot = None
        
        self.w_axis = np.array( [ self.origin[0], self.w[0] ] ), np.array( [ self.origin[1], self.w[1] ] ), np.array( [ self.origin[2], self.w[2] ] )
        
        
    def update_theta(self, theta):
        self.theta = theta
    
    
    def update_axes(self):
        from modern_robotics import VecToso3, MatrixExp3
        
        origin = self.origin
        theta = self.theta
        
        # 1- Get Point's unit vector
        w = self.w + origin
        # 1.1- Compute length of
        w_len = np.linalg.norm( self.w,ord=1)
        if w_len > 0:
            # 1.2- Divide vector by its length
            w_hat = self.w / w_len
        else:
            w_hat = np.array([ 0,0,0 ]) 
        #print(w_hat)
        
        theta_rad = theta*math.pi / 180
        #print(w_hat)
        #print(theta_rad)
        # Compute the Exponential coordinate representation
        w_hat = w_hat * theta_rad
        #print(w_hat)
        # Compute skew-symmetric matrix ŵ
        self.w_skew = VecToso3( w_hat )
        
        # Transform skew_matrix to a Rotation matrix
        R = MatrixExp3( self.w_skew )
        #print(R)
        # Convert rotation matrix to a full transformation matrix
        self.T = Transforms.r2t( np.asmatrix(R) )
        # Apply offset from origin
        self.T = Transforms.transl( origin[0], origin[1], origin[2] ) * self.T
        
        # Compute x-axis
        coordsx = np.array([ [  self.len ], [ 0 ], [ 0 ], [1] ])
        coordsx = self.T * coordsx
        self.x_axis = np.array( [ origin[0], coordsx.item(0) ] ), np.array( [ origin[1], coordsx.item(1) ] ), np.array( [ origin[2], coordsx.item(2) ] )
        
        # Compute y-axis
        coordsy = np.array([ [  0 ], [ self.len ], [ 0 ], [1] ])
        coordsy = self.T * coordsy
        self.y_axis = np.array( [ origin[0], coordsy.item(0) ] ), np.array( [ origin[1], coordsy.item(1) ] ), np.array( [ origin[2], coordsy.item(2) ] )
        
        # Compute z-axis
        coordsz = np.array([ [  0 ], [ 0 ], [ self.len  ], [1] ])
        coordsz = self.T * coordsz
        self.z_axis = np.array( [ origin[0], coordsz.item(0) ] ), np.array( [ origin[1], coordsz.item(1) ] ), np.array( [ origin[2], coordsz.item(2) ] )
        
        # Update W vector
        self.w_axis = np.array( [ self.origin[0], w[0] ] ), np.array( [ self.origin[1], w[1] ] ), np.array( [ self.origin[2], w[2] ] )
        
    
    def clear_plots(self, update_canvas = True):
        # Check if lines were previously created
        self.rem_plot( self.x_plot )
        self.rem_plot( self.y_plot )
        self.rem_plot( self.z_plot )
        self.rem_plot( self.text_plot )
        self.rem_plot( self.w_plot )
            
        if update_canvas:
            self.PlotCanvas.draw()
    
    def draw(self, screw_frame):
        # Update axes angles
        self.update_axes()
        
        # Update Transformation label
        T = self.T
        W = self.w_skew
        #print(T)
        screw_frame.screw_lb_rotation_matrix.setText( np.array2string( T, formatter={'float_kind':lambda T: "%.2f" % T} ))
        screw_frame.screw_lb_skew_matrix.setText( np.array2string( W, formatter={'float_kind':lambda W: "%.2f" % W} ) )
        
        # Check if lines were previously created
        if self.x_plot != None:
            self.x_plot.remove()
        if self.y_plot != None:
            self.y_plot.remove()
        if self.z_plot != None:
            self.z_plot.remove()
        if self.text_plot != None:
            self.text_plot.remove()
        if self.w_plot != None:
            self.w_plot.remove()
        
        # https://matplotlib.org/examples/mplot3d/text3d_demo.html
        self.text_plot = self.PlotCanvas.ax.text( self.x_axis[0][0]-0.25, self.x_axis[1][0], self.x_axis[2][0]-0.4, self.axe_label, (1,1,0), fontsize=12)
        
        self.x_plot, = self.PlotCanvas.ax.plot( self.x_axis[0], self.x_axis[1], self.x_axis[2], color=self.x_color )
        self.y_plot, = self.PlotCanvas.ax.plot( self.y_axis[0], self.y_axis[1], self.y_axis[2], color=self.y_color )
        self.z_plot, = self.PlotCanvas.ax.plot( self.z_axis[0], self.z_axis[1], self.z_axis[2], color=self.z_color )
        
        self.w_plot, = self.PlotCanvas.ax.plot( self.w_axis[0], self.w_axis[1], self.w_axis[2], color=self.w_color )
        
        self.PlotCanvas.draw()
    
class Screw( Frame_Template ):
    
    path_max_theta = -1
    
    def __init__(self, plotCanvas):
        '''
        Constructor
        '''
        self.PlotCanvas = plotCanvas
        
        self.origin = np.array( [0.,0.,0.], dtype=np.float )
        
        self.s = np.array( [0.,0.,0.], dtype=np.float )
        self.s_end = np.array( [0.,0.,0.], dtype=np.float )
        
        self.theta = .0
        self.h = .0
        
        self.q = np.array( [0.,0.,0.], dtype=np.float )
        self.q_factor = 0.
        
        self.s_hat_plot = None
        self.s_hat_color = 'yellow'
        
        self.q_plot = None
        self.h_plot = None
        self.q_text = None
        
        self.screw_path_plot = None
        self.bl_show_path = False
        
        
    def update_theta(self, theta):
        self.theta = theta
    
    def update_h(self, h):
        self.h = h
        
    def update_q(self, q):
        
        if( q >=0 ):
            self.q_factor = q
        
        self.q = ( self.s_end - self.s ) * (self.q_factor/100.0)
        self.q += self.s
        #print(self.q)
        
        
    def update_s(self, s):
        
        # Convert vector s to unit vector
        s_len = np.linalg.norm( s,ord=1)
        
        if s_len > 0:
            s_hat = s / s_len
        else:
            s_hat = np.array([ 0,0,0 ])
            
        self.s = s_hat
    
    def update_axes(self):
        
        origin = self.origin
        theta = self.theta
        
        theta_rad = theta*math.pi / 180
        
        s_hat = self.s + self.s_end
        
        
        s_hat_len = np.linalg.norm( s_hat,ord=1)
        if s_hat_len > 0:
            # 1.2- Divide vector by its length
            s_hat = s_hat / s_hat_len
        else:
            s_hat = np.array([ 0,0,0 ]) 
        
        S = ScrewToAxis( self.q, s_hat, self.h ) * theta_rad
        
        self.V_skew = VecTose3( S )
        
        self.T = MatrixExp6( self.V_skew )
        
        #print(R)
        # Apply Rotation/Translation from screw axis to the frame
        T = Transforms.transl( origin[0], origin[1], origin[2] ) * self.T
        
        new_origin = np.array([ [  0 ], [ 0 ], [ 0 ], [1] ])
        # 2- Translate it to configured origin
        # 3- Apply previous transformations
        new_origin =  T * new_origin
        
        new_origin = np.array( [ new_origin.item(0), new_origin.item(1), new_origin.item(2) ] )
        
        #print(T)
        #print(new_origin)
        #print(new_origin.item(0))
        
        coordsx = np.array([ [  self.len ], [ 0 ], [ 0 ], [1] ])
        coordsx = T * coordsx
        self.x_axis = np.array( [ new_origin[0], coordsx.item(0) ] ), np.array( [ new_origin[1], coordsx.item(1) ] ), np.array( [ new_origin[2], coordsx.item(2) ] )
        
        coordsy = np.array([ [  0 ], [ self.len ], [ 0 ], [1] ])
        coordsy = T * coordsy
        self.y_axis = np.array( [ new_origin[0], coordsy.item(0) ] ), np.array( [ new_origin[1], coordsy.item(1) ] ), np.array( [ new_origin[2], coordsy.item(2) ] )
        
        coordsz = np.array([ [  0 ], [ 0 ], [ self.len  ], [1] ])
        coordsz = T * coordsz
        self.z_axis = np.array( [ new_origin[0], coordsz.item(0) ] ), np.array( [ new_origin[1], coordsz.item(1) ] ), np.array( [ new_origin[2], coordsz.item(2) ] )
        
        # Update s_hat vector
        self.s_hat_axis = np.array( [ self.s[0], self.s_end[0] ] ), np.array( [ self.s[1], self.s_end[1] ] ), np.array( [ self.s[2], self.s_end[2] ] )
        
        # Update q point, position in s_hat vector
        self.update_q( -1 )
    
    def compute_screw_point(self, theta):
        origin = self.origin
        
        theta_rad = theta*math.pi / 180
        
        s_hat = self.s + self.s_end
        
        
        s_hat_len = np.linalg.norm( s_hat,ord=1)
        if s_hat_len > 0:
            # 1.2- Divide vector by its length
            s_hat = s_hat / s_hat_len
        else:
            s_hat = np.array([ 0,0,0 ]) 
        
        S = ScrewToAxis( self.q, s_hat, self.h ) * theta_rad
        
        self.V_skew = VecTose3( S )
        
        self.T = MatrixExp6( self.V_skew )
        
        #print(R)
        # Apply Rotation/Translation from screw axis to the frame
        T = Transforms.transl( origin[0], origin[1], origin[2] ) * self.T
        
        new_origin = np.array([ [  0 ], [ 0 ], [ 0 ], [1] ])
        # 2- Translate it to configured origin
        # 3- Apply previous transformations
        new_origin =  T * new_origin
        
        new_origin = np.array( [ new_origin.item(0), new_origin.item(1), new_origin.item(2) ] )
        
        return new_origin    
    
    def show_path(self):
        self.rem_plot( self.screw_path_plot )
        
        if( self.bl_show_path ):
            #print(self.path_max_theta)
            screw_x = []
            screw_y = []
            screw_z = []
            #c = []        # Used in scatter3d
            
            count = 50
            while count < (self.path_max_theta) * 1.5/self.h:
                
                p = self.compute_screw_point( count )
                
                screw_x.append( p[0] )
                screw_y.append( p[1] )
                screw_z.append( p[2] )
                #c.append(0)
                
                
                count += 10
                #print(p)
                
            #self.screw_path_plot = self.PlotCanvas.ax.scatter3D( screw_x, screw_y, screw_z, s=20, c=c)
            self.screw_path_plot, = self.PlotCanvas.ax.plot( screw_x, screw_y, screw_z, color='black' )
        
        self.PlotCanvas.draw()

    def clear_plots(self, update_canvas = True):
        # Check if lines were previously created
        self.rem_plot( self.x_plot )
        self.rem_plot( self.y_plot )
        self.rem_plot( self.z_plot )

        self.rem_plot( self.text_plot )
        self.rem_plot( self.s_hat_plot )
        
        self.rem_plot( self.q_plot )
        self.rem_plot( self.q_text )
        self.rem_plot( self.screw_path_plot )
        
        if update_canvas:
            self.PlotCanvas.draw()
        
    
    def draw(self, screw_frame):
        
        # Update axes angles
        self.update_axes()
        
        # Update Transformation label
        T = self.T
        V = self.V_skew
        #print(T)
        screw_frame.screw_lb_rotation_matrix.setText( np.array2string( T, formatter={'float_kind':lambda T: "%.2f" % T} ))
        screw_frame.screw_lb_skew_matrix.setText( np.array2string( V, formatter={'float_kind':lambda V: "%.2f" % V} ) )
        
        # Check if lines were previously created
        self.rem_plot( self.x_plot )
        self.rem_plot( self.y_plot )
        self.rem_plot( self.z_plot )

        self.rem_plot( self.text_plot )
        self.rem_plot( self.s_hat_plot )
        
        self.rem_plot( self.q_plot )
        self.rem_plot( self.q_text )
            
        
        # https://matplotlib.org/examples/mplot3d/text3d_demo.html
        self.text_plot = self.PlotCanvas.ax.text( self.x_axis[0][0]-0.25, self.x_axis[1][0], self.x_axis[2][0]-0.4, self.axe_label, (1,1,0), fontsize=12)
        
        self.x_plot, = self.PlotCanvas.ax.plot( self.x_axis[0], self.x_axis[1], self.x_axis[2], color=self.x_color )
        self.y_plot, = self.PlotCanvas.ax.plot( self.y_axis[0], self.y_axis[1], self.y_axis[2], color=self.y_color )
        self.z_plot, = self.PlotCanvas.ax.plot( self.z_axis[0], self.z_axis[1], self.z_axis[2], color=self.z_color )
        
        self.s_hat_plot, = self.PlotCanvas.ax.plot( self.s_hat_axis[0], self.s_hat_axis[1], self.s_hat_axis[2], color=self.s_hat_color )
        
        # Check if
        #if( np.sum( self.s_end ) != 0 or np.sum( self.s ) != 0 ):
        if ( np.linalg.norm( self.s_hat_axis,ord=1) ):
            self.q_plot = self.PlotCanvas.ax.scatter3D( [self.q[0]], [self.q[1]], [self.q[2]], s=40, c=[0])
            self.q_text = self.PlotCanvas.ax.text( self.q[0], self.q[1], self.q[2]-1, 'q', (1,1,0), fontsize=12)
            
            self.show_path()
            
        self.PlotCanvas.draw()


class Frame_Element( Frame_Template ):
    
    Type = 'Frame'
    
    color = 'g'
    
    
    def __init__(self, plotCanvas):
        '''
        Constructor
        '''
        self.PlotCanvas = plotCanvas
        
        self.origin = np.array( [0.,0.,0.], dtype=np.float )
        self.trans = np.array( [0.,0.,0.], dtype=np.float )
        self.angles = np.array( [ 0.,0.,0. ], dtype=np.float )
        self.rotation_order = []
        
        #self.origin = params['origin']
        
    def update_angles(self, angles):
        self.angles[0] = angles[0]
        self.angles[1] = angles[1]
        self.angles[2] = angles[2]
    
     
    def set_translation(self, rot_hom_matrix):
        rot_hom_matrix.itemset( (0,3), self.origin[0] )
        rot_hom_matrix.itemset( (1,3), self.origin[1] )
        rot_hom_matrix.itemset( (2,3), self.origin[2] )
     
    def update_axes(self):
        
        origin = self.origin
        
        #self.angles[2] = 181
        
        x_angle = int( self.angles[0] )
        y_angle = int( self.angles[1] )
        z_angle = int( self.angles[2] )
        
        rx = Transforms.trotx( x_angle , unit='deg' )
        ry = Transforms.troty( y_angle , unit='deg' )
        rz = Transforms.trotz( z_angle , unit='deg' )
        
        # This only creates a homogeneous Transformation
        R = Transforms.trotx( 0 , unit='deg' )
        
        for axe in self.rotation_order:
            
            #print('Rotation order: ' + str(self.rotation_order) )
            # Do rotation about X axe
            if axe == 0:
                R = R * rx

            # Do Y's rotation
            elif axe == 1:
                R = R * ry

            # Do Z's rotation
            elif axe == 2:
                R = R * rz
            
            # Axe == 3 X, == 5 Y, == 6 Z
            elif axe >= 3:
                R = R * Transforms.transl( self.trans[0] *int( axe == 3 ), self.trans[1] * int( axe == 4) \
                    , self.trans[2] *int( axe == 5) )
                    
        
        self.Trans = R
        
        # Compute Rx line
        # X_axe line endpoint coordinates before any transformations
        coordsx = np.array([ [  self.len ], [ 0 ], [ 0 ], [1] ])
        # Program needs different sets of x,y,z for translation displacement
        #if True or np.sum( self.trans ) != 0 and len( self.rotation_order )  > 0 and self.rotation_order[ 0 ] != 3:
            
        # 1- Set origin to 0,0,0    
        new_origin = np.array([ [  0 ], [ 0 ], [ 0 ], [1] ])
        # 2- Translate it to configured origin
        # 3- Apply previous transformations
        new_origin = Transforms.transl( origin[0], origin[1], origin[2] ) * R * new_origin
        
        coordsx = Transforms.transl( origin[0], origin[1], origin[2] ) * R * coordsx
        
        self.x_axis = np.array( [ new_origin.item(0), coordsx.item(0) ] ), np.array( [ new_origin.item(1), coordsx.item(1) ] ), np.array( [ new_origin.item(2), coordsx.item(2) ] )
        
        # Compute Ry line
        # Apply Transformation to Y's point A
        y_origin = np.array([ [  0 ], [ 0 ], [ 0 ], [1] ])
        y_origin = Transforms.transl( origin[0], origin[1], origin[2] ) * R * y_origin
        
        coordsy = np.array([ [  0 ], [ self.len ], [ 0 ], [1] ])
        coordsy = Transforms.transl( origin[0], origin[1], origin[2] ) * R * coordsy
        
        self.y_axis = np.array( [ y_origin.item(0), coordsy.item(0) ] ), np.array( [ y_origin.item(1), coordsy.item(1) ] ), np.array( [ y_origin.item(2), coordsy.item(2) ] )
        
        
        # Compute Rz line
        z_origin = np.array([ [  0 ], [ 0 ], [ 0 ], [1] ])
        z_origin = Transforms.transl( origin[0], origin[1], origin[2] ) * R * z_origin
        
        coordsz = np.array([ [  0 ], [ 0 ], [ self.len ], [1] ])
        coordsz = Transforms.transl( origin[0], origin[1], origin[2] ) * R * coordsz
        self.z_axis = np.array( [ z_origin.item(0), coordsz.item(0) ] ), np.array( [ z_origin.item(1), coordsz.item(1) ] ), np.array( [ z_origin.item(2), coordsz.item(2) ] )
     
    
    def clear_plots(self, bl_update_canvas = True):
        # Check if lines were previously created
        self.rem_plot( self.x_plot )
        self.rem_plot( self.y_plot )
        self.rem_plot( self.z_plot )
        self.rem_plot( self.text_plot )
        
        if bl_update_canvas:
            self.PlotCanvas.draw()
        
    def draw(self, rotation_frame):
        # Update axes angles
        self.update_axes()
        
        # Check if lines were previously created
        if self.x_plot != None:
            self.x_plot.remove()
        if self.y_plot != None:
            self.y_plot.remove()
        if self.z_plot != None:
            self.z_plot.remove()
        if self.text_plot != None:
            self.text_plot.remove()
        
        rotation_frame.frame_lb_rotation_matrix.setText( np.array2string( self.Trans, formatter={'float_kind':lambda T: "%.2f" % T} ))
        
        # https://matplotlib.org/examples/mplot3d/text3d_demo.html
        self.text_plot = self.PlotCanvas.ax.text( self.x_axis[0][0]-0.25, self.x_axis[1][0], self.x_axis[2][0]-0.4, self.axe_label, (1,1,0), fontsize=12)
        
        self.x_plot, = self.PlotCanvas.ax.plot( self.x_axis[0], self.x_axis[1], self.x_axis[2], color=self.x_color )
        self.y_plot, = self.PlotCanvas.ax.plot( self.y_axis[0], self.y_axis[1], self.y_axis[2], color=self.y_color )
        self.z_plot, = self.PlotCanvas.ax.plot( self.z_axis[0], self.z_axis[1], self.z_axis[2], color=self.z_color )
        
        self.PlotCanvas.draw()