#Import basura de QT
from PyQt5 import uic
from PyQt5.QtWidgets import QHeaderView, QMainWindow, QDialog, QMessageBox, QVBoxLayout
from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui
from PyQt5 import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5 import QtSql
from PyQt5.QtSql import *
from PyQt5.QtSql import QSqlQuery, QSqlTableModel
#Import Ventanas
from ventanaMenu import Ui_MainWindow
from ventanaGestionarProducto import Ui_Dialogvgp
from ventanaListarInventario import Ui_Dialogvli
from ventanaRegistrarVenta import Ui_Dialogvrv
from ventanaAnadirProducto import Ui_Dialogap
from ventanaRegistrarVentaDatosCliente import Ui_Dialogvrvdc
from ventanaModificarProducto import Ui_Dialogvmp
from ventanaEliminarProducto import Ui_Dialogvep
from ventanaModificarCantidad import Ui_Dialogvmc
from ventanaModificarProductoCampos import Ui_Dialogvmpc
#Import Database
from manejadorDataBase import ConexionDataBase

def tipoPopUp(tipo): #funcion que retorna la expresion del PopUp
    switch = {
        "advertencia": QtWidgets.QMessageBox.Warning,
        "informativo" : QtWidgets.QMessageBox.Information,
        "dubitativo" : QtWidgets.QMessageBox.Question,
        "critico" : QtWidgets.QMessageBox.Critical
    }
    return switch.get(tipo)
class Validaciones():
    def isNotFloat(self, string_):
            try:
                float(string_)
                return False
            except ValueError:
                return True

    def isNotDigit(self, string_):
        try:
            int(string_)
            return False
        except ValueError:
            return True

    def isNotNumeric(self, string_):
        try:

            return False
        except ValueError:
            return True

    def isNotAlpha(self, string_):
        for i in range(0, len(string_)):
            if((string_[i].isdigit() == True) or ((string_[i].isalnum() == False) and (string_[i] != ' ') )):
                return True
        return False

class ventanaListarInventario(QDialog):
    def __init__(self):
        super(ventanaListarInventario, self).__init__() #redefinicion de la clase QDialog con las necesidades de ventanaListarInventariopy, IDEM a todas las ventanas
        self.ui = Ui_Dialogvli() #1- descarga de la interfaz
        self.ui.setupUi(self) #2- carga de la interfaz sobre el objeto. 1 y 2 IDEM todas las ventanas
        self.setWindowTitle("Listar Inventario")
        self.setWindowModality(2) #Detiene toda la actividad en las otras ventanas, ejemplo, salir pulsando la "x", IDEM a todas las ventanas
        self.funcionPiedreraTabla()

    def irVentanaModificarCantidad(self):
            self.ventana_ModificarCantidad = ventanaModificarCantidad(self.ui.tableView.model().index(self.ui.tableView.currentIndex().row(), 0).data())
            self.ventana_ModificarCantidad.show()
            self.model.updateRowInTable(self.ui.tableView.model().index(self.ui.tableView.currentIndex().row()))

    def funcionPiedreraTabla(self):
        self.conector = ConexionDataBase()
        self.query1 = QSqlQuery()
        self.model = QSqlTableModel()
        self.conector.openDB()
        self.query1.exec_("select nombre,cantidad,precio,iva from producto;")
        self.model.setQuery(self.query1)
        self.conector.closeDB()
        self.model.insertColumn(4)
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, str("Modificar"))
        self.filter_proxy_model = QtCore.QSortFilterProxyModel()
        self.filter_proxy_model.setFilterCaseSensitivity(0)
        self.filter_proxy_model.setSourceModel(self.model)
        self.filter_proxy_model.setFilterKeyColumn(0)
        self.ui.lineEdit.textChanged.connect(self.filter_proxy_model.setFilterRegExp)
        self.ui.tableView.setModel(self.filter_proxy_model)
        self.ui.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ui.tableView.selectionModel().currentRowChanged.connect(self.irVentanaModificarCantidad)

    def irVolver(self):
        self.close()

