import json
import time
import sys
import os
from colorama import init, Fore

init(autoreset=True)

path = "D:/py/file-mcmeta/pack.mcmeta"

def generate_pack_mcmeta(pack_format, description):
    mcmeta = {
        "pack": {
            "pack_format": pack_format,
            "description": description
        }
    }

    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w") as file:
        json.dump(mcmeta, file, indent=4)
    print("File pack.mcmeta telah berhasil dibuat.")

def user_guide():
    guide = f"""
{Fore.GREEN}
    Cara Menggunakan Script Pack.mcmeta Generator:

    python pack_mcmeta_generator.py [action]

    Actions:
      create  - Membuat file pack.mcmeta dengan meminta input 'pack_format' dan 'description'
      help    - Menampilkan bantuan ini
      quit    - Keluar dari script

    Contoh:
      python pack_mcmeta_generator.py create
      python pack_mcmeta_generator.py help
      python pack_mcmeta_generator.py quit
{Fore.RESET}
    """
    print(guide)

def version():
    version_info = f"""
{Fore.GREEN}
    pack_format Guide:

    (-) 1.6.1 - 1.8.9 = 1
    (-) 1.9 - 1.10.2 = 2
    (-) 1.11 - 1.12.2 = 3
    (-) 1.13 - 1.14.4 = 4
    (-) 1.15 - 1.16.1 = 5
    (-) 1.16.2 - 1.16.5 = 6
    (-) 1.17 - 1.17.1 = 7
    (-) 1.18 - 1.18.2 = 8
    (-) 1.19 - 1.19.2 = 9
    (-) 1.19.3 = 12
    (-) 1.19.4 = 13
    (-) 1.20 - 1.20.1 = 15
    (-) 1.20.2 = 18
    (-) 1.20.3 - 1.20.4 = 22
    (-) 1.20.5 = 32
    (-) 1.21 - 1.21.1 = 34
    (-) 1.21.2 - 1.21.3 = 42
{Fore.RESET}
    """
    print(version_info)

print("Ketik 'create' untuk membuat pack.mcmeta, 'help' untuk bantuan, dan 'quit' untuk selesai.")

while True:
    action = input("create/help/quit: ").strip().lower()

    if action == "create":
        try:
            pack_format = int(input("Masukkan pack_format sesuai versi MC yang diinginkan: "))
            description = input("Masukkan deskripsi untuk resource pack: ")
            print("Membuat file...")
            time.sleep(2)
            generate_pack_mcmeta(pack_format, description)
        except ValueError:
            print("Error: pack_format harus berupa angka.")

    elif action == "help":
        print("1. User Guide \n2. pack_format version")
        choice = input("Pilih (1/2): ").strip()

        if choice == "1":
            user_guide()
        elif choice == "2":
            version()
        else:
            print("Error: input tidak valid.")

    elif action == "quit":
        print("Program selesai.")
        sys.exit(0)

    else:
        print("Error: input tidak valid. Silakan coba lagi.")
