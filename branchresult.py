# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'branchreslut.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_branchshow(object):
    def __init__(self,n,t,p,f):
        self.n1=n
        self.total=t
        self.passs=p
        self.fail=f
    def setupUi(self, branchshow):
        branchshow.setObjectName("branchshow")
        branchshow.resize(637, 525)
        self.centralwidget = QtWidgets.QWidget(branchshow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 638, 481))
        self.label.setStyleSheet("background-color: rgb(250, 177, 88);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(165, 136, 150, 17))
        self.label_2.setStyleSheet("font: 63 13pt \"URW Bookman\";")
        self.label_2.setObjectName("label_2")
        self.T1 = QtWidgets.QLineEdit(self.centralwidget)
        self.T1.setGeometry(QtCore.QRect(330, 131, 144, 30))
        self.T1.setStyleSheet("font: 63 13pt \"URW Bookman\";")
        self.T1.setObjectName("T1")
        self.T2 = QtWidgets.QLineEdit(self.centralwidget)
        self.T2.setGeometry(QtCore.QRect(330, 173, 144, 30))
        self.T2.setStyleSheet("font: 63 13pt \"URW Bookman\";")
        self.T2.setObjectName("T2")
        self.T3 = QtWidgets.QLineEdit(self.centralwidget)
        self.T3.setGeometry(QtCore.QRect(330, 214, 144, 30))
        self.T3.setStyleSheet("font: 63 13pt \"URW Bookman\";")
        self.T3.setObjectName("T3")
        self.T4 = QtWidgets.QLineEdit(self.centralwidget)
        self.T4.setGeometry(QtCore.QRect(330, 258, 144, 30))
        self.T4.setStyleSheet("font: 63 13pt \"URW Bookman\";")
        self.T4.setObjectName("T4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(165, 180, 150, 17))
        self.label_3.setStyleSheet("font: 63 13pt \"URW Bookman\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(165, 220, 150, 17))
        self.label_4.setStyleSheet("font: 63 13pt \"URW Bookman\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(165, 262, 150, 17))
        self.label_5.setStyleSheet("font: 63 13pt \"URW Bookman\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(170, 320, 101, 17))
        self.label_6.setStyleSheet("font: 63 13pt \"URW Bookman\";")
        self.label_6.setObjectName("label_6")
        self.T5 = QtWidgets.QLineEdit(self.centralwidget)
        self.T5.setGeometry(QtCore.QRect(330, 310, 141, 31))
        self.T5.setObjectName("T5")
        branchshow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(branchshow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 637, 22))
        self.menubar.setObjectName("menubar")
        branchshow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(branchshow)
        self.statusbar.setObjectName("statusbar")
        branchshow.setStatusBar(self.statusbar)

        self.retranslateUi(branchshow)
        QtCore.QMetaObject.connectSlotsByName(branchshow)

    def retranslateUi(self, branchshow):
        _translate = QtCore.QCoreApplication.translate
        branchshow.setWindowTitle(_translate("branchshow", "BRANCH RESULT"))
        self.label_2.setText(_translate("branchshow", "BRANCH"))
        self.label_3.setText(_translate("branchshow", "TOTAL STUDENT"))
        self.label_4.setText(_translate("branchshow", "PASS STUDENT"))
        self.label_5.setText(_translate("branchshow", "FAIL STUDENT"))
        self.label_6.setText(_translate("branchshow", "PASSING %"))
        self.T1.setText(str(self.n1))
        self.T2.setText(str(self.total))
        self.T3.setText(str(self.passs))
        self.T4.setText(str(self.fail))
        i1=(self.passs/self.total)*100
        self.T5.setText(str(format(i1,'.2f')))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    branchshow = QtWidgets.QMainWindow()
    ui = Ui_branchshow()
    ui.setupUi(branchshow)
    branchshow.show()
    sys.exit(app.exec_())
