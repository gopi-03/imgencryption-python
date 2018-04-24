# System imports
import sys
import traceback

# Package imports
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from ftplib import FTP

# Local imports
from static import create_user_files, IP_ADDR, PORT
from mainwindow import Ui_EDwindow


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(371, 245)
        self.usernameInput = QtWidgets.QLineEdit(Dialog)
        self.usernameInput.setGeometry(QtCore.QRect(80, 60, 211, 31))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        self.usernameInput.setFont(font)
        self.usernameInput.setMaxLength(15)
        self.usernameInput.setObjectName("usernameInput")
        self.userPwdInput = QtWidgets.QLineEdit(Dialog)
        self.userPwdInput.setGeometry(QtCore.QRect(80, 120, 211, 31))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        self.userPwdInput.setFont(font)
        self.userPwdInput.setText("")
        self.userPwdInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.userPwdInput.setObjectName("userPwdInput")
        self.loginBtn = QtWidgets.QPushButton(Dialog)
        self.loginBtn.setGeometry(QtCore.QRect(140, 170, 91, 31))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        self.loginBtn.setFont(font)
        self.loginBtn.setObjectName("loginBtn")
        self.loginLabel = QtWidgets.QLabel(Dialog)
        self.loginLabel.setGeometry(QtCore.QRect(160, 20, 61, 31))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.loginLabel.setFont(font)
        self.loginLabel.setObjectName("loginLabel")

        # Login Button action
        self.loginBtn.clicked.connect(self.login)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Login"))
        self.usernameInput.setPlaceholderText(_translate("Dialog", "Enter User Name"))
        self.userPwdInput.setPlaceholderText(_translate("Dialog", "Enter Password"))
        self.loginBtn.setText(_translate("Dialog", "Login"))
        self.loginLabel.setText(_translate("Dialog", "Login"))

    def login(self):
        userid  = self.usernameInput.text()
        userpwd = self.userPwdInput.text()

        try:
            sendftp = FTP('')
            sendftp.connect(IP_ADDR, PORT)
            sendftp.login(userid, userpwd)

            receiveftp = FTP('')
            receiveftp.connect(IP_ADDR, PORT)
            receiveftp.login(userid, userpwd)

            create_user_files(userid)

            Dialog.close()

            Ui_EDwindow.userid = userid
            Ui_EDwindow.sendftp = sendftp
            Ui_EDwindow.receiveftp = receiveftp

            self.EDwindow = QtWidgets.QDialog()
            self.ui = Ui_EDwindow()
            self.ui.setupUi(self.EDwindow)
            self.EDwindow.show()
        except :
            print("Error Occured!")
            traceback.print_exc()
            mb = QMessageBox()
            mb.setIcon(QMessageBox.Warning)
            mb.setWindowTitle(":-( ")
            mb.setText('Invalid Details !')
            mb.exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

