from manejadorDataBase import ConexionDataBase
from PyQt5.QtCore import Qt
from datetime import date

class GestorCsv():
    def __init__(self,usuario):
        self.conector = ConexionDataBase()
        self.culpable = usuario
        self.movimientos = self.conector.buscarMovimientos()

    def crearArchivo(self):
        archivo = open(r"../CSV/csv.txt", "w")
        archivo.write('Fecha: '+str(date.today())+',\nReporte generado por: '+self.culpable+',\n')
        archivo.write('JUSTIFICACION,MONTO,FIRMA,FECHA\n')
        montoTotal = 0
        for mov in self.movimientos:
            archivo.write(mov.getJustificacion()+',')
            if mov.getTipo():
                montoTotal += mov.getMonto()
                archivo.write('+ '+str(mov.getMonto())+',')
            else:
                montoTotal -= mov.getMonto()
                archivo.write('- '+str(mov.getMonto())+',')
            archivo.write(mov.getUsuario()+','+mov.getFecha().toString(Qt.ISODate))
            archivo.write('\n')
        archivo.write('\n,MONTO TOTAL: '+str(montoTotal))
        archivo.close()
