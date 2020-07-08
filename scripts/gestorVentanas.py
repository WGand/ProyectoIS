#Import basura de QT
from PyQt5 import uic
from PyQt5.QtWidgets import QHeaderView, QMainWindow, QDialog, QMessageBox, QVBoxLayout, QTableView
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
from ventanaAnadirCantidadVenta import Ui_Dialogvacv
from ventanaRegistrarUsuario import Ui_QDialogvru
from ventanaGestionarUsuario import Ui_Dialogvgu
#Import Database
from manejadorDataBase import ConexionDataBase
from objetosPrograma import Venta, Producto, Cliente

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

    def doesnthasSpace(self, string_):
        for letra in string_:
            if(letra == ' '):
                return False
        return True

    def isNotDigit(self, string_):
        try:
            int(string_)
            return False
        except ValueError:
            return True
    
    def hasNumber(self, string_):
        for letra in string_:
            if(letra.isdigit() == True):
                return True
        return False

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
        self.db = ConexionDataBase()
        self.result = self.db.recorrerProducto()
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Nombre','Cantidad','Precio','IVA','Modificar'])
        self.columnas = 4
        self.nombreModificar = ''
        self.filaModificar = 0
        self.fila = len(self.result)
        for filas in range(self.fila):
            objects = self.result[filas]
            self.model.setItem(filas, 0, QtGui.QStandardItem(objects.getNombre()))
            self.model.setItem(filas, 1, QtGui.QStandardItem(str(objects.getCantidad())))
            self.model.setItem(filas, 2, QtGui.QStandardItem(str(objects.getPrecio())))
            self.model.setItem(filas, 3, QtGui.QStandardItem(str(objects.getIva())))
            self.model.setItem(filas, 4, QtGui.QStandardItem("Modificar"))
        self.filtro = QtCore.QSortFilterProxyModel()
        self.filtro.setFilterCaseSensitivity(0)
        self.filtro.setSourceModel(self.model)
        self.filtro.setFilterKeyColumn(0)
        self.ui.lineEdit.textChanged.connect(self.filtro.setFilterRegExp)
        self.ui.tableView.setModel(self.filtro)
        self.ui.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ui.tableView.setColumnWidth(0, self.width()/4)
        self.ui.tableView.setColumnWidth(1, self.width()/6)
        self.ui.tableView.setColumnWidth(2, self.width()/4)
        self.ui.tableView.setColumnWidth(3, self.width()/6)
        self.ui.tableView.setColumnWidth(4, self.width()/7)
        self.ui.tableView.clicked.connect(self.irVentanaModificarCantidad)
        self.ui.botonVolver.clicked.connect(self.irVolver)

    def irVentanaModificarCantidad(self):
        if(self.ui.tableView.currentIndex().column() != 0):
            self.nombreModificar = self.ui.tableView.model().index(self.ui.tableView.currentIndex().row(), 0).data()
            self.filaModificar = self.ui.tableView.currentIndex().row()
            self.ventana_ModificarCantidad = ventanaModificarCantidad(self, self.ui.tableView.model().index(self.ui.tableView.currentIndex().row(), 0).data())
            self.ventana_ModificarCantidad.show()

    def cambiarDato(self):
        productoNuevo = self.db.busquedaProducto(self.nombreModificar)
        self.model.setItem(self.filaModificar, 1, QtGui.QStandardItem(str(productoNuevo.getCantidad())))


    def irVolver(self):
        self.close()

class ventanaModificarCantidad(QDialog):
    def __init__(self, ventana, nombre):
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
        self.ui.botonOk.pressed.connect(self.popUpConfirmarCantidad)
        self.setWindowTitle("Modificar Cantidad")
        self.setWindowModality(2)
        self.ventana = ventana

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
        self.popUp_ConfirmarCantidad = popUp('El producto '+self.producto_.getNombre()+' tiene una cantidad existente de '
        +str(self.cantidadActual)+' unidades registrada \n¿Desea actualizar a: '+str(self.producto_.getCantidad())+' unidades?','Confirmar Cambios',
        True, 'dubitativo', 'Confirmar', 'Cancelar' )
        self.popUp_ConfirmarCantidad.buttons()[1].pressed.connect(self.guardarCambios)
        self.popUp_ConfirmarCantidad.buttons()[0].pressed.connect(self.close)
        self.popUp_ConfirmarCantidad.cerrarPopup()
        self.popUp_ConfirmarCantidad.exec_()

    def irVolver(self):
        self.close()

    def guardarCambios(self):
        self.conector.modificarCantidadProducto(self.producto_.getCantidad(), self.producto_.getNombre())
        self.ventana.cambiarDato()
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
        self.ventana_ModificarProducto = ventanaModificarProducto()
        self.ventana_ModificarProducto.show()

    def irEliminarProducto(self):
        self.ventana_EliminarProducto = ventanaEliminarProducto()
        self.ventana_EliminarProducto.show()

