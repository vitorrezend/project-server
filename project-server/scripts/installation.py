# scripts/installation.py
import subprocess
import sys
import logging

def install_packages(packages):
    try:
        subprocess.run(["apt", "install"] + packages, check=True)
        logging.info("Pacotes instalados com sucesso.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Erro durante a instalação dos pacotes: {e}")
        sys.exit(1)
