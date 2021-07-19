# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainpage.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from loginpage import *
from mainpage import *
from eloginpage import *
from mainpage2 import *

class Ui_mainpage1(object):
    def setupUi(self, mainpage1):
        mainpage1.setObjectName("mainpage1")
        mainpage1.resize(1366, 768)
        self.centralwidget = QtWidgets.QWidget(mainpage1)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1366, 768))
        self.label.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.B1 = QtWidgets.QPushButton(self.centralwidget)
        self.B1.setGeometry(QtCore.QRect(0, 0, 60, 21))
        self.B1.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.B1.setObjectName("B1")
        self.B2 = QtWidgets.QPushButton(self.centralwidget)
        self.B2.setGeometry(QtCore.QRect(58, 0, 60, 21))
        self.B2.setStyleSheet("background-color: rgb(32, 74, 135);\n"
"color: rgb(255, 255, 255);")
        self.B2.setObjectName("B2")
        self.B3 = QtWidgets.QPushButton(self.centralwidget)
        self.B3.setGeometry(QtCore.QRect(76, 21, 70, 25))
        self.B3.setStyleSheet("background-color: rgb(32, 74, 135);\n"
"color: rgb(255, 255, 255);")
        self.B3.setObjectName("B3")
        self.B4 = QtWidgets.QPushButton(self.centralwidget)
        self.B4.setGeometry(QtCore.QRect(76, 46, 70, 25))
        self.B4.setObjectName("B4")
        mainpage1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainpage1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1366, 22))
        self.menubar.setObjectName("menubar")
        mainpage1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainpage1)
        self.statusbar.setObjectName("statusbar")
        mainpage1.setStatusBar(self.statusbar)

        self.retranslateUi(mainpage1)
        QtCore.QMetaObject.connectSlotsByName(mainpage1)

    def retranslateUi(self, mainpage1):
        _translate = QtCore.QCoreApplication.translate
        mainpage1.setWindowTitle(_translate("mainpage1", "Main Menu"))
        self.B1.setText(_translate("mainpage1", "USER"))
        self.B2.setText(_translate("mainpage1", "ADMIN"))
        self.B3.setText(_translate("mainpage1", "Login"))
        self.B4.setText(_translate("mainpage1", "Edit"))
        self.B3.clicked.connect(self.login)
        self.B4.clicked.connect(self.edit)
        self.B1.clicked.connect(self.user)
        self.B1.clicked.connect(mainpage1.close)



    def login(self):
        self.page1 = QtWidgets.QMainWindow()
        self.ui = Ui_loginpage()
        self.ui.setupUi(self.page1)
        self.page1.show()
    def user(self):
        self.page1 = QtWidgets.QMainWindow()
        self.ui = Ui_mainpage2()
        self.ui.setupUi(self.page1)
        self.page1.show()
    def edit(self):
        self.page1 = QtWidgets.QMainWindow()
        self.ui = Ui_Eloginpage()
        self.ui.setupUi(self.page1)
        self.page1.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainpage1 = QtWidgets.QMainWindow()
    ui = Ui_mainpage1()
    ui.setupUi(mainpage1)
    mainpage1.show()
    sys.exit(app.exec_())
