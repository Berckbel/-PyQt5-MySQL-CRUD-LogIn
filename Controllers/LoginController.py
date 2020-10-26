import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets
from Database.Connection import connection
from Models.User import User

class LoginController():

    def __init__(self, log_in):
        self.user = User(connection())
        self.log_in = log_in

    def logIn(self,user,password, Ui_Principal, LogIn):
        if user and password:
            user = self.user.getUser(user,password)
            if user:
                LogIn.hide()
                self.log_in.Form = QtWidgets.QMainWindow()
                self.log_in.ui = Ui_Principal()
                self.log_in.ui.setupUi(self.log_in.Form)
                self.log_in.Form.show()
                print('Estas logeado')
            else:
                print('No estas logeado')
