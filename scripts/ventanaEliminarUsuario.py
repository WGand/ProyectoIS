from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialogveu(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(750, 502)
        self.tableView = QtWidgets.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(20, 40, 711, 421))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../assets/iconoLogo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.tableView.setObjectName("tableView")
        self.barraBusqueda = QtWidgets.QLineEdit(Dialog)
        self.barraBusqueda.setGeometry(QtCore.QRect(20, 10, 691, 25))
        self.barraBusqueda.setObjectName("barraBusqueda")
        self.labelIconoLupa = QtWidgets.QLabel(Dialog)
        self.labelIconoLupa.setGeometry(QtCore.QRect(710, 10, 21, 25))
        self.labelIconoLupa.setText("")
        self.labelIconoLupa.setPixmap(QtGui.QPixmap("../assets/iconoLupa.png"))
        self.labelIconoLupa.setObjectName("labelIconoLupa")
        self.botonVolver = QtWidgets.QPushButton(Dialog)
        self.botonVolver.setGeometry(QtCore.QRect(330, 470, 90, 25))
        self.botonVolver.setObjectName("botonVolver")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Eliminar Usuarios."))
        self.botonVolver.setText(_translate("Dialog", "Volver"))
