import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
import time

firma_path = 'firmas/firma_carlos.png'

def sendEmail(destinatarios, asunto, cc, local_path):

    # Configura los detalles del correo
    remitente = "app@acdata.cl"  # Cambia por tu correo de dominio propio
    password = "jtzgdfwnkmgnkpgy"  # Cambia por tu contraseña 

    # Carga la firma desde el archivo
    if local_path:
        with open(local_path, 'rb') as firma_file:
            estado_imagen = firma_file.read()
    
    # Convierte la firma a base64
    status_base64 = base64.b64encode(estado_imagen).decode("utf-8")
    
    # Carga la firma desde el archivo
    if firma_path:
        with open(firma_path, 'rb') as firma_file:
            firma_imagen = firma_file.read()

    # Convierte la firma a base64
    firma_base64 = base64.b64encode(firma_imagen).decode("utf-8")

    cuerpo_html = f"""
            <html>
            <body>
                <p>Estimados:</p>
                <p>Junto con saludar, se adjunta estado cato del día de hoy:</p>
                <img src="data:image/png;base64,{status_base64}" alt="Status">
                <p>Saludos Cordiales.</p>
                <img src="data:image/png;base64,{firma_base64}" alt="Firma">
            </body>
            </html>
            """
    
    subject = asunto
    cuerpo = cuerpo_html
    ruta_adjunto = local_path

    # Configura el mensaje
    mensaje = MIMEMultipart()
    mensaje['From'] = remitente
    mensaje['To'] = ", ".join(destinatarios)
    mensaje['Subject'] = subject
    
    if cc:
        mensaje['Cc'] = ", ".join(cc)

    mensaje.attach(MIMEText(cuerpo, 'html'))

    if firma_path:
        # Adjunta la imagen de la firma al mensaje
        firma_adjunta = MIMEImage(firma_imagen, name='firma_carlos.png')
        mensaje.attach(firma_adjunta)

    if(ruta_adjunto):

        # Adjunta la imagen al mensaje
        with open(ruta_adjunto, 'rb') as adjunto:
            imagen_adjunta = MIMEImage(adjunto.read(), name=f'Estado_CATO_{time.time()}.png')
        mensaje.attach(imagen_adjunta)

    # Configura el servidor SMTP de Gmail
    servidor_smtp = "smtp.office365.com"
    #smtp-mail.outlook.com
    #smtp.office365.com
    #smtp.gmail.com
    
    puerto_smtp = 587

    # Crea una conexión al servidor SMTP
    sesion_smtp = smtplib.SMTP(servidor_smtp, puerto_smtp)
    sesion_smtp.starttls()
    
    try:
        # Inicia sesión en el servidor
        sesion_smtp.login(remitente, password)

        # Envía el mensaje
        sesion_smtp.sendmail(remitente, destinatarios + cc, mensaje.as_string())
        print("Correo enviado con éxito")

        # Retorna True indicando que el correo fue enviado correctamente
        return True

    except smtplib.SMTPAuthenticationError as e:
        print(f"Error de autenticación: {e}")
        # Retorna False indicando que hubo un error al enviar el correo
        return False
    finally:
        # Cierra la conexión
        sesion_smtp.quit()