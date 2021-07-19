# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'result.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from  branchresult import *

class Ui_branchresult(object):
    def setupUi(self, branchresult):
        branchresult.setObjectName("branchresult")
        branchresult.resize(471, 421)
        self.centralwidget = QtWidgets.QWidget(branchresult)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 471, 381))
        self.label.setStyleSheet("background-color: rgb(254, 89, 89);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 120, 67, 17))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 130, 161, 17))
        self.label_3.setObjectName("label_3")
        self.CM1 = QtWidgets.QComboBox(self.centralwidget)
        self.CM1.setGeometry(QtCore.QRect(230, 125, 121, 25))
        self.CM1.setObjectName("CM1")
        self.CM1.addItem("")
        self.CM1.addItem("CIVIL")
        self.CM1.addItem("CSE")
        self.CM1.addItem("IT")
        self.CM1.addItem("MECHA")
        self.CM1.addItem("META")
        self.B1 = QtWidgets.QPushButton(self.centralwidget)
        self.B1.setGeometry(QtCore.QRect(200, 180, 91, 25))
        self.B1.setObjectName("B1")
        branchresult.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(branchresult)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 471, 22))
        self.menubar.setObjectName("menubar")
        branchresult.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(branchresult)
        self.statusbar.setObjectName("statusbar")
        branchresult.setStatusBar(self.statusbar)

        self.retranslateUi(branchresult)
        QtCore.QMetaObject.connectSlotsByName(branchresult)

    def retranslateUi(self, branchresult):
        _translate = QtCore.QCoreApplication.translate
        branchresult.setWindowTitle(_translate("branchresult", "BRANCH RESULT PAGE"))
        self.label_3.setText(_translate("branchresult", "ENTER BRACH NAME "))
        self.B1.setText(_translate("branchresult", "RESULT"))
        self.B1.clicked.connect(self.res)
    
    
    def res(self):
        n1= self.CM1.currentText()
        mydb=mysql.connector.connect(host="localhost",user="root",password="",database="collage")
        mycursor=mydb.cursor()
        mycursor.execute("SHOW TABLES")
        c=0
        passs=0
        fail=0
        total=0
        #myresult=mycursor.fetchall()
        for i in mycursor:
            if i[0]==n1:
                c+=1
        if c>0:
            s= "SELECT sub1,sub2,sub3,sub4,sub5 FROM "+str(n1)
            mycursor.execute(s)
            myresult=mycursor.fetchall()
            
            for i in myresult:
                if i[0]>=33 and i[1]>=33 and i[2]>=33 and i[3]>=33 and i[4]>=33 :
                    passs+=1
                else:
                    fail+=1
                total+=1
        
        self.branch = QtWidgets.QMainWindow()
        self.ui = Ui_branchshow(n1,total,passs,fail)
        self.ui.setupUi(self.branch)
        self.branch.show()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    branchresult = QtWidgets.QMainWindow()
    ui = Ui_branchresult()
    ui.setupUi(branchresult)
    branchresult.show()
    sys.exit(app.exec_())
