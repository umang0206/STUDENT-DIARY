# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainpage.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from bresult import *
from indiresult import *
from mainpage11 import *

class Ui_mainpage2(object):
    def setupUi(self, mainpage2):
        mainpage2.setObjectName("mainpage2")
        mainpage2.resize(1366, 768)
        self.centralwidget = QtWidgets.QWidget(mainpage2)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1366, 721))
        self.label.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.B1 = QtWidgets.QPushButton(self.centralwidget)
        self.B1.setGeometry(QtCore.QRect(0, 0, 60, 21))
        self.B1.setStyleSheet("background-color: rgb(32, 74, 135);\n"
"color: rgb(255, 255, 255);")
        self.B1.setObjectName("B1")
        self.B2 = QtWidgets.QPushButton(self.centralwidget)
        self.B2.setGeometry(QtCore.QRect(58, 0, 60, 21))
        self.B2.setStyleSheet("")
        self.B2.setObjectName("B2")
        self.B3 = QtWidgets.QPushButton(self.centralwidget)
        self.B3.setGeometry(QtCore.QRect(20, 23, 121, 25))
        self.B3.setStyleSheet("background-color: rgb(32, 74, 135);\n"
"color: rgb(255, 255, 255);")
        self.B3.setFlat(False)
        self.B3.setObjectName("B3")
        self.B4 = QtWidgets.QPushButton(self.centralwidget)
        self.B4.setGeometry(QtCore.QRect(140, 35, 151, 25))
        self.B4.setIconSize(QtCore.QSize(22, 16))
        self.B4.setAutoDefault(False)
        self.B4.setDefault(False)
        self.B4.setFlat(False)
        self.B4.setObjectName("B4")
        self.B5 = QtWidgets.QPushButton(self.centralwidget)
        self.B5.setGeometry(QtCore.QRect(140, 60, 151, 25))
        self.B5.setIconSize(QtCore.QSize(22, 16))
        self.B5.setAutoDefault(False)
        self.B5.setDefault(False)
        self.B5.setFlat(False)
        self.B5.setObjectName("B5")
        mainpage2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainpage2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1366, 22))
        self.menubar.setObjectName("menubar")
        mainpage2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainpage2)
        self.statusbar.setObjectName("statusbar")
        mainpage2.setStatusBar(self.statusbar)

        self.retranslateUi(mainpage2)
        QtCore.QMetaObject.connectSlotsByName(mainpage2)

    def retranslateUi(self, mainpage2):
        _translate = QtCore.QCoreApplication.translate
        mainpage2.setWindowTitle(_translate("mainpage2", "Main Menu"))
        self.B1.setText(_translate("mainpage2", "USER"))
        self.B2.setText(_translate("mainpage2", "ADMIN"))
        self.B3.setText(_translate("mainpage2", "SHOW RESULT-->"))
        self.B4.setText(_translate("mainpage2", "BRANCH RESULT"))
        self.B5.setText(_translate("mainpage2", "INDIVIDUAL RESULT"))
        self.B2.clicked.connect(self.admin)
        self.B4.clicked.connect(self.branchresult2)
        self.B5.clicked.connect(self.indiresult)
        self.B2.clicked.connect(mainpage2.close)
    
    def branchresult2(self):
        self.page1 = QtWidgets.QMainWindow()
        self.ui = Ui_branchresult()
        self.ui.setupUi(self.page1)
        self.page1.show()

    def admin(self):
        self.page1 = QtWidgets.QMainWindow()
        self.ui = Ui_mainpage1()
        self.ui.setupUi(self.page1)
        self.page1.show()
    
    def indiresult(self):
        self.page1 = QtWidgets.QMainWindow()
        self.ui = Ui_indiresult()
        self.ui.setupUi(self.page1)
        self.page1.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainpage2 = QtWidgets.QMainWindow()
    ui = Ui_mainpage2()
    ui.setupUi(mainpage2)
    mainpage2.show()
    sys.exit(app.exec_())