class ventanaModificarCantidad(QDialog):
    def __init__(self, nombre):
        super(ventanaModificarCantidad, self).__init__()
        self.ui = Ui_Dialogvmc()
        self.ui.setupUi(self)
        self.conector = ConexionDataBase()
        self.producto_ = self.conector.busquedaProducto(nombre)
        self.cantidadActual = self.producto_.getCantidad()
        self.ui.textCantidad.setText(str(self.producto_.getCantidad()))
        self.ui.labelInformacion.setText('Producto: '+str(self.producto_.getNombre())+'\nCantidad actual: '+str(self.producto_.getCantidad())+'\nPrecio: '+ str(self.producto_.getPrecio()))
        self.ui.botonMas.clicked.connect(self.sumar)
        self.ui.botonMenos.clicked.connect(self.restar)
        self.ui.textCantidad.setReadOnly(True)
        self.ui.botonOk.clicked.connect(self.popUpConfirmarCantidad)    
        self.setWindowTitle("Modificar Cantidad")
        self.setWindowModality(2)

    def sumar(self):
        sumando = int(self.ui.textCantidad.toPlainText())
        if(sumando == 0):
            self.ui.botonMenos.setEnabled(True)
        sumando += 1
        self.ui.textCantidad.setText(str(sumando))
        self.producto_.setCantidad(int(self.ui.textCantidad.toPlainText()))

    def restar(self):
        restando = int(self.ui.textCantidad.toPlainText())
        if(restando == 1):
            self.ui.botonMenos.setDisabled(True)
        restando -= 1
        self.ui.textCantidad.setText(str(restando))
        self.producto_.setCantidad(int(self.ui.textCantidad.toPlainText()))
        
    def popUpConfirmarCantidad(self):
        self.popUp_ConfirmarCantidad = popUp('El producto '+self.producto_.getNombre()+' tiene una cantidad existente de'
        +str(self.cantidadActual)+'unidades registrada \n¿Desea actualizar a: '+str(self.producto_.getCantidad())+' unidades?','Confirmar Cambios',
        True, 'dubitativo', 'Confirmar', 'Cancelar' )
        self.popUp_ConfirmarCantidad.buttons()[1].pressed.connect(self.guardarCambios)
        self.popUp_ConfirmarCantidad.buttons()[0].pressed.connect(self.close)
        self.popUp_ConfirmarCantidad.exec()
    
    def irVolver(self):
        self.close()
    
    def guardarCambios(self):
        self.conector.modificarCantidadProducto(self.producto_.getCantidad(), self.producto_.getNombre())
        self.irVolver()

class ventanaGestionarProducto(QDialog):
    def __init__(self):
        super(ventanaGestionarProducto, self).__init__()
        self.ui = Ui_Dialogvgp()
        self.ui.setupUi(self)
        self.ui.botonAddProducto.clicked.connect(self.irAnadirProducto)
        self.ui.botonModificarProducto.clicked.connect(self.irModificarProducto)
        self.ui.botonEliminarProducto.clicked.connect(self.irEliminarProducto)
        self.ui.botonVolver.clicked.connect(self.irVolver)
        self.setWindowTitle("Gestionar Producto")
        self.setWindowModality(2)

    def irAnadirProducto(self):
        self.ventana_AnadirProducto = ventanaAnadirProducto()
        self.ventana_AnadirProducto.show()

    def irVolver(self):
        self.close()

    def irModificarProducto(self):
        self.ventanaModificarProducto = ventanaModificarProducto()
        self.ventanaModificarProducto.show()

    def irEliminarProducto(self):
        self.ventanaEliminarProducto = ventanaEliminarProducto()
        self.ventanaEliminarProducto.show()

class ventanaModificarProducto(QDialog):
    def __init__(self):
        super(ventanaModificarProducto, self).__init__()
        self.ui = Ui_Dialogvmp()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.volver)
        self.setWindowTitle("Modificar Producto")
        self.setWindowModality(2)
        self.conector = ConexionDataBase()
        self.conector.openDB()
        self.query1 = QtSql.QSqlQuery()
        self.query1.exec_("select nombre,cantidad,precio,iva from producto;")
        model = QtSql.QSqlTableModel()
        model.setQuery(self.query1)
        self.conector.closeDB()
        filter_proxy_model = QtCore.QSortFilterProxyModel()
        filter_proxy_model.setFilterCaseSensitivity(0)
        filter_proxy_model.setSourceModel(model)
        filter_proxy_model.setFilterKeyColumn(0)
        self.ui.campoTexto.textChanged.connect(filter_proxy_model.setFilterRegExp)
        self.ui.tableView.setModel(filter_proxy_model)
        self.ui.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ui.tableView.selectionModel().currentRowChanged.connect(self.irProximaVentana)

    def irProximaVentana(self):
        nombre = self.ui.tableView.model().index(self.ui.tableView.currentIndex().row(), 0).data()
        precio = self.ui.tableView.model().index(self.ui.tableView.currentIndex().row(), 2).data()
        iva = self.ui.tableView.model().index(self.ui.tableView.currentIndex().row(), 3).data()
        self.ventanaModificarProductoCampos = ventanaModificarProductoCampos(nombre, precio ,iva)
        self.ventanaModificarProductoCampos.show()

    def volver(self):
        self.close()

