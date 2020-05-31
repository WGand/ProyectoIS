import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel


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

    ###
    # INSERCIONES
    ###



    def insertCliente(self, cedula, telefono, nombre):

        sql = "INSERT INTO cliente(cedula, telefono, nombre) VALUES ("+str(cedula)+", "+str(telefono)+", '"+str(nombre)+"');"
        query = QSqlQuery()
        query.exec_(sql)
    
    def insertMarca(self, nombre):

        sql = "INSERT INTO marca(nombre) VALUES ('"+str(nombre)+"');"
        query = QSqlQuery()
        query.exec_(sql)
    
    def insertProducto(self, nombre, cantidad, precio, proveedor_id, marca_id):

        sql = "INSERT INTO producto(nombre, cantidad, precio, proveedor_id, marca_id) VALUES ('"+str(nombre)+"', "+str(cantidad)+", "+str(precio)+", "+str(proveedor_id)+", "+str(marca_id)+");"
        query = QSqlQuery()
        query.exec_(sql)
    
    def insertProveedor(self, nombre):

        sql = "INSERT INTO proveedor(nombre) VALUES ('"+str(nombre)+"');"
        query = QSqlQuery()
        query.exec_(sql)
    
    def insertVendedor(self, cedula, telefono, nombre, proveedor_id):

        sqlsearch = "SELECT nombre FROM cliente WHERE cedula = "+str(cedula)+";"
"       
        sql = "INSERT INTO vendedor(cedula, telefono, nombre) VALUES ("+str(cedula)+", "+str(telefono)+", '"+str(nombre)+"', "+str(proveedor_id)+");"
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
    

     








##########                  MAIN




conector = ConexionDataBase()
conector.openDB()

cedula = 12312323
telefono = 2325252525
nombre = 'fROIlan ROasxdxd'

print("INSERT INTO marca(nombre) VALUES ('"+str(nombre)+"');")


