import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel


class ConexionDataBase:
    
    db = QSqlDatabase.addDatabase("QPSQL")

    def __init__(self):
        
        ConexionDataBase.db.setHostName("localhost")
        ConexionDataBase.db.setPort(5432)
        ConexionDataBase.db.setDatabaseName("inventarioabasto")
        ConexionDataBase.db.setUserName("froilanroac")
        ConexionDataBase.db.setPassword("123456")

    def openDB(self):
        return ConexionDataBase.db.open()


    #Select
    def validarCliente(self,cedula):
        'Devuelve True si esta en la DB'
        sql = "SELECT FROM cliente WHERE cedula = " + str(cedula) + ";"
        query = QSqlQuery()
        query.exec_(sql)
        if (query.size() > 0):
            return True
        else:
            return False

    def validarMarca(self,nombre):
        'Devuelve True si esta en la DB'
        sql = "SELECT FROM marca WHERE nombre = '" + str(nombre) + "';"
        query = QSqlQuery()
        query.exec_(sql)
        if (query.size() > 0):
            return True
        else:
            return False

    def validarProducto(self,nombre):
        'Devuelve True si esta en la DB'
        sql = "SELECT FROM producto WHERE nombre = '" + str(nombre) + "';"
        query = QSqlQuery()
        query.exec_(sql)
        if (query.size() > 0):
            return True
        else:
            return False

    def validarProveedor(self,nombre):
        'Devuelve True si esta en la DB'
        sql = "SELECT FROM proveedor WHERE nombre = '" + str(nombre) + "';"
        query = QSqlQuery()
        query.exec_(sql)
        if (query.size() > 0):
            return True
        else:
            return False

    def validarVendedor(self,cedula):
        'Devuelve True si esta en la DB'
        sql = "SELECT FROM vendedor WHERE cedula = " + str(cedula) + ";"
        query = QSqlQuery()
        query.exec_(sql)
        if (query.size() > 0):
            return True
        else:
            return False

    #Insert
    def insertCliente(self, cedula, telefono, nombre):

        if (self.validarCliente(cedula) == False):
            sql = "INSERT INTO cliente(cedula, telefono, nombre) VALUES ("+str(cedula)+", "+str(telefono)+", '"+str(nombre)+"');"
            query = QSqlQuery()
            query.exec_(sql)
    
    def insertMarca(self, nombre):

        if (self.validarMarca(nombre) == False):
            sql = "INSERT INTO marca(nombre) VALUES ('"+str(nombre)+"');"
            query = QSqlQuery()
            query.exec_(sql)
    
    def insertProducto(self, nombre, cantidad, precio, proveedor_id, marca_id):

        if (self.validarProducto(nombre) == False):
            sql = "INSERT INTO producto(nombre, cantidad, precio, proveedor_id, marca_id) VALUES ('"+str(nombre)+"',"+str(cantidad)+","+str(precio)+","+str(proveedor_id)+","+str(marca_id)+");"
            query = QSqlQuery()
            query.exec_(sql)

    def insertProveedor(self, nombre):

        if (self.validarProveedor(nombre) == False):
            sql = "INSERT INTO proveedor(nombre) VALUES ('"+str(nombre)+"');"
            query = QSqlQuery()
            query.exec_(sql)

    def insertVendedor(self, cedula, telefono, nombre, proveedor_id):

        if (self.validarVendedor(cedula) == False):  
            sql = "INSERT INTO vendedor(cedula, telefono, nombre,proveedor_id) VALUES ("+str(cedula)+", "+str(telefono)+", '"+str(nombre)+"', "+str(proveedor_id)+");"
            query = QSqlQuery()
            query.exec_(sql)
    
    def insertVenta(self, monto, cliente_id):

        sql = "INSERT INTO venta(monto, cliente_id) VALUES ("+str(monto)+", "+str(cliente_id)+");"
        query = QSqlQuery()
        query.exec_(sql)
    
    def insertVentaProducto(self, cantidad, producto_id, venta_id):

        sql = "INSERT INTO venta_producto(cantidad, producto_id, venta_id) VALUES ("+str(cantidad)+", "+str(producto_id)+", "+str(venta_id)+");"
        query = QSqlQuery()
        query.exec_(sql)

    #Delete
    def deleteCliente(self, cedula):
        sql = "DELETE FROM cliente WHERE cedula = " + str(cedula) + ";"
        query = QSqlQuery()
        query.exec_(sql)

    def deleteMarca(self, nombre):
        sql = "DELETE FROM marca WHERE nombre = '" + nombre + "';"
        print (sql)
        query = QSqlQuery()
        query.exec_(sql)

    def deleteProducto(self, nombre):
        sql = "DELETE FROM producto WHERE nombre = '" + nombre + "';"
        query = QSqlQuery()
        query.exec_(sql)

    def deleteProveedor(self, nombre):
        sql = "DELETE FROM proveedor WHERE nombre = '" + nombre + "';"
        query = QSqlQuery()
        query.exec_(sql)

    def deleteVendedor(self, cedula):
        sql = "DELETE FROM vendedor WHERE cedula = '" + str(cedula) + "';"
        query = QSqlQuery()
        query.exec_(sql)



#Main
conector = ConexionDataBase()
conector.openDB()