class ventanaModificarProductoCampos(QDialog):
    def __init__(self, nombre, precio, iva):
        super(ventanaModificarProductoCampos, self).__init__()
        self.ui = Ui_Dialogvmpc()
        self.ui.setupUi(self)
        self.ui.botonCancelar.clicked.connect(self.volver)
        self.ui.campoNombre.setPlainText(nombre)
        self.conector = ConexionDataBase()
        self.ui.campoPrecio.setPlainText(str(precio))
        if (iva):
            self.ui.radioButtonSi.setChecked(True)
        else:
            self.ui.radioButtonNo.setChecked(True)
        self.setWindowTitle("Modificar Producto")
        self.setWindowModality(2)
        self.ui.okBoton.clicked.connect(self.validarIngreso)
        self.nombre = nombre
        self.precio = precio
        self.iva = iva

    def volver(self):
        self.close()

    def validarIngreso(self):
        if ((len(self.ui.campoNombre.toPlainText()) == 0) or (len(self.ui.campoPrecio.toPlainText()) == 0) or ((self.ui.radioButtonSi.isChecked() == False) and (self.ui.radioButtonNo.isChecked() == False))):
            self.popUp_AdvertenciaDatoIncompleto = popUp('No se llenaron todos los datos requeridos.', 'Error', False, 'informativo', 'Ok')
            self.popUp_AdvertenciaDatoIncompleto.exec()
        else: #Validar
            validador = Validaciones()
            if ((validador.isNotFloat(self.ui.campoPrecio.toPlainText())) or (validador.isNotAlpha(self.ui.campoNombre.toPlainText()))):
                self.popUp_AdvertenciaDatoIncorrecto = popUp('Algún dato se ingresó de manera incorrecta.', 'Error', False, 'advertencia', 'Ok')
                self.popUp_AdvertenciaDatoIncorrecto.exec()
            else:
                self.conector.modificarPrecioProducto(self.ui.campoPrecio.toPlainText(),self.nombre)
                if (self.ui.radioButtonSi.isChecked() == True):
                    self.conector.modificarIvaProducto("True",self.nombre)
                elif(self.ui.radioButtonSi.isChecked() == False):
                    self.conector.modificarIvaProducto("False",self.nombre)
                self.conector.modificarNombreProducto(self.ui.campoNombre.toPlainText(),self.nombre)
                self.popUp_ModificarProducto = popUp('¿Desea modificar otro producto?', 'Producto modificado correctamente', True, 'informativo', 'Si', 'No')
                self.popUp_ModificarProducto.buttons()[1].pressed.connect(self.close)
                self.popUp_ModificarProducto.exec()
   

class ventanaEliminarProducto(QDialog):
    def __init__(self):
        super(ventanaEliminarProducto, self).__init__()
        self.ui = Ui_Dialogvep()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.volver)
        self.setWindowTitle("Eliminar Producto")
        self.setWindowModality(2)

        self.conector = ConexionDataBase()
        self.conector.openDB()
        self.query1 = QSqlQuery()
        self.query1.exec_("SELECT nombre,cantidad,precio,iva FROM producto WHERE cantidad=0;")
        model = QSqlTableModel()
        model.setQuery(self.query1)
        self.conector.closeDB()
        filter_proxy_model = QtCore.QSortFilterProxyModel()
        filter_proxy_model.setFilterCaseSensitivity(0)
        filter_proxy_model.setSourceModel(model)
        filter_proxy_model.setFilterKeyColumn(0)
        self.ui.campoTexto.textChanged.connect(filter_proxy_model.setFilterRegExp)
        self.ui.tableView.setModel(filter_proxy_model)
        self.ui.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ui.tableView.selectionModel().currentRowChanged.connect(self.irProximaVentana)

    def volver(self):
        self.close()        

    def irProximaVentana(self):
        self.popUp_eliminarProducto = popUp('¿Desea eliminar el producto seleccionado?', 'Aviso', True, 'informativo', 'Confirmar', 'Cancelar')
        self.popUp_eliminarProducto.buttons()[1].pressed.connect(self.eliminarProducto)
        self.popUp_eliminarProducto.buttons()[0].pressed.connect(self.close) 
        self.popUp_eliminarProducto.exec()   

    def eliminarProducto(self):
        self.conector = ConexionDataBase()
        self.conector.openDB()
        self.conector.deleteProducto(self.ui.tableView.model().index(self.ui.tableView.currentIndex().row(), 0).data())
        self.conector.closeDB()
        self.popUp_eliminarProducto.cerrarPopup()
        self.popUp_confirmacion = popUp('Producto eliminado Exitosamente.', 'Aviso', False, 'informativo', 'Ok')
        self.popUp_confirmacion.exec()



