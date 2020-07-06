# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaGestionarUsuario.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialogvgu(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 421)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../assets/iconoLogo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.botonAnadirUsuario = QtWidgets.QPushButton(Dialog)
        self.botonAnadirUsuario.setGeometry(QtCore.QRect(230, 70, 180, 70))
        self.botonAnadirUsuario.setObjectName("botonAnadirUsuario")
        self.botonEliminarUsuario = QtWidgets.QPushButton(Dialog)
        self.botonEliminarUsuario.setGeometry(QtCore.QRect(230, 175, 180, 70))
        self.botonEliminarUsuario.setObjectName("botonEliminarUsuario")
        self.botonVolver = QtWidgets.QPushButton(Dialog)
        self.botonVolver.setGeometry(QtCore.QRect(230, 280, 180, 70))
        self.botonVolver.setObjectName("botonVolver")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Gestionar Usuarios"))
        self.botonAnadirUsuario.setText(_translate("Dialog", "Añadir Usuario"))
        self.botonEliminarUsuario.setText(_translate("Dialog", "Eliminar Usuario"))
        self.botonVolver.setText(_translate("Dialog", "Volver"))
