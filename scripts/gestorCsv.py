from manejadorDataBase import ConexionDataBase()
from datetime import date

class gestorCsv():
    def __init__(self, fecha):
        self.conector = ConexionDataBase()
        self.movimientos = self.conector.buscarMovimientosFecha(str(date.today()))

    def crearArchivo(self, movimientos):
        pass