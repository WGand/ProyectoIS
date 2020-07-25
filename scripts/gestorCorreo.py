import random
import smtplib
from urllib.request import urlopen
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

class GestorCorreo():
    def __init__(self):
        self.correoAbasto = "manejadorabasto@gmail.com"
        self.claveCorreoAbasto = r"inventarioabasto1"
        self.msg = MIMEMultipart('alternative')
        self.msg['From'] = self.correoAbasto
        self.s = smtplib.SMTP_SSL('smtp.gmail.com')
    
    def sendEmail(self, objetivo, asunto, mensaje):
        self.msg['To'] = objetivo
        self.msg['Subject'] = asunto
        html = mensaje
        part2 = MIMEText(html, 'html')
        self.msg.attach(part2)
        self.s.login(self.correoAbasto, self.claveCorreoAbasto)
        try:
            self.s.sendmail(self.correoAbasto, objetivo, self.msg.as_string())
            self.s.quit()
            return 1
        except:
            self.s.quit()
            return 0

    def enviarCorreoSeguridad(self, usuario, usuarioAccion, objetivo, motivo, admin):
        if motivo == 'Eliminar':
            asunto = "Usuario eliminado"
            mensaje = usuario + " ha eliminado a " + usuarioAccion + " del sistema"
        elif motivo == "Anadir":
            asunto = "Usuario añadido"
            if admin:
                mensaje = usuario + " ha añadido a " + usuarioAccion + " al sistema con permisos de administrador"
            else:
                mensaje = mensaje = usuario + " ha añadido a " + usuarioAccion + " al sistema"
        self.msg['To'] = objetivo
        self.msg['Subject'] = asunto
        html = mensaje
        part2 = MIMEText(html, 'html')
        self.msg.attach(part2)
        self.s.login(self.correoAbasto, self.claveCorreoAbasto)
        try:
            self.s.sendmail(self.correoAbasto, objetivo, self.msg.as_string())
            self.s.quit()
            return 1
        except:
            self.s.quit()
            return 0


    def enviarReporte(self, objetivo, usuario):
        # open the file to be sent
        filename = "csv.csv"
        attachment = open("../CSV/csv.csv", "rb") 

        # instance of MIMEBase and named as p 
        p = MIMEBase('application', 'octet-stream') 

        # To change the payload into encoded form 
        p.set_payload((attachment).read()) 

        # encode into base64 
        encoders.encode_base64(p) 

        p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 

        # attach the instance 'p' to instance 'msg' 
        self.msg.attach(p) 
        i = self.sendEmail(objetivo, 'Reporte de movimientos', 'Reporte generado por '+usuario+'.')
        if i:
            return 1
        else:
            return 0

    def codigoConfirmacion(self, objetivo):
        codigo = random.randint(999, 9999)
        i = self.sendEmail(objetivo, 'Código de confirmación', 'Su código de confirmación es: '+ str(codigo))
        if i:
            return codigo
        else:
            return 0

class verificarConexion():
    def __init__(self):
        self.pagina = "http://216.58.192.142"
    
    def verificar(self):
        try:
            urlopen(self.pagina, timeout = 1)
            return True
        except:
            return False