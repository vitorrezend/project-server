# scripts/folders.py
import subprocess
import sys
import logging
import os

def create_folders():
    backup_dir = "/backup/"
    os.makedirs(backup_dir, exist_ok=True)
    os.makedirs("/backup/gd", exist_ok=True)

    try:
        subprocess.run(["chown", "-R", "mt8:mt8", "/backup"])
        logging.info("Permissões configuradas com sucesso.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Erro ao configurar permissões: {e}")
        sys.exit(1)

