import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from objetosPrograma import Cliente, Producto, usuario, Venta

class ConexionDataBase:

    db = QSqlDatabase.addDatabase("QPSQL")

    def __init__(self):
        ConexionDataBase.db.setHostName("localhost")
        ConexionDataBase.db.setPort(5432)
        ConexionDataBase.db.setDatabaseName("inventarioabasto")
        ConexionDataBase.db.setUserName("inventarioabasto")
        ConexionDataBase.db.setPassword("123456")
    
    def insertarMovimiento(self, tipo, monto, justificacion, usuario):
        sql = "INSERT INTO movimiento(tipo, monto, justificacion, usuario) VALUES ("+str(tipo)+","+str(monto)+",'"+justificacion+"','"+usuario+"');"
        self.excuteQuery(sql)
    
    def recorrerProveedor(self):
        listaProveedor = []
        sql = "SELECT nombre from proveedor;"
        query = self.excuteQuery(sql)
        while query.next():
            listaProveedor.append(str(query.value(0)))
        return listaProveedor

    def getIdProducto(self,nombre): #Devuelve True si esta en la DB
        sql = "SELECT id_producto FROM producto WHERE nombre = '" + str(nombre) + "';"
        query = self.excuteQuery(sql)
        while query.next():
            i = query.value(0)
        return i

    def buscarProveedoresProducto(self, nombre):
        listaProveedorID = []
        listaProveedor = []
        idproducto = self.getIdProducto(nombre)
        sql = "SELECT proveedor_id FROM proveedor_producto WHERE producto_id = '" + str(idproducto) + "';"
        query = self.excuteQuery(sql)
        while query.next():
            listaProveedorID.append(str(query.value(0)))
        for i in listaProveedorID:
            sql = "SELECT nombre FROM proveedor WHERE id_proveedor = '" + str(i) + "';"
            query = self.excuteQuery(sql)
            query.next()
            listaProveedor.append(str(query.value(0)))
        return listaProveedor
        

    def verificarProveedor(self, nombre): #Devuelve True si esta en la DB
        sql = "SELECT FROM proveedor WHERE nombre = '" + str(nombre) + "';"
        query = self.excuteQuery(sql)
        if (query.size() > 0):
            return False
        else:
            return True

    def getIdProveedor(self,nombre):
        sql = "SELECT id_proveedor FROM proveedor WHERE nombre = '" + str(nombre) + "';"
        query = self.excuteQuery(sql)
        while query.next():
            i = query.value(0)
        return i

    def excuteQuery(self, sql):
        ConexionDataBase.db.open()
        query = QSqlQuery(sql)
        ConexionDataBase.db.close()
        return query

    def buscarUsuario(self, nombre):
        sql = "SELECT nombre, admininstrador from usuario WHERE nombre = '" + nombre + "';"
        query = self.excuteQuery(sql)
        while query.next():
            user = usuario(query.value(0), query.value(1))
        return user

    def recorrerUsuarioCero(self):
        listaUsuarios = []
        sql = "SELECT nombre, admininstrador FROM usuario;"
        query = self.excuteQuery(sql)
        while query.next():
            nombre = query.value(0)
            admin = query.value(1)
            objeto = usuario(nombre, admin)
            listaUsuarios.append(objeto)
        return listaUsuarios


    def verificarUsuario(self, nombre): #Devuelve True si esta en la DB
        sql = "SELECT FROM usuario WHERE nombre = '" + str(nombre) + "';"
        query = self.excuteQuery(sql)
        if (query.size() > 0):
            return True
        else:
            return False

    #Precondicion: Existe el usuario.
    def verificarClave(self, nombre, clave):
        sql = "SELECT clave FROM usuario WHERE nombre = '"+str(nombre)+"';"
        query = self.excuteQuery(sql)
        while query.next():
            hash_ = query.value(0)
        sql2 = "SELECT FROM usuario WHERE nombre = '"+str(nombre)+"' and clave = crypt('"+str(clave)+"', '"+str(hash_)+"');"
        query2 = self.excuteQuery(sql2)
        if (query2.size() > 0):
            return True
        else:
            return False
        
    def verificarCliente(self,cedula): #Devuelve True si esta en la DB
        sql = "SELECT FROM cliente WHERE cedula = " + str(cedula) + ";"
        query = self.excuteQuery(sql)
        if (query.size() > 0):
            return True
        else:
            return False

    def verificarProducto(self,nombre): #Devuelve True si esta en la DB
        sql = "SELECT FROM producto WHERE nombre = '" + str(nombre) + "';"
        query = self.excuteQuery(sql)
        if (query.size() > 0):
            return True
        else:
            return False

    def insertarUsuario(self, nombre, clave, admin):
        sql = "INSERT INTO usuario(nombre, clave, admininstrador) VALUES ('"+str(nombre)+"',crypt('"+str(clave)+"', gen_salt('bf')),"+str(admin)+");"
        self.excuteQuery(sql)

    def insertarCliente(self, cedula, telefono, nombre):
        sql = "INSERT INTO cliente(cedula, telefono, nombre) VALUES ("+str(cedula)+", '"+str(telefono)+"', '"+str(nombre)+"');"
        self.excuteQuery(sql)
    
    def insertarProducto(self, nombre, cantidad, precioventa, iva, preciocompra):
        sql = "INSERT INTO producto(nombre, cantidad, precioventa, iva, preciocompra) VALUES ('"+str(nombre)+"',"+str(cantidad)+","+str(precioventa)+","+str(iva)+","+str(preciocompra)+");"
        self.excuteQuery(sql)

    def insertarVenta(self, monto, cliente_id, usuario_id):
        sql = "INSERT INTO venta(monto, cliente_id, usuario_id) VALUES ("+str(monto)+", "+str(cliente_id)+", "+str(usuario_id)+");"
        self.excuteQuery(sql)
    
    def insertarCompra(self, monto):
        sql = "insert into compra(monto) values ("+str(monto)+");"
        self.excuteQuery(sql)
    
    def insertarHproducto(self, nombre):
        sql = "insert into hproducto(nombre) values ('"+nombre+"');"
        self.excuteQuery(sql)
    
    def insertarProveedor(self, nombre):
        sql = "insert into proveedor(nombre) values ('"+nombre+"');"
        self.excuteQuery(sql)

    def insertarProveedorProducto(self, producto_id, proveedor_id):
        sql = "insert into proveedor_producto(producto_id, proveedor_id) values ("+str(producto_id)+", "+str(proveedor_id)+");"
        self.excuteQuery(sql)
    
    def insertarRerror(self, error):
        sql = "insert into rerror(error) values ('"+error+"');"
        self.excuteQuery(sql)

    def insertarVentaHproducto(self, cantidad, hproducto_id, venta_id):
        sql = "INSERT INTO venta_hproducto(cantidad, hproducto_id, venta_id) VALUES ("+str(cantidad)+", "+str(hproducto_id)+", "+str(venta_id)+");"
        self.excuteQuery(sql)

    #Delete
    def eliminarUsuario(self, nombre):
        sql = "DELETE FROM usuario WHERE nombre = '" + str(nombre) + "';"
        self.excuteQuery(sql)

    def eliminarProducto(self, nombre):
        sql = "DELETE FROM producto WHERE nombre = '" + str(nombre) + "';"
        self.excuteQuery(sql)

    #Producto
    def modificarNombreProducto(self, nuevoNombre, nombre):
        sql = "UPDATE producto SET nombre = '" + str(nuevoNombre) +"' WHERE nombre = '"+ str(nombre) +"';"
        self.excuteQuery(sql)

    def modificarCantidadProducto(self, nuevaCantidad, nombre):
        sql = "UPDATE producto SET cantidad = " + str(nuevaCantidad) +" WHERE nombre = '"+ str(nombre) +"';"
        self.excuteQuery(sql)

    def modificarPrecioventaProducto(self, nuevoPrecio, nombre):
        sql = "UPDATE producto SET precioventa = " + str(nuevoPrecio) +" WHERE nombre = '"+ str(nombre) +"';"
        self.excuteQuery(sql)
    
    def modificarPreciocompraProducto(self, nuevoPrecio, nombre):
        sql = "UPDATE producto SET preciocompra = " + str(nuevoPrecio) +" WHERE nombre = '"+ str(nombre) +"';"
        self.excuteQuery(sql)

    def modificarIvaProducto(self, nuevoIva, nombre):
        sql = "UPDATE producto SET iva = " + str(nuevoIva) +" WHERE nombre = '"+ str(nombre) +"';"
        self.excuteQuery(sql)

    def busquedaProducto(self, nombre):
        sql = "SELECT cantidad, precioventa, iva, preciocompra FROM producto WHERE nombre = '"+str(nombre)+"';"
        query = self.excuteQuery(sql)
        producto_ = Producto()
        producto_.setNombre(nombre)
        while (query.next()):
            for i in range (0,4):
                if(i == 0):
                    producto_.setCantidad(query.value(i))
                elif(i == 1):
                    producto_.setPrecioVenta(query.value(i))
                elif(i == 2):
                    producto_.setIva(query.value(i))
                else:
                    producto_.setPrecioCompra(query.value(i))
        return producto_
  
    def recorrerProducto(self):
        listaProducto = []
        sql = "SELECT * FROM producto;"
        query = self.excuteQuery(sql)
        while query.next():
            nombre = query.value(1)
            cantidad = query.value(2)
            precioVenta = query.value(3)
            iva = query.value(4)
            precioCompra = query.value(5)
            objeto = Producto(nombre,cantidad,precioVenta,iva,precioCompra)
            listaProducto.append(objeto)
        return listaProducto

    def recorrerProductoCero(self):
        listaProducto = []
        sql = "SELECT * FROM producto WHERE cantidad = 0"
        query = self.excuteQuery(sql)
        while query.next():
            nombre = query.value(1)
            cantidad = query.value(2)
            precioVenta = query.value(3)
            iva = query.value(4)
            precioCompra = query.value(5)
            objeto = Producto(nombre,cantidad,precioVenta,iva,precioCompra)
            listaProducto.append(objeto)
        return listaProducto
    
    def getIdHproducto(self,nombre): #Devuelve True si esta en la DB
        sql = "SELECT id_hproducto FROM hproducto WHERE nombre = '" + str(nombre) + "';"
        query = self.excuteQuery(sql)
        while query.next():
            i = query.value(0)
        return i

    def getIdUltimaVenta(self):
        sql = "SELECT id_venta FROM venta;"
        query = self.excuteQuery(sql)
        if query.size() > 0:
            while query.next():
                i = query.value(0)
        else:
            i = 0
        return i

    def getIdCliente(self,cedula): #Devuelve True si esta en la DB
        sql = "SELECT id_cliente FROM cliente WHERE cedula = " + str(cedula) + ";"
        query = self.excuteQuery(sql)
        while query.next():
            i = query.value(0)
        return i

    def getIdUsuario(self, nombre):
        sql = "select id_usuario from usuario where nombre = '"+nombre+"';"
        query = self.excuteQuery(sql)
        while query.next():
            i = query.value(0)
        return i

    def guardarVenta(self, venta, usuario):
        clienteVenta = Cliente()
        clienteVenta.setCedula(venta.getCliente().getCedula())
        clienteVenta.setNombre(venta.getCliente().getNombre())
        clienteVenta.setTelefono(venta.getCliente().getTelefono())
        if(self.verificarCliente(int(clienteVenta.getCedula()))):
            id_cliente = self.getIdCliente(int(clienteVenta.getCedula()))
        else:
            self.insertarCliente(clienteVenta.getCedula(), clienteVenta.getTelefono(), clienteVenta.getNombre())
            id_cliente = self.getIdCliente(clienteVenta.getCedula())
        id_usuario = self.getIdUsuario(usuario)
        self.insertarVenta(venta.getMonto(), id_cliente, id_usuario)
        id_venta = self.getIdUltimaVenta()
        for producto_ in venta.getProducto():
            print(producto_.getNombre())
            id_hproducto = self.getIdHproducto(producto_.getNombre())
            self.insertarVentaHproducto(producto_.getCantidad(), id_hproducto, id_venta)
