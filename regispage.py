# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registrationpage.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from mainpage import *
class Ui_studentdetail(object):
    def __init__(self):
        self.a1=0
    def setupUi(self, studentdetail):
        studentdetail.setObjectName("studentdetail")
        studentdetail.resize(600, 550)
        self.centralwidget = QtWidgets.QWidget(studentdetail)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 600, 511))
        self.label.setStyleSheet("background-color: rgb(250, 243, 26);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 131, 124, 30))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Ubuntu Condensed\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 162, 124, 30))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Ubuntu Condensed\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(150, 193, 124, 30))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Ubuntu Condensed\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(150, 224, 124, 30))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Ubuntu Condensed\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(150, 255, 124, 30))
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Ubuntu Condensed\";")
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(150, 100, 124, 30))
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Ubuntu Condensed\";")
        self.label_8.setObjectName("label_8")
        self.T1 = QtWidgets.QLineEdit(self.centralwidget)
        self.T1.setGeometry(QtCore.QRect(284, 100, 181, 30))
        self.T1.setFrame(False)
        self.T1.setObjectName("T1")
        self.T2 = QtWidgets.QLineEdit(self.centralwidget)
        self.T2.setGeometry(QtCore.QRect(284, 131, 181, 30))
        self.T2.setFrame(False)
        self.T2.setObjectName("T2")
        self.T3 = QtWidgets.QLineEdit(self.centralwidget)
        self.T3.setGeometry(QtCore.QRect(284, 162, 181, 30))
        self.T3.setFrame(False)
        self.T3.setObjectName("T3")
        self.T4 = QtWidgets.QLineEdit(self.centralwidget)
        self.T4.setGeometry(QtCore.QRect(284, 193, 181, 30))
        self.T4.setFrame(False)
        self.T4.setObjectName("T4")
        self.CM1 = QtWidgets.QComboBox(self.centralwidget)
        self.CM1.setGeometry(QtCore.QRect(284, 224, 181, 30))
        self.CM1.setObjectName("CM1")
        self.CM1.addItem("CIVIL")
        self.CM1.addItem("CSE")
        self.CM1.addItem("IT")
        self.CM1.addItem("MECHA")
        self.CM1.addItem("META")
        

        self.T5 = QtWidgets.QLineEdit(self.centralwidget)
        self.T5.setGeometry(QtCore.QRect(284, 255, 181, 30))
        self.T5.setFrame(False)
        self.T5.setObjectName("T5")
        self.T6 = QtWidgets.QLineEdit(self.centralwidget)
        self.T6.setGeometry(QtCore.QRect(160, 420, 321, 25))
        self.T6.setStyleSheet("background-color: rgb(250, 243, 26);") 
        self.T6.setFrame(False)
        self.T6.setAlignment(QtCore.Qt.AlignCenter)
        self.T6.setObjectName("T6")
        self.B1 = QtWidgets.QPushButton(self.centralwidget)
        self.B1.setGeometry(QtCore.QRect(260, 310, 89, 31))
        self.B1.setStyleSheet("background-color: rgb(32, 74, 135);\n"
"color: rgb(255, 255, 255);")
        self.B1.setObjectName("B1")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(160, 40, 271, 31))
        self.label_7.setStyleSheet("font: 75 italic 17pt \"Tibetan Machine Uni\";")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.B4 = QtWidgets.QPushButton(self.centralwidget)
        self.B4.setGeometry(QtCore.QRect(460, 361, 76, 25))
        self.B4.setStyleSheet("background-color: rgb(123, 244, 136);\n"
"background-color: rgb(123, 244, 136);")
        self.B4.setObjectName("B4")
        self.B2 = QtWidgets.QPushButton(self.centralwidget)
        self.B2.setGeometry(QtCore.QRect(30, 361, 76, 25))
        self.B2.setStyleSheet("background-color: rgb(123, 244, 136);\n"
"background-color: rgb(123, 244, 136);")
        self.B2.setObjectName("B2")
        self.B3 = QtWidgets.QPushButton(self.centralwidget)
        self.B3.setGeometry(QtCore.QRect(260, 361, 76, 25))
        self.B3.setObjectName("B3")
        studentdetail.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(studentdetail)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 22))
        self.menubar.setObjectName("menubar")
        studentdetail.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(studentdetail)
        self.statusbar.setObjectName("statusbar")
        studentdetail.setStatusBar(self.statusbar)
        self.retranslateUi(studentdetail)
        QtCore.QMetaObject.connectSlotsByName(studentdetail)

    def retranslateUi(self, studentdetail):
        _translate = QtCore.QCoreApplication.translate
        studentdetail.setWindowTitle(_translate("studentdetail", "REGISTRATION FORM(STUDENT DETAILS)"))
        self.label_2.setText(_translate("studentdetail", " Name"))
        self.label_3.setText(_translate("studentdetail", " DOB"))
        self.label_4.setText(_translate("studentdetail", " Registration NO."))
        self.label_5.setText(_translate("studentdetail", " Branch"))
        self.label_6.setText(_translate("studentdetail", " Contact NO."))
        self.label_8.setText(_translate("studentdetail", " Roll NO."))
        self.B1.setText(_translate("studentdetail", "SUBMIT"))
        self.label_7.setText(_translate("studentdetail", "STUDENT DETAILS"))
        self.B4.setText(_translate("studentdetail", "EXIT"))
        self.B2.setText(_translate("studentdetail", "HOME"))
        self.B3.setStyleSheet(_translate("studentdetail", "background-color: rgb(123, 244, 136);\n"
"background-color: rgb(123, 244, 136);"))
        self.B3.setText(_translate("studentdetail", "CLEAR"))
        self.B2.clicked.connect(self.home)
        self.B3.clicked.connect(self.clear)
        self.B1.clicked.connect(self.add)
        self.B2.clicked.connect(studentdetail.close)
        self.B4.clicked.connect(studentdetail.close)


        
    def add(self):
        if self.a1==0:
            n1=str(self.T1.text())
            n2=str(self.T2.text())
            n3=str(self.T3.text())
            n4=str(self.T4.text())
            n5=str(self.CM1.currentText())
            n6=str(self.T5.text())
            mydb=mysql.connector.connect(host="localhost",user="root",password="",database="collage")
            mycursor=mydb.cursor()
            s="INSERT INTO "+str(n5)+"(roll,name,dob,registration,branch,contact)VALUES(%s,%s,%s,%s,%s,%s)"
            v=(n1,n2,n3,n4,n5,n6)
            mycursor.execute(s,v)
            mydb.commit()
            self.T6.setText("your student id is registered")
            self.a1=1







    def home(self):
        self.page = QtWidgets.QMainWindow()
        self.ui = Ui_mainpage()
        self.ui.setupUi(self.page)
        self.page.show()
    def clear(self):
        self.T1.setText("")
        self.T2.setText("")
        self.T3.setText("")
        self.T4.setText("")
        self.T5.setText("")
        self.T6.setText("")
        self.a1=0




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    studentdetail = QtWidgets.QMainWindow()
    ui = Ui_studentdetail()
    ui.setupUi(studentdetail)
    studentdetail.show()
    sys.exit(app.exec_())
