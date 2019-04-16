'''
Created on Feb 21, 2019

@author: ramon
'''
from PyQt5 import QtCore, QtGui, QtWidgets


import sys, os

dirName = os.path.dirname(os.path.abspath(__file__)) + "/"
print(dirName)
sys.path.append( dirName + 'UIs')
sys.path.append( dirName + 'classes')
sys.path.append( dirName + 'MatPlot')

from Layours_Manager import Frame_Transform, Frame_W_Theta, Frame_Screw,\
    Frame_Robot_Arm
from mr_test import Ui_MainWindow

from PlotCanvas import PlotCanvas

from Components import Frame_Element, W_Hat, Screw, Robot

    #app = QtWidgets.QApplication(sys.argv)
    #QtWidgets.QMessageBox.critical(None, "OpenGL hellogl",
            #"PyOpenGL must be installed to run this example."
    
ui = None
Components = []
current_element = -1
Control_Bar = None
plotCanvas = None

def update_control_bar_values():
    global Components, Control_Bar, current_element
    print(len(Components))
    print('%d- '%(current_element) + Components[ current_element ].Qframe.frame_lb_component_name.text())
    
    component = Components[ current_element ]
    
    Control_Bar = component.Qframe
    
    Components[ current_element ].Qframe.show()
    """
    if component.Type == 'Frame':
        Components[ current_element ].origin[0] = Components[ current_element ].Qframe.frame_sb_x_origin.value()
        Components[ current_element ].origin[1] = Components[ current_element ].Qframe.frame_sb_y_origin.value()
        Components[ current_element ].origin[2] = Components[ current_element ].Qframe.frame_sb_z_origin.value()
        
        Components[ current_element ].trans[0] = Components[ current_element ].Qframe.frame_sb_x_trans.value()
        Components[ current_element ].trans[1] = Components[ current_element ].Qframe.frame_sb_y_trans.value()
        Components[ current_element ].trans[2] = Components[ current_element ].Qframe.frame_sb_z_trans.value()
        
        Components[ current_element ].angles[0] = Components[ current_element ].Qframe.frame_sb_x_angle.value()
        Components[ current_element ].angles[1] = Components[ current_element ].Qframe.frame_sb_y_angle.value()
        Components[ current_element ].angles[2] = Components[ current_element ].Qframe.frame_sb_z_angle.value()
        print('Component %d updated' %(current_element))
    
        Components[ current_element ].draw()
    """    
     
    
def add_component( comp_type ):
    global ui, Components, Control_Bar, plotCanvas
    
    if ui.cbComponents.currentText() == "Transform":
        
        matplot_frame = Frame_Element( plotCanvas )
        
        if Control_Bar != None:
            #Control_Bar.destroy0()
            Control_Bar = None
        
        Control_Bar = Frame_Transform( ui.centralwidget )
        
        label = Control_Bar.set_label('Transform_')
        label = str( label )
        
        matplot_frame.set_axe_label("{"+ label +"}")
        
        
        Control_Bar.set_component_frame( matplot_frame )
        
        
        matplot_frame.set_Qframe( Control_Bar )
        
        # Change seekbar value only to call its callback and update classes variables
        matplot_frame.Qframe.on_x_origin_changed()
        
        matplot_frame.draw( matplot_frame.Qframe )
        Components.append( matplot_frame )
        
        # Update list after created and set widget
        ui.lv_Components.addItem("Transform_" + label)
        ui.lv_Components.setCurrentRow( ui.lv_Components.count()-1 )
        
    elif ui.cbComponents.currentText() == "Robot_Arm":
        matplot_frame = Robot( plotCanvas )
        
        if Control_Bar != None:
            #Control_Bar.destroy0()
            Control_Bar = None
        
        Control_Bar = Frame_Robot_Arm( ui.centralwidget )

        matplot_frame.set_axe_label("{"+ str( ui.lv_Components.count() ) +"}")
        Control_Bar.set_label('Frame_' + str( ui.lv_Components.count() ))
        
        Control_Bar.set_component_frame( matplot_frame )
        
        
        matplot_frame.set_Qframe( Control_Bar )
        
        # Change seekbar value only to call its callback and update classes variables
        #matplot_frame.Qframe.on_x_origin_changed()
        
        #matplot_frame.draw( Control_Bar.screw_lb_rotation_matrix )
        Components.append( matplot_frame )
        
        # Update list after created and set widget
        
        ui.lv_Components.addItem("Robot_Arm")
        ui.lv_Components.setCurrentRow( ui.lv_Components.count()-1 )
        
    elif ui.cbComponents.currentText() == "w_hat":
        matplot_frame = W_Hat( plotCanvas )
        
        if Control_Bar != None:
            #Control_Bar.destroy0()
            Control_Bar = None
        
        Control_Bar = Frame_W_Theta( ui.centralwidget )
        
        label = Control_Bar.set_label('Ŵ_')
        label = str( label )
        
        matplot_frame.set_axe_label("{"+  label +"}")
        
        
        Control_Bar.set_component_frame( matplot_frame )
        
        matplot_frame.set_Qframe( Control_Bar )
        
        # Change seekbar value only to call its callback and update classes variables
        matplot_frame.Qframe.on_x_origin_changed()
        
        #matplot_frame.draw( Control_Bar.screw_lb_rotation_matrix )
        Components.append( matplot_frame )
        
        # Update list after created and set widget
        ui.lv_Components.addItem("w_hat_" + label)
        ui.lv_Components.setCurrentRow( ui.lv_Components.count()-1 )
    
    elif ui.cbComponents.currentText() == "Screw":
        matplot_frame = Screw( plotCanvas )
        
        if Control_Bar != None:
            #Control_Bar.destroy0()
            Control_Bar = None
        
        Control_Bar = Frame_Screw( ui.centralwidget )
        
        label = Control_Bar.set_label('Screw_')
        label = str(label)
        matplot_frame.set_axe_label("{"+ label +"}")
        
        Control_Bar.set_component_frame( matplot_frame )
        
        matplot_frame.set_Qframe( Control_Bar )
        
        matplot_frame.Qframe.screw_sb_x_end.setValue( matplot_frame.Qframe.screw_sb_x_end.maximum() )
        matplot_frame.Qframe.screw_sb_h.setValue( 1 )
        
        # Change seekbar value only to call its callback and update classes variables
        matplot_frame.Qframe.on_theta_changed()
        
        #matplot_frame.draw( Control_Bar.screw_lb_rotation_matrix )
        Components.append( matplot_frame )
        
        # Update list after created and set widget
        ui.lv_Components.addItem("Screw_" + label)
        ui.lv_Components.setCurrentRow( ui.lv_Components.count()-1 )

