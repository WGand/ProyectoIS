from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialogvcc(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 276)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../assets/iconoLogo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.lineEditCodigo = QtWidgets.QLineEdit(Dialog)
        self.lineEditCodigo.setGeometry(QtCore.QRect(142, 140, 116, 25))
        self.lineEditCodigo.setObjectName("lineEditCodigo")
        self.labelMensajeConfirmacion = QtWidgets.QLabel(Dialog)
        self.labelMensajeConfirmacion.setGeometry(QtCore.QRect(80, 30, 240, 61))
        self.labelMensajeConfirmacion.setObjectName("labelMensajeConfirmacion")
        self.labelCodigo = QtWidgets.QLabel(Dialog)
        self.labelCodigo.setGeometry(QtCore.QRect(135, 115, 130, 20))
        self.labelCodigo.setObjectName("labelCodigo")
        self.botonAceptar = QtWidgets.QPushButton(Dialog)
        self.botonAceptar.setGeometry(QtCore.QRect(220, 190, 90, 25))
        self.botonAceptar.setObjectName("botonAceptar")
        self.botonVolver = QtWidgets.QPushButton(Dialog)
        self.botonVolver.setGeometry(QtCore.QRect(90, 190, 90, 25))
        self.botonVolver.setObjectName("botonVolver")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Confirmar Correo"))
        self.labelMensajeConfirmacion.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">Se ha enviado un código de<br/>confirmación a su correo.</span></p></body></html>"))
        self.labelCodigo.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">Ingrese el código:</span></p></body></html>"))
        self.botonAceptar.setText(_translate("Dialog", "Aceptar"))
        self.botonVolver.setText(_translate("Dialog", "Volver"))
