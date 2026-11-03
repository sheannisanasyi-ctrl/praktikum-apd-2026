import os

def bersihkanLayar():
    try:
        os.system("cls" if os.name == "nt" else "clear")
    except Exception:
        pass

def tekanEnter(pesan="\nTekan Enter untuk melanjutkan..."):
    input(pesan)
