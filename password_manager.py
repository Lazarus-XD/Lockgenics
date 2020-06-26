import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from modules.info import Ui_DataWindow
from modules.new_user import Ui_createUserWidget
from modules.database import *

class Ui_LoginWindow(QMainWindow):
    def __init__(self):
        super(Ui_LoginWindow, self).__init__()
        self.setupUi()
        self.db = Database()
        self.db.createTable()

    def setupUi(self):
        self.setObjectName("Login")
        self.setFixedSize(800, 600)

        #background setup
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(106, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        self.setPalette(palette)

        #text white color setup
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)

        #icon setup
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("modules/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        #font setup
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        #label setup
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(218, 30, 371, 61))
        self.titleLabel.setPalette(palette)
        font.setPointSize(30)
        font.setUnderline(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName("titleLabel")

        self.titleLabel2 = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel2.setGeometry(QtCore.QRect(255, 90, 301, 61))
        self.titleLabel2.setPalette(palette)
        font.setPointSize(18)
        font.setUnderline(False)
        self.titleLabel2.setFont(font)
        self.titleLabel2.setObjectName("titleLabel2")

        self.usernameLabel = QtWidgets.QLabel(self.centralwidget)
        self.usernameLabel.setGeometry(QtCore.QRect(105, 210, 121, 31))
        self.usernameLabel.setPalette(palette)
        font.setPointSize(14)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setObjectName("usernameLabel")

        self.passwordLabel = QtWidgets.QLabel(self.centralwidget)
        self.passwordLabel.setGeometry(QtCore.QRect(105, 310, 151, 31))
        self.passwordLabel.setPalette(palette)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setObjectName("passwordLabel")

        self.borderLabel = QtWidgets.QLabel(self.centralwidget)
        self.borderLabel.setGeometry(QtCore.QRect(90, 200, 621, 211))
        self.borderLabel.setPalette(palette)
        self.borderLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.borderLabel.setLineWidth(2)
        self.borderLabel.setText("")
        self.borderLabel.setObjectName("borderLabel")

        #text input setup
        font.setPointSize(12)
        self.usernameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameInput.setGeometry(QtCore.QRect(100, 250, 601, 40))
        self.usernameInput.setFont(font)
        self.usernameInput.setAlignment(QtCore.Qt.AlignCenter)
        self.usernameInput.setObjectName("usernameInput")

        self.passwordInput = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordInput.setGeometry(QtCore.QRect(100, 350, 601, 40))
        self.passwordInput.setFont(font)
        self.passwordInput.setAlignment(QtCore.Qt.AlignCenter)
        self.passwordInput.setObjectName("passwordInput")
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)

        #button setup
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(180, 430, 200, 40))
        self.loginButton.setFont(font)
        self.loginButton.setAutoFillBackground(False)
        self.loginButton.setObjectName("loginButton")

        self.createUserButton = QtWidgets.QPushButton(self.centralwidget)
        self.createUserButton.setGeometry(QtCore.QRect(420, 430, 200, 40))
        self.createUserButton.setFont(font)
        self.createUserButton.setObjectName("pushButton")

        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(712, 540, 71, 41))
        self.exitButton.setFont(font)
        self.exitButton.setObjectName("exitButton")
        self.exitButton.setToolTip("Exit application and close database connection")

        self.setCentralWidget(self.centralwidget)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Password Manager"))
        self.loginButton.setText(_translate("LoginWindow", "LOGIN"))
        self.titleLabel.setText(_translate("LoginWindow", "Password Manager "))
        self.titleLabel2.setText(_translate("LoginWindow", "Created by Rizwan Ahsan"))
        self.usernameLabel.setText(_translate("LoginWindow", "Username:"))
        self.passwordLabel.setText(_translate("LoginWindow", "Password:"))
        self.createUserButton.setText(_translate("LoginWindow", "CREATE NEW USER"))
        self.exitButton.setText(_translate("DataWindow", "EXIT"))
        self.usernameInput.setPlaceholderText(_translate("LoginWindow", "Enter Username"))
        self.passwordInput.setPlaceholderText(_translate("LoginWindow", "Enter Password"))

        #button clicking action
        self.loginButton.clicked.connect(self.loginButtonAction)
        self.createUserButton.clicked.connect(self.openNewUserWindow)
        self.exitButton.clicked.connect(self.exitButtonAction)

    def exitButtonAction(self):
        self.db.conn.close()
        self.close()

    def loginButtonAction(self):
        self.username = self.usernameInput.text()
        self.password = self.passwordInput.text()

        if self.db.checkPass(self.username, self.password):
            self.openDataWindow()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Invalid Username or Password!")
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.exec_()

    def openNewUserWindow(self):
        self.newUserWindow = Ui_createUserWidget()
        self.newUserWindow.show()
        self.newUserWindow.createUserButton.clicked.connect(self.newUserButtonAction)

    def newUserButtonAction(self):
        msg = QtWidgets.QMessageBox()
        self.username = self.newUserWindow.newUserInput.text()
        self.db.cur.execute("SELECT COUNT(username) FROM info WHERE username = ?", (self.username,))
        record = self.db.cur.fetchone()[0]

        if record == 0 and self.username != "":
            self.db.storeUser(self.username)
            self.password = self.db.generateKey(self.username)
            msg.setWindowTitle("Information")
            msg.setText("The master key was stored in {}(key).txt\nStore it in a secure place!".format(self.username))
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.exec_()
            self.newUserWindow.hide()
            self.openDataWindow()
        elif self.username == "":
            msg.setWindowTitle("Error")
            msg.setText("Username Field Cannot be Empty!")
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.exec_()
        else:
            msg.setWindowTitle("Error")
            msg.setText("Username Already Exists!")
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.exec_()

    def openDataWindow(self):
        self.dataWindow = Ui_DataWindow()
        self.hide()
        self.dataWindow.show()
        self.dataWindow.username = self.username
        self.dataWindow.key = self.password
        self.dataWindow.addComboBoxItems()
        self.dataWindow.exitButton.clicked.connect(self.exitButtonAction)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = Ui_LoginWindow()
    LoginWindow.show()
    sys.exit(app.exec_())