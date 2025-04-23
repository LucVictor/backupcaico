import os
from datetime import datetime, timezone
import subprocess
from drive import enviar_backup
from dotenv import load_dotenv
import schedule
import time


load_dotenv()
endereco_banco =os.getenv('endereco_banco')
porta_banco = os.getenv('porta_banco')
usuario_banco = os.getenv('usuario_banco')
senha_banco = os.getenv('senha_banco')
banco = os.getenv('banco')


def realizar_backup():
    horario_backup = datetime.now()
    comando_backup = f"mysqldump -h {endereco_banco} -u {usuario_banco} --port={porta_banco} -p{senha_banco} {banco} > './backups/backup_{horario_backup}.sql'"
    comando = subprocess.run(comando_backup, shell=True, capture_output=True, text=True)
    enviar_backup(horario_backup)
    return print('Backup realizado')


schedule.every().day.at("18:00").do(realizar_backup)

while True:
    schedule.run_pending()
    time.sleep(1)