def on_component_selected():
    global current_element, Components
    
    index = ui.lv_Components.currentRow()
    current_element = index
    
    for frame in Components:
        frame.Qframe.hide()
    
    #Components[ current_element ].Qframe.show()
    update_control_bar_values()

def on_lv_delete_component():
    global ui, current_element
    
    if ui.lv_Components.hasFocus():
        #ui.lv_Components.item( current_element ).deleteAfter()
        
        remove_index = ui.lv_Components.currentRow()
        
        item = ui.lv_Components.takeItem( remove_index )
        item = None
        
        if Components[ remove_index ].Qframe != None:
            Components[ remove_index ].Qframe.destroy0()
        
        del Components[ remove_index ]
        
        if len( Components ) > 0:
            ui.lv_Components.setCurrentRow(0)
        
        #if ui.lv_Components.count() > 0:
            #ui.lv_Components.setCurrentRow( ui.lv_Components.count()-1 )
        #else:
            #current_element = len( Components )

def setup_widgets(ui):
    # Components ComboBox
    #"Screw"
    ui.cbComponents.addItems(["Transform", "w_hat", "Screw"]) #"Robot_Arm"
    #ui.cbComponents.currentIndexChanged.connect(self.selectionchange)
    
    # btAdd ( Rotation or Robot )
    ui.btAdd_Component.clicked.connect( add_component )
    
    # Components added ListView
    ui.lv_Components.currentItemChanged.connect( on_component_selected )
    #ui.lv_Components.addItem("First")
    #ui.lv_Components.addItem("Second")
    #QtGui.QtShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Delete), ui.lv_Components)
    #QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Delete), self.list_one)
    deleteShortcut = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Delete), ui.lv_Components)
    deleteShortcut.activated.connect( on_lv_delete_component )
    #ui.lv_Components.setCurrentRow(0)
    #ui.lv_Components.item(0).setForeground(QtGui.QBrush(QtCore.Qt.green))
    #ui.lv_Components..item(1)->setForeground(Qt::blue);    

"""
    Keyboard events
"""
def eventFilter(self, source, event):
    if event.type() == QtCore.QEvent.KeyPress:
        print('KeyPress: %s [%r]' % (event.key(), source))
    return
    #return super(Window, self).eventFilter(source, event)

if __name__ == '__main__':
    global plotCanvas
    
    app = QtWidgets.QApplication(sys.argv)
    
    # Configure Main Ui
    MainWindow = QtWidgets.QMainWindow()
    
    # Install keyboard events
    #ui = Ui_MainWindow( playerControl )
    ui = Ui_MainWindow( )
    #ui = Ui_MainWindow( )
    ui.setupUi(MainWindow)
    
    MainWindow.setWindowTitle("MR ToolBox")
    
    QtWidgets.qApp.installEventFilter( MainWindow )
    
    #800x600
    plotCanvas = PlotCanvas(ui.frm_matplot, width=8, height=6)
    plotCanvas.move(0,0)
    
    #frame = Frame_Transforma( ui.centralwidget )
    #frame.destroy0()
    
    # Configure each widget
    setup_widgets(ui)
    
    #app.installEventFilter( MainWindow )
    # Show Main Ui
    MainWindow.show()
        
    # Configure Library UI
    #Form = QtWidgets.QMainWindow()
    #frm = Ui_mwLibrary( playerControl )
    #frm.setupUi( Form )
    
    
    sys.exit(app.exec_())
