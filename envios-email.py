import smtplib
from email.mime.text import MIMEText


#Configuracion para la cuenta con la que enviaras SMTP

smtp_server = "smtp.office365.com"
smtp_port = 587
smtp_user = "coloca el email aqui"
smtp_password = "coloca la passwords del email aqui"

destinatario = "email destinatario."
asunto = "Asunto del Email"
mensaje = "Mensaje de Prueba numero 2"
from_address = f"PRUEBA DE ENVIO<{smtp_user}>"


#Crear el mensaje MIME
msg = MIMEText(mensaje)
msg['Subject'] = asunto
msg['From'] = from_address
msg['To'] = destinatario

#Script para Enviar mensaje, con StartTTLS

try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.send_message(msg)
    print("Correo Enviado Exitosamente")
except Exception as e:
    print(f"Error al enviar el correo: {e}")