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
        Dialog.resize(803, 719)
        Dialog.setSizeGripEnabled(False)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 718))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.textoIva = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textoIva.setEnabled(False)
        self.textoIva.setMinimumSize(QtCore.QSize(0, 70))
        self.textoIva.setObjectName("textoIva")
        self.gridLayout.addWidget(self.textoIva, 6, 0, 2, 1)
        self.textoPrecioVenta = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textoPrecioVenta.setEnabled(False)
        self.textoPrecioVenta.setMinimumSize(QtCore.QSize(0, 100))
        self.textoPrecioVenta.setObjectName("textoPrecioVenta")
        self.gridLayout.addWidget(self.textoPrecioVenta, 3, 0, 1, 1)
        self.textoCantidad = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textoCantidad.setEnabled(False)
        self.textoCantidad.setMinimumSize(QtCore.QSize(0, 100))
        self.textoCantidad.setObjectName("textoCantidad")
        self.gridLayout.addWidget(self.textoCantidad, 4, 0, 1, 1)
        self.radioSi = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioSi.setObjectName("radioSi")
        self.gridLayout.addWidget(self.radioSi, 6, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.radioNo = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioNo.setObjectName("radioNo")
        self.gridLayout.addWidget(self.radioNo, 7, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.botonAnadir = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.botonAnadir.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.botonAnadir.setFont(font)
        self.botonAnadir.setObjectName("botonAnadir")
        self.gridLayout.addWidget(self.botonAnadir, 9, 1, 1, 1)
        self.textoPrecioCompra = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textoPrecioCompra.setEnabled(False)
        self.textoPrecioCompra.setMinimumSize(QtCore.QSize(0, 100))
        self.textoPrecioCompra.setObjectName("textoPrecioCompra")
        self.gridLayout.addWidget(self.textoPrecioCompra, 2, 0, 1, 1)
        self.campoTextoNombre = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.campoTextoNombre.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.campoTextoNombre.setFont(font)
        self.campoTextoNombre.setAcceptDrops(False)
        self.campoTextoNombre.setObjectName("campoTextoNombre")
        self.gridLayout.addWidget(self.campoTextoNombre, 0, 1, 1, 1)
        self.botonVolver = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.botonVolver.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.botonVolver.setFont(font)
        self.botonVolver.setObjectName("botonVolver")
        self.gridLayout.addWidget(self.botonVolver, 9, 0, 1, 1)
        self.campoTextoCantidad = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.campoTextoCantidad.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.campoTextoCantidad.setFont(font)
        self.campoTextoCantidad.setAcceptDrops(False)
        self.campoTextoCantidad.setAutoFillBackground(False)
        self.campoTextoCantidad.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.campoTextoCantidad.setObjectName("campoTextoCantidad")
        self.gridLayout.addWidget(self.campoTextoCantidad, 4, 1, 1, 1)
        self.campoTextoPrecioCompra = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.campoTextoPrecioCompra.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.campoTextoPrecioCompra.setFont(font)
        self.campoTextoPrecioCompra.setAcceptDrops(False)
        self.campoTextoPrecioCompra.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.campoTextoPrecioCompra.setObjectName("campoTextoPrecioCompra")
        self.gridLayout.addWidget(self.campoTextoPrecioCompra, 2, 1, 1, 1)
        self.textoNombre = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textoNombre.setEnabled(False)
        self.textoNombre.setMinimumSize(QtCore.QSize(0, 100))
        self.textoNombre.setPlaceholderText("")
        self.textoNombre.setObjectName("textoNombre")
        self.gridLayout.addWidget(self.textoNombre, 0, 0, 1, 1)
        self.campoTextoPrecioVenta = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.campoTextoPrecioVenta.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.campoTextoPrecioVenta.setFont(font)
        self.campoTextoPrecioVenta.setAcceptDrops(False)
        self.campoTextoPrecioVenta.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.campoTextoPrecioVenta.setObjectName("campoTextoPrecioVenta")
        self.gridLayout.addWidget(self.campoTextoPrecioVenta, 3, 1, 1, 1)
        self.campoTextoProveedor = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.campoTextoProveedor.setMinimumSize(QtCore.QSize(0, 0))
        self.campoTextoProveedor.setObjectName("campoTextoProveedor")
        self.gridLayout.addWidget(self.campoTextoProveedor, 5, 1, 1, 1)
        self.textoProveedor = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textoProveedor.setEnabled(False)
        self.textoProveedor.setMinimumSize(QtCore.QSize(0, 70))
        self.textoProveedor.setMaximumSize(QtCore.QSize(16777215, 70))
        self.textoProveedor.setObjectName("textoProveedor")
        self.gridLayout.addWidget(self.textoProveedor, 5, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.textoIva.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">¿IVA?</span></p></body></html>"))
        self.textoPrecioVenta.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">PRECIO VENTA</span></p></body></html>"))
        self.textoCantidad.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">CANTIDAD</span></p></body></html>"))
        self.radioSi.setText(_translate("Dialog", "Sí"))
        self.radioNo.setText(_translate("Dialog", "No"))
        self.botonAnadir.setText(_translate("Dialog", "Añadir"))
        self.textoPrecioCompra.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">PRECIO COMPRA</span></p></body></html>"))
        self.botonVolver.setText(_translate("Dialog", "Volver"))
        self.textoNombre.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">NOMBRE</span></p></body></html>"))
        self.textoProveedor.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">PROVEEDOR</span></p></body></html>"))
