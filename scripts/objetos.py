from objetosPrograma import Persona,Cliente,Proveedor,Vendedor,Marca,Producto,Venta
from manejadorDataBase import ConexionDataBase

datos = { 'id_producto':'','nombre':'','cantidad':'','precio':'','proveedor_id':'','marca_id':'' }

listaCliente = []

connection = ConexionDataBase()
connection.openDB()

def recorrerCliente(connection):
	sql = "SELECT * FROM cliente"
	query = QSqlQuery(sql)
	while query.next():
		cedula = query.value(1)
		telefono = query.value(2)
		nombre = query.value(3)
		print (cedula, telefono,nombre)
proveedor = Proveedor()


