import dropbox
import os
from dotenv import load_dotenv

load_dotenv()
dbx = dropbox.Dropbox(os.getenv('token_dropbox'))
dbx.users_get_current_account()


def enviar_backup(horario_backup):
  with open(f'./backups/backup_{horario_backup}.sql', 'rb') as f:
    arquivo = f.read()
  dbx.files_upload(arquivo, f'/backup_{horario_backup}.sql')
  return print('Upload realizado')