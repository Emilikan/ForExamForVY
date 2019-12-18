# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/emilka/administrator.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Administrator(object):
    def setupUi(self, Administrator):
        Administrator.setObjectName("Administrator")
        Administrator.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Administrator)
        self.centralwidget.setObjectName("centralwidget")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(140, 90, 88, 29))
        self.back.setObjectName("back")
        self.delete_2 = QtWidgets.QPushButton(self.centralwidget)
        self.delete_2.setGeometry(QtCore.QRect(440, 430, 88, 29))
        self.delete_2.setObjectName("delete_2")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(140, 170, 341, 201))
        self.listWidget.setObjectName("listWidget")
        self.is_bloked = QtWidgets.QCheckBox(self.centralwidget)
        self.is_bloked.setGeometry(QtCore.QRect(540, 190, 86, 22))
        self.is_bloked.setCheckable(False)
        self.is_bloked.setObjectName("is_bloked")
        self.show_phone = QtWidgets.QPushButton(self.centralwidget)
        self.show_phone.setGeometry(QtCore.QRect(540, 300, 91, 31))
        self.show_phone.setObjectName("show_phone")
        Administrator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Administrator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        Administrator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Administrator)
        self.statusbar.setObjectName("statusbar")
        Administrator.setStatusBar(self.statusbar)

        self.retranslateUi(Administrator)
        QtCore.QMetaObject.connectSlotsByName(Administrator)

    def retranslateUi(self, Administrator):
        _translate = QtCore.QCoreApplication.translate
        Administrator.setWindowTitle(_translate("Administrator", "MainWindow"))
        self.back.setText(_translate("Administrator", "Back"))
        self.delete_2.setText(_translate("Administrator", "Delete"))
        self.is_bloked.setText(_translate("Administrator", "Blocked"))
        self.show_phone.setText(_translate("Administrator", "Show Phone"))

