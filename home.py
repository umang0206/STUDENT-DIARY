# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from mainpage import *
import mysql.connector 
class Ui_strat(object):
    def setupUi(self, strat):
        strat.setObjectName("strat")
        strat.resize(630, 461)
        self.centralwidget = QtWidgets.QWidget(strat)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 630, 421))
        self.label.setStyleSheet("background-color: rgb(253, 250, 142);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 140, 181, 51))
        self.label_2.setStyleSheet("font: 75 italic 21pt \"System-ui\";\n"
"color: rgb(255, 91, 44);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.B1 = QtWidgets.QPushButton(self.centralwidget)
        self.B1.setGeometry(QtCore.QRect(480, 340, 89, 25))
        self.B1.setStyleSheet("background-color: rgb(138, 226, 52);\n"
"color: rgb(0, 0, 0);")
        self.B1.setObjectName("B1")
        strat.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(strat)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 630, 22))
        self.menubar.setObjectName("menubar")
        strat.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(strat)
        self.statusbar.setObjectName("statusbar")
        strat.setStatusBar(self.statusbar)

        self.retranslateUi(strat)
        QtCore.QMetaObject.connectSlotsByName(strat)

    def retranslateUi(self, strat):
        _translate = QtCore.QCoreApplication.translate
        strat.setWindowTitle(_translate("strat", "HOME PAGE"))
        self.label_2.setText(_translate("strat", "WELL-COME"))
        self.B1.setText(_translate("strat", "START....."))
        self.B1.clicked.connect(self.install)
        self.B1.clicked.connect(strat.close)
    
    
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
        self.ui = Ui_mainpage()
        self.ui.setupUi(self.chec)
        self.chec.show()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    strat = QtWidgets.QMainWindow()
    ui = Ui_strat()
    ui.setupUi(strat)
    strat.show()
    sys.exit(app.exec_())
