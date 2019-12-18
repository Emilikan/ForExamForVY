# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/emilka/user.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_User(object):
    def setupUi(self, User):
        User.setObjectName("User")
        User.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(User)
        self.centralwidget.setObjectName("centralwidget")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(170, 140, 88, 29))
        self.exit.setObjectName("exit")
        self.math = QtWidgets.QLabel(self.centralwidget)
        self.math.setGeometry(QtCore.QRect(270, 230, 101, 41))
        self.math.setObjectName("math")
        self.answer = QtWidgets.QLineEdit(self.centralwidget)
        self.answer.setGeometry(QtCore.QRect(390, 230, 111, 41))
        self.answer.setObjectName("answer")
        self.enter = QtWidgets.QPushButton(self.centralwidget)
        self.enter.setGeometry(QtCore.QRect(290, 320, 151, 61))
        self.enter.setObjectName("enter")
        User.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(User)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        User.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(User)
        self.statusbar.setObjectName("statusbar")
        User.setStatusBar(self.statusbar)

        self.retranslateUi(User)
        QtCore.QMetaObject.connectSlotsByName(User)

    def retranslateUi(self, User):
        _translate = QtCore.QCoreApplication.translate
        User.setWindowTitle(_translate("User", "MainWindow"))
        self.exit.setText(_translate("User", "Back"))
        self.math.setText(_translate("User", "fff"))
        self.enter.setText(_translate("User", "Enter"))

