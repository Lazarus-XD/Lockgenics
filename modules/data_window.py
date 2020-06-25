from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from modules.database import *
from modules.new_service_window import Ui_newServiceWidget


class Ui_DataWindow(QMainWindow):
    def __init__(self):
        super(Ui_DataWindow, self).__init__()
        self.setupUi()
        self.db = Database()
        self.columns = [i[1] for i in self.db.cur.execute("PRAGMA table_info(info)")]
        self.counter = 0
        self.username = None
        self.key = None

    def setupUi(self):
        self.setObjectName("DataWindow")
        self.setFixedSize(800, 600)

        #background setup
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(106, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        self.setPalette(palette)

        #font setup
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(13)
        self.setFont(font)

        #icon setup
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("modules/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        #text white color setup
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        # line edit boxes setup
        self.usernameEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameEdit.setGeometry(QtCore.QRect(50, 135, 701, 41))
        self.usernameEdit.setFont(font)
        self.usernameEdit.setAlignment(QtCore.Qt.AlignCenter)
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

        self.usernameEdit.setReadOnly(True)
        self.passwordEdit.setReadOnly(True)
        self.emailEdit.setReadOnly(True)
        self.urlEdit.setReadOnly(True)

        #label setup
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 20, 91, 41))
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
        self.editButton.setGeometry(QtCore.QRect(530, 20, 125, 41))
        self.editButton.setFont(font)
        self.editButton.setObjectName("editButton")
        self.editButton.setToolTip("Edit service information")

        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(690, 20, 61, 41))
        self.exitButton.setFont(font)
        self.exitButton.setObjectName("exitButton")
        self.exitButton.setToolTip("Exit application and close database connection")

        #combo box setup
        self.servicesComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.servicesComboBox.setGeometry(QtCore.QRect(320, 20, 181, 41))
        font.setWeight(50)
        self.servicesComboBox.setFont(font)
        self.servicesComboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.servicesComboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.servicesComboBox.setObjectName("servicesComboBox")
        # self.servicesComboBox.addItem("")

        self.setCentralWidget(self.centralwidget)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def addComboBoxItems(self):
        self.db.cur.execute("SELECT * FROM info WHERE username = ?", (self.username,))
        record = self.db.cur.fetchall()
        f = Fernet(self.key)

        for row in record:
            for data in range(len(row)-2):
                try:
                    if type(f.decrypt(row[data+2].encode("utf-8")).decode("utf-8")) == str:
                        item = self.columns[data+2]
                        item = item.split("_")
                        item = " ".join(item)
                        self.servicesComboBox.addItem(item)
                except AttributeError:
                    continue

    def retranslateUi(self, DataWindow):
        _translate = QtCore.QCoreApplication.translate
        DataWindow.setWindowTitle(_translate("DataWindow", "Password Manager"))
        self.addServiceButton.setText(_translate("DataWindow", "Add New Service"))
        # self.servicesComboBox.setItemText(0, _translate("DataWindow", "facebook"))
        self.label.setText(_translate("DataWindow", "Services:"))
        self.label_2.setText(_translate("DataWindow", "Username:"))
        self.label_3.setText(_translate("DataWindow", "Password:"))
        self.label_4.setText(_translate("DataWindow", "Email:"))
        self.label_5.setText(_translate("DataWindow", "URL:"))
        self.editButton.setText(_translate("DataWindow", "Edit"))
        self.exitButton.setText(_translate("DataWindow", "Exit"))
        self.usernameEdit.setText(_translate("DataWindow", "RizwanAhsan"))
        self.usernameEdit.setPlaceholderText(_translate("DataWindow", "Enter Username"))
        self.passwordEdit.setPlaceholderText(_translate("DataWindow", "Enter Password"))
        self.emailEdit.setPlaceholderText(_translate("DataWindow", "Enter Email Address"))
        self.urlEdit.setPlaceholderText(_translate("DataWindow", "Enter URL of Service"))

        #button clicking action
        self.editButton.clicked.connect(self.editButtonAction)
        self.addServiceButton.clicked.connect(self.addServiceButtonAction)
        self.exitButton.clicked.connect(self.close)

    def editButtonAction(self):
        _translate = QtCore.QCoreApplication.translate
        self.counter += 1

        def setReadyOnly():
            self.usernameEdit.setReadOnly(True)
            self.passwordEdit.setReadOnly(True)
            self.emailEdit.setReadOnly(True)
            self.urlEdit.setReadOnly(True)

        def setEdit():
            self.usernameEdit.setReadOnly(False)
            self.passwordEdit.setReadOnly(False)
            self.emailEdit.setReadOnly(False)
            self.urlEdit.setReadOnly(False)

        if self.counter % 2 == 0:
            self.editButton.setText(_translate("DataWindow", "Edit"))
            setReadyOnly()
        else:
            self.editButton.setText(_translate("DataWindow", "Save Changes"))
            setEdit()

    def addServiceButtonAction(self):
        self.newServiceWindow = Ui_newServiceWidget()
        self.newServiceWindow.show()
        self.newServiceWindow.confirmButton.clicked.connect(self.confirmButtonAction)
        self.newServiceWindow.genPassButton.clicked.connect(self.genPassButtonAction)

    def confirmButtonAction(self):
        msg = QtWidgets.QMessageBox()
        service1 = self.newServiceWindow.serviceInput.text().lower()
        service = service1.split()
        service = "_".join(service)
        password = self.newServiceWindow.passwordInput.text()

        if service not in self.columns:
            self.db.cur.execute("ALTER TABLE info ADD COLUMN '{}' TEXT".format(service))
            self.db.conn.commit()

        self.db.cur.execute("SELECT COUNT({}) FROM info WHERE username = ?".format(service), (self.username,))
        record = self.db.cur.fetchone()[0]

        if service1 == "" or password == "":
            msg.setWindowTitle("Error")
            msg.setText("Service or Password Field Cannot be Empty!")
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.exec_()
        elif record != 0:
            msg.setWindowTitle("Error")
            msg.setText("Cannot Have Duplicate Service!")
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.exec_()
        else:
            self.db.addServiceAndPass(service, self.username, password, self.key)
            self.newServiceWindow.hide()
            self.servicesComboBox.addItem(service)
            index = self.servicesComboBox.findText(service, QtCore.Qt.MatchFixedString)
            self.servicesComboBox.setCurrentIndex(index)

    def genPassButtonAction(self):
        _translate = QtCore.QCoreApplication.translate
        Pass = self.db.generatePass(self.key)[1]
        self.newServiceWindow.passwordInput.setText(_translate("newServiceWidget", "{}".format(Pass)))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DataWindow = Ui_DataWindow()
    DataWindow.show()
    sys.exit(app.exec_())