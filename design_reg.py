# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/emilka/design_reg.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_design_registration(object):
    def setupUi(self, design_registration):
        design_registration.setObjectName("design_registration")
        design_registration.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(design_registration)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 170, 54, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 210, 54, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(270, 260, 54, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(270, 290, 54, 17))
        self.label_4.setObjectName("label_4")
        self.Back = QtWidgets.QPushButton(self.centralwidget)
        self.Back.setGeometry(QtCore.QRect(120, 60, 88, 29))
        self.Back.setObjectName("Back")
        self.Enter = QtWidgets.QPushButton(self.centralwidget)
        self.Enter.setGeometry(QtCore.QRect(310, 390, 88, 29))
        self.Enter.setObjectName("Enter")
        self.login = QtWidgets.QLineEdit(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(340, 160, 113, 29))
        self.login.setObjectName("login")
        self.password1 = QtWidgets.QLineEdit(self.centralwidget)
        self.password1.setGeometry(QtCore.QRect(340, 200, 113, 29))
        self.password1.setObjectName("password1")
        self.password2 = QtWidgets.QLineEdit(self.centralwidget)
        self.password2.setGeometry(QtCore.QRect(340, 280, 113, 29))
        self.password2.setObjectName("password2")
        design_registration.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(design_registration)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        design_registration.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(design_registration)
        self.statusbar.setObjectName("statusbar")
        design_registration.setStatusBar(self.statusbar)

        self.retranslateUi(design_registration)
        QtCore.QMetaObject.connectSlotsByName(design_registration)

    def retranslateUi(self, design_registration):
        _translate = QtCore.QCoreApplication.translate
        design_registration.setWindowTitle(_translate("design_registration", "MainWindow"))
        self.label.setText(_translate("design_registration", "Login"))
        self.label_2.setText(_translate("design_registration", "Password"))
        self.label_3.setText(_translate("design_registration", "Repeat"))
        self.label_4.setText(_translate("design_registration", "password"))
        self.Back.setText(_translate("design_registration", "Back"))
        self.Enter.setText(_translate("design_registration", "Enter"))

