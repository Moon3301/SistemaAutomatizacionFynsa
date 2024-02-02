import paramiko
import time

# Configuración de la conexión SSH
hostname = '192.168.31.1'
port = 22
username = 'admin'
password = 'Fynsa_Edge2021@'

def connectSSH(comand):
    # Crear una instancia de la clase SSHClient
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Conectar al servidor
        ssh.connect(hostname, port, username, password)

        # Ejecutar comandos SSH de manera interactiva
        channel = ssh.invoke_shell()

        print(f"Ejecutando comando: {comand}")
                        
        # Ejecuta el comando
        channel.send(comand + '\n')

        # Espera hasta que haya datos disponibles en el canal
        # Espera un tiempo para que el comando se ejecute
        time.sleep(2)

        # Lee la salida
        output = channel.recv(4096).decode()

        # Imprime la salida
        print(f"Resultado de '{comand}':")
        print(output)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Cerrar la conexión SSH
        ssh.close()

    return output