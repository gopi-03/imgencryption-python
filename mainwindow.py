# System imports
from os import getcwd, listdir
import sqlite3 as db

# Package imports
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
from PIL import Image
from ftplib import FTP

# Local imports
from static import timestamp_generator,amtopm,NOF_KEYS
from ImageED import ExtendedImage


class Ui_EDwindow(object):
    userid = ''
    receiveftp = FTP('')
    sendftp = FTP('')
    files = []
    def setupUi(self, EDwindow):
        EDwindow.setObjectName("EDwindow")
        EDwindow.resize(751, 602)
        self.timer = QtCore.QTimer()
        self.horline0 = QtWidgets.QFrame(EDwindow)
        self.horline0.setGeometry(QtCore.QRect(27, 50, 711, 20))
        self.horline0.setFrameShape(QtWidgets.QFrame.HLine)
        self.horline0.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.horline0.setObjectName("horline0")
        self.welcomeLabel = QtWidgets.QLabel(EDwindow)
        self.welcomeLabel.setGeometry(QtCore.QRect(28, 19, 711, 31))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.welcomeLabel.setFont(font)
        self.welcomeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.welcomeLabel.setObjectName("welcomeLabel")


        self.msgInput = QtWidgets.QPlainTextEdit(EDwindow)
        self.msgInput.setGeometry(QtCore.QRect(20, 100, 261, 101))
        self.msgInput.setTabChangesFocus(True)
        self.msgInput.setObjectName("msgInput")
        self.passkeyInput = QtWidgets.QLineEdit(EDwindow)
        self.passkeyInput.setGeometry(QtCore.QRect(20, 210, 261, 31))
        self.passkeyInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passkeyInput.setObjectName("passkeyInput")
        self.receiverInput = QtWidgets.QLineEdit(EDwindow)
        self.receiverInput.setReadOnly(True)
        self.receiverInput.setGeometry(QtCore.QRect(20, 250, 261, 31))
        self.receiverInput.setObjectName("receiverInput")
        self.verLine = QtWidgets.QFrame(EDwindow)
        self.verLine.setGeometry(QtCore.QRect(300,  100, 20, 491))
        self.verLine.setFrameShape(QtWidgets.QFrame.VLine)
        self.verLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.verLine.setObjectName("verLine")
        self.encryptionLabel = QtWidgets.QLabel(EDwindow)
        self.encryptionLabel.setGeometry(QtCore.QRect(20, 70, 111, 21))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.encryptionLabel.setFont(font)
        self.encryptionLabel.setObjectName("encryptionLabel")
        self.usersLabel = QtWidgets.QLabel(EDwindow)
        self.usersLabel.setGeometry(QtCore.QRect(20, 360, 141, 21))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.usersLabel.setFont(font)
        self.usersLabel.setObjectName("usersLabel")
        self.sendBtn = QtWidgets.QPushButton(EDwindow)
        self.sendBtn.setGeometry(QtCore.QRect(180, 290, 80, 23))
        self.sendBtn.setObjectName("sendBtn")
        self.horline = QtWidgets.QFrame(EDwindow)
        self.horline.setGeometry(QtCore.QRect(10, 330, 271, 16))
        self.horline.setFrameShape(QtWidgets.QFrame.HLine)
        self.horline.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.horline.setObjectName("horline")

        self.userslistTable = QtWidgets.QTableWidget(EDwindow)
        self.userslistTable.setGeometry(QtCore.QRect(20, 390, 261, 181))
        self.userslistTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.userslistTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.userslistTable.setObjectName("userslistTable")
        self.userslistTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.download_db()
        self.createuserslist_table()

        self.receivedmsgsLabel = QtWidgets.QLabel(EDwindow)
        self.receivedmsgsLabel.setGeometry(QtCore.QRect(320, 70, 181, 21))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.receivedmsgsLabel.setFont(font)
        self.receivedmsgsLabel.setObjectName("receivedmsgsLabel")

        self.msgsTable = QtWidgets.QTableWidget(EDwindow)
        self.msgsTable.setGeometry(QtCore.QRect(320, 100, 411, 211))
        self.msgsTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.msgsTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.msgsTable.setObjectName("msgsTable")
        self.msgsTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.createmsgs_table()


        self.horLine2 = QtWidgets.QFrame(EDwindow)
        self.horLine2.setGeometry(QtCore.QRect(320, 330, 421, 16))
        self.horLine2.setFrameShape(QtWidgets.QFrame.HLine)
        self.horLine2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.horLine2.setObjectName("horLine2")
        self.decryptImgInput = QtWidgets.QLineEdit(EDwindow)
        self.decryptImgInput.setReadOnly(True)
        self.decryptImgInput.setGeometry(QtCore.QRect(390, 390, 341, 31))
        self.decryptImgInput.setText("")
        self.decryptImgInput.setObjectName("decryptImgInput")
        self.decryptLabel = QtWidgets.QLabel(EDwindow)
        self.decryptLabel.setGeometry(QtCore.QRect(330, 360, 141, 21))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(11)
        font.setBold(True)
        self.decryptLabel.setFont(font)
        self.decryptLabel.setObjectName("decryptLabel")
        self.decryptpasskeyInput = QtWidgets.QLineEdit(EDwindow)
        self.decryptpasskeyInput.setGeometry(QtCore.QRect(390, 430, 341, 31))
        self.decryptpasskeyInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.decryptpasskeyInput.setObjectName("decryptpasskeyInput")
        self.decryptBtn = QtWidgets.QPushButton(EDwindow)
        self.decryptBtn.setGeometry(QtCore.QRect(620, 470, 80, 23))
        self.decryptBtn.setObjectName("decryptBtn")

        # Button Action  ############################
        self.msgsTable.cellClicked.connect(self.retrieve_image_name)
        self.sendBtn.clicked.connect(self.image_send)
        self.decryptBtn.clicked.connect(self.decrypt_img)
        self.userslistTable.cellClicked.connect(self.retrieve_user_name)
        #############################################

        self.retranslateUi(EDwindow)
        QtCore.QMetaObject.connectSlotsByName(EDwindow)

    def retranslateUi(self, EDwindow):
        _translate = QtCore.QCoreApplication.translate
        EDwindow.setWindowTitle(_translate("EDwindow", "Image Encryption Decryption"))
        self.msgInput.setProperty("placeholderText", _translate("EDwindow", "Enter Message"))
        self.passkeyInput.setPlaceholderText(_translate("EDwindow", "Enter PassKey"))
        self.receiverInput.setPlaceholderText(_translate("EDwindow", "Select Username from Userslist"))
        self.encryptionLabel.setText(_translate("EDwindow", "Encryption"))
        self.usersLabel.setText(_translate("EDwindow", "List of Users"))
        self.sendBtn.setText(_translate("EDwindow", "Send"))
        self.decryptImgInput.setPlaceholderText(_translate("EDwindow", "Select Image name from Messages Table"))
        self.decryptLabel.setText(_translate("EDwindow", "Decryption"))
        self.decryptpasskeyInput.setPlaceholderText(_translate("EDwindow", "Enter PassKey"))
        self.decryptBtn.setText(_translate("EDwindow", "Decrypt"))
        self.receivedmsgsLabel.setText(_translate("EDwindow", "Received Messages "))
        self.welcomeLabel.setText(_translate("EDwindow", "Welcome " + Ui_EDwindow.userid))

    # Image Creation and Encryption     #############################

    def image_send(self):
        text = str(self.msgInput.toPlainText())
        passkey = str(self.passkeyInput.text())
        receiver = str(self.receiverInput.text())

        self.receiverInput.clear()
        self.passkeyInput.clear()
        self.msgInput.clear()

        abspath = getcwd()

        timestamp = timestamp_generator()

        input_img_path      = abspath + "/images/" + Ui_EDwindow.userid + "/input_img/" + receiver + "-" + timestamp + ".png"
        enc_img_name        = Ui_EDwindow.userid + "-" + timestamp + ".png"
        abs_enc_img_path    = abspath + "/images/" + Ui_EDwindow.userid + "/enc_img/" + enc_img_name

        ExtendedImage.genimg(text, input_img_path)
        image = ExtendedImage(Image.open(input_img_path))
        image.encryptimg(passkey, abs_enc_img_path)

        Ui_EDwindow.sendftp.cwd(receiver)
        Ui_EDwindow.sendftp.storbinary('STOR ' + enc_img_name, open(abs_enc_img_path, 'rb'))
        print("Msg files sent to " + receiver)
        Ui_EDwindow.sendftp.cwd("./..")
        self.gen_msgbox(QMessageBox.Information,"Msg Sent Successfully","Success!")

    def createuserslist_table(self):
        conn        = db.connect('users_list.db')
        users_list = []
        for user in conn.cursor().execute('SELECT * FROM users'):
            users_list.append(user[0])
        self.userslistTable.setRowCount(len(users_list))
        self.userslistTable.setColumnCount(1)
        self.userslistTable.setHorizontalHeaderLabels(("UsersList",))
        header = self.userslistTable.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        count = 0
        for user in sorted(users_list):
            self.userslistTable.setItem(count, 0, QTableWidgetItem(user))
            count += 1
        conn.close()

    def retrieve_user_name(self, row, col):
        self.receiverInput.setText(self.userslistTable.item(row,0).text())

    def createmsgs_table(self):
        self.receiveftp.cwd(Ui_EDwindow.userid)
        Ui_EDwindow.files   = self.receiveftp.nlst()
        rowlength = len(Ui_EDwindow.files) == 0 and 0 or len(Ui_EDwindow.files)
        print("Files that are already in your database : " + str(len(Ui_EDwindow.files)))
        for f in Ui_EDwindow.files:
            print(f)
        self.msgsTable.setRowCount(rowlength)
        self.msgsTable.setColumnCount(2)
        self.msgsTable.setHorizontalHeaderLabels(("From", "Received on"))
        header = self.msgsTable.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        count = 0
        for f in reversed(Ui_EDwindow.files):
            sender = f
            timestamp = f[-23:-13] + ' ' + amtopm(f[-12:-4])
            self.msgsTable.setItem(count,0, QTableWidgetItem(sender))
            self.msgsTable.setItem(count,1, QTableWidgetItem(timestamp))
            count += 1
        self.timer.timeout.connect(self.fetch_files)
        self.timer.start(2000)

    def fetch_files(self):
        newfiles = Ui_EDwindow.receiveftp.nlst()
        insertfiles = list(set(newfiles) - set(Ui_EDwindow.files))
        print("New Messages arrived are : " + str(len(insertfiles)))
        print(insertfiles)
        if len(insertfiles) > 0:
            for f in insertfiles:
                sender = f
                timestamp = f[-23:-13] + ' ' + amtopm(f[-12:-4])
                self.msgsTable.insertRow(0)
                self.msgsTable.setItem(0, 0, QTableWidgetItem(sender))
                self.msgsTable.setItem(0, 1, QTableWidgetItem(timestamp))
        Ui_EDwindow.files = list(newfiles)

    def retrieve_image_name(self, row, col):
        self.decryptImgInput.setText(self.msgsTable.item(row,0).text())

    def decrypt_img(self):
        downloadedimg   = self.download_img()
        decryptpasskey  = self.decryptpasskeyInput.text()
        image = ExtendedImage(Image.open(downloadedimg))
        image.decryptimg(decryptpasskey, "")
        image.show()

    def download_img(self):
        decryptimgname  = self.decryptImgInput.text()
        downloaded_img  = str(getcwd()) + "/images/" + Ui_EDwindow.userid \
                          + "/downloaded_img/" + decryptimgname
        path = str(getcwd()) + "/images/" + Ui_EDwindow.userid \
                         + "/downloaded_img/"
        if decryptimgname in listdir(path):
            return downloaded_img
        img             = open(downloaded_img, 'wb')
        self.receiveftp.retrbinary('RETR ' + decryptimgname, img.write)
        print("Image Downloaded from FTPSERVER")
        return downloaded_img

    def download_db(self):
        database    = open('users_list.db','wb')
        self.sendftp.retrbinary('RETR users_list.db',database.write)

    def gen_msgbox(self, icon, description,title):
        msg = QMessageBox()
        msg.setIcon(icon)
        msg.setText(description)
        msg.setWindowTitle(title)
        msg.exec()