from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QDialog
from PyQt5 import QtWidgets
from ventanaMenu import Ui_MainWindow
from ventanaGestionarProducto import Ui_Dialogvgp
from ventanaListarInventario import Ui_Dialogvli
from ventanaRegistrarVenta import Ui_Dialogvrv
from ventanaAnadirProducto import Ui_Dialogap
#Editado con Sublime Text
class ventanaListarInventario(QDialog):
    def __init__(self):
        super(ventanaListarInventario, self).__init__() #redefinicion de la clase QDialog con las necesidades de ventanaListarInventariopy, IDEM a todas las ventanas
        self.ui = Ui_Dialogvli() #1- descarga de la interfaz 
        self.ui.setupUi(self) #2- carga de la interfaz sobre el objeto. 1 y 2 IDEM todas las ventanas
        self.setWindowTitle("Listar Inventario")
        self.setWindowModality(2) #Detiene toda la actividad en las otras ventanas, ejemplo, salir pulsando la "x", IDEM a todas las ventanas

class ventanaGestionarProducto(QDialog):
    def __init__(self):
        super(ventanaGestionarProducto, self).__init__()
        self.ui = Ui_Dialogvgp()
        self.ui.setupUi(self)
        self.ui.botonAddProducto.clicked.connect(self.irAnadirProducto)
        self.ui.botonVolver.clicked.connect(self.irVolver)
        self.setWindowTitle("Gestionar Producto")
        self.setWindowModality(2)

    def irAnadirProducto(self):
        self.ventana_AnadirProducto = ventanaAnadirProducto()
        self.ventana_AnadirProducto.show()

    def irVolver(self):
        self.close()

class ventanaRegistrarVenta(QDialog):
    def __init__(self):
        super(ventanaRegistrarVenta, self).__init__()
        self.ui = Ui_Dialogvrv()
        self.ui.setupUi(self)
        self.ui.pushButtonFinzalizar.clicked.connect(self.popUpFinalizarVenta)
        self.setWindowTitle("Registrar Venta")
        self.setWindowModality(2)
    def popUpFinalizarVenta(self):
        self.popUp_FinalizarVenta = popUp('Desea confirmar la venta', 'Finalizar Venta', 'Confirmar', 'Cancelar')        

class popUp(): # Ventanas emergentes.
    def __init__(self, mensaje='', tituloVentana='', botonSi = '', botonNo=''):
        self = QtWidgets.QMessageBox()
        self.setIcon(QtWidgets.QMessageBox.Warning)
        self.setWindowTitle(tituloVentana)
        self.setInformativeText(mensaje)
        self.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Cancel)
        botonSi_ = self.button(QtWidgets.QMessageBox.Yes)
        botonSi_.setText(botonSi)
        botonNo_ = self.button(QtWidgets.QMessageBox.Cancel)
        botonNo_.setText(botonNo)
        print(self.children())
        self.exec()
        
class ventanaAnadirProducto(QDialog):
    def __init__(self):
        super(ventanaAnadirProducto, self).__init__()
        self.ui = Ui_Dialogap()
        self.ui.setupUi(self)
        self.ui.botonVolver.clicked.connect(self.volver)
        self.setWindowTitle("Añadir Producto")
        self.setWindowModality(2)

    def volver(self):
        self.close()

class ventanaMenu(QMainWindow):
    def __init__(self):
        super(ventanaMenu, self).__init__() 
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Menu")
        self.ui.botonGestionarProducto.clicked.connect(self.irGestionarProducto) #conexion entre el boton y su ventana, mas accion. IDEM a todos los botones
        self.ui.botonListarInventario.clicked.connect(self.irListarInventario)
        self.ui.botonRegistrarVenta.clicked.connect(self.irRegistrarVenta)
        self.ui.botonSalir.clicked.connect(self.salir)
        self.centerOnScreen()

    def irGestionarProducto(self):
        self.ventana_GestionarProducto = ventanaGestionarProducto() #ventana_GestionarProducto en vez de ventanaGestionarProducto para confusion en el interpretador, IDEM a todas las ventanas
        self.ventana_GestionarProducto.show()

    def irListarInventario(self):
        self.ventana_ListarInventario = ventanaListarInventario()
        self.ventana_ListarInventario.show()

    def irRegistrarVenta(self):
        self.ventana_RegistrarVenta = ventanaRegistrarVenta()
        self.ventana_RegistrarVenta.show()

    def salir(self):
        self.close()

    def centerOnScreen(self): #metodo centra la ventana principal
        resolution = QtWidgets.QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                          (resolution.height() / 2) - (self.frameSize().height() / 2))
