from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DataWindow(object):
    def setupUi(self, DataWindow):
        DataWindow.setObjectName("DataWindow")
        DataWindow.setFixedSize(800, 600)

        #background setup
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(106, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        DataWindow.setPalette(palette)

        #font setup
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight SemiConde")
        font.setPointSize(14)
        DataWindow.setFont(font)

        #icon setup
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DataWindow.setWindowIcon(icon)

        #text white color setup
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)

        self.centralwidget = QtWidgets.QWidget(DataWindow)
        self.centralwidget.setObjectName("centralwidget")

        # line edit boxes setup
        self.usernameEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameEdit.setGeometry(QtCore.QRect(50, 135, 701, 41))
        self.usernameEdit.setFont(font)
        self.usernameEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.usernameEdit.setReadOnly(True)
        self.usernameEdit.setObjectName("usernameEdit")

        self.passwordEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordEdit.setGeometry(QtCore.QRect(50, 255, 701, 41))
        self.passwordEdit.setFont(font)
        self.passwordEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.passwordEdit.setObjectName("passwordEdit")

        self.emailEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.emailEdit.setGeometry(QtCore.QRect(50, 375, 701, 41))
        self.emailEdit.setFont(font)
        self.emailEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.emailEdit.setObjectName("emailEdit")

        self.urlEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.urlEdit.setGeometry(QtCore.QRect(50, 495, 701, 41))
        self.urlEdit.setFont(font)
        self.urlEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.urlEdit.setObjectName("urlEdit")

        #label setup
        font.setFamily("Bahnschrift SemiBold SemiConden")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 20, 91, 41))
        self.label.setPalette(palette)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 90, 111, 31))
        self.label_2.setPalette(palette)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 210, 101, 31))
        self.label_3.setPalette(palette)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 330, 61, 31))
        self.label_4.setPalette(palette)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 450, 51, 31))
        self.label_5.setPalette(palette)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        #button setup
        font.setPointSize(12)
        self.addServiceButton = QtWidgets.QPushButton(self.centralwidget)
        self.addServiceButton.setGeometry(QtCore.QRect(50, 20, 161, 41))
        self.addServiceButton.setFont(font)
        self.addServiceButton.setObjectName("addServiceButton")

        self.editButton = QtWidgets.QPushButton(self.centralwidget)
        self.editButton.setGeometry(QtCore.QRect(630, 20, 125, 41))
        self.editButton.setFont(font)
        self.editButton.setObjectName("editButton")

        #combo box setup
        self.servicesComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.servicesComboBox.setGeometry(QtCore.QRect(380, 20, 181, 41))
        font.setWeight(50)
        self.servicesComboBox.setFont(font)
        self.servicesComboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.servicesComboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.servicesComboBox.setObjectName("servicesComboBox")
        self.servicesComboBox.addItem("")

        DataWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(DataWindow)
        QtCore.QMetaObject.connectSlotsByName(DataWindow)

    def retranslateUi(self, DataWindow):
        _translate = QtCore.QCoreApplication.translate
        DataWindow.setWindowTitle(_translate("DataWindow", "Password Manager"))
        self.addServiceButton.setText(_translate("DataWindow", "Add New Service"))
        self.servicesComboBox.setItemText(0, _translate("DataWindow", "facebook"))
        self.label.setText(_translate("DataWindow", "Services:"))
        self.label_2.setText(_translate("DataWindow", "Username:"))
        self.label_3.setText(_translate("DataWindow", "Password:"))
        self.label_4.setText(_translate("DataWindow", "Email:"))
        self.label_5.setText(_translate("DataWindow", "URL:"))
        self.editButton.setText(_translate("DataWindow", "Edit"))
        self.usernameEdit.setText(_translate("DataWindow", "RizwanAhsan"))
        self.usernameEdit.setPlaceholderText(_translate("DataWindow", "Enter Username"))
        self.passwordEdit.setPlaceholderText(_translate("DataWindow", "Enter Password"))
        self.emailEdit.setPlaceholderText(_translate("DataWindow", "Enter Email Address"))
        self.urlEdit.setPlaceholderText(_translate("DataWindow", "Enter URL of Service"))


# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     DataWindow = QtWidgets.QMainWindow()
#     ui = Ui_DataWindow()
#     ui.setupUi(DataWindow)
#     DataWindow.show()
#     sys.exit(app.exec_())