import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from objetosPrograma import Cliente, Producto, usuario
from objetosPrograma import Venta

class ConexionDataBase:

    db = QSqlDatabase.addDatabase("QPSQL")

    def __init__(self):
        ConexionDataBase.db.setHostName("localhost")
        ConexionDataBase.db.setPort(5432)
        ConexionDataBase.db.setDatabaseName("postgres")
        ConexionDataBase.db.setUserName("postgres")
        ConexionDataBase.db.setPassword("123456")

    def openDB(self):
        ConexionDataBase.db.open()
    
    def closeDB(self):
        ConexionDataBase.db.close()

    def buscarUsuario(self, nombre):
        sql = "SELECT nombre, admininstrador from usuario WHERE nombre = '" + nombre + "';"
        query = QSqlQuery()
        self.openDB()
        query.exec_(sql)
        self.closeDB()
        while query.next():
            user = usuario(query.value(0), query.value(1))
        return user

    def recorrerUsuarioCero(self):
        listaUsuarios = []
        sql = "SELECT nombre, admininstrador FROM usuario;"
        self.openDB()
        query = QSqlQuery(sql)
        self.closeDB()
        while query.next():
            nombre = query.value(0)
            admin = query.value(1)
            objeto = usuario(nombre, admin)
            listaUsuarios.append(objeto)
        return listaUsuarios

    #Select

    def validarUsuario(self, nombre): #Devuelve True si esta en la DB
        sql = "SELECT FROM usuario WHERE nombre = '" + str(nombre) + "';"
        query = QSqlQuery()
        self.openDB()
        query.exec_(sql)
        self.closeDB()
        if (query.size() > 0):
            return True
        else:
            return False

    #Precondicion: Existe el usuario.
    def validarClave(self, nombre, clave):
        sql = "SELECT clave FROM usuario WHERE nombre = '"+str(nombre)+"';"
        query = QSqlQuery()
        self.openDB()
        query.exec_(sql)
        self.closeDB()
        while query.next():
            hash_ = query.value(0)
        sql2 = "SELECT FROM usuario WHERE nombre = '"+str(nombre)+"' and clave = crypt('"+str(clave)+"', '"+str(hash_)+"');"
        query2 = QSqlQuery()
        self.openDB()
        query2.exec_(sql2)
        self.closeDB()
        if (query2.size() > 0):
            return True
        else:
            return False
        
    def validarCliente(self,cedula): #Devuelve True si esta en la DB
        sql = "SELECT FROM cliente WHERE cedula = " + str(cedula) + ";"
        query = QSqlQuery()
        self.openDB()
        query.exec_(sql)
        self.closeDB()
        if (query.size() > 0):
            return True
        else:
            return False

    def validarProducto(self,nombre): #Devuelve True si esta en la DB
        sql = "SELECT FROM producto WHERE nombre = '" + str(nombre) + "';"
        query = QSqlQuery()
        self.openDB()
        query.exec_(sql)
        self.closeDB()
        if (query.size() > 0):
            return True
        else:
            return False

    def validarVendedor(self,cedula): #Devuelve True si esta en la DB
        sql = "SELECT FROM vendedor WHERE cedula = " + str(cedula) + ";"
        query = QSqlQuery()
        self.openDB()
        query.exec_(sql)
        self.closeDB()
        if (query.size() > 0):
            return True
        else:
            return False

    #Insert
    def insertUsuario(self, nombre, clave, admin):
        sql = "INSERT INTO usuario(nombre, clave, admininstrador) VALUES ('"+str(nombre)+"',crypt('"+str(clave)+"', gen_salt('bf')),"+str(admin)+");"
        query = QSqlQuery()
        self.openDB()
        query.exec_(sql)
        self.closeDB()

    def insertCliente(self, cedula, telefono, nombre):
        if (self.validarCliente(cedula) == False):
            sql = "INSERT INTO cliente(cedula, telefono, nombre) VALUES ("+str(cedula)+", "+str(telefono)+", '"+str(nombre)+"');"
            query = QSqlQuery()
            self.openDB()
            query.exec_(sql)
            self.closeDB()
    
    def insertProducto(self, nombre, cantidad, precio, iva):
        sql = "INSERT INTO producto(nombre, cantidad, precio, iva) VALUES ('"+str(nombre)+"',"+str(cantidad)+","+str(precio)+","+str(iva)+");"
        query = QSqlQuery()
        self.openDB()
        query.exec_(sql)
        self.closeDB()

    def insertVendedor(self, cedula, telefono, nombre):
        if (self.validarVendedor(cedula) == False):  
            sql = "INSERT INTO vendedor(cedula, telefono, nombre) VALUES ("+str(cedula)+", "+str(telefono)+", '"+str(nombre)+"');"
            query = QSqlQuery()
            self.openDB()
            query.exec_(sql)
            self.closeDB()
    
    def insertVenta(self, monto, cliente_id):
        sql = "INSERT INTO venta(monto, cliente_id) VALUES ("+str(monto)+", "+str(cliente_id)+");"
        query = QSqlQuery()
        self.openDB()
        query.exec_(sql)
        self.closeDB()
    
    def insertVentaProducto(self, cantidad, producto_id, venta_id):
        sql = "INSERT INTO venta_producto(cantidad, producto_id, venta_id) VALUES ("+str(cantidad)+", "+str(producto_id)+", "+str(venta_id)+");"
        query = QSqlQuery()
        self.openDB()
        query.exec_(sql)
        self.closeDB()

    #Delete
    def deleteCliente(self, cedula):
        sql = "DELETE FROM cliente WHERE cedula = " + str(cedula) + ";"
        query = QSqlQuery()
        self.openDB()
        query.exec_(sql)
        self.closeDB()

    def deleteProducto(self, nombre):
        sql = "DELETE FROM producto WHERE nombre = '" + str(nombre) + "';"
        query = QSqlQuery()
        self.openDB()
        query.exec_(sql)
        self.closeDB()

    def deleteVendedor(self, cedula):
        sql = "DELETE FROM vendedor WHERE cedula = '" + str(cedula) + "';"
        query = QSqlQuery()
        self.openDB()
        query.exec_(sql)
        self.closeDB()

    #Modificaciones

    #Cliente
    def modificarNombreCliente(self, nombre, cedula):
        if (self.validarCliente(cedula) == True):
            sql = "UPDATE cliente SET nombre = '" + str(nombre) +"' WHERE cedula = "+ str(cedula)
            query = QSqlQuery()
            self.openDB()
            query.exec_(sql)
            self.closeDB()

    def modificarCedulaCliente(self, nuevaCedula, cedula):
        if (self.validarCliente(cedula) == True):
            sql = "UPDATE cliente SET cedula = " + str(nuevaCedula) +" WHERE cedula = "+ str(cedula)
            query = QSqlQuery()
            self.openDB()
            query.exec_(sql)
            self.closeDB()

    def modificarTelefonoCliente(self, telefono, cedula):
        if (self.validarCliente(cedula) == True):
            sql = "UPDATE cliente SET telefono = " + str(telefono) +" WHERE cedula = "+ str(cedula)
            query = QSqlQuery()
            self.openDB()
            query.exec_(sql)
            self.closeDB()

    #Producto
    def modificarNombreProducto(self, nuevoNombre, nombre):
        if (self.validarProducto(nombre) == True):
            sql = "UPDATE producto SET nombre = '" + str(nuevoNombre) +"' WHERE nombre = '"+ str(nombre) +"';"
            query = QSqlQuery()
            self.openDB()
            query.exec_(sql)
            self.closeDB()

    def modificarCantidadProducto(self, nuevaCantidad, nombre):
        if (self.validarProducto(nombre) == True):
            self.openDB()
            sql = "UPDATE producto SET cantidad = " + str(nuevaCantidad) +" WHERE nombre = '"+ str(nombre) +"';"
            query = QSqlQuery()
            self.openDB()
            query.exec_(sql)
            self.closeDB()

    def modificarPrecioProducto(self, nuevoPrecio, nombre):
        if (self.validarProducto(nombre) == True):
            sql = "UPDATE producto SET precio = " + str(nuevoPrecio) +" WHERE nombre = '"+ str(nombre) +"';"
            query = QSqlQuery()
            self.openDB()
            query.exec_(sql)
            self.closeDB()

    def modificarIvaProducto(self, nuevoIva, nombre):
        sql = "UPDATE producto SET iva = " + str(nuevoIva) +" WHERE nombre = '"+ str(nombre) +"';"
        query = QSqlQuery()
        self.openDB()
        query.exec_(sql)
        self.closeDB()

    #Vendedor        
    def modificarCedulaVendedor(self, nuevaCedula, cedula):
        if (self.validarVendedor(cedula) == True):
            sql = "UPDATE vendedor SET cedula = " + str(nuevaCedula) +" WHERE cedula = "+ str(cedula) +";"
            query = QSqlQuery()
            self.openDB()
            query.exec_(sql)
            self.closeDB()

    def modificarTelefonoVendedor(self, nuevoTelefono, cedula):
        if (self.validarVendedor(cedula) == True):
            sql = "UPDATE vendedor SET telefono = " + str(nuevoTelefono) +" WHERE cedula = "+ str(cedula) +";"
            query = QSqlQuery()
            self.openDB()
            query.exec_(sql)
            self.closeDB()

    def modificarNombreVendedor(self, nuevoNombre, cedula):
        if (self.validarVendedor(cedula) == True):
            sql = "UPDATE vendedor SET nombre = '" + str(nuevoNombre) +"' WHERE cedula = "+ str(cedula) +";"
            query = QSqlQuery()
            self.openDB()
            query.exec_(sql)
            self.closeDB()

    def retornarTodoProducto(self):
        sql = 'SELECT * FROM producto;'
        query = QSqlQuery()
        self.openDB()
        query.exec_(sql)
        self.closeDB()
        return query

    def busquedaProducto(self, nombre):

        sql = "SELECT cantidad, precio, iva FROM producto WHERE nombre = '"+str(nombre)+"';"
        query = QSqlQuery()
        self.openDB()
        query.exec_(sql)
        self.closeDB()
        producto_ = Producto()
        producto_.setNombre(nombre)
        while (query.next()):
            for i in range (0,3):
                if(i == 0):
                    producto_.setCantidad(query.value(i))
                elif(i == 1):
                    producto_.setPrecio(query.value(i))
                else:
                    producto_.setIva(query.value(i))
        return producto_
  
    def recorrerProducto(self):
        listaProducto = []
        sql = "SELECT * FROM producto;"
        query = QSqlQuery()
        self.openDB()
        query.exec_(sql)
        self.closeDB()
        while query.next():
            nombre = query.value(1)
            cantidad = query.value(2)
            precio = query.value(3)
            iva = query.value(4)
            objeto = Producto(nombre,cantidad,precio,iva)
            listaProducto.append(objeto)
        return listaProducto

    def recorrerProductoCero(self):
        listaProducto = []
        sql = "SELECT * FROM producto WHERE cantidad = 0"
        query = QSqlQuery()
        self.openDB()
        query.exec_(sql)
        self.closeDB()
        while query.next():
            nombre = query.value(1)
            cantidad = query.value(2)
            precio = query.value(3)
            iva = query.value(4)
            objeto = Producto(nombre,cantidad,precio,iva)
            listaProducto.append(objeto)
        return listaProducto

    def getIdUltimaVenta(self):
        sql = "SELECT id_venta FROM venta;"
        query = QSqlQuery()
        self.openDB()
        query.exec_(sql)
        self.closeDB()
        while query.next():
            i = query.value(0)
        return i

    def getIdCliente(self,cedula): #Devuelve True si esta en la DB
        sql = "SELECT id_cliente FROM cliente WHERE cedula = " + str(cedula) + ";"
        query = QSqlQuery()
        self.openDB()
        query.exec_(sql)
        self.closeDB()
        while query.next():
            i = query.value(0)
        return i
    
    def getIdProducto(self,nombre): #Devuelve True si esta en la DB
        sql = "SELECT id_producto FROM producto WHERE nombre = '" + str(nombre) + "';"
        query = QSqlQuery()
        self.openDB()
        query.exec_(sql)
        self.closeDB()
        while query.next():
            i = query.value(0)
        return i

    def guardarVenta(self, venta ):
        clienteIntenso = Cliente()
        clienteIntenso.setCedula(venta.getCliente().getCedula())
        clienteIntenso.setNombre(venta.getCliente().getNombre())
        clienteIntenso.setTelefono(venta.getCliente().getTelefono())
        if(self.validarCliente(int(clienteIntenso.getCedula()))):
            id_cliente = self.getIdCliente(int(clienteIntenso.getCedula()))
        else:
            self.insertCliente(clienteIntenso.getCedula(), clienteIntenso.getTelefono(), clienteIntenso.getNombre())
            id_cliente = self.getIdCliente(clienteIntenso.getCedula())
        self.insertVenta(venta.getMonto(), id_cliente)
        #id_venta = self.getIdUltimaVenta()
        #for producto_ in venta.getProducto():
        #    id_producto = self.getIdProducto(producto_.getNombre())
        #    self.insertVentaProducto(producto_.getCantidad(), id_producto, id_venta)
