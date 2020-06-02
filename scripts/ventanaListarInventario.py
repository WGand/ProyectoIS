from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialogvli(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(614, 530)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 611, 521))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setVerticalSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.campoTextoBuscador = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.campoTextoBuscador.setObjectName("campoTextoBuscador")
        self.gridLayout.addWidget(self.campoTextoBuscador, 0, 0, 1, 1)
        self.labelLupa = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labelLupa.setText("")
        self.labelLupa.setPixmap(QtGui.QPixmap("../assets/iconoLupa.png"))
        self.labelLupa.setObjectName("labelLupa")
        self.gridLayout.addWidget(self.labelLupa, 0, 1, 1, 1)
        self.tablaProductos = QtWidgets.QTableWidget(self.gridLayoutWidget)
        self.tablaProductos.setObjectName("tablaProductos")
        self.tablaProductos.setColumnCount(0)
        self.tablaProductos.setRowCount(0)
        self.gridLayout.addWidget(self.tablaProductos, 1, 0, 1, 2)
        self.botonVolver = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.botonVolver.setObjectName("botonVolver")
        self.gridLayout.addWidget(self.botonVolver, 2, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.botonVolver.setText(_translate("Dialog", "Volver"))
