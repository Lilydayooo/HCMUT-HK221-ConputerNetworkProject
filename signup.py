import res
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import socket, pickle
from subprocess import call
from login import serverIP

HEADER_LENGTH = 10

class SignUp(object):
    #UI 'til line 100
    def setupUi(self, SignUp):
        SignUp.setObjectName("SignUp")
        SignUp.resize(482, 379)
        SignUp.setStyleSheet("")
        self.SignUp = SignUp
        self.txtSignUp = QtWidgets.QLabel(SignUp)
        self.txtSignUp.setGeometry(QtCore.QRect(170, 30, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.txtSignUp.setFont(font)
        self.txtSignUp.setStyleSheet("color: white;")
        self.txtSignUp.setObjectName("txtSignUp")
        self.txtFullname = QtWidgets.QLabel(SignUp)
        self.txtFullname.setGeometry(QtCore.QRect(40, 120, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.txtFullname.setFont(font)
        self.txtFullname.setStyleSheet("color: white;")
        self.txtFullname.setObjectName("txtFullname")
        self.txtUsername = QtWidgets.QLabel(SignUp)
        self.txtUsername.setGeometry(QtCore.QRect(40, 180, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.txtUsername.setFont(font)
        self.txtUsername.setStyleSheet("color: white;")
        self.txtUsername.setObjectName("txtUsername")
        self.txtPassword = QtWidgets.QLabel(SignUp)
        self.txtPassword.setGeometry(QtCore.QRect(40, 240, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.txtPassword.setFont(font)
        self.txtPassword.setStyleSheet("color: white;")
        self.txtPassword.setObjectName("txtPassword")
        self.Fullname = QtWidgets.QLineEdit(SignUp)
        self.Fullname.setGeometry(QtCore.QRect(160, 125, 291, 31))
        self.Fullname.setObjectName("Fullname")
        self.Password = QtWidgets.QLineEdit(SignUp)
        self.Password.setGeometry(QtCore.QRect(160, 240, 291, 31))
        self.Password.setObjectName("Password")
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Username = QtWidgets.QLineEdit(SignUp)
        self.Username.setGeometry(QtCore.QRect(160, 180, 291, 31))
        self.Username.setObjectName("Username")
        self.btSignUp = QtWidgets.QPushButton(SignUp)
        self.btSignUp.setGeometry(QtCore.QRect(190, 310, 93, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btSignUp.setFont(font)
        self.btSignUp.setObjectName("btSignUp")
        self.bgImage = QtWidgets.QLabel(SignUp)
        self.bgImage.setGeometry(QtCore.QRect(0, 0, 482, 379))
        self.bgImage.setStyleSheet(
            "background-image: url(:/image/image/welcome.jpg)")
        self.bgImage.setText("")
        self.bgImage.setObjectName("bgImage")
        self.bgImage.raise_()
        self.txtSignUp.raise_()
        self.txtUsername.raise_()
        self.Fullname.raise_()
        self.Password.raise_()
        self.Username.raise_()
        self.btSignUp.raise_()
        self.txtPassword.raise_()
        self.txtFullname.raise_()

        self.retranslateUi(SignUp)
        QtCore.QMetaObject.connectSlotsByName(SignUp)
    def retranslateUi(self, SignUp):
        _translate = QtCore.QCoreApplication.translate
        SignUp.setWindowTitle(_translate("SignUp", "SignUp"))
        self.txtSignUp.setText(_translate("SignUp", "SIGN UP"))
        self.txtFullname.setText(_translate("SignUp", "FullName"))
        self.txtUsername.setText(_translate("SignUp", "Username"))
        self.txtPassword.setText(_translate("SignUp", "Password"))
        self.Fullname.setPlaceholderText(
            _translate("SignUp", "Enter your name"))
        self.Password.setPlaceholderText(
            _translate("SignUp", "Enter your password"))
        self.Username.setPlaceholderText(
            _translate("SignUp", "Enter your account"))
        self.btSignUp.setText(_translate("SignUp", "SIGN UP"))
        self.btSignUp.clicked.connect(self.signup)
    
    def signup(self):
        mess = QMessageBox()
        if self.Fullname.text() == "" or self.Username.text() == "" or self.Password.text() == "":
            mess.setIcon(QMessageBox.Warning)
            mess.setText("You need to fill in all the blank!")
            mess.exec_()
        else:
            print("Starting Client...")
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((serverIP, 8082))
            hostname = socket.gethostname()
            ip_address = socket.gethostbyname(hostname)            
            
            print("Sending from " + hostname + " with IP address " + ip_address)

            message = {}
            message["method"] = "signup"
            message["name"] = self.Fullname.text()
            message["user_name"] = self.Username.text()
            message["password"] = self.Password.text()
            message["ip"] = ip_address

            msg = pickle.dumps(message)
            msg = bytes(f"{len(msg):<{HEADER_LENGTH}}","utf-8") + msg

            client_socket.send(msg)

            text = client_socket.recv(1024)
            response = text.decode()

            if (response == "Not"):
                mess = QMessageBox()
                mess.setIcon(QMessageBox.Warning)
                mess.setText("Account has already existed!")
                mess.exec_()
            else:
                self.SignUp.close()
                call(["python", "login.py"])

            client_socket.close()

            print("Ending Client....")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Signup = QtWidgets.QDialog()
    ui = SignUp()
    ui.setupUi(Signup)
    Signup.show()
    sys.exit(app.exec_())
