# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaAnadirCantidadVenta.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialogvacv(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(422, 241)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 421, 241))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.botonMas = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.botonMas.setStyleSheet("color: rgb(223, 0, 0);\n"
"")
        self.botonMas.setObjectName("botonMas")
        self.gridLayout.addWidget(self.botonMas, 1, 0, 1, 1)
        self.textCantidad = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textCantidad.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textCantidad.setObjectName("textCantidad")
        self.gridLayout.addWidget(self.textCantidad, 1, 2, 1, 1)
        self.botonOk = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.botonOk.setMaximumSize(QtCore.QSize(200, 16777215))
        self.botonOk.setObjectName("botonOk")
        self.gridLayout.addWidget(self.botonOk, 2, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.botonMenos = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.botonMenos.setStyleSheet("")
        self.botonMenos.setObjectName("botonMenos")
        self.gridLayout.addWidget(self.botonMenos, 1, 1, 1, 1)
        self.labelInformacion = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labelInformacion.setMaximumSize(QtCore.QSize(200, 100))
        self.labelInformacion.setObjectName("labelInformacion")
        self.gridLayout.addWidget(self.labelInformacion, 0, 2, 1, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Seleccionar Cantidad"))
        self.botonMas.setText(_translate("Dialog", "+"))
        self.textCantidad.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.botonOk.setText(_translate("Dialog", "Ok"))
        self.botonMenos.setText(_translate("Dialog", "-"))
        self.labelInformacion.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Nombre Producto</p><p>Cantidad actual: X</p><p>Precio: X</p><p><br/></p></body></html>"))
