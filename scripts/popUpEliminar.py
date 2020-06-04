
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_Dialogpop(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(345, 191)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(60, 100, 226, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.botonCancelar = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.botonCancelar.setObjectName("botonCancelar")
        self.horizontalLayout.addWidget(self.botonCancelar)
        self.botonConfirmar = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.botonConfirmar.setObjectName("botonConfirmar")
        self.horizontalLayout.addWidget(self.botonConfirmar)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 20, 241, 71))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Aviso"))
        self.botonCancelar.setText(_translate("Dialog", "Cancelar"))
        self.botonConfirmar.setText(_translate("Dialog", "Confirmar"))
        self.label.setText(_translate("Dialog", "Seguro que desea eliminar Producto?"))

