# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'check.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from message import *
from mainpage import *
import mysql.connector 


class Ui_check(object):
    def setupUi(self, check):
        check.setObjectName("check")
        check.resize(568, 216)
        self.centralwidget = QtWidgets.QWidget(check)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 571, 181))
        self.label.setStyleSheet("background-color: rgb(29, 126, 253);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 521, 51))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.B1 = QtWidgets.QPushButton(self.centralwidget)
        self.B1.setGeometry(QtCore.QRect(20, 130, 89, 25))
        self.B1.setStyleSheet("background-color: rgb(255, 91, 44);")
        self.B1.setObjectName("B1")
        self.B2 = QtWidgets.QPushButton(self.centralwidget)
        self.B2.setGeometry(QtCore.QRect(380, 130, 141, 25))
        self.B2.setStyleSheet("background-color: rgb(255, 91, 44);")
        self.B2.setObjectName("B2")
        check.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(check)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 568, 22))
        self.menubar.setObjectName("menubar")
        check.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(check)
        self.statusbar.setObjectName("statusbar")
        check.setStatusBar(self.statusbar)

        self.retranslateUi(check)
        QtCore.QMetaObject.connectSlotsByName(check)

    def retranslateUi(self, check):
        _translate = QtCore.QCoreApplication.translate
        check.setWindowTitle(_translate("check", "ALERT"))
        self.label_2.setText(_translate("check", "   IF YOU ARE USING FIRST TIME  THEN PLEASE INSTALL DATABASE SYSTEM"))
        self.B1.setText(_translate("check", "INSTALL"))
        self.B2.setText(_translate("check", "ALLREADY INSTALL"))
        self.B1.clicked.connect(self.install)
        self.B2.clicked.connect(self.allready)
        self.B2.clicked.connect(check.close)
        self.B1.clicked.connect(check.close)

    
    
    def install(self):
        a,b,c,d=0,0,0,0
        mydb1=mysql.connector.connect(host="localhost",user="root",password="")
        mycursor1=mydb1.cursor()
        mycursor1.execute("SHOW DATABASES")
        myre1=mycursor1.fetchall()
        for i in myre1:
            if i[0]=="clg3":
                c+=1
        
        if c==0:
            mycursor1.execute("CREATE DATABASE clg3")


        mydb2=mysql.connector.connect(host="localhost",user="root",password="",database="clg3")
        mycursor2=mydb2.cursor()
        mycursor2.execute("SHOW TABLES")
        myre2=mycursor2.fetchall()
        for i in myre2:
            if i[0]=="A" :
                a+=1
            if i[0]=="B" :
                b+=1
            if i[0]=="D":
                d+=1
            
        

        if a==0:
            s="CREATE TABLE A(roll varchar(15), name varchar(200))"
            mycursor2.execute(s)
            
        
        if b==0:
            s="CREATE TABLE B(roll varchar(15), name varchar(200))"
            mycursor2.execute(s)
            
        if d==0:
            s="CREATE TABLE D(roll varchar(15), name varchar(200))"
            mycursor2.execute(s)
        
        
        self.chec = QtWidgets.QMainWindow()
        self.ui = Ui_notice()
        self.ui.setupUi(self.chec)
        self.chec.show()

        
        

    def allready(self):
        self.chec = QtWidgets.QMainWindow()
        self.ui = Ui_mainpage()
        self.ui.setupUi(self.chec)
        self.chec.show()
        





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    check = QtWidgets.QMainWindow()
    ui = Ui_check()
    ui.setupUi(check)
    check.show()
    sys.exit(app.exec_())
