import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5 import QtSql, QtGui
import MySQLdb as mdb
from ventanaMMenu import Ui_MainWindow

class MyDialog(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('/home/wgan/untitled1/ops.ui', self)
        self.show()

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__() #NombreVentana, self en super
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
if __name__ == '__main__':

    App = QApplication(sys.argv)
    db = QtSql.QSqlDatabase.addDatabase('QMYSQL','first')
    db.setDatabaseName('test')
    db.setHostName('localhost')
    db.setUserName('wgan')
    db.setPassword('123456789')
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    print(MainWindow.findChild("label", QLabel))
    MainWindow.show()
    sys.exit(App.exec())
