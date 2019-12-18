import random
import sqlite3
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from user import Ui_User


class User(QtWidgets.QMainWindow):
    def get_is_blocked(self):
        conn = sqlite3.connect("dataBase.db")
        cursor = conn.cursor()
        sql = "SELECT Blocked FROM users WHERE Login=?"
        res = ''
        for i in cursor.execute(sql, [self.login]):
            for k in i:
                res += k
        if res == '':
            return None
        else:
            return res

    def set_math_problem(self):
        x = random.randint(1, 1000)
        y = random.randint(1, 1000)
        res = x + y
        self.res = str(res)

        self.ui1.math.setText(str(x) + ' + ' + str(y) + '=')

    def enter(self):
        decision = self.ui1.answer.text()
        if decision == self.res:
            QMessageBox.question(self, 'Правильный ответ', 'Новый пример уже ждет вас', QMessageBox.Ok, QMessageBox.Ok)
            self.ui1.answer.setText('')
            self.set_math_problem()
        else:
            QMessageBox.question(self, 'Неверный ответ', 'Попробуйте еще', QMessageBox.Ok, QMessageBox.Ok)
            self.ui1.answer.setText('')

    def exit(self):
        self.close()

    def __init__(self, login):
        super(User, self).__init__()
        self.res = ''
        self.login = login
        self.ui1 = Ui_User()
        self.ui1.setupUi(self)
        self.ui1.enter.clicked.connect(self.enter)
        self.ui1.exit.clicked.connect(self.exit)
        self.set_math_problem()