class ventanaModificarProducto(QDialog):
    def __init__(self):
        super(ventanaModificarProducto, self).__init__()
        self.ui = Ui_Dialogvmp()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.volver)
        self.setWindowTitle("Modificar Producto")
        self.setWindowModality(2)
        self.conector = ConexionDataBase()
        self.result = self.conector.recorrerProducto()
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Nombre', 'Cantidad', 'Precio', 'IVA'])
        self.columnas = 3
        self.fila = len(self.result)
        for filas in range(self.fila):
            objects = self.result[filas]
            self.model.setItem(filas, 0, QtGui.QStandardItem(objects.getNombre()))
            self.model.setItem(filas, 1, QtGui.QStandardItem(str(objects.getCantidad())))
            self.model.setItem(filas, 2, QtGui.QStandardItem(str(objects.getPrecio())))
            self.model.setItem(filas, 3, QtGui.QStandardItem(str(objects.getIva())))
        self.filtro = QtCore.QSortFilterProxyModel()
        self.filtro.setFilterCaseSensitivity(0)
        self.filtro.setSourceModel(self.model)
        self.filtro.setFilterKeyColumn(0)
        self.ui.campoTexto.textChanged.connect(self.filtro.setFilterRegExp)
        self.ui.tableView.setModel(self.filtro)
        self.ui.tableView.selectionModel().currentChanged.connect(self.irProximaVentana)
        self.ui.pushButton.clicked.connect(self.volver)

    def llenarTabla(self):
        self.conector = ConexionDataBase()
        self.result = self.conector.recorrerProducto()
        self.fila = len(self.result)
        for filas in range(self.fila):
            objects = self.result[filas]
            self.model.setItem(filas, 0, QtGui.QStandardItem(objects.getNombre()))
            self.model.setItem(filas, 1, QtGui.QStandardItem(str(objects.getCantidad())))
            self.model.setItem(filas, 2, QtGui.QStandardItem(str(objects.getPrecio())))
            self.model.setItem(filas, 3, QtGui.QStandardItem(str(objects.getIva())))

    def irProximaVentana(self):
        if(self.ui.tableView.currentIndex().column() != 0):
            nombre = self.ui.tableView.model().index(self.ui.tableView.currentIndex().row(), 0).data()
            precio = self.ui.tableView.model().index(self.ui.tableView.currentIndex().row(), 2).data()
            iva = self.ui.tableView.model().index(self.ui.tableView.currentIndex().row(), 3).data()
            self.ventanaModificarProductoCampos = ventanaModificarProductoCampos(self, nombre, precio ,iva)
            self.ventanaModificarProductoCampos.show()

    def volver(self):
        self.close()

class ventanaModificarProductoCampos(QDialog):
    def __init__(self, ventana, nombre, precio, iva):
        super(ventanaModificarProductoCampos, self).__init__()
        self.ui = Ui_Dialogvmpc()
        self.ui.setupUi(self)
        self.ui.botonCancelar.clicked.connect(self.volver)
        self.ui.campoNombre.setPlainText(nombre)
        self.conector = ConexionDataBase()
        self.ui.campoPrecio.setPlainText(str(precio))
        if iva == True:
            self.ui.radioButtonSi.setChecked(True)
            self.ui.radioButtonNo.setChecked(False)
        else:
            self.ui.radioButtonNo.setChecked(True)
            self.ui.radioButtonSi.setChecked(False)
        self.setWindowTitle("Modificar Producto")
        self.setWindowModality(2)
        self.ui.okBoton.clicked.connect(self.validarIngreso)
        self.nombre = nombre
        self.precio = precio
        self.iva = iva
        self.ventana = ventana

    def validarIngreso(self):
        if ((len(self.ui.campoNombre.toPlainText()) == 0) or (len(self.ui.campoPrecio.toPlainText()) == 0) or ((self.ui.radioButtonSi.isChecked() == False) and (self.ui.radioButtonNo.isChecked() == False))):
            self.popUp_AdvertenciaDatoIncompleto = popUp('No se llenaron todos los datos requeridos.', 'Error', False, 'informativo', 'Ok')
            self.popUp_AdvertenciaDatoIncompleto.cerrarPopup()
            self.popUp_AdvertenciaDatoIncompleto.exec()
        else: #Validar
            validador = Validaciones()
            if ((validador.isNotFloat(self.ui.campoPrecio.toPlainText())) or (validador.isNotAlpha(self.ui.campoNombre.toPlainText()))):
                self.popUp_AdvertenciaDatoIncorrecto = popUp('Algún dato se ingresó con caracteres invalidos.', 'Error', False, 'advertencia', 'Ok')
                self.popUp_AdvertenciaDatoIncorrecto.cerrarPopup()
                self.popUp_AdvertenciaDatoIncorrecto.exec()
            else:
                self.conector.modificarPrecioProducto(self.ui.campoPrecio.toPlainText(),self.nombre)
                if (self.ui.radioButtonSi.isChecked() == True):
                    self.conector.modificarIvaProducto("True",self.nombre)
                elif(self.ui.radioButtonSi.isChecked() == False):
                    self.conector.modificarIvaProducto("False",self.nombre)
                self.conector.modificarNombreProducto(self.ui.campoNombre.toPlainText(),self.nombre)
                self.popUp_ModificarProducto = popUp('¿Desea modificar otro producto?', 'Producto modificado correctamente', True, 'informativo', 'Si', 'No')

                self.popUp_ModificarProducto.buttons()[1].pressed.connect(self.cerrarPopUp)
                self.popUp_ModificarProducto.buttons()[0].pressed.connect(self.cerrarTodo)#NO
                self.popUp_ModificarProducto.exec()

    def cerrarPopUp(self):
        self.ventana.llenarTabla()
        self.popUp_ModificarProducto.close()
        self.close()

    def volver(self):
        self.close()

    def cerrarTodo(self):
        self.popUp_ModificarProducto.close()
        self.ventana.close()
        self.close()

