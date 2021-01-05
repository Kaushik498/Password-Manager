#--------------------------------------------------------------------------------------------------#
# @author: Kaushik Biswas                                                                          #
# @version: 1.0.2                                                                                  #
# @description: This class contains useful functions for UI                                        #
#--------------------------------------------------------------------------------------------------#


#   Library Imports
#--------------------------------------------------------------------------------------------------#
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


#   Global variables
#--------------------------------------------------------------------------------------------------#
WINDOW_SIZE_FLAG = 0
HOME_LABEL = None


class Util():

#   Assign functions/modifcations to different ui elements
#--------------------------------------------------------------------------------------------------#
    @staticmethod
    def setup_ui_functions(window):

        Util.title_bar_modifcations(window)
        window.ui.left_panel.setGraphicsEffect(Util.loadShadow(window))
        
        window.ui.add_new_password_frame.setGraphicsEffect(Util.loadShadow(window))
        window.ui.update_password_frame.setGraphicsEffect(Util.loadShadow(window))
        window.ui.most_used_password_frame.setGraphicsEffect(Util.loadShadow(window))
        window.ui.password_reports_frame.setGraphicsEffect(Util.loadShadow(window))
        
        window.ui.password_list_container.setGraphicsEffect(Util.loadShadow(window))
        window.ui.search_container.setGraphicsEffect(Util.loadShadow(window))
        
        window.ui.account_details_container.setGraphicsEffect(Util.loadShadow(window))
        window.ui.extra_details_container.setGraphicsEffect(Util.loadShadow(window))

        # Sign up / Log in
        window.ui.login_button.clicked.connect(lambda: Util.callContentPage(window))
        window.ui.signup_button.clicked.connect(lambda: Util.callContentPage(window))
        
        # Title bar button functions
        window.ui.maximize_button.clicked.connect(lambda: Util.maximize_button_function(window))
        window.ui.minimize_button.clicked.connect(lambda: window.showMinimized())
        window.ui.close_button.clicked.connect(lambda: window.close())

        # Resize functionality for the bottom right corner
        window.sizegrip = QSizeGrip(window.ui.resize_frame)
        window.sizegrip.setStyleSheet("QSizeGrip { background-color: transparent; width: 10px; height: 10px; margin: 5px }")


#--------------------------------------------------------------------------------------------------#
    @staticmethod
    def callContentPage(window):
        window.ui.middle_stack.setCurrentWidget(window.ui.content_page)


#   Title bar modifications -
#       1. remove the ugly outer layer.
#--------------------------------------------------------------------------------------------------#
    @staticmethod
    def title_bar_modifcations(window):
        window.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        window.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        window.ui.outer_frame.setGraphicsEffect(Util.loadShadow(window))

#       1. remove the ugly outer layer.
#--------------------------------------------------------------------------------------------------#
    @staticmethod
    def loadShadow(window):
        shadow = QGraphicsDropShadowEffect(window)
        shadow.setBlurRadius(20)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        shadow.setColor(QColor(0, 0, 0, 100))
        return shadow

#   When green button is clicked - 
#       1. maximize if the window is normal sized update left pannel
#       1. minimize if the window is already maximized update left pannel
#   State of the window is saved in the global variable: WINDOW_SIZE_FLAG
#--------------------------------------------------------------------------------------------------#
    @staticmethod
    def maximize_button_function(window):
        global WINDOW_SIZE_FLAG
        status = WINDOW_SIZE_FLAG

        if status == 0:
            # Case if not maximized
            window.ui.toggleLeftPannel(0)
            window.showMaximized()
            WINDOW_SIZE_FLAG = 1
            window.ui.outer_layout.setContentsMargins(0, 0, 0, 0)
            # Border radius needs to ne 0 when maximized
            window.ui.outer_frame.setStyleSheet("border-radius: 0px;background-color: rgb(160, 205, 212);")
        else:
            # Case if already maximized
            window.ui.toggleLeftPannel(1)
            WINDOW_SIZE_FLAG = 0
            window.showNormal()
            window.resize(window.width()+1, window.height()+1)
            window.ui.outer_layout.setContentsMargins(10, 10, 10, 10)
            window.ui.outer_frame.setStyleSheet("border-radius: 15px;background-color: rgb(160, 205, 212);")

    
#   Return window size status
#--------------------------------------------------------------------------------------------------#
    @staticmethod
    def returnWindowSize():
        return WINDOW_SIZE_FLAG

'''

#  Frame Size change when maximized
#--------------------------------------------------------------------------------------------------#
    def toggleLeftPannel(self, status):
        if status == 0:
            # While maximizing
            self.left_panel_container.setMinimumSize(QSize(250, 0))
            self.left_panel_container.setMaximumSize(QSize(250, 16777215))
            self.home_label.setParent(self.home_icon_frame)
            self.horizontalLayout_10.addWidget(self.home_label, 0, Qt.AlignVCenter)
            self.password_label.setParent(self.password_icon_frame)
            self.horizontalLayout_11.addWidget(self.password_label, 0, Qt.AlignVCenter)
            self.settings_label.setParent(self.settings_icon_frame)
            self.horizontalLayout_12.addWidget(self.settings_label, 0, Qt.AlignVCenter)
        else:
            # if already maximized
            self.home_label.setParent(None)
            self.password_label.setParent(None)
            self.settings_label.setParent(None)
            self.left_panel_container.setMinimumSize(QSize(120, 0))
            self.left_panel_container.setMaximumSize(QSize(150, 16777215))

#  Create virtual labels to use. 
#  Add this function in main_ui setup. self.loadLabels()
#--------------------------------------------------------------------------------------------------#
    def loadLabels(self):
            self.left_panel_font = QFont()
            self.left_panel_font.setFamily(u"Cambria")
            self.left_panel_font.setPointSize(10)
            self.left_panel_font.setBold(True)
            
            self.home_label = QLabel()
            self.home_label.setObjectName(u"home_label")
            self.home_label.setMinimumSize(QSize(100, 0))
            self.home_label.setMaximumSize(QSize(100, 16777215))
            self.home_label.setFont(self.left_panel_font)
            self.home_label.setStyleSheet(u"color: rgb(0, 0, 71);")
            self.home_label.setText("Home")    
        
            self.password_label = QLabel()
            self.password_label.setObjectName(u"password_label")
            self.password_label.setMinimumSize(QSize(100, 0))
            self.password_label.setMaximumSize(QSize(100, 16777215))
            self.password_label.setFont(self.left_panel_font)
            self.password_label.setStyleSheet(u"color: rgb(0, 0, 71);")
            self.password_label.setText("Passwords")

            self.settings_label = QLabel()
            self.settings_label.setObjectName(u"password_label")
            self.settings_label.setMinimumSize(QSize(100, 0))
            self.settings_label.setMaximumSize(QSize(100, 16777215))
            self.settings_label.setFont(self.left_panel_font)
            self.settings_label.setStyleSheet(u"color: rgb(0, 0, 71);")
            self.settings_label.setText("Settings")


'''