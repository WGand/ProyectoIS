from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialogvl(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 500)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../assets/iconoLogo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.labelLogo = QtWidgets.QLabel(Dialog)
        self.labelLogo.setGeometry(QtCore.QRect(-220, -290, 1051, 791))
        self.labelLogo.setText("")
        self.labelLogo.setPixmap(QtGui.QPixmap("../assets/abastoLogo.png"))
        self.labelLogo.setObjectName("labelLogo")
        self.lineEditUsuario = QtWidgets.QLineEdit(Dialog)
        self.lineEditUsuario.setGeometry(QtCore.QRect(350, 280, 150, 31))
        self.lineEditUsuario.setObjectName("lineEditUsuario")
        self.lineEditContrasena = QtWidgets.QLineEdit(Dialog)
        self.lineEditContrasena.setGeometry(QtCore.QRect(350, 325, 150, 31))
        self.lineEditContrasena.setObjectName("lineEditContrasena")
        self.labelUsuario = QtWidgets.QLabel(Dialog)
        self.labelUsuario.setGeometry(QtCore.QRect(230, 280, 120, 31))
        self.labelUsuario.setObjectName("labelUsuario")
        self.labelContrasena = QtWidgets.QLabel(Dialog)
        self.labelContrasena.setGeometry(QtCore.QRect(230, 325, 120, 31))
        self.labelContrasena.setObjectName("labelContrasena")
        self.botonEntrar = QtWidgets.QPushButton(Dialog)
        self.botonEntrar.setGeometry(QtCore.QRect(320, 370, 90, 25))
        self.botonEntrar.setObjectName("botonEntrar")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(270, 430, 191, 21))
        self.label.setOpenExternalLinks(False)
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def setupClickToggle(self):
        def mousePressEvent(*args, **kwargs):
            print("click")
        self.label.mousePressEvent = mousePressEvent

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Login"))
        self.labelUsuario.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; color:#eeeeec;\">Usuario:</span></p></body></html>"))
        self.labelContrasena.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; color:#eeeeec;\">Contraseña:</span></p></body></html>"))
        self.botonEntrar.setText(_translate("Dialog", "Entrar"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#eeeeec;\"><a>¿Ha olvidado su contraseña?</a></span></p></body></html>"))