class ventanaEliminarProducto(QDialog):
    def __init__(self):
        super(ventanaEliminarProducto, self).__init__()
        self.ui = Ui_Dialogvep()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.volver)
        self.setWindowTitle("Eliminar Producto")
        self.setWindowModality(2)
        self.conector = ConexionDataBase()
        self.result = self.conector.recorrerProductoCero()
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Nombre', 'Cantidad', 'Precio', 'IVA'])
        self.columnas = 3
        self.fila = len(self.result)
        for filas in range(self.fila):
            objects = self.result[filas]
            self.model.setItem(filas, 0, QtGui.QStandardItem(objects.getNombre()))
            self.model.setItem(filas, 1, QtGui.QStandardItem(str(objects.getCantidad())))
            self.model.setItem(filas, 2, QtGui.QStandardItem(str(objects.getPrecio())))
            self.model.setItem(filas, 3, QtGui.QStandardItem(str(objects.getIva())))
        self.filtro = QtCore.QSortFilterProxyModel()
        self.filtro.setFilterCaseSensitivity(0)
        self.filtro.setSourceModel(self.model)
        self.filtro.setFilterKeyColumn(0)
        self.ui.campoTexto.textChanged.connect(self.filtro.setFilterRegExp)
        self.ui.tableView.setModel(self.filtro)
        self.ui.tableView.selectionModel().currentChanged.connect(self.popUpEliminarProducto)
        self.ui.pushButton.clicked.connect(self.volver)

    def llenarTabla(self):
        self.conector = ConexionDataBase()
        self.result = self.conector.recorrerProductoCero()
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Nombre', 'Cantidad', 'Precio', 'IVA'])
        self.columnas = 3
        self.fila = len(self.result)
        for filas in range(self.fila):
            objects = self.result[filas]
            self.model.setItem(filas, 0, QtGui.QStandardItem(objects.getNombre()))
            self.model.setItem(filas, 1, QtGui.QStandardItem(str(objects.getCantidad())))
            self.model.setItem(filas, 2, QtGui.QStandardItem(str(objects.getPrecio())))
            self.model.setItem(filas, 3, QtGui.QStandardItem(str(objects.getIva())))
        self.filtro = QtCore.QSortFilterProxyModel()
        self.filtro.setFilterCaseSensitivity(0)
        self.filtro.setSourceModel(self.model)
        self.filtro.setFilterKeyColumn(0)
        self.ui.campoTexto.textChanged.connect(self.filtro.setFilterRegExp)
        self.ui.tableView.setModel(self.filtro)
        #self.ui.tableView.selectionModel().currentChanged.connect(self.irProximaVentana)
        self.ui.pushButton.clicked.connect(self.volver)

    def volver(self):
        self.close()        

    def popUpEliminarProducto(self):
        self.productoEliminar = self.conector.busquedaProducto(self.ui.tableView.model().index(self.ui.tableView.currentIndex().row(), 0).data())
        self.popUp_EliminarProducto = popUp('Se eliminara el producto: '+self.productoEliminar.getNombre()+'\n¿Desea continuar?', 'Eliminar', True, 'advertencia', 'Confirmar', 'Cancelar')    
        self.popUp_EliminarProducto.buttons()[1].pressed.connect(self.eliminarProducto)
        self.popUp_EliminarProducto.cerrarPopup()
        self.popUp_EliminarProducto.exec_()

    def eliminarProducto(self):
        self.conector.deleteProducto(self.productoEliminar.getNombre())
        self.llenarTabla()

