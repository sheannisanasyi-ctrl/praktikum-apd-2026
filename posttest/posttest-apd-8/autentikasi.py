import pwinput
from helper import bersihkanLayar, tekanEnter
from data import dataPengguna

def prosesLogin():
    bersihkanLayar()
    print("\n--- LOGIN ---")
    username = input("Username: ")
    password = pwinput.pwinput(prompt="Password: ", mask="*")

    try:
        if username in dataPengguna and dataPengguna[username]["password"] == password:
            print("Login berhasil!")
            tekanEnter()
            return True, dataPengguna[username]["role"]
        else:
            print("Login gagal! Username atau password salah.")
            tekanEnter()
            return False, ""
    except Exception as e:
        print(f"Error saat login: {e}")
        tekanEnter()
        return False, ""

def prosesBuatAkun():
    bersihkanLayar()
    print("\n--- BUAT AKUN BARU ---")
    usernameBaru = input("Username: ").lower()
    passwordBaru = pwinput.pwinput(prompt="Password: ", mask="*")

    if usernameBaru == "":
        print("Username tidak boleh kosong!")
    elif passwordBaru == "":
        print("Password tidak boleh kosong!")
    elif usernameBaru in dataPengguna:
        print("Username sudah digunakan!")
    else:
        dataPengguna[usernameBaru] = {"password": passwordBaru, "role": "user"}
        print("Akun baru berhasil dibuat! Silakan login.")
    tekanEnter()

def logout():
    bersihkanLayar()
    print("Berhasil logout!")
    tekanEnter()
    return False, ""