import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("Login")
        LoginWindow.setFixedSize(800, 600)

        #Background setup
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(106, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        LoginWindow.setPalette(palette)

        #text white color setup
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)

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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())