class ventanaAnadirCantidadVenta(QDialog):
    def __init__(self, ventana, nombre):
        super(ventanaAnadirCantidadVenta, self).__init__()
        self.ui = Ui_Dialogvacv()
        self.ui.setupUi(self)
        self.conector = ConexionDataBase()
        self.producto_ = self.conector.busquedaProducto(nombre)
        self.productoVenta = Producto(self.producto_.getNombre(), 0, self.producto_.getPrecio(), self.producto_.getIva())
        self.cantidadActual = self.producto_.getCantidad()
        self.ui.botonMenos.setDisabled(True)
        if (self.producto_.getCantidad() == 0):
            self.ui.botonMas.setDisabled(True)
        self.ui.textCantidad.setText('0')
        self.ui.labelInformacion.setText('Producto: '+str(self.producto_.getNombre())+'\nCantidad actual: '+str(self.producto_.getCantidad())+'\nPrecio: '+ str(self.producto_.getPrecio()))
        self.ui.botonMas.clicked.connect(self.sumar)
        self.ui.botonMenos.clicked.connect(self.restar)
        self.ui.textCantidad.setReadOnly(True)
        self.ui.botonOk.pressed.connect(self.popUpConfirmarCantidad)
        self.setWindowTitle("Modificar Cantidad")
        self.setWindowModality(2)
        self.ventana = ventana

    def sumar(self):
        sumando = int(self.ui.textCantidad.toPlainText())
        if(sumando == 0):
            self.ui.botonMenos.setEnabled(True)
        sumando += 1
        self.ui.textCantidad.setText(str(sumando))
        self.productoVenta.setCantidad(int(self.ui.textCantidad.toPlainText()))
        if((self.productoVenta.getCantidad()) == (self.producto_.getCantidad())):
            self.ui.botonMas.setDisabled(True)

    def restar(self):
        restando = int(self.ui.textCantidad.toPlainText())
        if(restando < (self.producto_.getCantidad())):
            self.ui.botonMas.setEnabled(True)
        if(restando == 1):
            self.ui.botonMenos.setDisabled(True)
        restando -= 1
        self.ui.textCantidad.setText(str(restando))
        self.productoVenta.setCantidad(int(self.ui.textCantidad.toPlainText()))

        
    def popUpConfirmarCantidad(self):
        self.popUp_ConfirmarCantidad = popUp('Añadiendo '+str(self.productoVenta.getCantidad()) +' unidades del producto '+str(self.productoVenta.getNombre()),'Confirmar',
        True, 'informativo', 'Confirmar', 'Cancelar' )
        self.popUp_ConfirmarCantidad.buttons()[1].pressed.connect(self.guardarCambios)
        self.popUp_ConfirmarCantidad.buttons()[0].pressed.connect(self.close)
        self.popUp_ConfirmarCantidad.cerrarPopup()
        self.popUp_ConfirmarCantidad.exec_()

    def guardarCambios(self):
        if(self.productoVenta.getCantidad() > 0):    
            self.producto_.setCantidad(self.producto_.getCantidad() - self.productoVenta.getCantidad())
            self.ventana.venta.addProducto(self.productoVenta)
            self.ventana.anadirProductoVenta(self.productoVenta)
            self.ventana.actualizarMonto()
            self.conector.modificarCantidadProducto(self.producto_.getCantidad(), self.producto_.getNombre())
            self.ventana.cambiarDatoInventario()
        self.irVolver()

    def irVolver(self):
        self.close()

