# scripts/backup.py
import os
import shutil
import sys
import logging

BACKUP_DIR = "/home/mt8/backup/"
VSFTPD_CONF = "/etc/vsftpd.conf"
SAMBA_CONF = "/etc/samba/smb.conf"

def backup_files():
    os.makedirs(BACKUP_DIR, exist_ok=True)
    
    try:
        shutil.copy(VSFTPD_CONF, BACKUP_DIR)
        shutil.copy(SAMBA_CONF, BACKUP_DIR)
        logging.info("Arquivos de configuração copiados com sucesso.")
    except shutil.Error as e:
        logging.error(f"Erro ao realizar backup dos arquivos: {e}")
        sys.exit(1)

