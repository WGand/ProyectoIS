from abc import ABC, abstractmethod

class persona(ABC):
	def __init__(self, nombre = '', cedula = '', telefono = ''):
		self.nombre = nombre
		self.cedula = cedula
		self.telefono = telefono

class cliente(persona):
	pass

class proveedor():
	def __init__(self, nombre = ''):
		self.nombre = nombre

class vendedor(persona):
	def __init__(self, proveedor = []):
		super(vendedor, self).__init__()
		self.proveedor = proveedor

class marca():
	def __init__(self, nombre = ''):
		self.nombre = nombre

class producto():
	def __init__(self, marca = [], nombre = '', cantidad = '', proveedor = [], precio = ''):
		self.marca = marca
		self.nombre = nombre
		self.cantidad = cantidad
		self.proveedor = proveedor
		self.precio = precio

class venta():
	def __init__(self, monto = '', cantidad = '', cliente = []):
		self.monto = monto
		self.cliente = cliente
		self.cantidad = cantidad