class ventanaRegistrarVentaDatosCliente(QDialog):
    def __init__(self, ventana):
        super(ventanaRegistrarVentaDatosCliente, self).__init__()
        self.ui = Ui_Dialogvrvdc()
        self.ui.setupUi(self)
        self.ventana = ventana
        self.ui.botonOK.clicked.connect(self.validadorDatos)
        self.setWindowTitle("Datos Cliente")
        self.setWindowModality(2)

    def validadorDatos(self):
        validador = Validaciones()
        if((len(self.ui.textCedula.toPlainText()) == 0) or (len(self.ui.textNombre.toPlainText()) == 0) or (len(self.ui.textTelefono.toPlainText()) == 0)):
            self.popUp_AdvertenciaDatoIncompleto = popUp('No se llenaron todos los datos requeridos.', 'Error', False, 'informativo', 'Ok')
            self.popUp_AdvertenciaDatoIncompleto.cerrarPopup()
            self.popUp_AdvertenciaDatoIncompleto.exec()
        elif(validador.isNotDigit(self.ui.textCedula.toPlainText()) or validador.isNotDigit(self.ui.textTelefono.toPlainText()) or validador.isNotAlpha(self.ui.textNombre.toPlainText())):
            self.popUp_AdvertenciaDatoInvalido = popUp('Algún dato contiene carácteres inválidos.', 'Error', False, 'informativo', 'Ok')
            self.popUp_AdvertenciaDatoInvalido.cerrarPopup()
            self.popUp_AdvertenciaDatoInvalido.exec()
        elif(((len(self.ui.textCedula.toPlainText()) != 8) and (len(self.ui.textCedula.toPlainText()) != 7)) or ((len(self.ui.textTelefono.toPlainText()) < 10)) or (len(self.ui.textTelefono.toPlainText()) > 11)):
            self.popUp_AdvertenciaDatoInvalido = popUp('Algún dato contiene no cumple con el rango adecuado.', 'Error', False, 'informativo', 'Ok')
            self.popUp_AdvertenciaDatoInvalido.cerrarPopup()
            self.popUp_AdvertenciaDatoInvalido.exec()
        else:
            self.popUpConfirmarDatosCliente()
    
    def popUpConfirmarDatosCliente(self):
        self.popUp_ConfirmarDatosCliente = popUp('¿Los datos ingresados son correctos? '+'\n\nCedula: '+str(self.ui.textCedula.toPlainText())+
        '\nNombre: '+str(self.ui.textNombre.toPlainText())+'\nTelefono: '+str(self.ui.textTelefono.toPlainText()), 'Datos Cliente', True,
        'dubitativo', 'Confirmar', 'Cancelar')
        self.popUp_ConfirmarDatosCliente.buttons()[1].clicked.connect(self.guardarDatosCliente)
        self.popUp_ConfirmarDatosCliente.exec()
    
    def guardarDatosCliente(self):
        self.popUp_ConfirmarDatosCliente.cerrarPopup()
        self.ventana.venta.setCliente(Cliente(str(self.ui.textNombre.toPlainText()), int(self.ui.textCedula.toPlainText()), int(self.ui.textTelefono.toPlainText())))
        self.conector = ConexionDataBase()
        self.conector.guardarVenta(self.ventana.venta)
        self.popUpListo()
        
    def popUpListo(self):
        self.popUp_Listo = popUp('Se ha registrado exitosamente la venta.', 'Exito', False, 'informativo', 'Ok')
        self.popUp_Listo.buttons()[0].pressed.connect(self.cerrarFinalizado)
        self.popUp_Listo.cerrarPopup()
        self.popUp_Listo.exec()
    
    def cerrarFinalizado(self):
        self.close()
        self.ventana.cerrarSignal()

class ventanaRegistrarUsuario(QDialog):
    def __init__(self):
        super(ventanaRegistrarUsuario, self).__init__()
        self.ui = Ui_QDialogvru()
        self.ui.setupUi(self)
        self.ui.labelCheck.setVisible(False)
        self.ui.labelX.setVisible(False)
        self.ui.buttonAceptar.setDisabled(True)
        self.ui.buttonVolver.clicked.connect(self.close)
        self.ui.lineEditContrasena.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.lineEditConfirmacion.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.lineEditContrasena.textChanged.connect(self.confirmacionContrasena)
        self.ui.lineEditConfirmacion.textChanged.connect(self.confirmacionContrasena)
        self.ui.lineEditUsuario.textChanged.connect(self.validarIngreso)
        self.ui.buttonAceptar.clicked.connect(self.verificarUsuario)
    
    def confirmacionContrasena(self):
        validador = Validaciones()
        if(self.ui.lineEditContrasena.text() == ''):
            return 0
        elif(str(self.ui.lineEditContrasena.text()) != str(self.ui.lineEditConfirmacion.text())):
            self.ui.labelCheck.setVisible(False)
            self.ui.labelX.setVisible(True)
        elif(str(self.ui.lineEditContrasena.text()) == str(self.ui.lineEditConfirmacion.text()) and (validador.hasNumber(self.ui.lineEditContrasena.text()))):
            self.ui.labelX.setVisible(False)
            self.ui.labelCheck.setVisible(True)
        self.validarIngreso()
    
    def validarIngreso(self):
        if((str(self.ui.lineEditUsuario.text()) != '') and (str(self.ui.lineEditContrasena.text()) != '') and (str(self.ui.lineEditConfirmacion.text()) != '')):
            validador = Validaciones()
            if((validador.doesnthasSpace(self.ui.lineEditUsuario.text())) and (len(self.ui.lineEditContrasena.text()) >= 7) and (validador.hasNumber(self.ui.lineEditContrasena.text()))
            and (self.ui.lineEditContrasena.text() == self.ui.lineEditConfirmacion.text())):
                self.ui.buttonAceptar.setEnabled(True)
            else:
                self.ui.buttonAceptar.setDisabled(True)
        else:
            self.ui.buttonAceptar.setDisabled(True)
    
    def verificarUsuario(self):
        conexion = ConexionDataBase()
        if(conexion.validarUsuario(self.ui.lineEditUsuario.text())):
            self.popUpUsuarioError()
        else:
            if(self.ui.radioButtonSi.isChecked()):
                adminBool = True
            else:
                adminBool = False
            conexion.insertUsuario(self.ui.lineEditUsuario.text(), self.ui.lineEditContrasena.text(), adminBool)
            self.popUpUsuarioCreado()
    
    def popUpUsuarioError(self):
        self.popUp_UsuarioError = popUp('El usuario ingresado ya se encuentra en el sistema.', '', False, 'advertencia', 'Ok')
        self.popUp_UsuarioError.exec_()

    def popUpUsuarioCreado(self):
        self.popUp_UsuarioCreado = popUp('El usuario se ha creado exitosamente.', '', False, 'informativo', 'Ok')
        self.popUp_UsuarioCreado.buttons()[0].pressed.connect(self.close)
        self.popUp_UsuarioCreado.exec_()

