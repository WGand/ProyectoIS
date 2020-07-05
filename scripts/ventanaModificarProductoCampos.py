# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaModificarProductoCampos.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialogvmpc(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(380, 368)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 60, 61, 16))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 120, 61, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(50, 190, 61, 16))
        self.label_4.setObjectName("label_4")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(150, 30, 211, 213))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.campoNombre = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.campoNombre.setObjectName("campoNombre")
        self.verticalLayout.addWidget(self.campoNombre)
        self.campoPrecio = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../assets/iconoLogo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.campoPrecio.setObjectName("campoPrecio")
        self.verticalLayout.addWidget(self.campoPrecio)
        self.radioButtonSi = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButtonSi.setObjectName("radioButtonSi")
        self.verticalLayout.addWidget(self.radioButtonSi)
        self.radioButtonNo = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButtonNo.setObjectName("radioButtonNo")
        self.verticalLayout.addWidget(self.radioButtonNo)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(80, 260, 226, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.botonCancelar = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.botonCancelar.setObjectName("botonCancelar")
        self.horizontalLayout.addWidget(self.botonCancelar)
        self.okBoton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.okBoton.setObjectName("okBoton")
        self.horizontalLayout.addWidget(self.okBoton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Modificar Producto"))
        self.label.setText(_translate("Dialog", "Nombre"))
        self.label_3.setText(_translate("Dialog", "Precio"))
        self.label_4.setText(_translate("Dialog", "Iva"))
        self.campoNombre.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">nombre aqui</p></body></html>"))
        self.campoPrecio.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">precio aqui</p></body></html>"))
        self.radioButtonSi.setText(_translate("Dialog", "si"))
        self.radioButtonNo.setText(_translate("Dialog", "no"))
        self.botonCancelar.setText(_translate("Dialog", "Cancelar"))
        self.okBoton.setText(_translate("Dialog", "Ok"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
