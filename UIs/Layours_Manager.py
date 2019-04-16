'''
Created on Feb 24, 2019

@author: ramon
'''


from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
from Components import Frame_Template

DEGREE = 57.2958

class Frames_Template( QtWidgets.QFrame ):
    
    axe_scale = .5
    rotation_order = []     # Orders where the operations has been done
    matplot_frame = None    # Element containing matplotlib library
    
    labels_tranformations = list( range(20) )
    labels_w = list( range(20) )
    labels_screws = list( range(20) )
    
    # Changes a widget's value without triggering a signal
    def nonSignal_change(self, widget, value):
        # Disable signals
        widget.blockSignals( True )
        # Set value
        widget.setValue( value )
        # Re-enable signals
        widget.blockSignals( False )

    def destroy0(self):
        
        for item in self.children():
            item.deleteLater()
        
        self.matplot_frame.clear_plots()
        
        self.deleteLater()
        self.destroy()
            #widget = item.widget()
            #if widget is not None:
            #    widget.deleteLater()
            #else:
            #    self.deleteLayout(item.layout())
                
        return
        
        while self.layout().count():
            item = self.layout().takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                self.deleteLayout(item.layout())

class Frame_W_Theta( Frames_Template ):
    
    def __init__(self, parent):
        '''
        Constructor
        '''
        super().__init__( parent)
        
        self.init_widgets()
        
        
        self.retranslateUi()
        
        # Seekbar signals
        self.screw_frame_sb_x_origin.valueChanged.connect(self.on_x_origin_changed)
        self.screw_frame_sb_y_origin.valueChanged.connect(self.on_y_origin_changed)
        self.screw_frame_sb_z_origin.valueChanged.connect(self.on_z_origin_changed)
        
        self.screw_sb_w_x_trans.valueChanged.connect(self.on_w_x_trans_changed)
        self.screw_sb_w_y_trans.valueChanged.connect(self.on_w_y_trans_changed)
        self.screw_sb_w_z_trans.valueChanged.connect(self.on_w_z_trans_changed)
        
        self.screw_sb_w_theta_angle.valueChanged.connect(self.on_theta_angle_changed)
        
        # DoubleSpinBox signals
        self.screw_frame_spinb_x_origin.valueChanged.connect(self.on_x_origin_changed)
        self.screw_frame_spinb_y_origin.valueChanged.connect(self.on_y_origin_changed)
        self.screw_frame_spinb_z_origin.valueChanged.connect(self.on_z_origin_changed)
        
        self.screw_spinb_w_x_trans.valueChanged.connect(self.on_w_x_trans_changed)
        self.screw_spinb_w_y_trans.valueChanged.connect(self.on_w_y_trans_changed)
        self.screw_spinb_w_z_trans.valueChanged.connect(self.on_w_z_trans_changed)
        
        self.screw_spinb_w_theta_angle.valueChanged.connect(self.on_theta_angle_changed)
        
        
        self.show()
    
    """ Create widgets"""
    def init_widgets(self):
        self.setGeometry(QtCore.QRect(800, 0, 221, 601))
        
        self.setStyleSheet("background-color: rgb(255, 255, 255)")
        
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        
        self.setPalette(palette)
        self.setAutoFillBackground(True)
        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.setFrameShadow(QtWidgets.QFrame.Raised)
        self.setObjectName("frm_screw_control")
        
        self.screw_frame_sb_x_origin = QtWidgets.QSlider(self)
        self.screw_frame_sb_x_origin.setGeometry(QtCore.QRect(22, 90, 121, 29))
        self.screw_frame_sb_x_origin.setMinimum(-10)
        self.screw_frame_sb_x_origin.setMaximum(10)
        self.screw_frame_sb_x_origin.setOrientation(QtCore.Qt.Horizontal)
        self.screw_frame_sb_x_origin.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.screw_frame_sb_x_origin.setTickInterval(0)
        self.screw_frame_sb_x_origin.setObjectName("screw_frame_sb_x_origin")
        self.frame_lb_component_name = QtWidgets.QLabel(self)
        self.frame_lb_component_name.setGeometry(QtCore.QRect(10, 10, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.frame_lb_component_name.setFont(font)
        self.frame_lb_component_name.setAlignment(QtCore.Qt.AlignCenter)
        self.frame_lb_component_name.setObjectName("frame_lb_component_name")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(2, 90, 21, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(2, 120, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.screw_frame_sb_y_origin = QtWidgets.QSlider(self)
        self.screw_frame_sb_y_origin.setGeometry(QtCore.QRect(22, 120, 121, 29))
        self.screw_frame_sb_y_origin.setMinimum(-10)
        self.screw_frame_sb_y_origin.setMaximum(10)
        self.screw_frame_sb_y_origin.setOrientation(QtCore.Qt.Horizontal)
        self.screw_frame_sb_y_origin.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.screw_frame_sb_y_origin.setTickInterval(0)
        self.screw_frame_sb_y_origin.setObjectName("screw_frame_sb_y_origin")
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(2, 150, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.screw_frame_sb_z_origin = QtWidgets.QSlider(self)
        self.screw_frame_sb_z_origin.setGeometry(QtCore.QRect(22, 150, 121, 29))
        self.screw_frame_sb_z_origin.setMinimum(-10)
        self.screw_frame_sb_z_origin.setMaximum(10)
        self.screw_frame_sb_z_origin.setOrientation(QtCore.Qt.Horizontal)
        self.screw_frame_sb_z_origin.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.screw_frame_sb_z_origin.setTickInterval(0)
        self.screw_frame_sb_z_origin.setObjectName("screw_frame_sb_z_origin")
        self.label_8 = QtWidgets.QLabel(self)
        self.label_8.setGeometry(QtCore.QRect(2, 343, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.screw_sb_w_theta_angle = QtWidgets.QSlider(self)
        self.screw_sb_w_theta_angle.setGeometry(QtCore.QRect(22, 340, 121, 29))
        self.screw_sb_w_theta_angle.setMinimum(0)
        self.screw_sb_w_theta_angle.setMaximum(359)
        self.screw_sb_w_theta_angle.setOrientation(QtCore.Qt.Horizontal)
        self.screw_sb_w_theta_angle.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.screw_sb_w_theta_angle.setTickInterval(0)
        self.screw_sb_w_theta_angle.setObjectName("screw_sb_w_theta_angle")
        
        self.label_15 = QtWidgets.QLabel(self)
        self.label_15.setGeometry(QtCore.QRect(20, 200, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_23 = QtWidgets.QLabel(self)
        self.label_23.setGeometry(QtCore.QRect(2, 235, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.screw_sb_w_z_trans = QtWidgets.QSlider(self)
        self.screw_sb_w_z_trans.setGeometry(QtCore.QRect(22, 300, 121, 29))
        self.screw_sb_w_z_trans.setMinimum(-10)
        self.screw_sb_w_z_trans.setMaximum(10)
        self.screw_sb_w_z_trans.setOrientation(QtCore.Qt.Horizontal)
        self.screw_sb_w_z_trans.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.screw_sb_w_z_trans.setTickInterval(0)
        self.screw_sb_w_z_trans.setObjectName("screw_sb_w_z_trans")
        self.label_24 = QtWidgets.QLabel(self)
        self.label_24.setGeometry(QtCore.QRect(2, 270, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self)
        self.label_25.setGeometry(QtCore.QRect(2, 300, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.screw_sb_w_x_trans = QtWidgets.QSlider(self)
        self.screw_sb_w_x_trans.setGeometry(QtCore.QRect(22, 235, 121, 29))
        self.screw_sb_w_x_trans.setMinimum(-10)
        self.screw_sb_w_x_trans.setMaximum(10)
        self.screw_sb_w_x_trans.setOrientation(QtCore.Qt.Horizontal)
        self.screw_sb_w_x_trans.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.screw_sb_w_x_trans.setTickInterval(0)
        self.screw_sb_w_x_trans.setObjectName("screw_sb_w_x_trans")
        self.screw_sb_w_y_trans = QtWidgets.QSlider(self)
        self.screw_sb_w_y_trans.setGeometry(QtCore.QRect(22, 270, 121, 29))
        self.screw_sb_w_y_trans.setMinimum(-10)
        self.screw_sb_w_y_trans.setMaximum(10)
        self.screw_sb_w_y_trans.setOrientation(QtCore.Qt.Horizontal)
        self.screw_sb_w_y_trans.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.screw_sb_w_y_trans.setTickInterval(0)
        self.screw_sb_w_y_trans.setObjectName("screw_sb_w_y_trans")
        self.screw_lb_rotation_matrix = QtWidgets.QLabel(self)
        self.screw_lb_rotation_matrix.setGeometry(QtCore.QRect(30, 390, 190, 91))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setItalic(False)
        font.setBold(True)
        self.screw_lb_rotation_matrix.setFont(font)
        self.screw_lb_rotation_matrix.setTextFormat(QtCore.Qt.PlainText)
        self.screw_lb_rotation_matrix.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.screw_lb_rotation_matrix.setWordWrap(False)
        self.screw_lb_rotation_matrix.setObjectName("screw_lb_rotation_matrix")
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(5, 390, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_7.setWordWrap(False)
        self.label_7.setObjectName("label_7")
        self.screw_frame_spinb_x_origin = QtWidgets.QDoubleSpinBox(self)
        self.screw_frame_spinb_x_origin.setGeometry(QtCore.QRect(147, 90, 69, 26))
        self.screw_frame_spinb_x_origin.setDecimals(2)
        self.screw_frame_spinb_x_origin.setMinimum(-10.0)
        self.screw_frame_spinb_x_origin.setMaximum(10.0)
        self.screw_frame_spinb_x_origin.setSingleStep(0.5)
        self.screw_frame_spinb_x_origin.setProperty("value", 0.0)
        self.screw_frame_spinb_x_origin.setObjectName("screw_frame_spinb_x_origin")
        self.screw_frame_spinb_y_origin = QtWidgets.QDoubleSpinBox(self)
        self.screw_frame_spinb_y_origin.setGeometry(QtCore.QRect(147, 120, 69, 26))
        self.screw_frame_spinb_y_origin.setDecimals(2)
        self.screw_frame_spinb_y_origin.setMinimum(-10.0)
        self.screw_frame_spinb_y_origin.setMaximum(10.0)
        self.screw_frame_spinb_y_origin.setSingleStep(0.5)
        self.screw_frame_spinb_y_origin.setProperty("value", 0.0)
        self.screw_frame_spinb_y_origin.setObjectName("screw_frame_spinb_y_origin")
        self.screw_frame_spinb_z_origin = QtWidgets.QDoubleSpinBox(self)
        self.screw_frame_spinb_z_origin.setGeometry(QtCore.QRect(147, 150, 69, 26))
        self.screw_frame_spinb_z_origin.setDecimals(2)
        self.screw_frame_spinb_z_origin.setMinimum(-10.0)
        self.screw_frame_spinb_z_origin.setMaximum(10.0)
        self.screw_frame_spinb_z_origin.setSingleStep(0.5)
        self.screw_frame_spinb_z_origin.setProperty("value", 0.0)
        self.screw_frame_spinb_z_origin.setObjectName("screw_frame_spinb_z_origin")
        self.screw_spinb_w_x_trans = QtWidgets.QDoubleSpinBox(self)
        self.screw_spinb_w_x_trans.setGeometry(QtCore.QRect(147, 235, 69, 26))
        self.screw_spinb_w_x_trans.setDecimals(3)
        self.screw_spinb_w_x_trans.setMinimum(-10.0)
        self.screw_spinb_w_x_trans.setMaximum(10.0)
        self.screw_spinb_w_x_trans.setSingleStep(0.5)
        self.screw_spinb_w_x_trans.setProperty("value", 0.0)
        self.screw_spinb_w_x_trans.setObjectName("screw_spinb_w_x_trans")
        self.screw_spinb_w_y_trans = QtWidgets.QDoubleSpinBox(self)
        self.screw_spinb_w_y_trans.setGeometry(QtCore.QRect(147, 270, 69, 26))
        self.screw_spinb_w_y_trans.setDecimals(3)
        self.screw_spinb_w_y_trans.setMinimum(-10.0)
        self.screw_spinb_w_y_trans.setMaximum(10.0)
        self.screw_spinb_w_y_trans.setSingleStep(0.5)
        self.screw_spinb_w_y_trans.setProperty("value", 0.0)
        self.screw_spinb_w_y_trans.setObjectName("screw_spinb_w_y_trans")
        self.screw_spinb_w_z_trans = QtWidgets.QDoubleSpinBox(self)
        self.screw_spinb_w_z_trans.setGeometry(QtCore.QRect(147, 300, 69, 26))
        self.screw_spinb_w_z_trans.setDecimals(3)
        self.screw_spinb_w_z_trans.setMinimum(-10.0)
        self.screw_spinb_w_z_trans.setMaximum(10.0)
        self.screw_spinb_w_z_trans.setSingleStep(0.5)
        self.screw_spinb_w_z_trans.setProperty("value", 0.0)
        self.screw_spinb_w_z_trans.setObjectName("screw_spinb_w_z_trans")
        self.screw_spinb_w_theta_angle = QtWidgets.QDoubleSpinBox(self)
        self.screw_spinb_w_theta_angle.setGeometry(QtCore.QRect(147, 343, 69, 26))
        self.screw_spinb_w_theta_angle.setDecimals(2)
        self.screw_spinb_w_theta_angle.setMinimum(0.0)
        self.screw_spinb_w_theta_angle.setMaximum(359.0)
        self.screw_spinb_w_theta_angle.setSingleStep(0.5)
        self.screw_spinb_w_theta_angle.setProperty("value", 0)
        self.screw_spinb_w_theta_angle.setObjectName("screw_spinb_w_theta_angle")
        
        self.screw_lb_skew_matrix = QtWidgets.QLabel(self)
        self.screw_lb_skew_matrix.setGeometry(QtCore.QRect(30, 490, 190, 91))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.screw_lb_skew_matrix.setFont(font)
        self.screw_lb_skew_matrix.setTextFormat(QtCore.Qt.PlainText)
        self.screw_lb_skew_matrix.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.screw_lb_skew_matrix.setWordWrap(False)
        self.screw_lb_skew_matrix.setObjectName("screw_lb_skew_matrix")
        self.label_9 = QtWidgets.QLabel(self)
        self.label_9.setGeometry(QtCore.QRect(5, 490, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_9.setWordWrap(False)
        self.label_9.setObjectName("label_9")
    
    """Label widgets texts"""    
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        
        self.frame_lb_component_name.setText(_translate("MainWindow", "Component Name"))
        self.label_3.setText(_translate("MainWindow", "Frame Origin"))
        self.label_4.setText(_translate("MainWindow", "X:"))
        self.label_5.setText(_translate("MainWindow", "Y:"))
        self.label_6.setText(_translate("MainWindow", "Z:"))
        self.label_8.setText(_translate("MainWindow", "θ"))
        self.label_15.setText(_translate("MainWindow", "W Coordinates"))
        self.label_23.setText(_translate("MainWindow", "X:"))
        self.label_24.setText(_translate("MainWindow", "Y"))
        self.label_25.setText(_translate("MainWindow", "Z"))
        self.screw_lb_rotation_matrix.setText(_translate("MainWindow", "[[0.00 -0.50 0.33]\n"
"[0.50 0.00 -0.17]\n"
"[-0.33 0.17 0.00]]"))
        self.label_7.setText(_translate("MainWindow", "T:"))
        
        self.screw_lb_skew_matrix.setText(_translate("MainWindow", "[[0.00 -0.50 0.33]\n"
"[0.50 0.00 -0.17]\n"
"[-0.33 0.17 0.00]]"))
        self.label_9.setText(_translate("MainWindow", "[ω̂]:"))
        
        
    def set_label(self, label_name):
        label = self.get_label()
        self.frame_lb_component_name.setText( label_name + str(label))
        return label
        
    # Get a label number
    def get_label(self):
        self.label = Frames_Template.labels_w.pop(0)
        return self.label
    
    # Destroy/Clean object and release its label
    def destroy(self, *args, **kwargs):
        Frames_Template.destroy(self, *args, **kwargs)
        Frames_Template.labels_w.append( self.label )
    
    def set_component_frame(self, frame_component):
        self.matplot_frame = frame_component
        
    @QtCore.pyqtSlot()
    def on_x_origin_changed(self):
        
        #print(self.sender().__class__.__name__)
        # Check if called by SpinBox or SeekBar
        if self.sender().__class__ == QtWidgets.QDoubleSpinBox:
            value = self.screw_frame_spinb_x_origin.value()
            # Disable SeekBar signal before editing it or this method will be called again
            self.screw_frame_sb_x_origin.blockSignals( True )
            self.screw_frame_sb_x_origin.setValue( value )
            self.screw_frame_sb_x_origin.blockSignals( False )
        else:
            value = self.screw_frame_sb_x_origin.value()
            value *= self.axe_scale
            
            self.screw_frame_spinb_x_origin.blockSignals( True )
            self.screw_frame_spinb_x_origin.setValue( value )
            self.screw_frame_spinb_x_origin.blockSignals( False )
        
        if self.matplot_frame != None:
            self.matplot_frame.origin[0] = value
            self.matplot_frame.draw( self )
    
    @QtCore.pyqtSlot()            
    def on_y_origin_changed(self):
        
        # Check if called by SpinBox or SeekBar
        if self.sender().__class__ == QtWidgets.QDoubleSpinBox:
            value = self.screw_frame_spinb_y_origin.value()
            # Disable SeekBar signal before editing it or this method will be called again
            self.screw_frame_sb_y_origin.blockSignals( True )
            self.screw_frame_sb_y_origin.setValue( value )
            self.screw_frame_sb_y_origin.blockSignals( False )
        else:
            value = self.screw_frame_sb_y_origin.value()
            value *= self.axe_scale
            
            self.screw_frame_spinb_y_origin.blockSignals( True )
            self.screw_frame_spinb_y_origin.setValue( value )
            self.screw_frame_spinb_y_origin.blockSignals( False )
        
        if self.matplot_frame != None:
            self.matplot_frame.origin[1] = value
            self.matplot_frame.draw( self )
    
    @QtCore.pyqtSlot()        
    def on_z_origin_changed(self):
        
        # Check if called by SpinBox or SeekBar
        if self.sender().__class__ == QtWidgets.QDoubleSpinBox:
            value = self.screw_frame_spinb_z_origin.value()
            # Disable SeekBar signal before editing it or this method will be called again
            self.screw_frame_sb_z_origin.blockSignals( True )
            self.screw_frame_sb_z_origin.setValue( value )
            self.screw_frame_sb_z_origin.blockSignals( False )
        else:
            value = self.screw_frame_sb_z_origin.value()
            value *= self.axe_scale
            
            self.screw_frame_spinb_z_origin.blockSignals( True )
            self.screw_frame_spinb_z_origin.setValue( value )
            self.screw_frame_spinb_z_origin.blockSignals( False )
        
        if self.matplot_frame != None:
            self.matplot_frame.origin[2] = value
            self.matplot_frame.draw( self )
    
    @QtCore.pyqtSlot()
    def on_w_x_trans_changed(self):
        if self.sender().__class__ == QtWidgets.QDoubleSpinBox:
            value = self.screw_spinb_w_x_trans.value()
            # Disable SeekBar signal before editing it or this method will be called again
            self.screw_sb_w_x_trans.blockSignals( True )
            self.screw_sb_w_x_trans.setValue( value )
            self.screw_sb_w_x_trans.blockSignals( False )
        else:
            value = self.screw_sb_w_x_trans.value()
            value *= self.axe_scale
            
            self.screw_spinb_w_x_trans.blockSignals( True )
            self.screw_spinb_w_x_trans.setValue( value )
            self.screw_spinb_w_x_trans.blockSignals( False )
        
        if self.matplot_frame != None:
            self.matplot_frame.w[0] = value
            self.matplot_frame.draw( self )

    @QtCore.pyqtSlot()            
    def on_w_y_trans_changed(self):
        if self.sender().__class__ == QtWidgets.QDoubleSpinBox:
            value = self.screw_spinb_w_y_trans.value()
            # Disable SeekBar signal before editing it or this method will be called again
            self.screw_sb_w_y_trans.blockSignals( True )
            self.screw_sb_w_y_trans.setValue( value )
            self.screw_sb_w_y_trans.blockSignals( False )
        else:
            value = self.screw_sb_w_y_trans.value()
            value *= self.axe_scale
            
            self.screw_spinb_w_y_trans.blockSignals( True )
            self.screw_spinb_w_y_trans.setValue( value )
            self.screw_spinb_w_y_trans.blockSignals( False )
        
        if self.matplot_frame != None:
            self.matplot_frame.w[1] = value
            self.matplot_frame.draw( self )
       
    @QtCore.pyqtSlot()     
    def on_w_z_trans_changed(self):
        if self.sender().__class__ == QtWidgets.QDoubleSpinBox:
            value = self.screw_spinb_w_z_trans.value()
            # Disable SeekBar signal before editing it or this method will be called again
            self.screw_sb_w_z_trans.blockSignals( True )
            self.screw_sb_w_z_trans.setValue( value )
            self.screw_sb_w_z_trans.blockSignals( False )
        else:
            value = self.screw_sb_w_z_trans.value()
            value *= self.axe_scale
            
            self.screw_spinb_w_z_trans.blockSignals( True )
            self.screw_spinb_w_z_trans.setValue( value )
            self.screw_spinb_w_z_trans.blockSignals( False )
        
        if self.matplot_frame != None:
            self.matplot_frame.w[2] = value
            self.matplot_frame.draw( self )
    
    @QtCore.pyqtSlot()
    def on_theta_angle_changed(self):
        if self.sender().__class__ == QtWidgets.QDoubleSpinBox:
            value = self.screw_spinb_w_theta_angle.value()
            # Disable SeekBar signal before editing it or this method will be called again
            self.screw_sb_w_theta_angle.blockSignals( True )
            self.screw_sb_w_theta_angle.setValue( value )
            self.screw_sb_w_theta_angle.blockSignals( False )
        else:
            value = self.screw_sb_w_theta_angle.value()
            
            self.screw_spinb_w_theta_angle.blockSignals( True )
            self.screw_spinb_w_theta_angle.setValue( value )
            self.screw_spinb_w_theta_angle.blockSignals( False )
        
        if self.matplot_frame != None:
            self.matplot_frame.theta = value
            self.matplot_frame.draw( self )


class Frame_Screw( Frames_Template ):
    
    def __init__(self, parent):
        '''
        Constructor
        '''
        super().__init__( parent)
        
        self.init_widgets()
        
        
        self.retranslateUi()
        
        # Seekbar signals
        #self.screw_sb_x_origin.valueChanged.connect(self.on_x_origin_changed)
        #self.screw_sb_y_origin.valueChanged.connect(self.on_y_origin_changed)
        #self.screw_sb_z_origin.valueChanged.connect(self.on_z_origin_changed)
        
        self.screw_sb_x_end.valueChanged.connect(self.on_x_end_changed)
        self.screw_sb_y_end.valueChanged.connect(self.on_y_end_changed)
        self.screw_sb_z_end.valueChanged.connect(self.on_z_end_changed)
        
        self.screw_sb_theta.valueChanged.connect(self.on_theta_changed)
        self.screw_sb_q.valueChanged.connect(self.on_q_changed)
        self.screw_sb_h.valueChanged.connect(self.on_pitch_changed)
        
        # DoubleSpinBox signals
            # Frame Origin
        self.screw_frame_spinb_x_origin.valueChanged.connect(self.on_x_origin_changed)
        self.screw_frame_spinb_y_origin.valueChanged.connect(self.on_y_origin_changed)
        self.screw_frame_spinb_z_origin.valueChanged.connect(self.on_z_origin_changed)
            
            # S axis start coordinates
        self.screw_spinb_x_origin.valueChanged.connect(self.on_s_x_origin_changed)
        self.screw_spinb_y_origin.valueChanged.connect(self.on_s_y_origin_changed)
        self.screw_spinb_z_origin.valueChanged.connect(self.on_s_z_origin_changed)
            
            # S axis end coordinates
        self.screw_spinb_x_end.valueChanged.connect(self.on_x_end_changed)
        self.screw_spinb_y_end.valueChanged.connect(self.on_y_end_changed)
        self.screw_spinb_z_end.valueChanged.connect(self.on_z_end_changed)
        
            # Screw axis parameters
        self.screw_spinb_theta.valueChanged.connect(self.on_theta_changed)
        self.screw_spinb_q.valueChanged.connect(self.on_q_changed)
        self.screw_spinb_h.valueChanged.connect(self.on_pitch_changed)
        
            # Show/Hide Screw path
        self.cb_screw_show_path.stateChanged.connect(lambda:self.on_show_path(self.cb_screw_show_path))
        
        print('All widgets loaded')
        
        self.show()
    
    """ Create widgets"""
    def init_widgets(self):
        self.setGeometry(QtCore.QRect(800, 0, 221, 601))
        
        self.setStyleSheet("background-color: rgb(255, 255, 255)")
        
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        
        self.setPalette(palette)
        self.setAutoFillBackground(True)
        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.setFrameShadow(QtWidgets.QFrame.Raised)
        self.setObjectName("frm_screw_control")
        
        self.frame_lb_component_name = QtWidgets.QLabel(self)
        self.frame_lb_component_name.setGeometry(QtCore.QRect(10, 10, 201, 20))
        
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.frame_lb_component_name.setFont(font)
        self.frame_lb_component_name.setAlignment(QtCore.Qt.AlignCenter)
        self.frame_lb_component_name.setObjectName("frame_lb_component_name")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(30, 50, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(2, 90, 21, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(2, 120, 21, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(2, 150, 21, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self)
        self.label_8.setGeometry(QtCore.QRect(2, 380, 21, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.screw_sb_theta = QtWidgets.QSlider(self)
        self.screw_sb_theta.setGeometry(QtCore.QRect(22, 377, 121, 29))
        self.screw_sb_theta.setMinimum(0)
        self.screw_sb_theta.setMaximum(3590/4)
        self.screw_sb_theta.setOrientation(QtCore.Qt.Horizontal)
        self.screw_sb_theta.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.screw_sb_theta.setTickInterval(0)
        self.screw_sb_theta.setObjectName("screw_sb_theta")
        self.screw_lb_rotation_matrix = QtWidgets.QLabel(self)
        self.screw_lb_rotation_matrix.setGeometry(QtCore.QRect(30, 430, 190, 91))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.screw_lb_rotation_matrix.setFont(font)
        self.screw_lb_rotation_matrix.setTextFormat(QtCore.Qt.PlainText)
        self.screw_lb_rotation_matrix.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.screw_lb_rotation_matrix.setWordWrap(False)
        self.screw_lb_rotation_matrix.setObjectName("screw_lb_rotation_matrix")
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(5, 430, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_7.setWordWrap(False)
        self.label_7.setObjectName("label_7")
        self.screw_spinb_x_origin = QtWidgets.QDoubleSpinBox(self)
        self.screw_spinb_x_origin.setGeometry(QtCore.QRect(35, 90, 69, 26))
        self.screw_spinb_x_origin.setDecimals(2)
        self.screw_spinb_x_origin.setMinimum(-10.0)
        self.screw_spinb_x_origin.setMaximum(10.0)
        self.screw_spinb_x_origin.setSingleStep(0.5)
        self.screw_spinb_x_origin.setProperty("value", 0.0)
        self.screw_spinb_x_origin.setObjectName("screw_spinb_x_origin")
        self.screw_spinb_y_origin = QtWidgets.QDoubleSpinBox(self)
        self.screw_spinb_y_origin.setGeometry(QtCore.QRect(35, 120, 69, 26))
        self.screw_spinb_y_origin.setDecimals(2)
        self.screw_spinb_y_origin.setMinimum(-10.0)
        self.screw_spinb_y_origin.setMaximum(10.0)
        self.screw_spinb_y_origin.setSingleStep(0.5)
        self.screw_spinb_y_origin.setProperty("value", 0.0)
        self.screw_spinb_y_origin.setObjectName("screw_spinb_y_origin")
        self.screw_spinb_z_origin = QtWidgets.QDoubleSpinBox(self)
        self.screw_spinb_z_origin.setGeometry(QtCore.QRect(35, 150, 69, 26))
        self.screw_spinb_z_origin.setDecimals(2)
        self.screw_spinb_z_origin.setMinimum(-10.0)
        self.screw_spinb_z_origin.setMaximum(10.0)
        self.screw_spinb_z_origin.setSingleStep(0.5)
        self.screw_spinb_z_origin.setProperty("value", 0.0)
        self.screw_spinb_z_origin.setObjectName("screw_spinb_z_origin")
        self.screw_spinb_theta = QtWidgets.QDoubleSpinBox(self)
        self.screw_spinb_theta.setGeometry(QtCore.QRect(148, 380, 69, 26))
        self.screw_spinb_theta.setDecimals(2)
        self.screw_spinb_theta.setMinimum(0.0)
        self.screw_spinb_theta.setMaximum(3590/4)
        self.screw_spinb_theta.setSingleStep(50)
        self.screw_spinb_theta.setProperty("value", 0.0)
        self.screw_spinb_theta.setObjectName("screw_spinb_theta")
        self.screw_lb_skew_matrix = QtWidgets.QLabel(self)
        self.screw_lb_skew_matrix.setGeometry(QtCore.QRect(30, 520, 190, 91))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.screw_lb_skew_matrix.setFont(font)
        self.screw_lb_skew_matrix.setTextFormat(QtCore.Qt.PlainText)
        self.screw_lb_skew_matrix.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.screw_lb_skew_matrix.setWordWrap(False)
        self.screw_lb_skew_matrix.setObjectName("screw_lb_skew_matrix")
        self.label_9 = QtWidgets.QLabel(self)
        self.label_9.setGeometry(QtCore.QRect(5, 520, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_9.setWordWrap(False)
        self.label_9.setObjectName("label_9")
        self.screw_sb_y_end = QtWidgets.QSlider(self)
        self.screw_sb_y_end.setGeometry(QtCore.QRect(22, 250, 121, 29))
        self.screw_sb_y_end.setMinimum(-10)
        self.screw_sb_y_end.setMaximum(10)
        self.screw_sb_y_end.setOrientation(QtCore.Qt.Horizontal)
        self.screw_sb_y_end.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.screw_sb_y_end.setTickInterval(0)
        self.screw_sb_y_end.setObjectName("screw_sb_y_end")
        self.label_10 = QtWidgets.QLabel(self)
        self.label_10.setGeometry(QtCore.QRect(2, 220, 21, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self)
        self.label_11.setGeometry(QtCore.QRect(18, 190, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.screw_spinb_z_end = QtWidgets.QDoubleSpinBox(self)
        self.screw_spinb_z_end.setGeometry(QtCore.QRect(147, 280, 69, 26))
        self.screw_spinb_z_end.setDecimals(2)
        self.screw_spinb_z_end.setMinimum(-10.0)
        self.screw_spinb_z_end.setMaximum(10.0)
        self.screw_spinb_z_end.setSingleStep(0.5)
        self.screw_spinb_z_end.setProperty("value", 0.0)
        self.screw_spinb_z_end.setObjectName("screw_spinb_z_end")
        self.screw_spinb_x_end = QtWidgets.QDoubleSpinBox(self)
        self.screw_spinb_x_end.setGeometry(QtCore.QRect(147, 220, 69, 26))
        self.screw_spinb_x_end.setDecimals(2)
        self.screw_spinb_x_end.setMinimum(-10.0)
        self.screw_spinb_x_end.setMaximum(10.0)
        self.screw_spinb_x_end.setSingleStep(0.5)
        self.screw_spinb_x_end.setProperty("value", 0.0)
        self.screw_spinb_x_end.setObjectName("screw_spinb_x_end")
        self.label_12 = QtWidgets.QLabel(self)
        self.label_12.setGeometry(QtCore.QRect(2, 250, 21, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.screw_sb_z_end = QtWidgets.QSlider(self)
        self.screw_sb_z_end.setGeometry(QtCore.QRect(22, 280, 121, 29))
        self.screw_sb_z_end.setMinimum(-10)
        self.screw_sb_z_end.setMaximum(10)
        self.screw_sb_z_end.setOrientation(QtCore.Qt.Horizontal)
        self.screw_sb_z_end.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.screw_sb_z_end.setTickInterval(0)
        self.screw_sb_z_end.setObjectName("screw_sb_z_end")
        self.screw_spinb_y_end = QtWidgets.QDoubleSpinBox(self)
        self.screw_spinb_y_end.setGeometry(QtCore.QRect(147, 250, 69, 26))
        self.screw_spinb_y_end.setDecimals(2)
        self.screw_spinb_y_end.setMinimum(-10.0)
        self.screw_spinb_y_end.setMaximum(10.0)
        self.screw_spinb_y_end.setSingleStep(0.5)
        self.screw_spinb_y_end.setProperty("value", 0.0)
        self.screw_spinb_y_end.setObjectName("screw_spinb_y_end")
        self.label_13 = QtWidgets.QLabel(self)
        self.label_13.setGeometry(QtCore.QRect(2, 280, 21, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.screw_sb_x_end = QtWidgets.QSlider(self)
        self.screw_sb_x_end.setGeometry(QtCore.QRect(22, 220, 121, 29))
        self.screw_sb_x_end.setMinimum(-10)
        self.screw_sb_x_end.setMaximum(10)
        self.screw_sb_x_end.setOrientation(QtCore.Qt.Horizontal)
        self.screw_sb_x_end.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.screw_sb_x_end.setTickInterval(0)
        self.screw_sb_x_end.setObjectName("screw_sb_x_end")
        self.label_14 = QtWidgets.QLabel(self)
        self.label_14.setGeometry(QtCore.QRect(2, 350, 21, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.screw_sb_h = QtWidgets.QSlider(self)
        self.screw_sb_h.setGeometry(QtCore.QRect(22, 347, 121, 29))
        self.screw_sb_h.setMinimum(0)
        self.screw_sb_h.setMaximum(5)
        self.screw_sb_h.setOrientation(QtCore.Qt.Horizontal)
        self.screw_sb_h.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.screw_sb_h.setTickInterval(0)
        self.screw_sb_h.setObjectName("screw_sb_h")
        self.screw_spinb_h = QtWidgets.QDoubleSpinBox(self)
        self.screw_spinb_h.setGeometry(QtCore.QRect(148, 350, 69, 26))
        self.screw_spinb_h.setDecimals(2)
        self.screw_spinb_h.setMinimum(0.0)
        self.screw_spinb_h.setMaximum(5.0)
        self.screw_spinb_h.setSingleStep(0.025)
        self.screw_spinb_h.setProperty("value", 0.0)
        self.screw_spinb_h.setObjectName("screw_spinb_h")
        self.screw_spinb_q = QtWidgets.QDoubleSpinBox(self)
        self.screw_spinb_q.setGeometry(QtCore.QRect(148, 323, 69, 26))
        self.screw_spinb_q.setDecimals(2)
        self.screw_spinb_q.setMinimum(0.0)
        self.screw_spinb_q.setMaximum(100.0)
        self.screw_spinb_q.setSingleStep(0.5)
        self.screw_spinb_q.setProperty("value", 0.0)
        self.screw_spinb_q.setObjectName("screw_spinb_q")
        self.label_27 = QtWidgets.QLabel(self)
        self.label_27.setGeometry(QtCore.QRect(2, 323, 21, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.screw_sb_q = QtWidgets.QSlider(self)
        self.screw_sb_q.setGeometry(QtCore.QRect(22, 320, 121, 29))
        self.screw_sb_q.setMinimum(0)
        self.screw_sb_q.setMaximum(100)
        self.screw_sb_q.setOrientation(QtCore.Qt.Horizontal)
        self.screw_sb_q.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.screw_sb_q.setTickInterval(0)
        self.screw_sb_q.setObjectName("screw_sb_q")
        self.label_28 = QtWidgets.QLabel(self)
        self.label_28.setGeometry(QtCore.QRect(110, 50, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.screw_frame_spinb_z_origin = QtWidgets.QDoubleSpinBox(self)
        self.screw_frame_spinb_z_origin.setGeometry(QtCore.QRect(130, 150, 69, 26))
        self.screw_frame_spinb_z_origin.setDecimals(2)
        self.screw_frame_spinb_z_origin.setMinimum(-10.0)
        self.screw_frame_spinb_z_origin.setMaximum(10.0)
        self.screw_frame_spinb_z_origin.setSingleStep(0.5)
        self.screw_frame_spinb_z_origin.setProperty("value", 0.0)
        self.screw_frame_spinb_z_origin.setObjectName("screw_frame_spinb_z_origin")
        self.screw_frame_spinb_y_origin = QtWidgets.QDoubleSpinBox(self)
        self.screw_frame_spinb_y_origin.setGeometry(QtCore.QRect(130, 120, 69, 26))
        self.screw_frame_spinb_y_origin.setDecimals(2)
        self.screw_frame_spinb_y_origin.setMinimum(-10.0)
        self.screw_frame_spinb_y_origin.setMaximum(10.0)
        self.screw_frame_spinb_y_origin.setSingleStep(0.5)
        self.screw_frame_spinb_y_origin.setProperty("value", 0.0)
        self.screw_frame_spinb_y_origin.setObjectName("screw_frame_spinb_y_origin")
        self.screw_frame_spinb_x_origin = QtWidgets.QDoubleSpinBox(self)
        self.screw_frame_spinb_x_origin.setGeometry(QtCore.QRect(130, 90, 69, 26))
        self.screw_frame_spinb_x_origin.setDecimals(2)
        self.screw_frame_spinb_x_origin.setMinimum(-10.0)
        self.screw_frame_spinb_x_origin.setMaximum(10.0)
        self.screw_frame_spinb_x_origin.setSingleStep(0.5)
        self.screw_frame_spinb_x_origin.setProperty("value", 0.0)
        self.screw_frame_spinb_x_origin.setObjectName("screw_frame_spinb_x_origin")
        
        self.cb_screw_show_path = QtWidgets.QCheckBox(self)
        self.cb_screw_show_path.setGeometry(QtCore.QRect(100, 190, 96, 23))
        self.cb_screw_show_path.setObjectName("cb_screw_show_path")
        
        self.frame_lb_component_name.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_8.raise_()
        self.screw_sb_theta.raise_()
        self.screw_lb_rotation_matrix.raise_()
        self.label_7.raise_()
        self.screw_spinb_x_origin.raise_()
        self.screw_spinb_y_origin.raise_()
        self.screw_spinb_z_origin.raise_()
        self.screw_spinb_theta.raise_()
        self.screw_lb_skew_matrix.raise_()
        self.label_9.raise_()
        self.screw_sb_y_end.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.screw_spinb_z_end.raise_()
        self.screw_spinb_x_end.raise_()
        self.label_12.raise_()
        self.screw_sb_z_end.raise_()
        self.screw_spinb_y_end.raise_()
        self.label_13.raise_()
        self.screw_sb_x_end.raise_()
        self.label_14.raise_()
        self.screw_sb_h.raise_()
        self.screw_spinb_h.raise_()
        self.screw_spinb_q.raise_()
        self.label_27.raise_()
        self.screw_sb_q.raise_()
        self.screw_frame_spinb_x_origin.raise_()
        self.screw_frame_spinb_x_origin.raise_()
        self.screw_frame_spinb_z_origin.raise_()
        self.screw_frame_spinb_y_origin.raise_()
        self.screw_frame_spinb_x_origin.raise_()
        self.label_28.raise_()
        self.screw_frame_spinb_z_origin.raise_()
        self.screw_frame_spinb_y_origin.raise_()
        self.screw_frame_spinb_x_origin.raise_()
        self.cb_screw_show_path.raise_()
        
           
    """Label widgets texts"""    
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        
        self.frame_lb_component_name.setText(_translate("MainWindow", "Component Name"))
        self.label_3.setText(_translate("MainWindow", "S Origin"))
        self.label_4.setText(_translate("MainWindow", "X:"))
        self.label_5.setText(_translate("MainWindow", "Y:"))
        self.label_6.setText(_translate("MainWindow", "Z:"))
        self.label_8.setText(_translate("MainWindow", "θ"))
        self.screw_lb_rotation_matrix.setText(_translate("MainWindow", "[[0.00 -0.50 0.33]\n"
"[0.50 0.00 -0.17]\n"
"[-0.33 0.17 0.00]]"))
        self.label_7.setText(_translate("MainWindow", "T:"))
        self.screw_lb_skew_matrix.setText(_translate("MainWindow", "[[0.00 -0.50 0.33]\n"
"[0.50 0.00 -0.17]\n"
"[-0.33 0.17 0.00]]"))
        self.label_9.setText(_translate("MainWindow", "[S]:"))
        self.label_10.setText(_translate("MainWindow", "X:"))
        self.label_11.setText(_translate("MainWindow", "S End"))
        self.label_12.setText(_translate("MainWindow", "Y:"))
        self.label_13.setText(_translate("MainWindow", "Z:"))
        self.label_14.setText(_translate("MainWindow", "h"))
        self.label_27.setText(_translate("MainWindow", "q"))
        self.label_28.setText(_translate("MainWindow", "Frame Origin"))
        self.cb_screw_show_path.setText(_translate("MainWindow", "Show path"))
        
        
    def set_label(self, label_name):
        label = self.get_label()
        self.frame_lb_component_name.setText( label_name + str(label) )
        return label
    
    """ Get a label number """
    def get_label(self):
        self.label = Frames_Template.labels_screws.pop(0)
        return self.label
    
    """ Destroy/Clean object and release its label"""
    def destroy(self, *args, **kwargs):
        Frames_Template.destroy(self, *args, **kwargs)
        Frames_Template.labels_screws.append( self.label )
     
    def set_component_frame(self, frame_component):
        self.matplot_frame = frame_component
        
    def on_show_path(self, checkbox):
        state = checkbox.isChecked()
        
        self.matplot_frame.bl_show_path = state
        self.matplot_frame.path_max_theta = self.screw_sb_theta.maximum()
        
        self.matplot_frame.show_path()
        
        print(state)
    
    @QtCore.pyqtSlot()
    def on_x_origin_changed(self):
            
        value = self.screw_frame_spinb_x_origin.value()
        # Disable SeekBar signal before editing it or this method will be called again
        
        if self.matplot_frame != None:
            self.matplot_frame.origin[0] = value
            self.matplot_frame.draw( self )
    
    @QtCore.pyqtSlot()            
    def on_y_origin_changed(self):
        
        value = self.screw_frame_spinb_y_origin.value()
        
        if self.matplot_frame != None:
            self.matplot_frame.origin[1] = value
            self.matplot_frame.draw( self )
    
    @QtCore.pyqtSlot()        
    def on_z_origin_changed(self):
        
        value = self.screw_frame_spinb_z_origin.value()
        
        if self.matplot_frame != None:
            self.matplot_frame.origin[2] = value
            self.matplot_frame.draw( self )
    
    
    @QtCore.pyqtSlot()        
    def on_s_x_origin_changed(self):
        
        value = self.screw_spinb_x_origin.value()
        
        if self.matplot_frame != None:
            self.matplot_frame.s[0] = value
            self.matplot_frame.draw( self )
    
    @QtCore.pyqtSlot()        
    def on_s_y_origin_changed(self):
        
        value = self.screw_spinb_y_origin.value()
        
        if self.matplot_frame != None:
            self.matplot_frame.s[1] = value
            self.matplot_frame.draw( self )
    
    @QtCore.pyqtSlot()        
    def on_s_z_origin_changed(self):
        
        value = self.screw_spinb_z_origin.value()
        
        if self.matplot_frame != None:
            self.matplot_frame.s[2] = value
            self.matplot_frame.draw( self )
    
    @QtCore.pyqtSlot()
    def on_x_end_changed(self):
        
        #print(self.sender().__class__.__name__)
        # Check if called by SpinBox or SeekBar
        if self.sender().__class__ == QtWidgets.QDoubleSpinBox:
            value = self.screw_spinb_x_end.value()
            # Disable SeekBar signal before editing it or this method will be called again
            self.screw_sb_x_end.blockSignals( True )
            self.screw_sb_x_end.setValue( value )
            self.screw_sb_x_end.blockSignals( False )
        else:
            value = self.screw_sb_x_end.value()
            value *= self.axe_scale
            
            self.screw_spinb_x_end.blockSignals( True )
            self.screw_spinb_x_end.setValue( value )
            self.screw_spinb_x_end.blockSignals( False )
        
        if self.matplot_frame != None:
            self.matplot_frame.s_end[0] = value
            self.matplot_frame.draw( self )
    
    
    @QtCore.pyqtSlot()
    def on_y_end_changed(self):
        
        #print(self.sender().__class__.__name__)
        # Check if called by SpinBox or SeekBar
        if self.sender().__class__ == QtWidgets.QDoubleSpinBox:
            value = self.screw_spinb_y_end.value()
            # Disable SeekBar signal before editing it or this method will be called again
            self.screw_sb_y_end.blockSignals( True )
            self.screw_sb_y_end.setValue( value )
            self.screw_sb_y_end.blockSignals( False )
        else:
            value = self.screw_sb_y_end.value()
            value *= self.axe_scale
            
            self.screw_spinb_y_end.blockSignals( True )
            self.screw_spinb_y_end.setValue( value )
            self.screw_spinb_y_end.blockSignals( False )
        
        if self.matplot_frame != None:
            self.matplot_frame.s_end[1] = value
            self.matplot_frame.draw( self )
    
    @QtCore.pyqtSlot()
    def on_z_end_changed(self):
        
        #print(self.sender().__class__.__name__)
        # Check if called by SpinBox or SeekBar
        if self.sender().__class__ == QtWidgets.QDoubleSpinBox:
            value = self.screw_spinb_z_end.value()
            # Disable SeekBar signal before editing it or this method will be called again
            self.screw_sb_z_end.blockSignals( True )
            self.screw_sb_z_end.setValue( value )
            self.screw_sb_z_end.blockSignals( False )
        else:
            value = self.screw_sb_z_end.value()
            value *= self.axe_scale
            
            self.screw_spinb_z_end.blockSignals( True )
            self.screw_spinb_z_end.setValue( value )
            self.screw_spinb_z_end.blockSignals( False )
        
        if self.matplot_frame != None:
            self.matplot_frame.s_end[2] = value
            self.matplot_frame.draw( self )
    
    
    @QtCore.pyqtSlot()
    def on_theta_changed(self):
        if self.sender().__class__ == QtWidgets.QDoubleSpinBox:
            value = self.screw_spinb_theta.value()
            # Disable SeekBar signal before editing it or this method will be called again
            self.screw_sb_theta.blockSignals( True )
            self.screw_sb_theta.setValue( value )
            self.screw_sb_theta.blockSignals( False )
        else:
            value = self.screw_sb_theta.value()
            
            self.screw_spinb_theta.blockSignals( True )
            self.screw_spinb_theta.setValue( value )
            self.screw_spinb_theta.blockSignals( False )
        
        if self.matplot_frame != None:
            self.matplot_frame.theta = value
            self.matplot_frame.draw( self )
    
    @QtCore.pyqtSlot()
    def on_pitch_changed(self):
        if self.sender().__class__ == QtWidgets.QDoubleSpinBox:
            value = self.screw_spinb_h.value()
            # Disable SeekBar signal before editing it or this method will be called again
            self.screw_sb_h.blockSignals( True )
            self.screw_sb_h.setValue( value )
            self.screw_sb_h.blockSignals( False )
        else:
            value = self.screw_sb_h.value()
            
            self.screw_spinb_h.blockSignals( True )
            self.screw_spinb_h.setValue( value )
            self.screw_spinb_h.blockSignals( False )
        
        if self.matplot_frame != None:
            self.matplot_frame.update_h(value)
            self.matplot_frame.draw( self )
            
    @QtCore.pyqtSlot()
    def on_q_changed(self):
        if self.sender().__class__ == QtWidgets.QDoubleSpinBox:
            value = self.screw_spinb_q.value()
            # Disable SeekBar signal before editing it or this method will be called again
            self.screw_sb_q.blockSignals( True )
            self.screw_sb_q.setValue( value )
            self.screw_sb_q.blockSignals( False )
        else:
            value = self.screw_sb_q.value()
            
            self.screw_spinb_q.blockSignals( True )
            self.screw_spinb_q.setValue( value )
            self.screw_spinb_q.blockSignals( False )
        
        if self.matplot_frame != None:
            self.matplot_frame.update_q(value) 
            self.matplot_frame.draw( self )

class Frame_Robot_Arm( Frames_Template ):
    
    def __init__(self, parent):
        '''
        Constructor
        '''
        super().__init__( parent)
        
        self.init_widgets()
        
        
        self.retranslateUi()
        
        # Seekbar signals
        #self.screw_sb_x_origin.valueChanged.connect(self.on_x_origin_changed)
        #self.screw_sb_y_origin.valueChanged.connect(self.on_y_origin_changed)
        #self.screw_sb_z_origin.valueChanged.connect(self.on_z_origin_changed)
        
        self.show()
    
    """ Create widgets"""
    def init_widgets(self):
        self.setGeometry(QtCore.QRect(800, 0, 221, 681))
        
        self.setStyleSheet("background-color: rgb(255, 255, 255)")
        
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        
        self.setPalette(palette)
        self.setAutoFillBackground(True)
        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.setFrameShadow(QtWidgets.QFrame.Raised)
        self.setObjectName("frm_robot_arm_control")
        
        self.frame_lb_component_name = QtWidgets.QLabel(self)
        self.frame_lb_component_name.setGeometry(QtCore.QRect(10, 10, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.frame_lb_component_name.setFont(font)
        self.frame_lb_component_name.setAlignment(QtCore.Qt.AlignCenter)
        self.frame_lb_component_name.setObjectName("frame_lb_component_name")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(2, 130, 23, 26))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(2, 160, 23, 26))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(2, 190, 23, 26))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_15 = QtWidgets.QLabel(self)
        self.label_15.setGeometry(QtCore.QRect(0, 310, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_23 = QtWidgets.QLabel(self)
        self.label_23.setGeometry(QtCore.QRect(2, 345, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self)
        self.label_24.setGeometry(QtCore.QRect(2, 380, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self)
        self.label_25.setGeometry(QtCore.QRect(2, 410, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.robot_spinb_x_origin = QtWidgets.QDoubleSpinBox(self)
        self.robot_spinb_x_origin.setGeometry(QtCore.QRect(25, 130, 69, 26))
        self.robot_spinb_x_origin.setDecimals(2)
        self.robot_spinb_x_origin.setMinimum(-10.0)
        self.robot_spinb_x_origin.setMaximum(10.0)
        self.robot_spinb_x_origin.setSingleStep(0.5)
        self.robot_spinb_x_origin.setProperty("value", 0.0)
        self.robot_spinb_x_origin.setObjectName("robot_spinb_x_origin")
        self.robot_spinb_z_origin = QtWidgets.QDoubleSpinBox(self)
        self.robot_spinb_z_origin.setGeometry(QtCore.QRect(25, 190, 69, 26))
        self.robot_spinb_z_origin.setDecimals(2)
        self.robot_spinb_z_origin.setMinimum(-10.0)
        self.robot_spinb_z_origin.setMaximum(10.0)
        self.robot_spinb_z_origin.setSingleStep(0.5)
        self.robot_spinb_z_origin.setProperty("value", 0.0)
        self.robot_spinb_z_origin.setObjectName("robot_spinb_z_origin")
        self.robot_spinb_y_origin = QtWidgets.QDoubleSpinBox(self)
        self.robot_spinb_y_origin.setGeometry(QtCore.QRect(25, 160, 69, 26))
        self.robot_spinb_y_origin.setDecimals(2)
        self.robot_spinb_y_origin.setMinimum(-10.0)
        self.robot_spinb_y_origin.setMaximum(10.0)
        self.robot_spinb_y_origin.setSingleStep(0.5)
        self.robot_spinb_y_origin.setProperty("value", 0.0)
        self.robot_spinb_y_origin.setObjectName("robot_spinb_y_origin")
        self.robot_spinb_link_frame_x_angle = QtWidgets.QDoubleSpinBox(self)
        self.robot_spinb_link_frame_x_angle.setGeometry(QtCore.QRect(30, 345, 69, 26))
        self.robot_spinb_link_frame_x_angle.setDecimals(2)
        self.robot_spinb_link_frame_x_angle.setMinimum(-10.0)
        self.robot_spinb_link_frame_x_angle.setMaximum(10.0)
        self.robot_spinb_link_frame_x_angle.setSingleStep(0.5)
        self.robot_spinb_link_frame_x_angle.setProperty("value", 0.0)
        self.robot_spinb_link_frame_x_angle.setObjectName("robot_spinb_link_frame_x_angle")
        self.robot_spinb_link_frame_y_angle = QtWidgets.QDoubleSpinBox(self)
        self.robot_spinb_link_frame_y_angle.setGeometry(QtCore.QRect(30, 380, 69, 26))
        self.robot_spinb_link_frame_y_angle.setDecimals(2)
        self.robot_spinb_link_frame_y_angle.setMinimum(-10.0)
        self.robot_spinb_link_frame_y_angle.setMaximum(10.0)
        self.robot_spinb_link_frame_y_angle.setSingleStep(0.5)
        self.robot_spinb_link_frame_y_angle.setProperty("value", 0.0)
        self.robot_spinb_link_frame_y_angle.setObjectName("robot_spinb_link_frame_y_angle")
        self.robot_spinb_link_frame_z_angle = QtWidgets.QDoubleSpinBox(self)
        self.robot_spinb_link_frame_z_angle.setGeometry(QtCore.QRect(30, 410, 69, 26))
        self.robot_spinb_link_frame_z_angle.setDecimals(2)
        self.robot_spinb_link_frame_z_angle.setMinimum(-10.0)
        self.robot_spinb_link_frame_z_angle.setMaximum(10.0)
        self.robot_spinb_link_frame_z_angle.setSingleStep(0.5)
        self.robot_spinb_link_frame_z_angle.setProperty("value", 0.0)
        self.robot_spinb_link_frame_z_angle.setObjectName("robot_spinb_link_frame_z_angle")
        self.robot_lb_m_matrix = QtWidgets.QLabel(self)
        self.robot_lb_m_matrix.setGeometry(QtCore.QRect(30, 450, 190, 91))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.robot_lb_m_matrix.setFont(font)
        self.robot_lb_m_matrix.setTextFormat(QtCore.Qt.PlainText)
        self.robot_lb_m_matrix.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.robot_lb_m_matrix.setWordWrap(False)
        self.robot_lb_m_matrix.setObjectName("robot_lb_m_matrix")
        self.label_11 = QtWidgets.QLabel(self)
        self.label_11.setGeometry(QtCore.QRect(5, 450, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_11.setWordWrap(False)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self)
        self.label_12.setGeometry(QtCore.QRect(3, 50, 51, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.robot_spinb_links_count = QtWidgets.QSpinBox(self)
        self.robot_spinb_links_count.setGeometry(QtCore.QRect(53, 50, 48, 26))
        self.robot_spinb_links_count.setMinimum(1)
        self.robot_spinb_links_count.setMaximum(10)
        self.robot_spinb_links_count.setDisplayIntegerBase(10)
        self.robot_spinb_links_count.setObjectName("robot_spinb_links_count")
        self.robot_cb_link = QtWidgets.QComboBox(self)
        self.robot_cb_link.setGeometry(QtCore.QRect(110, 50, 86, 25))
        self.robot_cb_link.setObjectName("robot_cb_link")
        self.robot_cb_link.addItem("")
        self.robot_cb_link.addItem("")
        self.robot_cb_link.setItemText(1, "")
        self.robot_cb_reference_frame = QtWidgets.QComboBox(self)
        self.robot_cb_reference_frame.setGeometry(QtCore.QRect(110, 130, 105, 25))
        self.robot_cb_reference_frame.setObjectName("robot_cb_reference_frame")
        self.robot_cb_reference_frame.addItem("")
        self.robot_cb_reference_frame.addItem("")
        self.robot_spinb_parallel_axis = QtWidgets.QComboBox(self)
        self.robot_spinb_parallel_axis.setGeometry(QtCore.QRect(100, 260, 105, 25))
        self.robot_spinb_parallel_axis.setObjectName("robot_spinb_parallel_axis")
        self.robot_spinb_parallel_axis.addItem("")
        self.robot_spinb_parallel_axis.addItem("")
        self.robot_spinb_parallel_axis.addItem("")
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(0, 230, 41, 26))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.robot_spinb_link_length = QtWidgets.QDoubleSpinBox(self)
        self.robot_spinb_link_length.setGeometry(QtCore.QRect(50, 230, 69, 26))
        self.robot_spinb_link_length.setMinimum(0.01)
        self.robot_spinb_link_length.setMaximum(10.0)
        self.robot_spinb_link_length.setSingleStep(0.5)
        self.robot_spinb_link_length.setProperty("value", 1.0)
        self.robot_spinb_link_length.setObjectName("robot_spinb_link_length")
        self.robot_cb_joint_type = QtWidgets.QComboBox(self)
        self.robot_cb_joint_type.setGeometry(QtCore.QRect(110, 160, 105, 25))
        self.robot_cb_joint_type.setObjectName("robot_cb_joint_type")
        self.robot_cb_joint_type.addItem("")
        self.robot_cb_joint_type.addItem("")
        self.label_8 = QtWidgets.QLabel(self)
        self.label_8.setGeometry(QtCore.QRect(0, 260, 101, 26))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.robot_pb_compute_m = QtWidgets.QPushButton(self)
        self.robot_pb_compute_m.setGeometry(QtCore.QRect(110, 410, 89, 26))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(148, 134, 131))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(148, 134, 131))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(148, 134, 131))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.robot_pb_compute_m.setPalette(palette)
        self.robot_pb_compute_m.setObjectName("robot_pb_compute_m")
        self.label_13 = QtWidgets.QLabel(self)
        self.label_13.setGeometry(QtCore.QRect(5, 560, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_13.setWordWrap(False)
        self.label_13.setObjectName("label_13")
        self.robot_lb_transformation_matrix = QtWidgets.QLabel(self)
        self.robot_lb_transformation_matrix.setGeometry(QtCore.QRect(30, 560, 190, 91))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.robot_lb_transformation_matrix.setFont(font)
        self.robot_lb_transformation_matrix.setTextFormat(QtCore.Qt.PlainText)
        self.robot_lb_transformation_matrix.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.robot_lb_transformation_matrix.setWordWrap(False)
        self.robot_lb_transformation_matrix.setObjectName("robot_lb_transformation_matrix")
        
           
    """Label widgets texts"""    
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        
        self.frame_lb_component_name.setText(_translate("MainWindow", "Component Name"))
        self.label_3.setText(_translate("MainWindow", "{0} Origin"))
        self.label_4.setText(_translate("MainWindow", "X:"))
        self.label_5.setText(_translate("MainWindow", "Y:"))
        self.label_6.setText(_translate("MainWindow", "Z:"))
        self.label_15.setText(_translate("MainWindow", "Link Frame Rotation Angles"))
        self.label_23.setText(_translate("MainWindow", "X:"))
        self.label_24.setText(_translate("MainWindow", "Y:"))
        self.label_25.setText(_translate("MainWindow", "Z:"))
        self.robot_lb_m_matrix.setText(_translate("MainWindow", "M:"))
        self.label_11.setText(_translate("MainWindow", "M:"))
        self.label_12.setText(_translate("MainWindow", "Links:"))
        self.robot_cb_link.setItemText(0, _translate("MainWindow", "Link 1"))
        self.robot_cb_reference_frame.setItemText(0, _translate("MainWindow", "S Frame"))
        self.robot_cb_reference_frame.setItemText(1, _translate("MainWindow", "B Frame"))
        self.robot_spinb_parallel_axis.setItemText(0, _translate("MainWindow", "X"))
        self.robot_spinb_parallel_axis.setItemText(1, _translate("MainWindow", "Y"))
        self.robot_spinb_parallel_axis.setItemText(2, _translate("MainWindow", "Z"))
        self.label_7.setText(_translate("MainWindow", "Size:"))
        self.robot_cb_joint_type.setItemText(0, _translate("MainWindow", "PRISMATIC"))
        self.robot_cb_joint_type.setItemText(1, _translate("MainWindow", "REVOLUTE"))
        self.label_8.setText(_translate("MainWindow", "Parallel to:"))
        self.robot_pb_compute_m.setText(_translate("MainWindow", "Compute M"))
        self.label_13.setText(_translate("MainWindow", "Tsb"))
        self.robot_lb_transformation_matrix.setText(_translate("MainWindow", "M:"))
        
        
    def set_label(self, label_name):
        self.frame_lb_component_name.setText( label_name)
        
    def set_component_frame(self, frame_component):
        self.matplot_frame = frame_component
        
    
    @QtCore.pyqtSlot()
    def on_theta_changed(self):
        
        value = self.screw_spinb_theta.value()
        # Disable SeekBar signal before editing it or this method will be called again
        
        if self.matplot_frame != None:
            self.matplot_frame.theta = value
            self.matplot_frame.draw( self )
    


class Frame_Transform( Frames_Template ):
    '''
    classdocs
    '''
    
    def __init__(self, parent):
        '''
        Constructor
        '''
        super().__init__( parent)
        
        # Create widgets
        self.init_widgets()
        # Label them
        self.retranslateUi()
        
        # Seekbar signals
        self.frame_sb_x_origin.valueChanged.connect(self.on_x_origin_changed)
        self.frame_sb_y_origin.valueChanged.connect(self.on_y_origin_changed)
        self.frame_sb_z_origin.valueChanged.connect(self.on_z_origin_changed)
        
        self.frame_sb_x_trans.valueChanged.connect(self.on_x_trans_changed)
        self.frame_sb_y_trans.valueChanged.connect(self.on_y_trans_changed)
        self.frame_sb_z_trans.valueChanged.connect(self.on_z_trans_changed)
        
        self.frame_sb_x_angle.valueChanged.connect(self.on_x_angle_changed)
        self.frame_sb_y_angle.valueChanged.connect(self.on_y_angle_changed)
        self.frame_sb_z_angle.valueChanged.connect(self.on_z_angle_changed)
        
        # DoubleSpinBox signals
        self.frame_spinb_x_origin.valueChanged.connect(self.on_x_origin_changed)
        self.frame_spinb_y_origin.valueChanged.connect(self.on_y_origin_changed)
        self.frame_spinb_z_origin.valueChanged.connect(self.on_z_origin_changed)
        
        self.frame_spinb_x_trans.valueChanged.connect(self.on_x_trans_changed)
        self.frame_spinb_y_trans.valueChanged.connect(self.on_y_trans_changed)
        self.frame_spinb_z_trans.valueChanged.connect(self.on_z_trans_changed)
        
        self.frame_spinb_x_angle.valueChanged.connect(self.on_x_angle_changed)
        self.frame_spinb_y_angle.valueChanged.connect(self.on_y_angle_changed)
        self.frame_spinb_z_angle.valueChanged.connect(self.on_z_angle_changed)
        
        
        self.show()
    
    def init_widgets(self):
        self.setGeometry(QtCore.QRect(800, 0, 221, 601))
        
        #self.frame.setStyleSheet("background-color: rgb(200, 255, 255)")
        self.setStyleSheet("background-color: rgb(255, 255, 255)")
        
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        
        self.setPalette(palette)
        self.setAutoFillBackground(True)
        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.setFrameShadow(QtWidgets.QFrame.Raised)
        self.setObjectName("frm_component_control")
        
        
        self.frame_sb_x_origin = QtWidgets.QSlider(self)
        self.frame_sb_x_origin.setGeometry(QtCore.QRect(22, 90, 121, 29))
        self.frame_sb_x_origin.setMinimum(-10)
        self.frame_sb_x_origin.setMaximum(10)
        self.frame_sb_x_origin.setOrientation(QtCore.Qt.Horizontal)
        self.frame_sb_x_origin.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.frame_sb_x_origin.setTickInterval(0)
        self.frame_sb_x_origin.setObjectName("frame_sb_x_origin")
        self.frame_lb_component_name = QtWidgets.QLabel(self)
        self.frame_lb_component_name.setGeometry(QtCore.QRect(10, 10, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.frame_lb_component_name.setFont(font)
        self.frame_lb_component_name.setAlignment(QtCore.Qt.AlignCenter)
        self.frame_lb_component_name.setObjectName("frame_lb_component_name")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(2, 90, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(2, 120, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.frame_sb_y_origin = QtWidgets.QSlider(self)
        self.frame_sb_y_origin.setGeometry(QtCore.QRect(22, 120, 121, 29))
        self.frame_sb_y_origin.setMinimum(-10)
        self.frame_sb_y_origin.setMaximum(10)
        self.frame_sb_y_origin.setOrientation(QtCore.Qt.Horizontal)
        self.frame_sb_y_origin.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.frame_sb_y_origin.setTickInterval(0)
        self.frame_sb_y_origin.setObjectName("frame_sb_y_origin")
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(2, 150, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.frame_sb_z_origin = QtWidgets.QSlider(self)
        self.frame_sb_z_origin.setGeometry(QtCore.QRect(22, 150, 121, 29))
        self.frame_sb_z_origin.setMinimum(-10)
        self.frame_sb_z_origin.setMaximum(10)
        self.frame_sb_z_origin.setOrientation(QtCore.Qt.Horizontal)
        self.frame_sb_z_origin.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.frame_sb_z_origin.setTickInterval(0)
        self.frame_sb_z_origin.setObjectName("frame_sb_z_origin")
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(20, 350, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self)
        self.label_8.setGeometry(QtCore.QRect(2, 385, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self)
        self.label_9.setGeometry(QtCore.QRect(2, 450, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self)
        self.label_10.setGeometry(QtCore.QRect(2, 418, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.frame_sb_y_angle = QtWidgets.QSlider(self)
        self.frame_sb_y_angle.setGeometry(QtCore.QRect(22, 418, 121, 29))
        self.frame_sb_y_angle.setMinimum(0)
        self.frame_sb_y_angle.setMaximum(359)
        self.frame_sb_y_angle.setOrientation(QtCore.Qt.Horizontal)
        self.frame_sb_y_angle.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.frame_sb_y_angle.setTickInterval(0)
        self.frame_sb_y_angle.setObjectName("frame_sb_y_angle")
        self.frame_sb_x_angle = QtWidgets.QSlider(self)
        self.frame_sb_x_angle.setGeometry(QtCore.QRect(22, 385, 121, 29))
        self.frame_sb_x_angle.setMinimum(0)
        self.frame_sb_x_angle.setMaximum(359)
        self.frame_sb_x_angle.setOrientation(QtCore.Qt.Horizontal)
        self.frame_sb_x_angle.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.frame_sb_x_angle.setTickInterval(0)
        self.frame_sb_x_angle.setObjectName("frame_sb_x_angle")
        self.frame_sb_z_angle = QtWidgets.QSlider(self)
        self.frame_sb_z_angle.setGeometry(QtCore.QRect(22, 450, 121, 29))
        self.frame_sb_z_angle.setMinimum(0)
        self.frame_sb_z_angle.setMaximum(359)
        self.frame_sb_z_angle.setOrientation(QtCore.Qt.Horizontal)
        self.frame_sb_z_angle.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.frame_sb_z_angle.setTickInterval(0)
        self.frame_sb_z_angle.setObjectName("frame_sb_z_angle")
        self.label_15 = QtWidgets.QLabel(self)
        self.label_15.setGeometry(QtCore.QRect(20, 200, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_23 = QtWidgets.QLabel(self)
        self.label_23.setGeometry(QtCore.QRect(2, 235, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.frame_sb_z_trans = QtWidgets.QSlider(self)
        self.frame_sb_z_trans.setGeometry(QtCore.QRect(22, 300, 121, 29))
        self.frame_sb_z_trans.setMinimum(-10)
        self.frame_sb_z_trans.setMaximum(10)
        self.frame_sb_z_trans.setOrientation(QtCore.Qt.Horizontal)
        self.frame_sb_z_trans.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.frame_sb_z_trans.setTickInterval(0)
        self.frame_sb_z_trans.setObjectName("frame_sb_z_trans")
        self.label_24 = QtWidgets.QLabel(self)
        self.label_24.setGeometry(QtCore.QRect(2, 270, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self)
        self.label_25.setGeometry(QtCore.QRect(2, 300, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.frame_sb_x_trans = QtWidgets.QSlider(self)
        self.frame_sb_x_trans.setGeometry(QtCore.QRect(22, 235, 121, 29))
        self.frame_sb_x_trans.setMinimum(-10)
        self.frame_sb_x_trans.setMaximum(10)
        self.frame_sb_x_trans.setOrientation(QtCore.Qt.Horizontal)
        self.frame_sb_x_trans.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.frame_sb_x_trans.setTickInterval(0)
        self.frame_sb_x_trans.setObjectName("frame_sb_x_trans")
        self.frame_sb_y_trans = QtWidgets.QSlider(self)
        self.frame_sb_y_trans.setGeometry(QtCore.QRect(22, 270, 121, 29))
        self.frame_sb_y_trans.setMinimum(-10)
        self.frame_sb_y_trans.setMaximum(10)
        self.frame_sb_y_trans.setOrientation(QtCore.Qt.Horizontal)
        self.frame_sb_y_trans.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.frame_sb_y_trans.setTickInterval(0)
        self.frame_sb_y_trans.setObjectName("frame_sb_y_trans")
        self.frame_spinb_x_origin = QtWidgets.QDoubleSpinBox(self)
        self.frame_spinb_x_origin.setGeometry(QtCore.QRect(147, 90, 69, 26))
        self.frame_spinb_x_origin.setDecimals(2)
        self.frame_spinb_x_origin.setMinimum(-10.0)
        self.frame_spinb_x_origin.setMaximum(10.0)
        self.frame_spinb_x_origin.setSingleStep(0.5)
        self.frame_spinb_x_origin.setProperty("value", 0.0)
        self.frame_spinb_x_origin.setObjectName("frame_spinb_x_origin")
        self.frame_spinb_z_origin = QtWidgets.QDoubleSpinBox(self)
        self.frame_spinb_z_origin.setGeometry(QtCore.QRect(147, 150, 69, 26))
        self.frame_spinb_z_origin.setDecimals(2)
        self.frame_spinb_z_origin.setMinimum(-10.0)
        self.frame_spinb_z_origin.setMaximum(10.0)
        self.frame_spinb_z_origin.setSingleStep(0.5)
        self.frame_spinb_z_origin.setProperty("value", 0.0)
        self.frame_spinb_z_origin.setObjectName("frame_spinb_z_origin")
        self.frame_spinb_y_origin = QtWidgets.QDoubleSpinBox(self)
        self.frame_spinb_y_origin.setGeometry(QtCore.QRect(147, 120, 69, 26))
        self.frame_spinb_y_origin.setDecimals(2)
        self.frame_spinb_y_origin.setMinimum(-10.0)
        self.frame_spinb_y_origin.setMaximum(10.0)
        self.frame_spinb_y_origin.setSingleStep(0.5)
        self.frame_spinb_y_origin.setProperty("value", 0.0)
        self.frame_spinb_y_origin.setObjectName("frame_spinb_y_origin")
        self.frame_spinb_x_trans = QtWidgets.QDoubleSpinBox(self)
        self.frame_spinb_x_trans.setGeometry(QtCore.QRect(147, 235, 69, 26))
        self.frame_spinb_x_trans.setDecimals(2)
        self.frame_spinb_x_trans.setMinimum(-10.0)
        self.frame_spinb_x_trans.setMaximum(10.0)
        self.frame_spinb_x_trans.setSingleStep(0.5)
        self.frame_spinb_x_trans.setProperty("value", 0.0)
        self.frame_spinb_x_trans.setObjectName("frame_spinb_x_trans")
        self.frame_spinb_y_trans = QtWidgets.QDoubleSpinBox(self)
        self.frame_spinb_y_trans.setGeometry(QtCore.QRect(147, 270, 69, 26))
        self.frame_spinb_y_trans.setDecimals(2)
        self.frame_spinb_y_trans.setMinimum(-10.0)
        self.frame_spinb_y_trans.setMaximum(10.0)
        self.frame_spinb_y_trans.setSingleStep(0.5)
        self.frame_spinb_y_trans.setProperty("value", 0.0)
        self.frame_spinb_y_trans.setObjectName("frame_spinb_y_trans")
        self.frame_spinb_z_trans = QtWidgets.QDoubleSpinBox(self)
        self.frame_spinb_z_trans.setGeometry(QtCore.QRect(147, 300, 69, 26))
        self.frame_spinb_z_trans.setDecimals(2)
        self.frame_spinb_z_trans.setMinimum(-10.0)
        self.frame_spinb_z_trans.setMaximum(10.0)
        self.frame_spinb_z_trans.setSingleStep(0.5)
        self.frame_spinb_z_trans.setProperty("value", 0.0)
        self.frame_spinb_z_trans.setObjectName("frame_spinb_z_trans")
        self.frame_spinb_x_angle = QtWidgets.QDoubleSpinBox(self)
        self.frame_spinb_x_angle.setGeometry(QtCore.QRect(147, 385, 69, 26))
        self.frame_spinb_x_angle.setDecimals(2)
        self.frame_spinb_x_angle.setMinimum(0.0)
        self.frame_spinb_x_angle.setMaximum(359.0)
        self.frame_spinb_x_angle.setSingleStep(0.5)
        self.frame_spinb_x_angle.setProperty("value", 0.0)
        self.frame_spinb_x_angle.setObjectName("frame_spinb_x_angle")
        self.frame_spinb_y_angle = QtWidgets.QDoubleSpinBox(self)
        self.frame_spinb_y_angle.setGeometry(QtCore.QRect(147, 418, 69, 26))
        self.frame_spinb_y_angle.setDecimals(2)
        self.frame_spinb_y_angle.setMinimum(0.0)
        self.frame_spinb_y_angle.setMaximum(359.0)
        self.frame_spinb_y_angle.setSingleStep(0.5)
        self.frame_spinb_y_angle.setProperty("value", 0.0)
        self.frame_spinb_y_angle.setObjectName("frame_spinb_y_angle")
        self.frame_spinb_z_angle = QtWidgets.QDoubleSpinBox(self)
        self.frame_spinb_z_angle.setGeometry(QtCore.QRect(147, 450, 69, 26))
        self.frame_spinb_z_angle.setDecimals(2)
        self.frame_spinb_z_angle.setMinimum(0.0)
        self.frame_spinb_z_angle.setMaximum(359.0)
        self.frame_spinb_z_angle.setSingleStep(0.5)
        self.frame_spinb_z_angle.setProperty("value", 0.0)
        self.frame_spinb_z_angle.setObjectName("frame_spinb_z_angle")
        self.frame_lb_rotation_matrix = QtWidgets.QLabel(self)
        self.frame_lb_rotation_matrix.setGeometry(QtCore.QRect(30, 490, 190, 91))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.frame_lb_rotation_matrix.setFont(font)
        self.frame_lb_rotation_matrix.setTextFormat(QtCore.Qt.PlainText)
        self.frame_lb_rotation_matrix.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.frame_lb_rotation_matrix.setWordWrap(False)
        self.frame_lb_rotation_matrix.setObjectName("frame_lb_rotation_matrix")
        self.label_11 = QtWidgets.QLabel(self)
        self.label_11.setGeometry(QtCore.QRect(5, 490, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_11.setWordWrap(False)
        self.label_11.setObjectName("label_11")
        
        self.frame_sb_x_origin.raise_()
    
    # Get a label number
    
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        
        self.frame_lb_component_name.setText(_translate("MainWindow", "Component Name"))
        self.label_3.setText(_translate("MainWindow", "Origin"))
        self.label_4.setText(_translate("MainWindow", "X:"))
        self.label_5.setText(_translate("MainWindow", "Y:"))
        self.label_6.setText(_translate("MainWindow", "Z:"))
        self.label_7.setText(_translate("MainWindow", "Axes Angles"))
        self.label_8.setText(_translate("MainWindow", "X:"))
        self.label_9.setText(_translate("MainWindow", "Z:"))
        self.label_10.setText(_translate("MainWindow", "Y:"))
        self.label_15.setText(_translate("MainWindow", "Translation"))
        self.label_23.setText(_translate("MainWindow", "X:"))
        self.label_24.setText(_translate("MainWindow", "Y:"))
        self.label_25.setText(_translate("MainWindow", "Z:"))
        self.frame_lb_rotation_matrix.setText(_translate("MainWindow", "[[0.00 -0.50 0.33]\n"
"[0.50 0.00 -0.17]\n"
"[-0.33 0.17 0.00]]"))
        self.label_11.setText(_translate("MainWindow", "T:"))
    
    def get_label(self):
        self.label = Frames_Template.labels_tranformations.pop(0)
        return self.label
    
    # Destroy/Clean object and release its label
    def destroy(self, *args, **kwargs):
        Frames_Template.destroy(self, *args, **kwargs)
        Frames_Template.labels_tranformations.append( self.label )    
        
    def set_label(self, label_name):
        label = self.get_label()
        self.frame_lb_component_name.setText( label_name + str(label) )
        return label
    
        
    # Callbacks
    
    @QtCore.pyqtSlot()
    def on_x_origin_changed(self):
        
        if self.sender().__class__ == QtWidgets.QDoubleSpinBox:
            value = self.frame_spinb_x_origin.value()
            # Update its seekbar without triggering a signal
            self.nonSignal_change( self.frame_sb_x_origin, value)
            
        else:
            value = self.frame_sb_x_origin.value()
            self.nonSignal_change( self.frame_spinb_x_origin, value)
        
        if self.matplot_frame != None:
            self.matplot_frame.origin[0] = value
            self.matplot_frame.draw( self )
        
    @QtCore.pyqtSlot()    
    def on_y_origin_changed(self):
        
        if self.sender().__class__ == QtWidgets.QDoubleSpinBox:
            value = self.frame_spinb_y_origin.value()
            # Update its seekbar without triggering a signal
            self.nonSignal_change( self.frame_sb_y_origin, value)
            
        else:
            value = self.frame_sb_y_origin.value()
            self.nonSignal_change( self.frame_spinb_y_origin, value)
        
        if self.matplot_frame != None:
            self.matplot_frame.origin[1] = value
            self.matplot_frame.draw( self )
        
    @QtCore.pyqtSlot()   
    def on_z_origin_changed(self):
        
        if self.sender().__class__ == QtWidgets.QDoubleSpinBox:
            value = self.frame_spinb_z_origin.value()
            # Update its seekbar without triggering a signal
            self.nonSignal_change( self.frame_sb_z_origin, value)
            
        else:
            value = self.frame_sb_z_origin.value()
            self.nonSignal_change( self.frame_spinb_z_origin, value)
        
        if self.matplot_frame != None:
            self.matplot_frame.origin[2] = value
            self.matplot_frame.draw( self )
    
    @QtCore.pyqtSlot()
    def on_x_trans_changed(self):
        
        if self.sender().__class__ == QtWidgets.QDoubleSpinBox:
            value = self.frame_spinb_x_trans.value()
            # Update its seekbar without triggering a signal
            self.nonSignal_change( self.frame_sb_x_trans, value)
            
        else:
            value = self.frame_sb_x_trans.value()
            self.nonSignal_change( self.frame_spinb_x_trans, value)
        
        if self.matplot_frame != None:
            self.matplot_frame.trans[0] = value
            self.manage_rotation_order(3, value)
            self.matplot_frame.draw( self )
    
    @QtCore.pyqtSlot()
    def on_y_trans_changed(self):
        
        if self.sender().__class__ == QtWidgets.QDoubleSpinBox:
            value = self.frame_spinb_y_trans.value()
            # Update its seekbar without triggering a signal
            self.nonSignal_change( self.frame_sb_y_trans, value)
            
        else:
            value = self.frame_sb_y_trans.value()
            self.nonSignal_change( self.frame_spinb_y_trans, value)
        
        if self.matplot_frame != None:
            self.matplot_frame.trans[1] = value
            self.manage_rotation_order(4, value)
            self.matplot_frame.draw( self )
    
    @QtCore.pyqtSlot()            
    def on_z_trans_changed(self):
        
        if self.sender().__class__ == QtWidgets.QDoubleSpinBox:
            value = self.frame_spinb_z_trans.value()
            # Update its seekbar without triggering a signal
            self.nonSignal_change( self.frame_sb_z_trans, value)
            
        else:
            value = self.frame_sb_z_trans.value()
            self.nonSignal_change( self.frame_spinb_z_trans, value)
        
        if self.matplot_frame != None:
            self.matplot_frame.trans[2] = value
            self.manage_rotation_order(5, value)
            self.matplot_frame.draw( self )
    
        
    @QtCore.pyqtSlot()
    def on_x_angle_changed(self):
        
        if self.sender().__class__ == QtWidgets.QDoubleSpinBox:
            value = self.frame_spinb_x_angle.value()
            # Update its seekbar without triggering a signal
            self.nonSignal_change( self.frame_sb_x_angle, value)
            
        else:
            value = self.frame_sb_x_angle.value()
            self.nonSignal_change( self.frame_spinb_x_angle, value)
        
        if self.matplot_frame != None:
            self.matplot_frame.angles[0] = value
            
            self.manage_rotation_order(0, value)
            
            self.matplot_frame.draw( self )
    
    @QtCore.pyqtSlot()
    def on_y_angle_changed(self):
        
        if self.sender().__class__ == QtWidgets.QDoubleSpinBox:
            value = self.frame_spinb_y_angle.value()
            # Update its seekbar without triggering a signal
            self.nonSignal_change( self.frame_sb_y_angle, value)
            
        else:
            value = self.frame_sb_y_angle.value()
            self.nonSignal_change( self.frame_spinb_y_angle, value)
        
        if self.matplot_frame != None:
            self.matplot_frame.angles[1] = value
            
            self.manage_rotation_order(1, value)
            
            self.matplot_frame.draw( self )
    
    @QtCore.pyqtSlot()
    def on_z_angle_changed(self):
        
        if self.sender().__class__ == QtWidgets.QDoubleSpinBox:
            value = self.frame_spinb_z_angle.value()
            # Update its seekbar without triggering a signal
            self.nonSignal_change( self.frame_sb_z_angle, value)
            
        else:
            value = self.frame_sb_z_angle.value()
            self.nonSignal_change( self.frame_spinb_z_angle, value)
        
        if self.matplot_frame != None:
            self.matplot_frame.angles[2] = value
            
            self.manage_rotation_order(2, value)
            
            self.matplot_frame.draw( self )
    
    # Manage sequence of Transformations
    def manage_rotation_order( self, current_axis, axis_value ):
        # Current axis already in list?
        if current_axis in self.rotation_order:
            # If its rotation became 0, remove it
            if axis_value == 0:
                # Check if translation axe
                if current_axis > 2:
                    # If all translation axe are 0, remove it from stack
                    if np.sum( self.matplot_frame.origin ) == 0:
                        self.rotation_order.remove( current_axis )
                else:
                    self.rotation_order.remove( current_axis )
        # If not in the list yet, add it
        else:
            if axis_value != 0:
                self.rotation_order.append( current_axis )
        
        # Update in its Frame element instance
        self.matplot_frame.rotation_order = self.rotation_order
            
    def set_component_frame(self, frame_component):
        self.matplot_frame = frame_component
        
if __name__ == '__main__':
    a = Frame_Transform()
    print('casa')
        