# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaAnadirProducto.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialogap(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(806, 666)
        Dialog.setSizeGripEnabled(False)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 661))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.textoCantidad = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textoCantidad.setEnabled(False)
        self.textoCantidad.setMinimumSize(QtCore.QSize(0, 100))
        self.textoCantidad.setObjectName("textoCantidad")
        self.gridLayout.addWidget(self.textoCantidad, 2, 0, 1, 1)
        self.radioSi = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioSi.setObjectName("radioSi")
        self.gridLayout.addWidget(self.radioSi, 3, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.radioNo = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioNo.setObjectName("radioNo")
        self.gridLayout.addWidget(self.radioNo, 4, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.botonVolver = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.botonVolver.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.botonVolver.setFont(font)
        self.botonVolver.setObjectName("botonVolver")
        self.gridLayout.addWidget(self.botonVolver, 5, 0, 1, 1)
        self.campoTextoNombre = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.campoTextoNombre.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.campoTextoNombre.setFont(font)
        self.campoTextoNombre.setAcceptDrops(False)
        self.campoTextoNombre.setObjectName("campoTextoNombre")
        self.gridLayout.addWidget(self.campoTextoNombre, 0, 1, 1, 1)
        self.botonAnadir = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.botonAnadir.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.botonAnadir.setFont(font)
        self.botonAnadir.setObjectName("botonAnadir")
        self.gridLayout.addWidget(self.botonAnadir, 5, 1, 1, 1)
        self.textoPrecio = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textoPrecio.setEnabled(False)
        self.textoPrecio.setMinimumSize(QtCore.QSize(0, 100))
        self.textoPrecio.setObjectName("textoPrecio")
        self.gridLayout.addWidget(self.textoPrecio, 1, 0, 1, 1)
        self.campoTextoCantidad = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.campoTextoCantidad.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.campoTextoCantidad.setFont(font)
        self.campoTextoCantidad.setAcceptDrops(False)
        self.campoTextoCantidad.setAutoFillBackground(False)
        self.campoTextoCantidad.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.campoTextoCantidad.setObjectName("campoTextoCantidad")
        self.gridLayout.addWidget(self.campoTextoCantidad, 2, 1, 1, 1)
        self.textoNombre = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textoNombre.setEnabled(False)
        self.textoNombre.setMinimumSize(QtCore.QSize(0, 100))
        self.textoNombre.setPlaceholderText("")
        self.textoNombre.setObjectName("textoNombre")
        self.gridLayout.addWidget(self.textoNombre, 0, 0, 1, 1)
        self.campoTextoPrecio = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.campoTextoPrecio.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.campoTextoPrecio.setFont(font)
        self.campoTextoPrecio.setAcceptDrops(False)
        self.campoTextoPrecio.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.campoTextoPrecio.setObjectName("campoTextoPrecio")
        self.gridLayout.addWidget(self.campoTextoPrecio, 1, 1, 1, 1)
        self.textoIva = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textoIva.setEnabled(False)
        self.textoIva.setMinimumSize(QtCore.QSize(0, 70))
        self.textoIva.setObjectName("textoIva")
        self.gridLayout.addWidget(self.textoIva, 3, 0, 2, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.textoCantidad.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">CANTIDAD</span></p></body></html>"))
        self.radioSi.setText(_translate("Dialog", "Sí"))
        self.radioNo.setText(_translate("Dialog", "No"))
        self.botonVolver.setText(_translate("Dialog", "Volver"))
        self.botonAnadir.setText(_translate("Dialog", "Añadir"))
        self.textoPrecio.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">PRECIO</span></p></body></html>"))
        self.textoNombre.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">NOMBRE</span></p></body></html>"))
        self.textoIva.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">¿IVA?</span></p></body></html>"))

