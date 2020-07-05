# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaGestionarProducto.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialogvgp(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(403, 306)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 401, 301))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../assets/iconoLogo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.botonEliminarProducto = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.botonEliminarProducto.setMinimumSize(QtCore.QSize(0, 90))
        self.botonEliminarProducto.setMaximumSize(QtCore.QSize(2000, 16777215))
        self.botonEliminarProducto.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.botonEliminarProducto.setObjectName("botonEliminarProducto")
        self.gridLayout.addWidget(self.botonEliminarProducto, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)
        self.botonModificarProducto = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.botonModificarProducto.setMinimumSize(QtCore.QSize(0, 90))
        self.botonModificarProducto.setMaximumSize(QtCore.QSize(2000, 16777215))
        self.botonModificarProducto.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.botonModificarProducto.setObjectName("botonModificarProducto")
        self.gridLayout.addWidget(self.botonModificarProducto, 0, 0, 1, 1)
        self.botonAddProducto = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.botonAddProducto.setMinimumSize(QtCore.QSize(0, 90))
        self.botonAddProducto.setMaximumSize(QtCore.QSize(2000, 16777215))
        self.botonAddProducto.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.botonAddProducto.setObjectName("botonAddProducto")
        self.gridLayout.addWidget(self.botonAddProducto, 1, 0, 1, 1)
        self.botonVolver = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.botonVolver.setMinimumSize(QtCore.QSize(0, 90))
        self.botonVolver.setMaximumSize(QtCore.QSize(2000, 16777215))
        self.botonVolver.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.botonVolver.setObjectName("botonVolver")
        self.gridLayout.addWidget(self.botonVolver, 1, 2, 1, 1)
        self.gridLayout.setColumnStretch(0, 10)
        self.gridLayout.setColumnStretch(2, 10)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Gestionar Producto"))
        self.botonEliminarProducto.setText(_translate("Dialog", "Eliminar Producto"))
        self.botonModificarProducto.setText(_translate("Dialog", "Modificar Producto"))
        self.botonAddProducto.setText(_translate("Dialog", "Añadir Producto"))
        self.botonVolver.setText(_translate("Dialog", "Volver"))

