from abc import ABC, abstractmethod

class Persona(ABC):
	def __init__(self, nombre = '', cedula = '', telefono = ''):
		self._nombre = nombre
		self._cedula = cedula
		self._telefono = telefono
	
	def setNombre(self, nombre):
		self._nombre = nombre
	
	def getNombre(self):
		return self._nombre

	def setCedula(self, cedula):
		self._cedula = cedula

	def getCedula(self):
		return self._cedula

	def setTelefono(self, telefono):
		self._telefono = telefono
	
	def getTelefono(self):
		return self._telefono

class Cliente(Persona):
	pass

class Vendedor(Persona):
	pass

class Producto():
	def __init__(self, nombre = '', cantidad = '', precio = '', iva = ''):
		self.__nombre = nombre
		self.__cantidad = cantidad
		self.__precio = precio
		self.__iva = iva
	
	def setIva(self, iva):
		self.__iva = iva

	def getIva(self):
		return self.__iva
	
	def setNombre(self, nombre):
		self.__nombre = nombre
	
	def getNombre(self):
		return self.__nombre

	def setCantidad(self, cantidad):
		self.__cantidad = cantidad
	
	def getCantidad(self):
		return self.__cantidad
	
	def setPrecio(self, precio):
		self.__precio = precio
	
	def getPrecio(self):
		return self.__precio

class Venta():
	def __init__(self, monto = '', cliente = []):
		self.__monto = monto
		self.__cliente = cliente
		self.__producto = []
	
	def setMonto(self, monto):
		self.__monto = monto
	
	def getMonto(self):
		return self.__monto
	
	def setCliente(self, cliente):
		self.__cliente = cliente
	
	def getCliente(self):
		return self.__cliente
	
	def addProducto(self, producto):
		self.__producto.append(producto)

	def getProducto(self):
		return self.__producto
