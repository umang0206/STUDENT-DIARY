# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginpage.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from regispage import *

class Ui_loginpage(object):
    def __init__(self):
        self.id=["rupesh","mayank","umang"]
        self.pas=["ru123","ma123","um123"]
    def setupUi(self, loginpage):
        loginpage.setObjectName("loginpage")
        loginpage.resize(500, 494)
        self.centralwidget = QtWidgets.QWidget(loginpage)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 500, 450))
        self.label_2.setStyleSheet("background-color: rgb(245, 113, 188);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(85, 149, 135, 17))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(85, 200, 135, 17))
        self.label_3.setObjectName("label_3")
        self.T1 = QtWidgets.QLineEdit(self.centralwidget)
        self.T1.setGeometry(QtCore.QRect(231, 144, 200, 30))
        self.T1.setObjectName("T1")
        self.T2 = QtWidgets.QLineEdit(self.centralwidget)
        self.T2.setGeometry(QtCore.QRect(231, 196, 200, 30))
        self.T2.setObjectName("T2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 260, 89, 25))
        self.pushButton.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.pushButton.setObjectName("pushButton")
        self.T3 = QtWidgets.QLineEdit(self.centralwidget)
        self.T3.setGeometry(QtCore.QRect(100, 350, 321, 25))
        self.T3.setStyleSheet("background-color: rgb(245, 113, 188);")
        self.T3.setFrame(False)
        self.T3.setAlignment(QtCore.Qt.AlignCenter)
        self.T3.setObjectName("T3")
        loginpage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(loginpage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 22))
        self.menubar.setObjectName("menubar")
        loginpage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(loginpage)
        self.statusbar.setObjectName("statusbar")
        loginpage.setStatusBar(self.statusbar)

        self.retranslateUi(loginpage)
        QtCore.QMetaObject.connectSlotsByName(loginpage)

    def retranslateUi(self, loginpage):
        _translate = QtCore.QCoreApplication.translate
        loginpage.setWindowTitle(_translate("loginpage", "Login PAGE"))
        self.label.setText(_translate("loginpage", "ENTER USER NAME"))
        self.label_3.setText(_translate("loginpage", "ENTER PASSWORD"))
        self.pushButton.setText(_translate("loginpage", "SUBMIT"))
        self.pushButton.clicked.connect(self.submit)


    def submit(self):
        n1=str(self.T1.text())
        n2=str(self.T2.text())
        c=0
        for i in range(0,len(self.id)):
            if(self.id[i]==n1) and (self.pas[i]==n2):
                c+=1
        if c>0:
            self.page = QtWidgets.QMainWindow()
            self.ui = Ui_studentdetail()
            self.ui.setupUi(self.page)
            self.page.show()
        else:
            self.T3.setText("your id or password incorrect")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    loginpage = QtWidgets.QMainWindow()
    ui = Ui_loginpage()
    ui.setupUi(loginpage)
    loginpage.show()
    sys.exit(app.exec_())
