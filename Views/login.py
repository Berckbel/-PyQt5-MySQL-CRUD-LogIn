import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from Controllers.LoginController import LoginController
from Views.principal import Ui_Principal
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LogIn(object):

    def __init__(self):
        self.login_controller = LoginController(self)

    def setupUi(self, LogIn):
        LogIn.setObjectName("LogIn")
        LogIn.resize(682, 375)
        self.centralwidget = QtWidgets.QWidget(LogIn)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(100, 40, 471, 291))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.input_user = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_user.setFont(font)
        self.input_user.setObjectName("input_user")
        self.gridLayout.addWidget(self.input_user, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.input_password = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_password.setFont(font)
        self.input_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_password.setObjectName("input_password")
        self.gridLayout.addWidget(self.input_password, 2, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.btn_login = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btn_login.setFont(font)
        self.btn_login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_login.setObjectName("btn_login")
        self.gridLayout_2.addWidget(self.btn_login, 1, 0, 1, 1)
        LogIn.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(LogIn)
        self.statusbar.setObjectName("statusbar")
        LogIn.setStatusBar(self.statusbar)

        self.retranslateUi(LogIn)
        QtCore.QMetaObject.connectSlotsByName(LogIn)
        #--------------------Events--------------------------------------
        self.x = self.btn_login.clicked.connect(lambda:self.login_controller.logIn(self.input_user.text(),self.input_password.text(),Ui_Principal,LogIn))
        #--------------------End Events---------------------------------
    def retranslateUi(self, LogIn):
        _translate = QtCore.QCoreApplication.translate
        LogIn.setWindowTitle(_translate("LogIn", "MainWindow"))
        self.label.setText(_translate("LogIn", "Iniciar Sesion"))
        self.label_2.setText(_translate("LogIn", "Usuario:"))
        self.input_user.setPlaceholderText(_translate("LogIn", "usuario"))
        self.label_3.setText(_translate("LogIn", "Contraseña:"))
        self.input_password.setPlaceholderText(_translate("LogIn", "contraseña"))
        self.btn_login.setText(_translate("LogIn", "Entrar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LogIn = QtWidgets.QMainWindow()
    ui = Ui_LogIn()
    ui.setupUi(LogIn)
    LogIn.show()
    sys.exit(app.exec_())
