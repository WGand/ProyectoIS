# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaMenu.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(794, 595)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../assets/iconoLogo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 791, 551))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("freeman.jpg"))
        self.label.setObjectName("label")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 791, 551))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.botonListarInventario = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.botonListarInventario.setMinimumSize(QtCore.QSize(0, 90))
        self.botonListarInventario.setMaximumSize(QtCore.QSize(2000, 16777215))
        self.botonListarInventario.setObjectName("botonListarInventario")
        self.gridLayout.addWidget(self.botonListarInventario, 0, 0, 1, 1)
        self.botonRegistrarVenta = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.botonRegistrarVenta.setMinimumSize(QtCore.QSize(0, 90))
        self.botonRegistrarVenta.setMaximumSize(QtCore.QSize(2000, 16777215))
        self.botonRegistrarVenta.setObjectName("botonRegistrarVenta")
        self.gridLayout.addWidget(self.botonRegistrarVenta, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.botonGestionarProducto = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.botonGestionarProducto.setMinimumSize(QtCore.QSize(0, 90))
        self.botonGestionarProducto.setMaximumSize(QtCore.QSize(2000, 16777215))
        self.botonGestionarProducto.setObjectName("botonGestionarProducto")
        self.gridLayout.addWidget(self.botonGestionarProducto, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 2, 1, 1, 1)
        self.botonSalir = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.botonSalir.setMinimumSize(QtCore.QSize(0, 90))
        self.botonSalir.setMaximumSize(QtCore.QSize(2000, 16777215))
        self.botonSalir.setObjectName("botonSalir")
        self.gridLayout.addWidget(self.botonSalir, 2, 2, 1, 1)
        self.botonGestionarUsuario = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.botonGestionarUsuario.setMinimumSize(QtCore.QSize(0, 90))
        self.botonGestionarUsuario.setMaximumSize(QtCore.QSize(2000, 16777215))
        self.botonGestionarUsuario.setObjectName("botonGestionarUsuario")
        self.gridLayout.addWidget(self.botonGestionarUsuario, 1, 2, 1, 1)
        self.botonajgsdvagsb = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.botonajgsdvagsb.setMinimumSize(QtCore.QSize(0, 90))
        self.botonajgsdvagsb.setMaximumSize(QtCore.QSize(2000, 16777215))
        self.botonajgsdvagsb.setObjectName("botonajgsdvagsb")
        self.gridLayout.addWidget(self.botonajgsdvagsb, 2, 0, 1, 1)
        self.gridLayout.setColumnStretch(0, 10)
        self.gridLayout.setColumnStretch(2, 10)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 794, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.botonListarInventario.setText(_translate("MainWindow", "Listar Inventario"))
        self.botonRegistrarVenta.setText(_translate("MainWindow", "Registrar venta"))
        self.botonGestionarProducto.setText(_translate("MainWindow", "Gestionar Producto"))
        self.botonSalir.setText(_translate("MainWindow", "Salir"))
        self.botonGestionarUsuario.setText(_translate("MainWindow", "Gestionar Usuarios"))
        self.botonajgsdvagsb.setText(_translate("MainWindow", "ajbdkiahsbla"))
