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


    #Insert
    def insertCliente(self, cedula, telefono, nombre):

        sql = "INSERT INTO cliente(cedula, telefono, nombre) VALUES ("+str(cedula)+", "+str(telefono)+", '"+str(nombre)+"');"
        query = QSqlQuery()
        query.exec_(sql)
    
    def insertMarca(self, nombre):

        sql = "INSERT INTO marca(nombre) VALUES ('"+str(nombre)+"');"
        query = QSqlQuery()
        query.exec_(sql)
    
    def insertProducto(self, nombre, cantidad, precio, proveedor_id, marca_id):

        sql = "INSERT INTO producto(nombre, cantidad, precio, proveedor_id, marca_id) VALUES ('"+str(nombre)+"',"+str(cantidad)+","+str(precio)+","+str(proveedor_id)+","+str(marca_id)+");"
        query = QSqlQuery()
        query.exec_(sql)

    
    def insertProveedor(self, nombre):

        sql = "INSERT INTO proveedor(nombre) VALUES ('"+str(nombre)+"');"
        query = QSqlQuery()
        query.exec_(sql)
    
    def insertVendedor(self, cedula, telefono, nombre, proveedor_id):

        sqlsearch = "SELECT nombre FROM cliente WHERE cedula = "+str(cedula)+";"    
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


