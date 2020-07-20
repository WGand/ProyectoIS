from abc import ABC, abstractmethod

class usuario():
	def __init__(self, nombre = '', admin = '', correo = ''):
		self.__nombre = nombre
		self.__admin = admin
		self.__correo = correo
	
	def getNombre(self):
		return self.__nombre
	
	def isAdmin(self):
		return self.__admin
	
	def getCorreo(self):
		return self.__correo

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
	def __init__(self, nombre = '', cantidad = '', precioVenta = '', iva = '', precioCompra =''):
		self.__nombre = nombre
		self.__cantidad = cantidad
		self.__precioVenta = precioVenta
		self.__iva = iva
		self.__precioCompra = precioCompra
	
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
	
	def setPrecioVenta(self, precioVenta):
		self.__precioVenta = precioVenta
	
	def setPrecioCompra(self, precioCompra):
		self.__precioCompra = precioCompra
	
	def getPrecioCompra(self):
			return self.__precioCompra

	def getPrecioVenta(self):
		return self.__precioVenta

class Venta():
	def __init__(self, cliente = ''):
		self.__monto = 0.0
		self.__cliente = cliente
		self.__producto = []
	
	def setMonto(self):
		monto_ = float(0)
		if(self.__producto):	
			for producto_ in self.__producto:
				if(producto_.getIva()):
					monto_ += (producto_.getPrecioVenta() + producto_.getPrecioVenta() * 0.16) * producto_.getCantidad()
				else:
					monto_ += (producto_.getPrecioVenta()) * producto_.getCantidad()
			self.__monto = monto_
		else:
			self.__monto = 0
	
	def getMonto(self):
		self.setMonto()
		return self.__monto
	
	def setCliente(self, cliente):
		self.__cliente = cliente
	
	def getCliente(self):
		return self.__cliente
	
	def addProducto(self, producto):
		self.__producto.append(producto)

	def delProducto(self, nombre, cantidad):
		for i in range(len(self.__producto)):
			if ((nombre == str(self.__producto[i].getNombre())) and (cantidad == self.__producto[i].getCantidad())):
				del self.__producto[i]
				break

	def getProducto(self):
		return self.__producto

	def truncate(self, f, n):
		'''Truncates/pads a float f to n decimal places without rounding'''
		s = '{}'.format(f)
		if 'e' in s or 'E' in s:
			return '{0:.{1}f}'.format(f, n)
		i, p, d = s.partition('.')
		return '.'.join([i, (d+'0'*n)[:n]])
