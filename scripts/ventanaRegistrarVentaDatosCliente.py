from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialogvrvdc(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.setEnabled(True)
        Dialog.resize(464, 393)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../assets/iconoLogo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 461, 391))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.botonOK = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.botonOK.setMaximumSize(QtCore.QSize(80, 30))
        self.botonOK.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.botonOK.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.botonOK.setObjectName("botonOK")
        self.gridLayout_2.addWidget(self.botonOK, 3, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.textCedula = QtWidgets.QTextEdit(self.gridLayoutWidget_2)
        self.textCedula.setMaximumSize(QtCore.QSize(400, 30))
        self.textCedula.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textCedula.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.textCedula.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.textCedula.setObjectName("textCedula")
        self.gridLayout_2.addWidget(self.textCedula, 0, 1, 1, 1)
        self.labelTelefono = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.labelTelefono.setMaximumSize(QtCore.QSize(200, 30))
        self.labelTelefono.setObjectName("labelTelefono")
        self.gridLayout_2.addWidget(self.labelTelefono, 2, 0, 1, 1)
        self.textTelefono = QtWidgets.QTextEdit(self.gridLayoutWidget_2)
        self.textTelefono.setMaximumSize(QtCore.QSize(400, 30))
        self.textTelefono.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textTelefono.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textTelefono.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.textTelefono.setObjectName("textTelefono")
        self.gridLayout_2.addWidget(self.textTelefono, 2, 1, 1, 1)
        self.labelCedula = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.labelCedula.setMaximumSize(QtCore.QSize(200, 30))
        self.labelCedula.setObjectName("labelCedula")
        self.gridLayout_2.addWidget(self.labelCedula, 0, 0, 1, 1)
        self.labelNombre = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.labelNombre.setMaximumSize(QtCore.QSize(200, 30))
        self.labelNombre.setObjectName("labelNombre")
        self.gridLayout_2.addWidget(self.labelNombre, 1, 0, 1, 1)
        self.textNombre = QtWidgets.QTextEdit(self.gridLayoutWidget_2)
        self.textNombre.setMaximumSize(QtCore.QSize(400, 30))
        self.textNombre.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textNombre.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textNombre.setInputMethodHints(QtCore.Qt.ImhNone)
        self.textNombre.setObjectName("textNombre")
        self.gridLayout_2.addWidget(self.textNombre, 1, 1, 1, 1)
        self.gridLayout_2.setRowStretch(0, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Ingreso de Datos"))
        self.botonOK.setText(_translate("Dialog", "Ok"))
        self.textCedula.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>"))
        self.labelTelefono.setText(_translate("Dialog", "<html><head/><body><p align=\"right\"><span style=\" font-size:14pt;\">Teléfono:</span></p></body></html>"))
        self.textTelefono.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>"))
        self.labelCedula.setText(_translate("Dialog", "<html><head/><body><p align=\"right\"><span style=\" font-size:14pt;\">Cédula:</span></p></body></html>"))
        self.labelNombre.setText(_translate("Dialog", "<html><head/><body><p align=\"right\"><span style=\" font-size:14pt;\">Nombre:</span></p></body></html>"))
        self.textNombre.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>"))

