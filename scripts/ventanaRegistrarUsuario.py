from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QDialogvru(object):
    def setupUi(self, QDialog):
        QDialog.setObjectName("QDialog")
        QDialog.resize(700, 460)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../assets/iconoLogo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        QDialog.setWindowIcon(icon)
        self.labelTitulo = QtWidgets.QLabel(QDialog)
        self.labelTitulo.setGeometry(QtCore.QRect(160, 50, 380, 31))
        self.labelTitulo.setObjectName("labelTitulo")
        self.labelUsuario = QtWidgets.QLabel(QDialog)
        self.labelUsuario.setGeometry(QtCore.QRect(189, 185, 120, 31))
        self.labelUsuario.setObjectName("labelUsuario")
        self.labelUsuario_2 = QtWidgets.QLabel(QDialog)
        self.labelUsuario_2.setGeometry(QtCore.QRect(189, 225, 120, 31))
        self.labelUsuario_2.setObjectName("labelUsuario_2")
        self.labelUsuario_3 = QtWidgets.QLabel(QDialog)
        self.labelUsuario_3.setGeometry(QtCore.QRect(189, 265, 120, 31))
        self.labelUsuario_3.setObjectName("labelUsuario_3")
        self.lineEditUsuario = QtWidgets.QLineEdit(QDialog)
        self.lineEditUsuario.setGeometry(QtCore.QRect(311, 185, 200, 25))
        self.lineEditUsuario.setObjectName("lineEditUsuario")
        self.lineEditContrasena = QtWidgets.QLineEdit(QDialog)
        self.lineEditContrasena.setGeometry(QtCore.QRect(311, 225, 200, 25))
        self.lineEditContrasena.setObjectName("lineEditContrasena")
        self.lineEditConfirmacion = QtWidgets.QLineEdit(QDialog)
        self.lineEditConfirmacion.setGeometry(QtCore.QRect(311, 265, 200, 25))
        self.lineEditConfirmacion.setObjectName("lineEditConfirmacion")
        self.radioButtonSi = QtWidgets.QRadioButton(QDialog)
        self.radioButtonSi.setGeometry(QtCore.QRect(321, 335, 42, 23))
        self.radioButtonSi.setChecked(False)
        self.radioButtonSi.setObjectName("radioButtonSi")
        self.radioButtonNo = QtWidgets.QRadioButton(QDialog)
        self.radioButtonNo.setGeometry(QtCore.QRect(363, 335, 42, 23))
        self.radioButtonNo.setChecked(True)
        self.radioButtonNo.setObjectName("radioButtonNo")
        self.buttonVolver = QtWidgets.QPushButton(QDialog)
        self.buttonVolver.setGeometry(QtCore.QRect(250, 375, 90, 25))
        self.buttonVolver.setObjectName("buttonVolver")
        self.buttonAceptar = QtWidgets.QPushButton(QDialog)
        self.buttonAceptar.setGeometry(QtCore.QRect(355, 375, 90, 25))
        self.buttonAceptar.setObjectName("buttonAceptar")
        self.labelAdministrador = QtWidgets.QLabel(QDialog)
        self.labelAdministrador.setGeometry(QtCore.QRect(190, 335, 130, 23))
        self.labelAdministrador.setObjectName("labelAdministrador")
        self.labelInfo = QtWidgets.QLabel(QDialog)
        self.labelInfo.setGeometry(QtCore.QRect(170, 100, 371, 71))
        self.labelInfo.setTextFormat(QtCore.Qt.AutoText)
        self.labelInfo.setScaledContents(False)
        self.labelInfo.setIndent(-1)
        self.labelInfo.setObjectName("labelInfo")
        self.labelCheck = QtWidgets.QLabel(QDialog)
        self.labelCheck.setGeometry(QtCore.QRect(520, 265, 25, 25))
        self.labelCheck.setText("")
        self.labelCheck.setPixmap(QtGui.QPixmap("../assets/iconoCheck.png"))
        self.labelCheck.setObjectName("labelCheck")
        self.labelX = QtWidgets.QLabel(QDialog)
        self.labelX.setGeometry(QtCore.QRect(520, 265, 25, 25))
        self.labelX.setText("")
        self.labelX.setPixmap(QtGui.QPixmap("../assets/iconoX.png"))
        self.labelX.setObjectName("labelX")
        self.labelCorreo = QtWidgets.QLabel(QDialog)
        self.labelCorreo.setGeometry(QtCore.QRect(190, 300, 120, 31))
        self.labelCorreo.setObjectName("labelCorreo")
        self.lineEditCorreo = QtWidgets.QLineEdit(QDialog)
        self.lineEditCorreo.setGeometry(QtCore.QRect(310, 305, 200, 25))
        self.lineEditCorreo.setObjectName("lineEditCorreo")

        self.retranslateUi(QDialog)
        QtCore.QMetaObject.connectSlotsByName(QDialog)

    def retranslateUi(self, QDialog):
        _translate = QtCore.QCoreApplication.translate
        QDialog.setWindowTitle(_translate("QDialog", "Registrar usuario"))
        self.labelTitulo.setText(_translate("QDialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Ingrese los datos del nuevo usuario:</span></p></body></html>"))
        self.labelUsuario.setText(_translate("QDialog", "<html><head/><body><p><span style=\" font-size:14pt;\">Usuario:</span></p></body></html>"))
        self.labelUsuario_2.setText(_translate("QDialog", "<html><head/><body><p><span style=\" font-size:14pt;\">Contraseña:</span></p></body></html>"))
        self.labelUsuario_3.setText(_translate("QDialog", "<html><head/><body><p><span style=\" font-size:14pt;\">Confirmación:</span></p></body></html>"))
        self.radioButtonSi.setText(_translate("QDialog", "Si"))
        self.radioButtonNo.setText(_translate("QDialog", "No"))
        self.buttonVolver.setText(_translate("QDialog", "Volver"))
        self.buttonAceptar.setText(_translate("QDialog", "Aceptar"))
        self.labelAdministrador.setText(_translate("QDialog", "<html><head/><body><p><span style=\" font-size:14pt;\">Administrador:</span></p></body></html>"))
        self.labelInfo.setText(_translate("QDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:5px; margin-bottom:5px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Info:</span></p>\n"
"<p style=\" margin-top:5px; margin-bottom:5px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">La contraseña debe contener mínimo 7 carácteres,</span></p>\n"
"<p style=\" margin-top:5px; margin-bottom:5px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">al menos 1 número y al menos 1 mayúscula.</span></p></body></html>"))
        self.labelCorreo.setText(_translate("QDialog", "<html><head/><body><p><span style=\" font-size:14pt;\">Correo:</span></p></body></html>"))
