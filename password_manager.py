import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from data_window import Ui_DataWindow
from new_user_window import Ui_createUserWidget
from database import *

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("Login")
        LoginWindow.setFixedSize(800, 600)

        #background setup
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(106, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        LoginWindow.setPalette(palette)

        #text white color setup
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)

        #icon setup
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LoginWindow.setWindowIcon(icon)

        #font setup
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")

        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")

        #label setup
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(218, 30, 371, 61))
        self.titleLabel.setPalette(palette)
        font.setPointSize(30)
        font.setBold(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName("titleLabel")

        self.titleLabel2 = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel2.setGeometry(QtCore.QRect(255, 90, 301, 61))
        self.titleLabel2.setPalette(palette)
        font.setPointSize(18)
        font.setBold(True)
        self.titleLabel2.setFont(font)
        self.titleLabel2.setObjectName("titleLabel2")

        self.usernameLabel = QtWidgets.QLabel(self.centralwidget)
        self.usernameLabel.setGeometry(QtCore.QRect(155, 210, 121, 31))
        self.usernameLabel.setPalette(palette)
        font.setPointSize(14)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setObjectName("usernameLabel")

        self.passwordLabel = QtWidgets.QLabel(self.centralwidget)
        self.passwordLabel.setGeometry(QtCore.QRect(155, 310, 151, 31))
        self.passwordLabel.setPalette(palette)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setObjectName("passwordLabel")

        self.borderLabel = QtWidgets.QLabel(self.centralwidget)
        self.borderLabel.setGeometry(QtCore.QRect(140, 200, 521, 211))
        self.borderLabel.setPalette(palette)
        self.borderLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.borderLabel.setLineWidth(2)
        self.borderLabel.setText("")
        self.borderLabel.setObjectName("borderLabel")

        #text input setup
        font.setPointSize(12)
        self.usernameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameInput.setGeometry(QtCore.QRect(150, 250, 500, 40))
        self.usernameInput.setFont(font)
        self.usernameInput.setAlignment(QtCore.Qt.AlignCenter)
        self.usernameInput.setObjectName("usernameInput")

        self.passwordInput = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordInput.setGeometry(QtCore.QRect(150, 350, 500, 40))
        self.passwordInput.setFont(font)
        self.passwordInput.setInputMethodHints(QtCore.Qt.ImhNone)
        self.passwordInput.setCursorPosition(0)
        self.passwordInput.setAlignment(QtCore.Qt.AlignCenter)
        self.passwordInput.setPlaceholderText("")
        self.passwordInput.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.passwordInput.setClearButtonEnabled(False)
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

        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Password Manager"))
        self.loginButton.setText(_translate("LoginWindow", "LOGIN"))
        self.titleLabel.setText(_translate("LoginWindow", "Password Manager "))
        self.titleLabel2.setText(_translate("LoginWindow", "Created by Rizwan Ahsan"))
        self.usernameLabel.setText(_translate("LoginWindow", "Username:"))
        self.passwordLabel.setText(_translate("LoginWindow", "Password:"))
        self.createUserButton.setText(_translate("LoginWindow", "CREATE NEW USER"))
        self.usernameInput.setPlaceholderText(_translate("LoginWindow", "Enter Username"))
        self.passwordInput.setPlaceholderText(_translate("LoginWindow", "Enter Password"))

        self.loginButton.clicked.connect(self.loginButtonAction)
        self.createUserButton.clicked.connect(self.openNewUserWindow)

    def loginButtonAction(self):
        username = self.usernameInput.text()
        password = self.passwordInput.text()
        if db.checkPass(username, password):
            self.openDataWindow()

    def openNewUserWindow(self):
        self.newUserWindow = QtWidgets.QMainWindow()
        self.newUserUI = Ui_createUserWidget()
        self.newUserUI.setupUi(self.newUserWindow)
        self.newUserWindow.show()
        self.newUserUI.createUserButton.clicked.connect(self.newUserButtonAction)

    def newUserButtonAction(self):
        msg = QtWidgets.QMessageBox()
        username = self.newUserUI.newUserInput.text()
        db.cur.execute("SELECT COUNT(username) FROM info WHERE username = ?", (username,))
        record = db.cur.fetchone()[0]
        if record == 0 and username != "":
            db.storeUser(username)
            key = db.generateKey(username)
            msg.setWindowTitle("Information")
            msg.setText("The master key was stored in {}(key).txt\nStore it in a secure place!".format(username))
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.exec_()
            self.newUserWindow.hide()
            self.openDataWindow()
        elif username == "":
            msg.setWindowTitle("Error")
            msg.setText("Enter A Valid Username!")
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.exec_()
        else:
            msg.setWindowTitle("Error")
            msg.setText("Username Already Exists!")
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.exec_()

    def openDataWindow(self):
        self.dataWindow = QtWidgets.QMainWindow()
        self.dataWindowUI = Ui_DataWindow()
        self.dataWindowUI.setupUi(self.dataWindow)
        LoginWindow.hide()
        self.dataWindow.show()


if __name__ == "__main__":
    db = Database()
    db.createTable()
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())