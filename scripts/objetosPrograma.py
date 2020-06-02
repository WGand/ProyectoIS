from abc import ABC, abstractmethod

class Persona(ABC):
	def __init__(self, nombre = '', cedula = '', telefono = ''):
		self.nombre = nombre
		self.cedula = cedula
		self.telefono = telefono

class Cliente(persona):
	pass

class Proveedor():
	def __init__(self, nombre = ''):
		self.nombre = nombre

class Vendedor(persona):
	def __init__(self, proveedor = []):
		super(vendedor, self).__init__()
		self.proveedor = proveedor

class Marca():
	def __init__(self, nombre = ''):
		self.nombre = nombre

class Producto():
	def __init__(self, marca = [], nombre = '', cantidad = '', proveedor = [], precio = ''):
		self.marca = marca
		self.nombre = nombre
		self.cantidad = cantidad
		self.proveedor = proveedor
		self.precio = precio

class Venta():
	def __init__(self, monto = '', cantidad = '', cliente = []):
		self.monto = monto
		self.cliente = cliente
		self.cantidad = cantidad