import re
import time
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import sendEmail

enviarCorreo = sendEmail

local_path = f"screenshots/local_screenshot_{time.time()}.png"

def validateTunnelStatus(output):
    # Convierte el log en un string
    log = str(output)
          
    # busca las palabras UP o DOWN en la palabra Status.
    status_matches = re.findall(r'Status: (UP|DOWN)', log)

    print(r'Status Actual: ',status_matches)

    tunel1 = status_matches[0]
    tunel2 = status_matches[1]
    tunel3 = status_matches[2]

    print(r'Status tunel 1: ', tunel1)
    print(r'Status tunel 2: ', tunel2)
    print(r'Status tunel 3: ', tunel3)

    if tunel1 == 'UP' and tunel2 == 'UP' and tunel3 == 'UP':
       
        time.sleep(1)
        # Crea una imagen y copia el status del tunnel
        createImageFromLog(log)

        # Obtener la fecha y hora actual
        fecha_hora_actual = datetime.now()
        # Formatear la fecha y hora en el formato deseado
        formato_deseado = "%d-%m-%Y %H:%M"
        fecha_hora_formateada = fecha_hora_actual.strftime(formato_deseado)

        asunto = f'ESTADO CATO {fecha_hora_formateada}'

        correo_enviado = enviarCorreo.sendEmail(['hortega@fynsa.cl', 'Mallende@fynsa.cl'], asunto, ['helpdesk@acdata.cl'], local_path)

        if correo_enviado:
            print("Correo enviado exitosamente.")
        else:
            print("Error al enviar el correo.")
    else:
        
        time.sleep(1)

        #captureCmdScreenshot(local_path)
        createImageFromLog(log)

        # Obtener la fecha y hora actual
        fecha_hora_actual = datetime.now()
        # Formatear la fecha y hora en el formato deseado
        formato_deseado = "%d-%m-%Y %H:%M"
        fecha_hora_formateada = fecha_hora_actual.strftime(formato_deseado)

        asunto = f'ESTADO CATO {fecha_hora_formateada}'

        status_tunnel = f'Estimados:\n\n Se indica registro de error en cato: \n\n{log}'
        
        # Envía el correo electrónico con la captura de pantalla adjunta
        correo_enviado = enviarCorreo.sendEmail(['helpdesk@acdata.cl'], asunto, [], local_path)

        if correo_enviado:
            print("Correo enviado exitosamente.")
        else:
            print("Error al enviar el correo.")

def validateTunnelStatus1(output):
    
    # busca las palabras UP o DOWN en la palabra Status.
    status_matches = re.findall(r'Status: (UP|DOWN)', output)

    print(r'Status Actual: ',status_matches)

    tunel1 = status_matches[0]
    tunel2 = status_matches[1]
    tunel3 = status_matches[2]

    print(r'Status tunel 1: ', tunel1)
    print(r'Status tunel 2: ', tunel2)
    print(r'Status tunel 3: ', tunel3)

    if tunel1 == 'UP' and tunel2 == 'UP' and tunel3 == 'UP':

        return True
    
    else:

        return False
    
def createImageFromLog(log):
    # Configura el tamaño y el formato de la imagen
    image_width = 800
    image_height = 600
    background_color = (0, 0, 0)  # Fondo negro
    text_color = (255, 255, 255)  # Texto blanco

    # Crea una imagen en blanco con fondo negro
    image = Image.new("RGB", (image_width, image_height), background_color)
    draw = ImageDraw.Draw(image)

    # Carga una fuente monoespaciada que asemeje el estilo de consola
    font_path = "consola.ttf"  # Descarga una fuente de consola monoespaciada

    try:
        font = ImageFont.truetype(font_path, 14)
    except IOError:
        # Si la fuente no está disponible, utiliza la fuente por defecto
        font = ImageFont.load_default()

    # Divide el log en líneas
    lines = log.split('\n')

    # Escribe cada línea en la imagen con el estilo de consola
    y_position = 10
    for line in lines:
        draw.text((10, y_position), line, font=font, fill=text_color)
        y_position += 18  # Ajusta el espacio entre líneas según sea necesario

    # Guarda la imagen
    image.save(local_path)



    


