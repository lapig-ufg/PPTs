import sys
import os
import platform
import webbrowser

from PyQt5 import QtGui, QtPrintSupport , QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication

def system_os():
	if platform.system() == 'Windows':
		return 1
	else:
		return 2

if system_os() == 1:
	backslh = '\\'

else:
	backslh = '/'


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class Ui_LoginWindow(object):
    
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.setWindowModality(QtCore.Qt.NonModal)
        LoginWindow.setEnabled(True)
        LoginWindow.resize(357, 161)
        icon = QtGui.QIcon()
        icon_location =  str(os.getcwd())+backslh+'EXE'+backslh+'GPM_PY_EXE'+backslh+'avatar.ico'
        icon.addPixmap(QtGui.QPixmap(icon_location), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LoginWindow.setWindowIcon(icon)
        LoginWindow.setModal(False)

        self.InfoMessage = QtWidgets.QLabel(LoginWindow)
        self.InfoMessage.setGeometry(QtCore.QRect(20, 10, 293, 20))
        self.InfoMessage.setObjectName("InfoMessage")

        self.LoginLine = QtWidgets.QLineEdit(LoginWindow)
        self.LoginLine.setGeometry(QtCore.QRect(80, 40, 231, 20))
        self.LoginLine.setObjectName("LoginLine")

        self.PasswordLine = QtWidgets.QLineEdit(LoginWindow)
        self.PasswordLine.setGeometry(QtCore.QRect(80, 70, 231, 20))
        self.PasswordLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PasswordLine.setObjectName("PasswordLine")
        
        self.buttonBox = QtWidgets.QDialogButtonBox(LoginWindow)
        self.buttonBox.setGeometry(QtCore.QRect(110, 100, 151, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.LoginMessage = QtWidgets.QLabel(LoginWindow)
        self.LoginMessage.setGeometry(QtCore.QRect(20, 40, 61, 20))
        self.LoginMessage.setObjectName("LoginMessage")

        self.PasswordMessage = QtWidgets.QLabel(LoginWindow)
        self.PasswordMessage.setGeometry(QtCore.QRect(20, 70, 61, 20))
        self.PasswordMessage.setObjectName("PasswordMessage")

        self.label = QtWidgets.QLabel(LoginWindow)
        self.label.setGeometry(QtCore.QRect(20, 140, 228, 21))
        self.label.setObjectName("RegisterPhrase")
        
        self.ClickHere = QtWidgets.QPushButton(LoginWindow)
        self.ClickHere.setGeometry(QtCore.QRect(234, 140, 61, 20))
        self.ClickHere.setObjectName("ClickHere")
        self.ClickHere.setStyleSheet("background-color: #2b90f5")
        self.ClickHere.clicked.connect(self.GoRegister)


        self.retranslateUi(LoginWindow)
        self.buttonBox.accepted.connect(LoginWindow.accept)
        self.buttonBox.rejected.connect(LoginWindow.reject)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)
        LoginWindow.setTabOrder(self.LoginLine, self.PasswordLine)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "NASA EarthData Login"))
        self.InfoMessage.setText(_translate("LoginWindow", "Please insert your NASA EarthData Username and Password:"))
        self.LoginMessage.setText(_translate("LoginWindow", "Username:"))
        self.PasswordMessage.setText(_translate("LoginWindow", "Password:"))
        self.label.setText(_translate("LoginWindow", "If you don\'t have an account or can\'t sing in"))
        self.ClickHere.setText(_translate("LoginWindow", "Click Here!"))

    def GoRegister(self):
        #https://urs.earthdata.nasa.gov/approve_app?client_id=e2WVk8Pw6weeLUKZYOxvTQ
        #return webbrowser.open('https://urs.earthdata.nasa.gov/')
        return webbrowser.open('https://urs.earthdata.nasa.gov/approve_app?client_id=e2WVk8Pw6weeLUKZYOxvTQ')

def retrieveLogin():
	app = QtWidgets.QApplication(sys.argv)
	LoginWindow = QtWidgets.QDialog()
	ex = Ui_LoginWindow()
	ex.setupUi(LoginWindow)
	LoginWindow.show()
	result = LoginWindow.exec_()
	
	if result == 1:
		text = (ex.LoginLine.text(),ex.PasswordLine.text())
		#print("Login in NASA HTTPS successful")
		return map(str,text)
	else:
		return None
	#sys.exit(app.exec_())