# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaLogin.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 500)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../assets/iconoLogo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.labelLogo = QtWidgets.QLabel(Dialog)
        self.labelLogo.setGeometry(QtCore.QRect(-220, -290, 1051, 791))
        self.labelLogo.setText("")
        self.labelLogo.setPixmap(QtGui.QPixmap("../assets/abastoLogo.png"))
        self.labelLogo.setObjectName("labelLogo")
        self.lineEditUsuario = QtWidgets.QLineEdit(Dialog)
        self.lineEditUsuario.setGeometry(QtCore.QRect(350, 280, 150, 31))
        self.lineEditUsuario.setObjectName("lineEditUsuario")
        self.lineEditContrasena = QtWidgets.QLineEdit(Dialog)
        self.lineEditContrasena.setGeometry(QtCore.QRect(350, 325, 150, 31))
        self.lineEditContrasena.setObjectName("lineEditContrasena")
        self.labelUsuario = QtWidgets.QLabel(Dialog)
        self.labelUsuario.setGeometry(QtCore.QRect(230, 280, 120, 31))
        self.labelUsuario.setObjectName("labelUsuario")
        self.labelContrasena = QtWidgets.QLabel(Dialog)
        self.labelContrasena.setGeometry(QtCore.QRect(230, 325, 120, 31))
        self.labelContrasena.setObjectName("labelContrasena")
        self.parche = QtWidgets.QLabel(Dialog)
        self.parche.setGeometry(QtCore.QRect(350, 40, 31, 31))
        self.parche.setAutoFillBackground(False)
        self.parche.setStyleSheet("background-color: rgb(36, 39, 42);")
        self.parche.setText("")
        self.parche.setTextFormat(QtCore.Qt.AutoText)
        self.parche.setObjectName("parche")
        self.botonEntrar = QtWidgets.QPushButton(Dialog)
        self.botonEntrar.setGeometry(QtCore.QRect(320, 370, 90, 25))
        self.botonEntrar.setObjectName("botonEntrar")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Login"))
        self.labelUsuario.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; color:#eeeeec;\">Usuario:</span></p></body></html>"))
        self.labelContrasena.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; color:#eeeeec;\">Contraseña:</span></p></body></html>"))
        self.botonEntrar.setText(_translate("Dialog", "Entrar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
