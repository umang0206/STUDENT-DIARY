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
    def setupUi(self, studentdetail):
        studentdetail.setObjectName("studentdetail")
        studentdetail.resize(800, 550)
        self.centralwidget = QtWidgets.QWidget(studentdetail)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 511))
        self.label.setStyleSheet("background-color: rgb(138, 226, 52);\n"
"background-color: rgb(123, 244, 136);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 99, 71, 30))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Ubuntu Condensed\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(290, 99, 71, 30))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Ubuntu Condensed\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(530, 99, 71, 30))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Ubuntu Condensed\";")
        self.label_5.setObjectName("label_5")
        self.D1 = QtWidgets.QLineEdit(self.centralwidget)
        self.D1.setGeometry(QtCore.QRect(92, 99, 181, 30))
        self.D1.setFrame(False)
        self.D1.setObjectName("D1")
        self.D2 = QtWidgets.QLineEdit(self.centralwidget)
        self.D2.setGeometry(QtCore.QRect(363, 99, 141, 30))
        self.D2.setFrame(False)
        self.D2.setObjectName("D2")
        self.D3 = QtWidgets.QComboBox(self.centralwidget)
        self.D3.setGeometry(QtCore.QRect(602, 99, 91, 30))
        self.D3.setObjectName("D3")
        self.D3.addItem("")
        self.D3.addItem("CIVIL")
        self.D3.addItem("CSE")
        self.D3.addItem("IT")
        self.D3.addItem("MECHA")
        self.D3.addItem("META")
        self.B1 = QtWidgets.QPushButton(self.centralwidget)
        self.B1.setGeometry(QtCore.QRect(340, 340, 89, 31))
        self.B1.setStyleSheet("background-color: rgb(32, 74, 135);\n"
"color: rgb(255, 255, 255);")
        self.B1.setObjectName("B1")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(160, 40, 451, 31))
        self.label_7.setStyleSheet("font: 75 italic 17pt \"Tibetan Machine Uni\";")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.B4 = QtWidgets.QPushButton(self.centralwidget)
        self.B4.setGeometry(QtCore.QRect(660, 460, 76, 25))
        self.B4.setStyleSheet("background-color: rgb(123, 244, 136);\n"
"background-color: rgb(123, 244, 136);")
        self.B4.setObjectName("B4")
        self.B2 = QtWidgets.QPushButton(self.centralwidget)
        self.B2.setGeometry(QtCore.QRect(40, 460, 76, 25))
        self.B2.setStyleSheet("background-color: rgb(123, 244, 136);\n"
"background-color: rgb(123, 244, 136);")
        self.B2.setObjectName("B2")
        self.B3 = QtWidgets.QPushButton(self.centralwidget)
        self.B3.setGeometry(QtCore.QRect(350, 450, 76, 25))
        self.B3.setObjectName("B3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(300, 174, 80, 21))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(300, 203, 80, 21))
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(300, 230, 80, 21))
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(300, 260, 80, 21))
        self.label_9.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(300, 290, 80, 21))
        self.label_10.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_10.setObjectName("label_10")
        self.T1 = QtWidgets.QLineEdit(self.centralwidget)
        self.T1.setGeometry(QtCore.QRect(390, 174, 70, 25))
        self.T1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.T1.setObjectName("T1")
        self.T2 = QtWidgets.QLineEdit(self.centralwidget)
        self.T2.setGeometry(QtCore.QRect(390, 202, 70, 25))
        self.T2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.T2.setObjectName("T2")
        self.T3 = QtWidgets.QLineEdit(self.centralwidget)
        self.T3.setGeometry(QtCore.QRect(390, 230, 70, 25))
        self.T3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.T3.setObjectName("T3")
        self.T4 = QtWidgets.QLineEdit(self.centralwidget)
        self.T4.setGeometry(QtCore.QRect(390, 260, 70, 25))
        self.T4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.T4.setObjectName("T4")
        self.T5 = QtWidgets.QLineEdit(self.centralwidget)
        self.T5.setGeometry(QtCore.QRect(390, 290, 70, 25))
        self.T5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.T5.setObjectName("T5")
        self.T6 = QtWidgets.QLineEdit(self.centralwidget)
        self.T6.setGeometry(QtCore.QRect(230, 390, 321, 25))
        self.T6.setStyleSheet("background-color: rgb(123, 244, 136);") 
        self.T6.setFrame(False)
        self.T6.setAlignment(QtCore.Qt.AlignCenter)
        self.T6.setObjectName("T6")
        studentdetail.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(studentdetail)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        studentdetail.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(studentdetail)
        self.statusbar.setObjectName("statusbar")
        studentdetail.setStatusBar(self.statusbar)

        self.retranslateUi(studentdetail)
        QtCore.QMetaObject.connectSlotsByName(studentdetail)

    def retranslateUi(self, studentdetail):
        _translate = QtCore.QCoreApplication.translate
        studentdetail.setWindowTitle(_translate("studentdetail", "STUDENT DETAILS"))
        self.label_3.setText(_translate("studentdetail", " Name"))
        self.label_4.setText(_translate("studentdetail", " Roll NO."))
        self.label_5.setText(_translate("studentdetail", " Branch"))
        self.B1.setText(_translate("studentdetail", "SUBMIT"))
        self.label_7.setText(_translate("studentdetail", "STUDENT ACADEMY DETAILS"))
        self.B4.setText(_translate("studentdetail", "EXIT"))
        self.B2.setText(_translate("studentdetail", "HOME"))
        self.B3.setStyleSheet(_translate("studentdetail", "background-color: rgb(123, 244, 136);\n"
"background-color: rgb(123, 244, 136);"))
        self.B3.setText(_translate("studentdetail", "CLEAR"))
        self.label_2.setText(_translate("studentdetail", "Subject  1"))
        self.label_6.setText(_translate("studentdetail", "Subject  2"))
        self.label_8.setText(_translate("studentdetail", "Subject  3"))
        self.label_9.setText(_translate("studentdetail", "Subject  4"))
        self.label_10.setText(_translate("studentdetail", "Subject  5"))
        self.B2.clicked.connect(self.home)
        self.B3.clicked.connect(self.clear)
        self.B1.clicked.connect(self.add)
        self.B2.clicked.connect(studentdetail.close)
        self.B4.clicked.connect(studentdetail.close)
    
        
    def add(self):
        
        b1=(self.T1.text())
        b2=(self.T2.text())
        b3=(self.T3.text())
        b4=(self.T4.text())
        b5=(self.T5.text())
        n1=(self.D1.text())
        n2=(self.D2.text())
        n3=(self.D3.currentText())
        mydb=mysql.connector.connect(host="localhost",user="root",password="",database="collage")
        mycursor=mydb.cursor()
        s="UPDATE "+str(n3)+" SET sub1=%s,sub2=%s,sub3=%s,sub4=%s,sub5=%s where roll="+str(n2)
        v=(int(b1),int(b2),int(b3),int(b4),int(b5))
        mycursor.execute(s,v)
        mydb.commit()
        self.T6.setText("Student marks is Upadate")
        
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
        self.D1.setText("")
        self.D2.setText("")
       
        
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    studentdetail = QtWidgets.QMainWindow()
    ui = Ui_studentdetail()
    ui.setupUi(studentdetail)
    studentdetail.show()
    sys.exit(app.exec_())
