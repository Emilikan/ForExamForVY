import sqlite3

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from design_reg import Ui_design_registration


def get_password(login):
    conn = sqlite3.connect("dataBase.db")
    cursor = conn.cursor()
    sql = "SELECT Password FROM users WHERE Login=?"
    res = ''
    for i in cursor.execute(sql, [login]):
        for k in i:
            res += k
    if res == '':
        sql = "SELECT Password FROM admins WHERE Login=?"
        for i in cursor.execute(sql, [login]):
            for k in i:
                res += k
    if res == '':
        return None
    else:
        return res


def add_new_user(password, login):
    conn = sqlite3.connect("dataBase.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users VALUES (?, ?, ?)", [password, login, 'No'])
    conn.commit()


class Account(QtWidgets.QMainWindow):

    def enter(self):
        login = self.ui1.login.text()
        password1 = self.ui1.password1.text()
        password2 = self.ui1.password2.text()

        if get_password(login) is not None:
            QMessageBox.question(self, 'Error', 'Такой пользователь уже существует', QMessageBox.Ok, QMessageBox.Ok)

        elif (password1 == password2) & (login != ''):
            add_new_user(password1, login)
            QMessageBox.question(self, 'Ок', 'Вы успешно зарегестрированы', QMessageBox.Ok, QMessageBox.Ok)

        else:
            QMessageBox.question(self, 'Error', 'Error', QMessageBox.Ok, QMessageBox.Ok)

    def exit(self):
        self.close()

    def __init__(self):
        super(Account, self).__init__()
        self.ui1 = Ui_design_registration()
        self.ui1.setupUi(self)
        self.ui1.Enter.clicked.connect(self.enter)
        self.ui1.Back.clicked.connect(self.exit)
