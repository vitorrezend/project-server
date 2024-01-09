# scripts/main.py
from installation import install_packages
from ports import allow_ftp_ports
from backup import backup_files
from folders import create_folders
import logging

def main():
    logging.basicConfig(level=logging.INFO)

    print("Iniciando instalação e configuração.")
    input("Pressione Enter para continuar...")

    packages_to_install = ["samba", "vsftpd"]
    
    install_packages(packages_to_install)
    allow_ftp_ports()
    backup_files()
    create_folders()

    print("Instalação e configuração concluídas com sucesso.")

if __name__ == "__main__":
    main()

