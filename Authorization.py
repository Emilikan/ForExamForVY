from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Account import Account
from design import Ui_MainWindow
import sqlite3
from User import User
from Administrator import Administrator


def create_tables():
    conn = sqlite3.connect("dataBase.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE users (Login text, Password text, Blocked text)""")

    cursor.execute("""CREATE TABLE admins (Login text, Password text, Phone text)""")

    cursor.execute("""INSERT INTO users VALUES ('johnSmith@ml.ru', 'Qwerty123', 'Yes')""")
    cursor.execute("""INSERT INTO users VALUES ('Vanya123@ml.ru', 'F345Hj23K', 'No')""")
    cursor.execute("""INSERT INTO users VALUES ('Liza6788@dml.com', 'Liza6788', 'No')""")

    cursor.execute("""INSERT INTO admins VALUES ('Admin', 'admin', '81234567890')""")
    cursor.execute("""INSERT INTO admins VALUES ('Master', 'Jnk2J2 ', '80987654321')""")

    conn.commit()


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
        return res + '~1'
    if res == '':
        return None
    else:
        return res


class Authorization(QtWidgets.QMainWindow):

    def enter(self):
        login = self.ui.loginEdit.text()
        password = self.ui.passworEdit.text()

        if get_password(login) is None:
            QMessageBox.question(self, 'Error', 'Error', QMessageBox.Ok, QMessageBox.Ok)
        elif get_password(login).lower() == password.lower():
            self.user_window = User(login)
            self.user_window.show()
        elif get_password(login).lower() == (password.lower() + '~1'):
            self.w3 = Administrator(login)
            self.w3.show()
        else:
            QMessageBox.question(self, 'Error', 'Error', QMessageBox.Ok, QMessageBox.Ok)

    def exit(self):
        self.close()

    def registration(self):
        self.w2 = Account()
        self.w2.show()

    def __init__(self):
        super(Authorization, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.enter.clicked.connect(self.enter)
        self.ui.exit.clicked.connect(self.exit)
        self.ui.reg.clicked.connect(self.registration)


def main():
    app = QtWidgets.QApplication([])
    window = Authorization()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
