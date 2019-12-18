# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/emilka/design.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.reg = QtWidgets.QPushButton(self.centralwidget)
        self.reg.setGeometry(QtCore.QRect(370, 390, 141, 51))
        self.reg.setObjectName("reg")
        self.enter = QtWidgets.QPushButton(self.centralwidget)
        self.enter.setGeometry(QtCore.QRect(370, 310, 141, 51))
        self.enter.setObjectName("enter")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(40, 470, 91, 51))
        self.exit.setObjectName("exit")
        self.passworEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.passworEdit.setGeometry(QtCore.QRect(370, 230, 141, 51))
        self.passworEdit.setText("")
        self.passworEdit.setObjectName("passworEdit")
        self.loginEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.loginEdit.setGeometry(QtCore.QRect(370, 150, 141, 51))
        self.loginEdit.setText("")
        self.loginEdit.setObjectName("loginEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 160, 51, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 240, 61, 21))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.reg.setText(_translate("MainWindow", "Registration"))
        self.enter.setText(_translate("MainWindow", "Enter"))
        self.exit.setText(_translate("MainWindow", "Exit"))
        self.label.setText(_translate("MainWindow", "Login"))
        self.label_2.setText(_translate("MainWindow", "Password"))