class ventanaRegistrarVentaDatosCliente(QDialog):
    def __init__(self):
        super(ventanaRegistrarVentaDatosCliente, self).__init__()
        self.ui = Ui_Dialogvrvdc()
        self.ui.setupUi(self)
        self.ui.botonOK.clicked.connect(self.popUpConfirmarDatosCliente)
        self.setWindowTitle("Datos Cliente")
        self.setWindowModality(2)

    def popUpConfirmarDatosCliente(self):
        self.popUp_ConfirmarDatosCliente = popUp('¿Los datos ingresados son correctos? '+'\n\nCedula: '+str(self.ui.textCedula.toPlainText())+
        '\nNombre: '+str(self.ui.textNombre.toPlainText())+'\nTelefono: '+str(self.ui.textTelefono.toPlainText()), 'Datos Cliente', True,
        'dubitativo', 'Confirmar', 'Cancelar')
        # SEGUIMOS TRABAJANDO AQUI ###############################
        ###################### NO ESTA TERMINADO HIJOS DE PUTA
        ##################### WORK IN PROGRESS
        self.popUp_ConfirmarDatosCliente.exec()

class ventanaRegistrarVenta(QDialog):
    def __init__(self):
        super(ventanaRegistrarVenta, self).__init__()
        self.ui = Ui_Dialogvrv()
        self.ui.setupUi(self)
        self.ui.pushButtonFinzalizar.clicked.connect(self.popUpFinalizarVenta)
        self.setWindowTitle("Registrar Venta")
        self.setWindowModality(2)
        self.conector = ConexionDataBase()
        self.conector.openDB()
        self.query1 = QtSql.QSqlQuery()
        self.query1.exec_("select nombre,cantidad,precio,iva from producto;")
        model = QtSql.QSqlTableModel()
        model.setQuery(self.query1)
        self.conector.closeDB()
        model.insertColumn(4)
        model.setHeaderData(4, QtCore.Qt.Horizontal, str("Añadir"))
        filter_proxy_model = QtCore.QSortFilterProxyModel()
        filter_proxy_model.setFilterCaseSensitivity(0)
        filter_proxy_model.setSourceModel(model)
        filter_proxy_model.setFilterKeyColumn(0)
        self.ui.BarraBusqueda.textChanged.connect(filter_proxy_model.setFilterRegExp)
        self.ui.tableInventario.setModel(filter_proxy_model)
        self.ui.tableInventario.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.model1 = QStandardItemModel(0,5)
        self.ui.tableVenta.setModel(self.model1)
        self.ui.tableInventario.selectionModel().currentRowChanged.connect(self.anadirProductoVenta)

    def anadirProductoVenta(self):
        producto = self.conector.busquedaProducto(self.ui.tableInventario.model().index(self.ui.tableInventario.currentIndex().row(), 0).data())
        nombre = QStandardItem(producto.getNombre())
        #cantidad = QStandardItem(str(producto.getCantidad()))
        precio = QStandardItem(str(producto.getPrecio()))
        iva = QStandardItem(str(producto.getIva()))
        filas = self.model1.rowCount()
        self.model1.setItem(filas, 0, nombre)
        #self.model1.setItem(filas, 1, cantidad)
        self.model1.setItem(filas, 2, precio)
        self.model1.setItem(filas, 3, iva)
        self.ui.tableVenta.setModel(self.model1)

    def irProximaVentana(self):
        print(self.ui.tableInventario.model().index(self.ui.tableInventario.currentIndex().row(), 0).data())



    def popUpFinalizarVenta(self):
        self.popUp_FinalizarVenta = popUp('Desea confirmar la venta', 'Finalizar Venta', True, 'dubitativo', 'Confirmar', 'Cancelar')
        self.popUp_FinalizarVenta.buttons()[1].pressed.connect(self.irVentanaRegistrarVentaDatosCliente)
        self.popUp_FinalizarVenta.buttons()[0].pressed.connect(self.close)
        self.popUp_FinalizarVenta.exec()

    def irVentanaRegistrarVentaDatosCliente(self):
        self.ventana_VentanaRegistrarVentaDatosCliente = ventanaRegistrarVentaDatosCliente()
        self.ventana_VentanaRegistrarVentaDatosCliente.show()

