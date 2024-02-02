
from PIL import Image, ImageDraw, ImageFont
import time

local_path = f"screenshots/local_screenshot_{time.time()}.png"

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