from flask import Flask
from flask_apscheduler import APScheduler
import time
import smtplib
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import base64
import traceback
from datetime import datetime, timedelta
from apscheduler.triggers.cron import CronTrigger
import requests
from oauthlib.oauth2 import BackendApplicationClient
from requests.auth import HTTPBasicAuth
from smtplib import SMTP
from email.utils import parseaddr

import connectSSH

#Inicializar servicios

conexionSSH = connectSSH


# set configuration values
class Config:
    SCHEDULER_API_ENABLED = True

# Inicializar app flask
app = Flask(__name__)
app.config.from_object(Config())

# initialize scheduler
scheduler = APScheduler()

def main():

    # Realiza la conexion SSH al servidor y obtiene el registro del comando indicado.
    output = conexionSSH.connectSSH('show service ipsec')






    return 0

@scheduler.task(trigger=CronTrigger(hour=9, minute=0, day_of_week="mon-fri"), id='1')
def tarea_1():
    try:
        print("Ejecutando tarea 1...")
        # Código de la tarea 1
        main()
        
    except Exception as e:
        print(f"Error en tarea 1: {e}")
        traceback.print_exc()

        # Calcular el próximo momento para ejecutar la tarea, 10 segundos después del error
        next_run_time = datetime.now() + timedelta(seconds=10)

       # Puedes reprogramar la tarea para intentar nuevamente
        scheduler.add_job(id=f'1_{time.time}', func=tarea_1, trigger='date', run_date=next_run_time)

@scheduler.task(trigger=CronTrigger(hour=12, minute=0, day_of_week="mon-fri"), id='2')
def tarea_2():
    try:
        print("Ejecutando tarea 2...")
        # Código de la tarea 2
        main()

    except Exception as e:
        print(f"Error en tarea 2: {e}")
        traceback.print_exc()

        # Calcular el próximo momento para ejecutar la tarea, 10 segundos después del error
        next_run_time = datetime.now() + timedelta(seconds=10)

       # Puedes reprogramar la tarea para intentar nuevamente
        scheduler.add_job(id=f'2_{time.time}', func=tarea_2, trigger='date', run_date=next_run_time)

@scheduler.task(trigger=CronTrigger(hour=15, minute=0, day_of_week="mon-fri"), id='3')
def tarea_3():
    try:
        print("Ejecutando tarea 3...")
        # Código de la tarea 3
        main()

    except Exception as e:
        print(f"Error en tarea 3: {e}")
        traceback.print_exc()

        # Calcular el próximo momento para ejecutar la tarea, 10 segundos después del error
        next_run_time = datetime.now() + timedelta(seconds=10)

       # Puedes reprogramar la tarea para intentar nuevamente
        scheduler.add_job(id=f'3_{time.time}', func=tarea_3, trigger='date', run_date=next_run_time)



scheduler.init_app(app)
scheduler.start()

if __name__ == '__main__':
    app.run()