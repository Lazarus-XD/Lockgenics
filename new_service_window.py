from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

class Ui_newServiceWidget(QMainWindow):
    def __init__(self):
        super(Ui_newServiceWidget, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("newServiceWidget")
        self.setFixedSize(646, 409)

        # background setup
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(135, 0, 202))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 0, 202))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        self.setPalette(palette)

        # icon setup
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

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
        font.setKerning(True)
        self.setFont(font)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(50, 40, 81, 31))
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setPalette(palette)

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(50, 170, 101, 31))
        self.label_2.setPalette(palette)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.confirmButton = QtWidgets.QPushButton(self)
        font.setPointSize(13)
        self.confirmButton.setFont(font)
        self.confirmButton.setGeometry(QtCore.QRect(130, 300, 151, 41))
        self.confirmButton.setObjectName("pushButton")

        self.genPassButton = QtWidgets.QPushButton(self)
        self.genPassButton.setFont(font)
        self.genPassButton.setGeometry(QtCore.QRect(350, 300, 201, 41))
        self.genPassButton.setObjectName("pushButton_2")

        self.serviceInput = QtWidgets.QLineEdit(self)
        self.serviceInput.setGeometry(QtCore.QRect(40, 80, 571, 41))
        font.setFamily("Bahnschrift SemiLight SemiConde")
        self.serviceInput.setFont(font)
        self.serviceInput.setAlignment(QtCore.Qt.AlignCenter)
        self.serviceInput.setObjectName("lineEdit")

        self.passwordInput = QtWidgets.QLineEdit(self)
        self.passwordInput.setGeometry(QtCore.QRect(40, 210, 571, 41))
        self.passwordInput.setFont(font)
        self.passwordInput.setAlignment(QtCore.Qt.AlignCenter)
        self.passwordInput.setObjectName("lineEdit_2")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, newServiceWidget):
        _translate = QtCore.QCoreApplication.translate
        newServiceWidget.setWindowTitle(_translate("newServiceWidget", "New Service"))
        self.label.setText(_translate("newServiceWidget", "Service:"))
        self.label_2.setText(_translate("newServiceWidget", "Password:"))
        self.serviceInput.setPlaceholderText(_translate("newServiceWidget", "Enter New Service Name"))
        self.passwordInput.setPlaceholderText(_translate("newServiceWidget", "Enter or Generate Password"))
        self.confirmButton.setText(_translate("newServiceWidget", "Confirm"))
        self.genPassButton.setText(_translate("newServiceWidget", "Generate Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    newServiceWindow = Ui_newServiceWidget()
    newServiceWindow.show()
    sys.exit(app.exec_())