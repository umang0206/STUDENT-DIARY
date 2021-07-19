# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainpage.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from mainpage11 import *
from mainpage2 import *

class Ui_mainpage(object):
    def setupUi(self, mainpage):
        mainpage.setObjectName("mainpage")
        mainpage.resize(1366, 768)
        self.centralwidget = QtWidgets.QWidget(mainpage)
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
        self.B2.setObjectName("B2")
        mainpage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainpage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1366, 22))
        self.menubar.setObjectName("menubar")
        mainpage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainpage)
        self.statusbar.setObjectName("statusbar")
        mainpage.setStatusBar(self.statusbar)

        self.retranslateUi(mainpage)
        QtCore.QMetaObject.connectSlotsByName(mainpage)

    def retranslateUi(self, mainpage):
        _translate = QtCore.QCoreApplication.translate
        mainpage.setWindowTitle(_translate("mainpage", "Main Menu"))
        self.B1.setText(_translate("mainpage", "USER"))
        self.B2.setText(_translate("mainpage", "ADMIN"))
        self.B2.clicked.connect(self.admin1)
        self.B2.clicked.connect(mainpage.close)
        self.B1.clicked.connect(self.user)
        self.B1.clicked.connect(mainpage.close)

    def admin1(self):
        self.page = QtWidgets.QMainWindow()
        self.ui = Ui_mainpage1()
        self.ui.setupUi(self.page)
        self.page.show()
    
    def user(self):
        self.page = QtWidgets.QMainWindow()
        self.ui = Ui_mainpage2()
        self.ui.setupUi(self.page)
        self.page.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainpage = QtWidgets.QMainWindow()
    ui = Ui_mainpage()
    ui.setupUi(mainpage)
    mainpage.show()
    sys.exit(app.exec_())
