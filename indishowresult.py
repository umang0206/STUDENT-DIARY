# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'result.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_showresult(object):
    def __init__(self,a):
        self.l=a
        self.I1=""
        self.I2=""
        self.I3=""
        self.I4=""
        self.I5=""
        

    def setupUi(self, showresult):
        showresult.setObjectName("showresult")
        showresult.resize(662, 559)
        self.centralwidget = QtWidgets.QWidget(showresult)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 662, 731))
        self.label.setStyleSheet("background-color: rgb(250, 177, 88);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 120, 67, 17))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 67, 17))
        self.label_3.setStyleSheet("font: 63 12pt \"URW Bookman\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 40, 67, 17))
        self.label_4.setStyleSheet("font: 63 12pt \"URW Bookman\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 70, 91, 17))
        self.label_5.setStyleSheet("font: 63 12pt \"URW Bookman\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(310, 10, 161, 16))
        self.label_6.setStyleSheet("font: 63 12pt \"URW Bookman\";")
        self.label_6.setObjectName("label_6")
        self.I1 = QtWidgets.QLineEdit(self.centralwidget)
        self.I1.setGeometry(QtCore.QRect(109, 7, 150, 25))
        self.I1.setObjectName("I1")
        self.I2 = QtWidgets.QLineEdit(self.centralwidget)
        self.I2.setGeometry(QtCore.QRect(109, 37, 150, 25))
        self.I2.setObjectName("I2")
        self.I3 = QtWidgets.QLineEdit(self.centralwidget)
        self.I3.setGeometry(QtCore.QRect(109, 67, 150, 25))
        self.I3.setObjectName("I3")
        self.I4 = QtWidgets.QLineEdit(self.centralwidget)
        self.I4.setGeometry(QtCore.QRect(480, 10, 151, 25))
        self.I4.setText("")
        self.I4.setObjectName("I4")
        self.I5 = QtWidgets.QLineEdit(self.centralwidget)
        self.I5.setGeometry(QtCore.QRect(480, 40, 151, 25))
        self.I5.setObjectName("I5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(370, 40, 91, 17))
        self.label_7.setStyleSheet("font: 63 12pt \"URW Bookman\";")
        self.label_7.setObjectName("label_7")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 126, 591, 20))
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(20, 360, 591, 20))
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(14, 136, 16, 240))
        self.line_3.setLineWidth(2)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(30, 140, 141, 17))
        self.label_8.setStyleSheet("font: 63 12pt \"URW Bookman\";")
        self.label_8.setObjectName("label_8")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(170, 135, 16, 240))
        self.line_4.setLineWidth(2)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(200, 140, 141, 21))
        self.label_9.setStyleSheet("font: 63 12pt \"URW Bookman\";")
        self.label_9.setObjectName("label_9")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(340, 135, 16, 240))
        self.line_5.setLineWidth(2)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(360, 140, 131, 17))
        self.label_10.setStyleSheet("font: 63 12pt \"URW Bookman\";")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(520, 140, 67, 17))
        self.label_11.setStyleSheet("font: 63 12pt \"URW Bookman\";")
        self.label_11.setObjectName("label_11")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(490, 135, 16, 240))
        self.line_6.setLineWidth(2)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(600, 133, 16, 240))
        self.line_7.setLineWidth(2)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(20, 160, 591, 20))
        self.line_8.setLineWidth(2)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(43, 175, 101, 22))
        self.label_12.setStyleSheet("font: 63 13pt \"URW Bookman\";")
        self.label_12.setObjectName("label_12")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(204, 175, 111, 22))
        self.label_17.setStyleSheet("font: 63 13pt \"URW Bookman\";")
        self.label_17.setObjectName("label_17")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(390, 175, 67, 22))
        self.label_22.setStyleSheet("font: 63 13pt \"URW Bookman\";")
        self.label_22.setObjectName("label_22")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(43, 210, 101, 22))
        self.label_13.setStyleSheet("font: 63 13pt \"URW Bookman\";")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(43, 245, 101, 22))
        self.label_14.setStyleSheet("font: 63 13pt \"URW Bookman\";")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(43, 280, 101, 22))
        self.label_15.setStyleSheet("font: 63 13pt \"URW Bookman\";")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(43, 315, 101, 22))
        self.label_16.setStyleSheet("font: 63 13pt \"URW Bookman\";")
        self.label_16.setObjectName("label_16")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(204, 210, 111, 22))
        self.label_18.setStyleSheet("font: 63 13pt \"URW Bookman\";")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(204, 245, 111, 22))
        self.label_19.setStyleSheet("font: 63 13pt \"URW Bookman\";")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(204, 280, 111, 22))
        self.label_20.setStyleSheet("font: 63 13pt \"URW Bookman\";")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(204, 315, 111, 22))
        self.label_21.setStyleSheet("font: 63 13pt \"URW Bookman\";")
        self.label_21.setObjectName("label_21")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(390, 210, 67, 22))
        self.label_23.setStyleSheet("font: 63 13pt \"URW Bookman\";")
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(390, 245, 67, 22))
        self.label_24.setStyleSheet("font: 63 13pt \"URW Bookman\";")
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(390, 280, 67, 22))
        self.label_25.setStyleSheet("font: 63 13pt \"URW Bookman\";")
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(390, 315, 67, 22))
        self.label_26.setStyleSheet("font: 63 13pt \"URW Bookman\";")
        self.label_26.setObjectName("label_26")
        self.T1 = QtWidgets.QLineEdit(self.centralwidget)
        self.T1.setGeometry(QtCore.QRect(510, 175, 81, 28))
        self.T1.setStyleSheet("font: 63 13pt \"URW Bookman\";\n"
"background-color: rgb(250, 177, 88);")
        self.T1.setText("")
        self.T1.setFrame(False)
        self.T1.setAlignment(QtCore.Qt.AlignCenter)
        self.T1.setObjectName("T1")
        self.T2 = QtWidgets.QLineEdit(self.centralwidget)
        self.T2.setGeometry(QtCore.QRect(510, 208, 81, 28))
        self.T2.setStyleSheet("font: 63 13pt \"URW Bookman\";\n"
"background-color: rgb(250, 177, 88);")
        self.T2.setText("")
        self.T2.setFrame(False)
        self.T2.setAlignment(QtCore.Qt.AlignCenter)
        self.T2.setObjectName("T2")
        self.T3 = QtWidgets.QLineEdit(self.centralwidget)
        self.T3.setGeometry(QtCore.QRect(510, 243, 81, 28))
        self.T3.setStyleSheet("font: 63 13pt \"URW Bookman\";\n"
"background-color: rgb(250, 177, 88);")
        self.T3.setText("")
        self.T3.setFrame(False)
        self.T3.setAlignment(QtCore.Qt.AlignCenter)
        self.T3.setObjectName("T3")
        self.T4 = QtWidgets.QLineEdit(self.centralwidget)
        self.T4.setGeometry(QtCore.QRect(510, 280, 81, 28))
        self.T4.setStyleSheet("font: 63 13pt \"URW Bookman\";\n"
"background-color: rgb(250, 177, 88);")
        self.T4.setText("")
        self.T4.setFrame(False)
        self.T4.setAlignment(QtCore.Qt.AlignCenter)
        self.T4.setObjectName("T4")
        self.T5 = QtWidgets.QLineEdit(self.centralwidget)
        self.T5.setGeometry(QtCore.QRect(510, 320, 81, 28))
        self.T5.setStyleSheet("font: 63 13pt \"URW Bookman\";\n"
"background-color: rgb(250, 177, 88);")
        self.T5.setText("")
        self.T5.setFrame(False)
        self.T5.setAlignment(QtCore.Qt.AlignCenter)
        self.T5.setObjectName("T5")
        self.T6 = QtWidgets.QLineEdit(self.centralwidget)
        self.T6.setGeometry(QtCore.QRect(500, 380, 113, 31))
        self.T6.setStyleSheet("font: 63 15pt \"URW Bookman\";")
        self.T6.setText("")
        self.T6.setAlignment(QtCore.Qt.AlignCenter)
        self.T6.setObjectName("T6")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(420, 380, 67, 31))
        self.label_27.setStyleSheet("font: 63 15pt \"URW Bookman\";")
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(440, 430, 31, 31))
        self.label_28.setStyleSheet("font: 63 15pt \"URW Bookman\";")
        self.label_28.setObjectName("label_28")
        self.T7 = QtWidgets.QLineEdit(self.centralwidget)
        self.T7.setGeometry(QtCore.QRect(500, 424, 113, 31))
        self.T7.setStyleSheet("font: 63 15pt \"URW Bookman\";")
        self.T7.setAlignment(QtCore.Qt.AlignCenter)
        self.T7.setObjectName("T7")
        showresult.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(showresult)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 662, 22))
        self.menubar.setObjectName("menubar")
        showresult.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(showresult)
        self.statusbar.setObjectName("statusbar")
        showresult.setStatusBar(self.statusbar)

        self.retranslateUi(showresult)
        QtCore.QMetaObject.connectSlotsByName(showresult)

    def retranslateUi(self, showresult):
        _translate = QtCore.QCoreApplication.translate
        showresult.setWindowTitle(_translate("showresult", " RESULT "))
        self.label_3.setText(_translate("showresult", "Name"))
        self.label_4.setText(_translate("showresult", "DOB"))
        self.label_5.setText(_translate("showresult", "ROLL NO."))
        self.label_6.setText(_translate("showresult", "REGISTRATION NO."))
        self.label_7.setText(_translate("showresult", "BRANCH"))
        self.label_8.setText(_translate("showresult", "SUBJECT NAME"))
        self.label_9.setText(_translate("showresult", "SUBJECT CODE"))
        self.label_10.setText(_translate("showresult", "PASSING MARK"))
        self.label_11.setText(_translate("showresult", "MARK"))
        self.label_12.setText(_translate("showresult", "SUBJECT 1"))
        self.label_17.setText(_translate("showresult", "SUB111SUB"))
        self.label_22.setText(_translate("showresult", "33/100"))
        self.label_13.setText(_translate("showresult", "SUBJECT 2"))
        self.label_14.setText(_translate("showresult", "SUBJECT 3"))
        self.label_15.setText(_translate("showresult", "SUBJECT 4"))
        self.label_16.setText(_translate("showresult", "SUBJECT 5"))
        self.label_18.setText(_translate("showresult", "SUB222SUB"))
        self.label_19.setText(_translate("showresult", "SUB333SUB"))
        self.label_20.setText(_translate("showresult", "SUB444SUB"))
        self.label_21.setText(_translate("showresult", "SUB555SUB"))
        self.label_23.setText(_translate("showresult", "33/100"))
        self.label_24.setText(_translate("showresult", "33/100"))
        self.label_25.setText(_translate("showresult", "33/100"))
        self.label_26.setText(_translate("showresult", "33/100"))
        self.label_27.setText(_translate("showresult", "TOTAL"))
        self.label_28.setText(_translate("showresult", "%"))
        self.I1.setText(str(self.l[1]))
        self.I2.setText(str(self.l[2]))
        self.I3.setText(str(self.l[0]))
        self.I4.setText(str(self.l[3]))
        self.I5.setText(str(self.l[4]))
        self.T1.setText(str(self.l[5]))
        self.T2.setText(str(self.l[6]))
        self.T3.setText(str(self.l[7]))
        self.T4.setText(str(self.l[8]))
        self.T5.setText(str(self.l[9]))
        self.T6.setText(str(self.l[6]+self.l[7]+self.l[8]+self.l[9]+self.l[5]))
        self.T7.setText(str((self.l[6]+self.l[7]+self.l[8]+self.l[9]+self.l[5])/5))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    showresult = QtWidgets.QMainWindow()
    ui = Ui_showresult()
    ui.setupUi(showresult)
    showresult.show()
    sys.exit(app.exec_())
