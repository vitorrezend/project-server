# scripts/ports.py
import subprocess
import sys
import logging

def allow_ftp_ports():
    try:
        subprocess.run(["ufw", "allow", "20,21,990/tcp"])
        subprocess.run(["ufw", "allow", "40000:50000/tcp"])
        logging.info("Portas do FTP liberadas com sucesso.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Erro ao liberar portas do FTP: {e}")
        sys.exit(1)

