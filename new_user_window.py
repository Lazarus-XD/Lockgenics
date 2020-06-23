from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_createUserWidget():
    def setupUi(self, createUserWidget):
        createUserWidget.setObjectName("createUserWidget")
        createUserWidget.setFixedSize(412, 187)

        #background setup
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(135, 0, 202))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 0, 202))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        createUserWidget.setPalette(palette)

        #icon setup
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        createUserWidget.setWindowIcon(icon)

        #text white color setup
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)

        #font setup
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(14)

        self.label = QtWidgets.QLabel(createUserWidget)
        self.label.setGeometry(QtCore.QRect(160, 20, 101, 31))
        self.label.setPalette(palette)
        self.label.setFont(font)
        self.label.setObjectName("label")

        font.setFamily("Bahnschrift SemiLight SemiConde")
        font.setPointSize(12)
        self.newUserInput = QtWidgets.QLineEdit(createUserWidget)
        self.newUserInput.setGeometry(QtCore.QRect(30, 60, 351, 41))
        self.newUserInput.setFont(font)
        self.newUserInput.setAlignment(QtCore.Qt.AlignCenter)
        self.newUserInput.setObjectName("newUserInput")

        self.createUserButton = QtWidgets.QPushButton(createUserWidget)
        self.createUserButton.setGeometry(QtCore.QRect(140, 120, 131, 41))
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(12)
        self.createUserButton.setFont(font)
        self.createUserButton.setObjectName("createUserButton")

        self.retranslateUi(createUserWidget)
        QtCore.QMetaObject.connectSlotsByName(createUserWidget)

    def retranslateUi(self, createUserWidget):
        _translate = QtCore.QCoreApplication.translate
        createUserWidget.setWindowTitle(_translate("createUserWidget", "New User"))
        self.label.setText(_translate("createUserWidget", "Username:"))
        self.newUserInput.setPlaceholderText(_translate("createUserWidget", "Enter Username"))
        self.createUserButton.setText(_translate("createUserWidget", "CREATE USER"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     createUserWidget = QtWidgets.QWidget()
#     ui = Ui_createUserWidget()
#     ui.setupUi(createUserWidget)
#     createUserWidget.show()
#     sys.exit(app.exec_())