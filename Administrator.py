import sqlite3
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from design_adm import Ui_Administrator

class Administrator(QtWidgets.QMainWindow):
    def get_phone(self):
        res = ''
        conn = sqlite3.connect("dataBase.db")
        cursor = conn.cursor()
        sql = "SELECT Phone FROM admins WHERE Login=?"
        for i in cursor.execute(sql, [self.login]):
            for k in i:
                res += k
        if res == '':
            return None
        else:
            return res

    def render_users(self):
        pass

    def show_phone(self):
        pass

    def delete(self):
        pass

    def back(self):
        self.close()

    def __init__(self, login):
        super(Administrator, self).__init__()
        self.ui = Ui_Administrator()
        self.ui.setupUi(self)
        self.ui.delete_2.clicked.connect(self.delete)
        self.ui.back.clicked.connect(self.back)
        self.ui.show_phone.clicked.connect(self.show_phone)
