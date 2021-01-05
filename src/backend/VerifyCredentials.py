#--------------------------------------------------------------------------------------------------#
# @author: Kaushik Biswas                                                                          #
# @version: 1.0.2                                                                                  #
# @description: This is the main ui class                                                          #
#--------------------------------------------------------------------------------------------------#

from FireBaseConfig import *

class Verifications:

    def __init__(self):
        self.auth = get_firebase_auth()

    
    def checkLogin(self, email, password):
        pass

    def create_account(self, username, email, password):
        pass