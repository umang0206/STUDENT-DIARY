# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'result.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from  indishowresult import *

class Ui_indiresult(object):
    def __init__(self):

        self.br=["CIVIL","CSE","IT","MECHA","META"]
    def setupUi(self, indiresult):
        indiresult.setObjectName("indiresult")
        indiresult.resize(471, 421)
        self.centralwidget = QtWidgets.QWidget(indiresult)
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
        self.label_3.setGeometry(QtCore.QRect(110, 130, 111, 20))
        self.label_3.setObjectName("label_3")
        self.B1 = QtWidgets.QPushButton(self.centralwidget)
        self.B1.setGeometry(QtCore.QRect(200, 250, 91, 25))
        self.B1.setObjectName("B1")
        self.T1 = QtWidgets.QLineEdit(self.centralwidget)
        self.T1.setGeometry(QtCore.QRect(230, 127, 141, 25))
        self.T1.setObjectName("T1")
        self.T2 = QtWidgets.QLineEdit(self.centralwidget)
        self.T2.setGeometry(QtCore.QRect(230, 190, 141, 25))
        self.T2.setObjectName("T2")
        self.T3 = QtWidgets.QLineEdit(self.centralwidget)
        self.T3.setGeometry(QtCore.QRect(100, 300, 300, 25))
        self.T3.setStyleSheet("background-color: rgb(254, 89, 89);")
        self.T3.setFrame(False)
        self.T3.setAlignment(QtCore.Qt.AlignCenter)
        self.T3.setObjectName("T3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(130, 190, 91, 17))
        self.label_4.setObjectName("label_4")
        indiresult.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(indiresult)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 471, 22))
        self.menubar.setObjectName("menubar")
        indiresult.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(indiresult)
        self.statusbar.setObjectName("statusbar")
        indiresult.setStatusBar(self.statusbar)

        self.retranslateUi(indiresult)
        QtCore.QMetaObject.connectSlotsByName(indiresult)

    def retranslateUi(self, indiresult):
        _translate = QtCore.QCoreApplication.translate
        indiresult.setWindowTitle(_translate("indiresult", " RESULT PAGE"))
        self.label_3.setText(_translate("indiresult", " ROLL NUMBER"))
        self.B1.setText(_translate("indiresult", "RESULT"))
        self.label_4.setText(_translate("indiresult", "PASSWORD"))
        self.B1.clicked.connect(self.res)
    
    def res(self):
        n1=str(self.T1.text())
        n2=str(self.T2.text())
        c=0
        self.l=[]
        for i in self.br:
            mydb=mysql.connector.connect(host="localhost",user="root",password="",database="collage")
            mycus=mydb.cursor()
            s="SELECT * FROM  "+str(i)
            mycus.execute(s)
            myres=mycus.fetchall()
            for j in myres:
                if(j[0]==n1) and (str(j[2])==n2):
                    c+=1
                    self.l.append(j[0])
                    self.l.append(j[1])
                    self.l.append(j[2])
                    self.l.append(j[3])
                    self.l.append(j[4])
                    self.l.append(j[6])
                    self.l.append(j[7])
                    self.l.append(j[8])
                    self.l.append(j[9])
                    self.l.append(j[10])
                    self.indi = QtWidgets.QMainWindow()
                    self.ui = Ui_showresult(self.l)
                    self.ui.setupUi(self.indi)
                    self.indi.show()
        
        if c==0:
            self.T3.setText("Your roll number or Password is incorrect")
                    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    indiresult = QtWidgets.QMainWindow()
    ui = Ui_indiresult()
    ui.setupUi(indiresult)
    indiresult.show()
    sys.exit(app.exec_())