class ventanaGestionarUsuario(QDialog):
    def __init__(self):    
        super(ventanaGestionarUsuario, self).__init__()
        self.ui = Ui_Dialogvgu()
        self.ui.setupUi(self)
        self.ui.botonAnadirUsuario.clicked.connect(self.irVentanaRegistrarUsuario)
        self.ui.botonVolver.clicked.connect(self.close)
    
    def irVentanaRegistrarUsuario(self):
        self.ventana_RegistrarUsuario = ventanaRegistrarUsuario()
        self.ventana_RegistrarUsuario.show()

class ventanaRegistrarVenta(QDialog):
    def __init__(self):
        super(ventanaRegistrarVenta, self).__init__()
        self.ui = Ui_Dialogvrv()
        self.ui.setupUi(self)
        self.ui.pushButtonFinzalizar.clicked.connect(self.popUpFinalizarVenta)
        self.setWindowTitle("Registrar Venta")
        self.setWindowModality(2)
        self.venta = Venta()
        self.db = ConexionDataBase()
        self.actualizarMonto()
        self.result = self.db.recorrerProducto()
        self.model = QStandardItemModel()
        self.modelVenta = QStandardItemModel()
        self.modelVenta.setHorizontalHeaderLabels(['Nombre','Cantidad','Precio','IVA','Anular'])
        self.filtroVenta =  QtCore.QSortFilterProxyModel()
        self.filtroVenta.setFilterCaseSensitivity(0)
        self.filtroVenta.setSourceModel(self.modelVenta)
        self.filtroVenta.setFilterKeyColumn(0)
        self.ui.BarraBusquedaVenta.textChanged.connect(self.filtroVenta.setFilterRegExp)
        self.ui.tableVenta.setModel(self.filtroVenta)
        self.model.setHorizontalHeaderLabels(['Nombre','Cantidad','Precio','IVA','Añadir'])
        self.columnas = 4
        self.nombreModificar = ''
        self.filaModificar = 0
        self.fila = len(self.result)
        for filas in range(self.fila):
            objects = self.result[filas]
            self.model.setItem(filas, 0, QtGui.QStandardItem(objects.getNombre()))
            self.model.setItem(filas, 1, QtGui.QStandardItem(str(objects.getCantidad())))
            self.model.setItem(filas, 2, QtGui.QStandardItem(str(objects.getPrecio())))
            self.model.setItem(filas, 3, QtGui.QStandardItem(str(objects.getIva())))
            self.model.setItem(filas, 4, QtGui.QStandardItem("Añadir"))
        self.filtro = QtCore.QSortFilterProxyModel()
        self.filtro.setFilterCaseSensitivity(0)
        self.filtro.setSourceModel(self.model)
        self.filtro.setFilterKeyColumn(0)
        self.ui.BarraBusqueda.textChanged.connect(self.filtro.setFilterRegExp)
        self.ui.tableInventario.setModel(self.filtro)
        self.ui.tableInventario.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ui.tableVenta.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ui.tableInventario.clicked.connect(self.irVentanaAnadirCantidadVenta)
        self.ui.tableInventario.setColumnWidth(1, self.width()/11)
        self.ui.tableInventario.setColumnWidth(2, self.width()/8)
        self.ui.tableInventario.setColumnWidth(0, self.width()/9)
        self.ui.tableInventario.setColumnWidth(3, self.width()/12)
        self.ui.tableInventario.setColumnWidth(4, self.width()/14)
        self.ui.tableVenta.setColumnWidth(1, self.width()/11)
        self.ui.tableVenta.setColumnWidth(2, self.width()/8)
        self.ui.tableVenta.setColumnWidth(0, self.width()/9)
        self.ui.tableVenta.setColumnWidth(3, self.width()/12)
        self.ui.tableVenta.setColumnWidth(4, self.width()/14)
        if(self.ui.tableVenta.currentIndex().column() != 0 or (self.ui.tableVenta.model().index(self.ui.tableVenta.selectionModel().currentIndex().row(),0).data() != '')):
            self.ui.tableVenta.clicked.connect(self.popUpEliminarProductoVenta)

    def irVentanaAnadirCantidadVenta(self):
        if(self.ui.tableInventario.currentIndex().column() != 0):
            self.nombreModificar = self.ui.tableInventario.model().index(self.ui.tableInventario.currentIndex().row(), 0).data()
            self.filaModificar = self.ui.tableInventario.currentIndex().row()
            self.ventana_AnadirCantidadVenta = ventanaAnadirCantidadVenta(self, self.ui.tableInventario.model().index(self.ui.tableInventario.currentIndex().row(), 0).data())
            self.ventana_AnadirCantidadVenta.show()

    def actualizarMonto(self):
        self.ui.labelMonto.setText(self.venta.truncate(self.venta.getMonto(), 2))

    def cerrar(self):
        if(self.venta.getProducto()):
            for producto_ in self.venta.getProducto():
                cantidadeliminar = producto_.getCantidad()
                nombreeliminar = producto_.getNombre()
                protocolo = self.db.busquedaProducto(nombreeliminar)
                self.db.modificarCantidadProducto((cantidadeliminar + protocolo.getCantidad()), nombreeliminar)
        self.close()

    def anadirProductoVenta(self, producto):
        productoJodedor = self.venta.getProducto()
        objeto = Producto('','','','')
        for filas in range(len(self.venta.getProducto())):
            objeto.setNombre(productoJodedor[filas].getNombre())
            objeto.setCantidad(productoJodedor[filas].getCantidad())
            objeto.setPrecio(productoJodedor[filas].getPrecio())
            objeto.setIva(productoJodedor[filas].getIva())
            self.modelVenta.setItem(filas, 0, QtGui.QStandardItem(str(objeto.getNombre())))
            self.modelVenta.setItem(filas, 1, QtGui.QStandardItem(str(objeto.getCantidad())))
            self.modelVenta.setItem(filas, 2, QtGui.QStandardItem(str(objeto.getPrecio())))
            self.modelVenta.setItem(filas, 3, QtGui.QStandardItem(str(objeto.getIva())))
            self.modelVenta.setItem(filas, 4, QtGui.QStandardItem("Anular"))
        self.ui.tableVenta.setColumnWidth(1, self.width()/11)
        self.ui.tableVenta.setColumnWidth(2, self.width()/8)
        self.ui.tableVenta.setColumnWidth(0, self.width()/9)
        self.ui.tableVenta.setColumnWidth(3, self.width()/12)
        self.ui.tableVenta.setColumnWidth(4, self.width()/14)
        self.actualizarMonto()

    def cambiarDatoInventario(self):
        productoNuevo = self.db.busquedaProducto(self.nombreModificar)
        self.model.setItem(self.filaModificar, 1, QtGui.QStandardItem(str(productoNuevo.getCantidad())))

    def popUpEliminarProductoVenta(self):  
        if(self.ui.tableVenta.currentIndex().column() != 0 and (self.ui.tableVenta.model().index(self.ui.tableVenta.selectionModel().currentIndex().row(),0).data() != '')):
            self.popUp_EliminarProductoVenta = popUp('Se eliminara el producto de la venta', 'Confirmar', True, 'advertencia', 'Confirmar', 'Cancelar')
            self.popUp_EliminarProductoVenta.buttons()[1].pressed.connect(self.eliminarProductoVenta)
            self.popUp_EliminarProductoVenta.cerrarPopup()
            self.popUp_EliminarProductoVenta.exec_()

    def cerrarSignal(self):
        self.close()

    def eliminarProductoVenta(self):
        if((self.ui.tableVenta.currentIndex().column() != 0) and (self.ui.tableVenta.model().index(self.ui.tableVenta.selectionModel().currentIndex().row(),0).data() != '')):
            nombreeliminar =self.ui.tableVenta.model().index(self.ui.tableVenta.selectionModel().currentIndex().row(),0).data()#nombre
            cantidadeliminar =int(self.ui.tableVenta.model().index(self.ui.tableVenta.selectionModel().currentIndex().row(),1).data())#cantidad
            for i in range(0,2):
                if(i == 1):
                        self.venta.delProducto(nombreeliminar, cantidadeliminar)
                        protocolo = self.db.busquedaProducto(nombreeliminar)
                        self.db.modificarCantidadProducto((cantidadeliminar + protocolo.getCantidad()), nombreeliminar)
                        self.cambiarDatoInventario()
                        productoJodedor = self.venta.getProducto()
                        for filas in range(len(self.venta.getProducto())):
                            objeto.setNombre(productoJodedor[filas].getNombre())
                            objeto.setCantidad(productoJodedor[filas].getCantidad())
                            objeto.setPrecio(productoJodedor[filas].getPrecio())
                            objeto.setIva(productoJodedor[filas].getIva())
                            self.modelVenta.setItem(filas, 0, QtGui.QStandardItem(str(objeto.getNombre())))
                            self.modelVenta.setItem(filas, 1, QtGui.QStandardItem(str(objeto.getCantidad())))
                            self.modelVenta.setItem(filas, 2, QtGui.QStandardItem(str(objeto.getPrecio())))
                            self.modelVenta.setItem(filas, 3, QtGui.QStandardItem(str(objeto.getIva())))
                            self.modelVenta.setItem(filas, 4, QtGui.QStandardItem("Anular"))
                elif(i == 0 ):
                    for filas in range(len(self.venta.getProducto())):
                        objeto = Producto('', '','','')
                        self.modelVenta.setItem(filas, 0, QtGui.QStandardItem(str(objeto.getNombre())))
                        self.modelVenta.setItem(filas, 1, QtGui.QStandardItem(str(objeto.getCantidad())))
                        self.modelVenta.setItem(filas, 2, QtGui.QStandardItem(str(objeto.getPrecio())))
                        self.modelVenta.setItem(filas, 3, QtGui.QStandardItem(str(objeto.getIva())))
                        self.modelVenta.setItem(filas, 4, QtGui.QStandardItem(""))
        self.ui.tableVenta.setColumnWidth(1, self.width()/11)
        self.ui.tableVenta.setColumnWidth(2, self.width()/8)
        self.ui.tableVenta.setColumnWidth(0, self.width()/9)
        self.ui.tableVenta.setColumnWidth(3, self.width()/12)
        self.ui.tableVenta.setColumnWidth(4, self.width()/14)
        self.actualizarMonto()
            
    def popUpFinalizarVenta(self):
        self.popUp_FinalizarVenta = popUp('¿Desea confirmar la venta?', 'Finalizar Venta', True, 'dubitativo', 'Confirmar', 'Cancelar')
        self.popUp_FinalizarVenta.buttons()[1].pressed.connect(self.irVentanaRegistrarVentaDatosCliente)
        self.popUp_FinalizarVenta.buttons()[0].pressed.connect(self.cerrar)
        self.popUp_FinalizarVenta.exec()

    def irVentanaRegistrarVentaDatosCliente(self):
        if(self.venta.getProducto() ):
            self.popUp_FinalizarVenta.cerrarPopup()
            self.ventana_VentanaRegistrarVentaDatosCliente = ventanaRegistrarVentaDatosCliente(self)
            self.ventana_VentanaRegistrarVentaDatosCliente.show()
        else:
            self.popUp_FinalizarVenta.close()
            self.popUp_AdvertenciaNoProducto = popUp('La venta no contiene productos.', 'Error', False, 'informativo', 'Ok')
            self.popUp_AdvertenciaNoProducto.buttons()[0].pressed.connect(self.close)
            self.popUp_AdvertenciaNoProducto.cerrarPopup()
            self.popUp_AdvertenciaNoProducto.exec()

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
                self.popUp_AdvertenciaDatoIncorrecto.cerrarPopup()
                self.popUp_AdvertenciaDatoIncorrecto.exec()
            else:
                if(self.conector.validarProducto(self.ui.campoTextoNombre.toPlainText())):
                    self.popUp_ProductoExistente = popUp('El nombre del producto ingresado ya se encuentra registrado.', 'Error', False, 'informativo', 'Ok')
                    self.popUp_ProductoExistente.cerrarPopup()
                    self.popUp_ProductoExistente.exec_()
                else:
                    if (self.ui.radioSi.isChecked() == True):
                        self.conector.insertProducto(self.ui.campoTextoNombre.toPlainText(), self.ui.campoTextoCantidad.toPlainText(), self.ui.campoTextoPrecio.toPlainText(), True)
                    else:
                        self.conector.insertProducto(self.ui.campoTextoNombre.toPlainText(), self.ui.campoTextoCantidad.toPlainText(), self.ui.campoTextoPrecio.toPlainText(), False)
                    self.popUp_InfoDatosCorrectos = popUp('Se agregó el nuevo producto exitosamente.', 'Éxito', False, 'informativo', 'Ok')
                    self.popUp_InfoDatosCorrectos.buttons()[0].pressed.connect(self.close)
                    self.popUp_InfoDatosCorrectos.cerrarPopup()
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
        self.ui.botonGestionarUsuario.clicked.connect(self.irGestionarUsuario)
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
    
    def irGestionarUsuario(self):
        self.ventana_GestionarUsuario = ventanaGestionarUsuario()
        self.ventana_GestionarUsuario.show()

    def salir(self):
        self.close()

    def centerOnScreen(self): #metodo centra la ventana principal
        resolution = QtWidgets.QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                          (resolution.height() / 2) - (self.frameSize().height() / 2))
