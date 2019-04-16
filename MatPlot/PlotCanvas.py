'''
Created on Feb 23, 2019

@author: ramon
'''

import numpy as np

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import axes3d

from PyQt5 import QtWidgets

class Draw_Object():
    
    PLOT_DEFAULT = 0
    PLOT_LINE = 1
    PLOT_SCATTER = 2

    
    def __init__(self, X, Y, Z, plot_type):
        pass

class PlotCanvas(FigureCanvas):
 
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        #self.axes = fig.add_subplot(111)
 
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
 
        FigureCanvas.setSizePolicy(self,
                QtWidgets.QSizePolicy.Expanding,
                QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        
        #plt.style.use('dark_background')
        
        self.ax = self.fig.add_subplot(111,projection='3d')
        self.reset_plot()
        #self.plot()
        
    def plot(self):

        X, Y, Z = np.array( [-5,4] ), np.array( [-5,4] ), np.array( [-5,4] )
        #ax.plot_wireframe(X,Y,Z)
        a, = self.ax.plot(X,Y,Z)
        #b = self.ax.scatter3D(X,Y,Z,c='r',marker='o')
        self.draw()
        #a.remove()
        #b.remove()
        
    def reset_plot(self):
        self.ax.set_xlabel('X axis')
        self.ax.set_ylabel('Y axis')
        self.ax.set_zlabel('Z axis')
        
        dist = 7
        alpha = .6
        
        # Draw X reference axe
        X, Y, Z = np.array( [-dist,dist] ), np.array( [0,0] ), np.array( [0,0] )
        a, = self.ax.plot(X,Y,Z, color='red')
        a.set_alpha( alpha )
        
        # Draw Y reference axe
        X, Y, Z = np.array( [0,0] ), np.array( [-dist,dist] ), np.array( [0,0] )
        b, = self.ax.plot(X,Y,Z, color='green')
        b.set_alpha( alpha )
        
        # Draw Z reference axe
        X, Y, Z = np.array( [0,0] ), np.array( [0,0] ), np.array( [-dist,dist] )
        c, = self.ax.plot(X,Y,Z, color='blue')
        c.set_alpha( alpha )
        
        #self.ax.legend()
        a, = self.ax.plot([0],[0], color='red', label='X')
        b, = self.ax.plot([0],[0], color='green', label='Y')
        c, = self.ax.plot([0],[0], color='blue', label='Z')
        d, = self.ax.plot([0],[0], color='yellow', label='ω̂--Ŝ')
        self.ax.legend()
        
        #self.ax.set_title('Boto pra quebrar')
        
        self.draw()
        
        
    def plot_lines(self):
        #xline=((min(data[:,0]),max(data[:,0])),(0,0),(0,0))
        #ax.plot(xline[0],xline[1],xline[2],'grey')
        #yline=((0,0),(min(data[:,1]),max(data[:,1])),(0,0))
        #ax.plot(yline[0],yline[1],yline[2],'grey')
        #zline=((0,0),(0,0),(min(data[:,2]),max(data[:,2])))
        #x.plot(zline[0],zline[1],zline[2],'grey')
        pass
        