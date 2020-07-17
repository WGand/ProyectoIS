import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
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


    def codigoConfirmacion(self, objetivo):
        codigo = random.randint(999, 9999)
        i = self.sendEmail(objetivo, 'Código de confirmación', 'Su código de confirmación es: '+ str(codigo))
        if i:
            return codigo
        else:
            return 0