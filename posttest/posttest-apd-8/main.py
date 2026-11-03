from helper import bersihkanLayar, tekanEnter
from autentikasi import prosesLogin, prosesBuatAkun, logout
from fitur import tampilTabelObat, tambahObat, ubahObat, hapusObat

def menuUtama():
    bersihkanLayar()
    print("=== DATA STOK OBAT ===")
    print("1. Login")
    print("2. Buat Akun Baru")
    print("3. Keluar")
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
    print("1. Lihat Data Obat")
    if role == "admin":
        print("2. Tambah Data Obat")
        print("3. Ubah Data Obat")
        print("4. Hapus Data Obat")
        print("5. Logout")
        pilihanMenu = input("Masukkan pilihan (1-5): ")
    else:
        print("2. Logout")
        pilihanMenu = input("Masukkan pilihan (1-2): ")

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