from objetosPrograma import Persona,Cliente,Proveedor,Vendedor,Marca,Producto,Venta
from manejadorDataBase import ConexionDataBase
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel

datos = { 'id_producto':'','nombre':'','cantidad':'','precio':'','proveedor_id':'','marca_id':'' }

listaCliente = []
listaProveedor = []

def recorrerCliente():

	connection = ConexionDataBase()
	connection.openDB()
	query = QSqlQuery("SELECT * FROM cliente")

	while query.next():
		cedula = query.value(1)
		telefono = query.value(2)
		nombre = query.value(3)
		cliente = Cliente(nombre,cedula,telefono)
		listaCliente.append(cliente)

# def recorrerProveedor():

# 	connection = ConexionDataBase()
# 	connection.openDB()
# 	query = QSqlQuery("SELECT * FROM proveedor")

# 	while query.next():
# 		nombre = query.value(1)
# 		proveedor = Proveedor(nombre)
# 		listaProveedor.append(proveedor)

# def recorrerVendedor():

# 	connection = ConexionDataBase()
# 	connection.openDB()
# 	query = QSqlQuery("SELECT * FROM vendedor")

# 	while query.next():
# 		nombre = query.value(1)
# 		proveedor = Proveedor(nombre)
# 		listaProveedor.append(proveedor)

recorrerCliente()
for x in listaCliente:
	print (x.getNombre())
	print (x.getCedula())
	print (x.getTelefono())
