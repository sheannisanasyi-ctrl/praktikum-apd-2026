from helper import bersihkanLayar, tekanEnter
from autentikasi import prosesLogin, prosesBuatAkun, logout
from fitur import tampilTabelObat, tambahObat, ubahObat, hapusObat
from prettytable import PrettyTable

def menuUtama():
    bersihkanLayar()
    print("=== APLIKASI STOK OBAT ===")

    tabelMenu = PrettyTable()
    tabelMenu.field_names = ["No", "Menu Utama"]
    tabelMenu.align = "c"
    tabelMenu.hrules = 1

    tabelMenu.add_row(["1", "Login"])
    tabelMenu.add_row(["2", "Buat Akun Baru"])
    tabelMenu.add_row(["3", "Keluar"])

    print(tabelMenu)
    pilihan = input("Masukkan pilihan (1-3): ")

    if pilihan == "1":
        return prosesLogin()
    elif pilihan == "2":
        prosesBuatAkun()
        return False, ""
    elif pilihan == "3":
        bersihkanLayar()
        print("Terima kasih telah menggunakan program ini.")
        return "keluar", ""
    else:
        print("Pilihan tidak valid!")
        tekanEnter()
    return False, ""

def menuSetelahLogin(role):
    bersihkanLayar()
    print(f"\n=== DATA STOK OBAT (Login sebagai {role}) ===")

    tabelMenu = PrettyTable()
    tabelMenu.field_names = ["No", "Pilihan Menu"]
    tabelMenu.align = "c"
    tabelMenu.hrules = 1

    tabelMenu.add_row(["1", "Lihat Data Obat"])
    
    if role == "admin":
        tabelMenu.add_row(["2", "Tambah Data Obat"])
        tabelMenu.add_row(["3", "Ubah Data Obat"])
        tabelMenu.add_row(["4", "Hapus Data Obat"])
        tabelMenu.add_row(["5", "Logout"])
    else:
        tabelMenu.add_row(["2", "Logout"])

    print(tabelMenu)
    pilihanMenu = input("Masukkan pilihan: ")

    if pilihanMenu == "1":
        bersihkanLayar()
        print("\n--- DATA OBAT ---")
        tampilTabelObat()
        tekanEnter("\nTekan Enter untuk kembali...")
    elif role == "admin" and pilihanMenu == "2":
        tambahObat()
    elif role == "admin" and pilihanMenu == "3":
        ubahObat()
    elif role == "admin" and pilihanMenu == "4":
        hapusObat()
    elif (role == "user" and pilihanMenu == "2") or (role == "admin" and pilihanMenu == "5"):
        return logout()
    else:
        print("\nPilihan menu tidak valid!")
        tekanEnter("\nTekan Enter untuk kembali...")

    return True, role

def main():
    loginSukses = False
    role = ""
    jalan = True

    while jalan:
        try:
            if not loginSukses:
                status, roleBaru = menuUtama()
                if status == "keluar":
                    break
                elif status:
                    loginSukses = True
                    role = roleBaru
            else:
                loginSukses, role = menuSetelahLogin(role)
        except ValueError as error:
            print(f"Terjadi kesalahan: {error}")
            tekanEnter()

if __name__ == "__main__":
    main()