class popUp(QMessageBox): # ventanas emergentes.
    #Ventana emergente con 2 opciones
    def __init__(self, mensaje='', tituloVentana='', boolBoton = '', tipo='', botonSi = '', botonNo=''):
        super(popUp, self).__init__()
        self.setIcon(tipoPopUp(tipo))
        self.setWindowTitle(tituloVentana)
        self.setInformativeText(mensaje)
        if(boolBoton == True):
            self.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Cancel)
            self.button(QtWidgets.QMessageBox.Yes).setText(botonSi)
            self.button(QtWidgets.QMessageBox.Cancel).setText(botonNo)
        else:
            self.setStandardButtons(QtWidgets.QMessageBox.Ok)
            self.button(QtWidgets.QMessageBox.Ok).setText(botonSi)
    def cerrarPopup(self):
        self.close()

class ventanaAnadirProducto(QDialog):

    def __init__(self):
        super(ventanaAnadirProducto, self).__init__()
        self.ui = Ui_Dialogap()
        self.ui.setupUi(self)
        self.ui.botonVolver.clicked.connect(self.volver)
        self.ui.botonAnadir.clicked.connect(self.validarIngreso)
        self.conector = ConexionDataBase()
        self.setWindowTitle("Añadir Producto")
        self.setWindowModality(2)

    def validarIngreso(self):
        if ((len(self.ui.campoTextoNombre.toPlainText()) == 0) or (len(self.ui.campoTextoPrecio.toPlainText()) == 0) or (len(self.ui.campoTextoCantidad.toPlainText()) == 0) or
        ((self.ui.radioSi.isChecked() == False) and (self.ui.radioNo.isChecked() == False))):
            self.popUp_AdvertenciaDatoIncompleto = popUp('No se llenaron todos los datos requeridos.', 'Error', False, 'informativo', 'Ok')
            self.popUp_AdvertenciaDatoIncompleto.exec()
        else: #Validar
            validador = Validaciones()
            if ((validador.isNotFloat(self.ui.campoTextoPrecio.toPlainText())) or (validador.isNotDigit(self.ui.campoTextoCantidad.toPlainText())) or (validador.isNotAlpha(self.ui.campoTextoNombre.toPlainText()))):
                self.popUp_AdvertenciaDatoIncorrecto = popUp('Algún dato se ingresó de manera incorrecta.', 'Error', False, 'advertencia', 'Ok')
                self.popUp_AdvertenciaDatoIncorrecto.exec()
            else:
                if(self.conector.validarProducto(self.ui.campoTextoNombre.toPlainText())):
                    self.popUp_ProductoExistente = popUp('El nombre del producto ingresado ya se encuentra registrado.', 'Error', False, 'informativo', 'Ok')
                    self.popUp_ProductoExistente.exec_()
                else:
                    if (self.ui.radioSi.isChecked() == True):
                        self.conector.insertProducto(self.ui.campoTextoNombre.toPlainText(), self.ui.campoTextoCantidad.toPlainText(), self.ui.campoTextoPrecio.toPlainText(), True)
                    else:
                        self.conector.insertProducto(self.ui.campoTextoNombre.toPlainText(), self.ui.campoTextoCantidad.toPlainText(), self.ui.campoTextoPrecio.toPlainText(), False)
                    self.popUp_InfoDatosCorrectos = popUp('Se agregó el nuevo producto exitosamente.', 'Éxito', False, 'informativo', 'Ok')
                    self.popUp_InfoDatosCorrectos.buttons()[0].pressed.connect(self.close)
                    self.popUp_InfoDatosCorrectos.exec()

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
