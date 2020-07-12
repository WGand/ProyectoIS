import sys
#from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel ya está importado en la linea 4, lo dejo de referencia
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtSql, QtGui
from gestorVentanas import ventanaLogin

if __name__ == '__main__':

    App = QApplication(sys.argv)
    win = ventanaLogin()
    win.show()
    sys.exit(App.exec())
