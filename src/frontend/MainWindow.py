#--------------------------------------------------------------------------------------------------#
# @author: Kaushik Biswas                                                                          #
# @version: 1.0.2                                                                                  #
# @description: This is the main ui class                                                          #
#--------------------------------------------------------------------------------------------------#


#   Library Imports
#--------------------------------------------------------------------------------------------------#
import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *



#   Local Imports
#--------------------------------------------------------------------------------------------------#
from MainUI import *
from UiUtils import Util


class AlohaMora(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_AlohaMora()
        self.ui.setupUi(self)

        ## Set ui functions
        self.ui.top_logo_frame.mouseMoveEvent = self.moveWindow
        
        # Stacked page set up
        self.ui.signup_option.mousePressEvent = self.callSignUpPage
        self.ui.home_icon_frame.mousePressEvent = self.callHomePage
        self.ui.password_icon_frame.mousePressEvent = self.callPasswordPage
        self.ui.settings_icon_frame.mousePressEvent = self.callSettingsPage

        # Set home page as default 
        self.ui.content_stack.setCurrentWidget(self.ui.home_page)
        self.ui.middle_stack.setCurrentWidget(self.ui.login_page)

        Util.setup_ui_functions(self)


#   Move Window By dragging on the top_logo_frame
#--------------------------------------------------------------------------------------------------#
    def moveWindow(self, event):
        # Restore window size before if maximized
        if Util.returnWindowSize() == 1:
            Util.maximize_button_function(self)

        # Move the window when left clicked
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

#   App Events
#--------------------------------------------------------------------------------------------------#
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def callSignUpPage(self, event):
        self.ui.middle_stack.setCurrentWidget(self.ui.signup_page)

    def callHomePage(self, event):
        self.ui.content_stack.setCurrentWidget(self.ui.home_page)

    def callPasswordPage(self, event):
        self.ui.content_stack.setCurrentWidget(self.ui.password_page)

    def callSettingsPage(self, event):
        self.ui.content_stack.setCurrentWidget(self.ui.settings_page)

#--------------------------------------------------------------------------------------------------#
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AlohaMora()
    window.show()
    sys.exit(app.exec_())
