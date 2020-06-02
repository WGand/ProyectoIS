import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from objetosPrograma import Cliente, Venta

class ConexionDataBase:
    
    db = QSqlDatabase.addDatabase("QPSQL")

    def __init__(self):
        
        ConexionDataBase.db.setHostName("localhost")
        ConexionDataBase.db.setPort(5432)
        ConexionDataBase.db.setDatabaseName("inventarioabasto")
        ConexionDataBase.db.setUserName("inventarioabasto")
        ConexionDataBase.db.setPassword("123456")

    def openDB(self):
        return ConexionDataBase.db.open()
    
    def closeDB(self):
        ConexionDataBase.db.close()

    #Select
    def validarCliente(self,cedula): #Devuelve True si esta en la DB
        self.openDB()
        sql = "SELECT FROM cliente WHERE cedula = " + str(cedula) + ";"
        query = QSqlQuery()
        query.exec_(sql)
        if (query.size() > 0):
            return True
        else:
            return False
        self.closeDB()

    def validarMarca(self,nombre): #Devuelve True si esta en la DB
        self.openDB()
        sql = "SELECT FROM marca WHERE nombre = '" + str(nombre) + "';"
        query = QSqlQuery()
        query.exec_(sql)
        if (query.size() > 0):
            return True
        else:
            return False
        self.closeDB()

    def validarProducto(self,nombre): #Devuelve True si esta en la DB
        self.openDB()
        sql = "SELECT FROM producto WHERE nombre = '" + str(nombre) + "';"
        query = QSqlQuery()
        query.exec_(sql)
        if (query.size() > 0):
            return True
        else:
            return False
        self.closeDB()

    def validarProveedor(self,nombre): #Devuelve True si esta en la DB
        self.openDB()
        sql = "SELECT FROM proveedor WHERE nombre = '" + str(nombre) + "';"
        query = QSqlQuery()
        query.exec_(sql)
        if (query.size() > 0):
            return True
        else:
            return False
        self.closeDB()

    def validarVendedor(self,cedula): #Devuelve True si esta en la DB
        self.openDB()
        sql = "SELECT FROM vendedor WHERE cedula = " + str(cedula) + ";"
        query = QSqlQuery()
        query.exec_(sql)
        if (query.size() > 0):
            return True
        else:
            return False
        self.closeDB()

    #Insert
    def insertCliente(self, cedula, telefono, nombre):
        self.openDB()
        if (self.validarCliente(cedula) == False):
            sql = "INSERT INTO cliente(cedula, telefono, nombre) VALUES ("+str(cedula)+", "+str(telefono)+", '"+str(nombre)+"');"
            query = QSqlQuery()
            query.exec_(sql)
        self.closeDB()
    
    def insertMarca(self, nombre):
        self.openDB()
        if (self.validarMarca(nombre) == False):
            sql = "INSERT INTO marca(nombre) VALUES ('"+str(nombre)+"');"
            query = QSqlQuery()
            query.exec_(sql)
        self.closeDB()
    
    def insertProducto(self, nombre, cantidad, precio, proveedor_id, marca_id):
        self.openDB()
        if (self.validarProducto(nombre) == False):
            sql = "INSERT INTO producto(nombre, cantidad, precio, proveedor_id, marca_id) VALUES ('"+str(nombre)+"',"+str(cantidad)+","+str(precio)+","+str(proveedor_id)+","+str(marca_id)+");"
            query = QSqlQuery()
            query.exec_(sql)
        self.closeDB()

    def insertProveedor(self, nombre):
        self.openDB()
        if (self.validarProveedor(nombre) == False):
            sql = "INSERT INTO proveedor(nombre) VALUES ('"+str(nombre)+"');"
            query = QSqlQuery()
            query.exec_(sql)
        self.closeDB()

    def insertVendedor(self, cedula, telefono, nombre, proveedor_id):
        self.openDB()
        if (self.validarVendedor(cedula) == False):  
            sql = "INSERT INTO vendedor(cedula, telefono, nombre,proveedor_id) VALUES ("+str(cedula)+", "+str(telefono)+", '"+str(nombre)+"', "+str(proveedor_id)+");"
            query = QSqlQuery()
            query.exec_(sql)
        self.closeDB()
    
    def insertVenta(self, monto, cliente_id):
        self.openDB()
        sql = "INSERT INTO venta(monto, cliente_id) VALUES ("+str(monto)+", "+str(cliente_id)+");"
        query = QSqlQuery()
        query.exec_(sql)
        self.closeDB()
    
    def insertVentaProducto(self, cantidad, producto_id, venta_id):
        self.openDB()
        sql = "INSERT INTO venta_producto(cantidad, producto_id, venta_id) VALUES ("+str(cantidad)+", "+str(producto_id)+", "+str(venta_id)+");"
        query = QSqlQuery()
        query.exec_(sql)
        self.closeDB()

    #Delete
    def deleteCliente(self, cedula):
        self.openDB()
        sql = "DELETE FROM cliente WHERE cedula = " + str(cedula) + ";"
        query = QSqlQuery()
        query.exec_(sql)
        self.closeDB()

    def deleteMarca(self, nombre):
        self.openDB()
        sql = "DELETE FROM marca WHERE nombre = '" + nombre + "';"
        print (sql)
        query = QSqlQuery()
        query.exec_(sql)
        self.closeDB()

    def deleteProducto(self, nombre):
        self.openDB()
        sql = "DELETE FROM producto WHERE nombre = '" + nombre + "';"
        query = QSqlQuery()
        query.exec_(sql)
        self.closeDB()

    def deleteProveedor(self, nombre):
        self.openDB()
        sql = "DELETE FROM proveedor WHERE nombre = '" + nombre + "';"
        query = QSqlQuery()
        query.exec_(sql)
        self.closeDB()

    def deleteVendedor(self, cedula):
        self.openDB()
        sql = "DELETE FROM vendedor WHERE cedula = '" + str(cedula) + "';"
        query = QSqlQuery()
        query.exec_(sql)
        self.closeDB()

    #Modificaciones

    #Cliente
    def modificarNombreCliente(self, nombre, cedula):
        self.openDB()
        if (self.validarCliente(cedula) == True):
            sql = "UPDATE cliente SET nombre = '" + str(nombre) +"' WHERE cedula = "+ str(cedula)
            query = QSqlQuery()
            query.exec_(sql)
        self.closeDB()

    def modificarCedulaCliente(self, nuevaCedula, cedula):
        self.openDB()
        if (self.validarCliente(cedula) == True):
            sql = "UPDATE cliente SET cedula = " + str(nuevaCedula) +" WHERE cedula = "+ str(cedula)
            query = QSqlQuery()
            query.exec_(sql)
        self.closeDB()

    def modificarTelefonoCliente(self, telefono, cedula):
        self.openDB()
        if (self.validarCliente(cedula) == True):
            sql = "UPDATE cliente SET telefono = " + str(telefono) +" WHERE cedula = "+ str(cedula)
            query = QSqlQuery()
            query.exec_(sql)
        self.closeDB()

    #Marca
    def modificarMarca(self, nuevoNombre, nombre):
        self.openDB()
        if (self.validarMarca(nombre) == True):
            sql = "UPDATE marca SET nombre = '" + str(nuevoNombre) +"' WHERE nombre = '"+ str(nombre) +"';"
            query = QSqlQuery()
            query.exec_(sql)
        self.closeDB()

    #Producto
    def modificarNombreProducto(self, nuevoNombre, nombre):
        self.openDB()
        if (self.validarProducto(nombre) == True):
            sql = "UPDATE producto SET nombre = '" + str(nuevoNombre) +"' WHERE nombre = '"+ str(nombre) +"';"
            query = QSqlQuery()
            query.exec_(sql)
        self.closeDB()

    def modificarCantidadProducto(self, nuevaCantidad, nombre):
        self.openDB()
        if (self.validarProducto(nombre) == True):
            sql = "UPDATE producto SET cantidad = " + str(nuevaCantidad) +" WHERE nombre = '"+ str(nombre) +"';"
            query = QSqlQuery()
            query.exec_(sql)
        self.closeDB()

    def modificarPrecioProducto(self, nuevoPrecio, nombre):
        self.openDB()
        if (self.validarProducto(nombre) == True):
            sql = "UPDATE producto SET precio = " + str(nuevoPrecio) +" WHERE nombre = '"+ str(nombre) +"';"
            query = QSqlQuery()
            query.exec_(sql)
        self.closeDB()

    #Proveedor
    def modificarNombreProveedor(self, nuevoNombre, nombre):
        self.openDB()
        if (self.validarProveedor(nombre) == True):
            sql = "UPDATE proveedor SET nombre = '" + str(nuevoNombre) +"' WHERE nombre = '"+ str(nombre) +"';"
            query = QSqlQuery()
            query.exec_(sql)
        self.closeDB()

    #Vendedor        
    def modificarCedulaVendedor(self, nuevaCedula, cedula):
        self.openDB()
        if (self.validarVendedor(cedula) == True):
            sql = "UPDATE vendedor SET cedula = " + str(nuevaCedula) +" WHERE cedula = "+ str(cedula) +";"
            query = QSqlQuery()
            query.exec_(sql)
        self.closeDB()

    def modificarTelefonoVendedor(self, nuevoTelefono, cedula):
        self.openDB()
        if (self.validarVendedor(cedula) == True):
            sql = "UPDATE vendedor SET telefono = " + str(nuevoTelefono) +" WHERE cedula = "+ str(cedula) +";"
            query = QSqlQuery()
            query.exec_(sql)
        self.closeDB()

    def modificarNombreVendedor(self, nuevoNombre, cedula):
        self.openDB()
        if (self.validarVendedor(cedula) == True):
            sql = "UPDATE vendedor SET nombre = '" + str(nuevoNombre) +"' WHERE cedula = "+ str(cedula) +";"
            query = QSqlQuery()
            query.exec_(sql)
        self.closeDB()
    
    def pruebitajeje(self):
        self.openDB()
        sql = 'SELECT id_cliente FROM cliente;'
        query = QSqlQuery()
        query.exec_(sql)
        
        ids = []
        while(query.next()):
            retorno = query.value(0)
            ids.append(retorno)
        print(ids)
        self.closeDB()

    def guardarVenta(self, venta):
        self.openDB()
        ##(Venta)
        ##BEGIN
        ##Verificar si existe el cliente
        ##Si existe-> buscar su id
        ##sino -> insertar el cliente y retornar el id del cliente
        ##insertar venta, con referencia al cliente
        ##retornar el id de la venta  id_venta
        ##recorremos la lista de productos de la venta
        ##  retornar su id id_producto
        ##  capturamos su cantidad
        ##  insertamos en venta_producto haciendo referencia con id_venta, id_producto
        ##END
        self.closeDB()
