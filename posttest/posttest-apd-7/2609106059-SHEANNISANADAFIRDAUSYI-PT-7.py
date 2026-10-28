import os

dataPengguna = {
    "shean": {"password": "3005", "role": "admin"},
    "user": {"password": "0508", "role": "user"}
}

dataObat = {
    1: {"nama": "Paracetamol", "stok": 50, "kadaluarsa": "2027-01-31", "dikonsumsi": 5},
    2: {"nama": "Amoxicillin", "stok": 30, "kadaluarsa": "2027-02-28", "dikonsumsi": 2},
    3: {"nama": "Ibuprofen", "stok": 20, "kadaluarsa": "2027-03-31", "dikonsumsi": 0},
    4: {"nama": "Cetirizine", "stok": 40, "kadaluarsa": "2027-04-30", "dikonsumsi": 3},
    5: {"nama": "Antasida Doen", "stok": 100, "kadaluarsa": "2027-05-31", "dikonsumsi": 15},
    6: {"nama": "Ambroxol", "stok": 25, "kadaluarsa": "2027-06-30", "dikonsumsi": 8},
    7: {"nama": "Lansoprazole", "stok": 15, "kadaluarsa": "2027-07-31", "dikonsumsi": 12},
    8: {"nama": "Demacolin", "stok": 60, "kadaluarsa": "2027-08-31", "dikonsumsi": 4},
    9: {"nama": "Diapet", "stok": 80, "kadaluarsa": "2027-09-30", "dikonsumsi": 6},
    10: {"nama": "Mefenamic Acid", "stok": 35, "kadaluarsa": "2027-10-31", "dikonsumsi": 9}
}

loginSukses = False
role = ""

def bersihkanLayar():
    os.system("cls" if os.name == "nt" else "clear")

def tekanEnter(pesan="\nTekan Enter untuk melanjutkan..."):
    input(pesan)

def hitungObatMenipis(listId, batas=10):
    if len(listId) == 0:
        return 0
    idPertama = listId[0]
    sisa = hitungSisaStok(dataObat[idPertama])

    if sisa < batas:
        return 1 + hitungObatMenipis(listId[1:], batas)
    else:
        return 0 + hitungObatMenipis(listId[1:], batas)

def tampilTabelObat():
    if hitungJumlahObat() == 0:
        print("Data obat masih kosong!")
        return

    print(f"{'ID':<4} | {'Nama Obat':<15} | {'Stok Awal':<9} | " 
        f"{'Tanggal Kadaluarsa':<18} | {'Jumlah Dikonsumsi':<17} | {'Sisa Stok'}")
    print("-" * 87)

    for idObat, obat in dataObat.items():
        print(f"{idObat:<4} | {obat['nama']:<15} | {obat['stok']:<9} | "
            f"{obat['kadaluarsa']:<18} | {obat['dikonsumsi']:<17} | {hitungSisaStok(obat)}")

    obatMenipis = hitungObatMenipis(list(dataObat.keys()), 10)
    print("-" * 87)
    print(f"Jumlah jenis obat dengan stok menipis (< 10): {obatMenipis}")

def buatIdBaru():
    idTerbesar = 0
    for idObat in dataObat.keys():
        if idObat > idTerbesar:
            idTerbesar = idObat
    return idTerbesar + 1

def hitungJumlahObat():
    return len(dataObat)

def hitungSisaStok(obat):
    return obat["stok"] - obat["dikonsumsi"]

def validasiTanggal(tanggal):
    if not (len(tanggal) == 10
            and tanggal[4] == "-"
            and tanggal[7] == "-"
            and tanggal[:4].isdigit()
            and tanggal[5:7].isdigit()
            and tanggal[8:].isdigit()):
        return False

    tahun = int(tanggal[:4])
    bulan = int(tanggal[5:7])
    hari = int(tanggal[8:])

    if bulan < 1 or bulan > 12:
        return False

    jumlahHari = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if tahun % 400  == 0 or (tahun % 4 == 0 and tahun % 100 != 0):
        jumlahHari[1] = 29

    return hari >= 1 and hari <= jumlahHari[bulan - 1]

def inputAngka(pesan, minimal=0, maksimal=None):
    teks = input(pesan)
    try:
        angka = int(teks)
    except ValueError:
        print("Input harus berupa angka!")
        return inputAngka(pesan, minimal, maksimal)

    if angka < minimal:
        print(f"Angka tidak boleh kurang dari {minimal}!")
        return inputAngka(pesan, minimal, maksimal)
    if maksimal is not None and angka > maksimal:
        print(f"Angka tidak boleh lebih dari{maksimal}")
        return inputAngka(pesan, minimal, maksimal)
    return angka

def inputTeks(pesan, namaInput):
    teks = input(pesan).strip()
    while teks == "":
        print(f"{namaInput} tidak boleh kosong!")
        teks = input(pesan).strip()
    return teks

def inputTanggal(pesan):
    tanggal = input(pesan).strip()
    while not validasiTanggal(tanggal):
        print("Format tanggal tidak valid! Contoh: 2027-01-31")
        tanggal = input(pesan).strip()
    return tanggal

def inputIdObat(pesan):
    try:
        idPilih = int(input(pesan))
        dataObat[idPilih]
        return idPilih
    except ValueError:
        print("Input harus berupa angka!")
    except KeyError:
        print("ID obat tidak ditemukan!")
    return None

def prosesLogin():
    global loginSukses, role
    bersihkanLayar()
    print("\n--- LOGIN ---")
    username = input("Username: ")
    password = input("Password: ")

    try:
        akun = dataPengguna[username]
        if akun["password"] != password:
            raise ValueError("Password salah!")
        loginSukses = True
        role = akun["role"]
        print("Login Berhasil!")
    except (KeyError, ValueError):
        print("Login gagal! Username atau password salah.")
    tekanEnter()

def prosesBuatAkun():
    bersihkanLayar()
    print("\n--- BUAT AKUN BARU ---")
    usernameBaru = input("Username: ")
    passwordBaru = input("Password: ")

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

def tambahObat():
    bersihkanLayar()
    print("\n--- TAMBAH DATA OBAT ---")
    namaObat = inputTeks("Nama Obat: ", "Nama obat")
    stokAwal = inputAngka("Stok Awal: ")
    tanggalKadaluarsa = inputTanggal("Tanggal Kadaluarsa (YYYY-MM-DD): ")
    konsumsi = inputAngka("Jumlah yang sudah dikonsumsi: ", 0, stokAwal)

    idBaru = buatIdBaru()
    dataObat[idBaru] = {
        "nama": namaObat,
        "stok": stokAwal,
        "kadaluarsa": tanggalKadaluarsa,
        "dikonsumsi": konsumsi
    }
    print(f"Data obat berhasil ditambahkan dengan ID {idBaru}!")
    tekanEnter("\nTekan Enter untuk kembali...")

def ubahObat():
    bersihkanLayar()
    print("\n--- UBAH DATA OBAT ---")

    if hitungJumlahObat() == 0:
        print("Data obat masih kosong!")
        tekanEnter("\nTekan Enter untuk kembali...")
        return

    tampilTabelObat()
    idPilih = inputIdObat("\nPilih ID obat yang mau diubah: ")
    if idPilih is None:
        tekanEnter("\nTekan Enter untuk kembali...")
        return

    obat = dataObat[idPilih]
    bersihkanLayar()
    print(f"\nMengubah data untuk: {obat['nama']}")
    print("1. Ubah Nama Obat")
    print("2. Ubah Stok Awal")
    print("3. Ubah Tanggal Kadaluarsa")
    print("4. Ubah Jumlah Dikonsumsi")
    print("5. Ubah Seluruh Data")
    pilihUbah = input("Pilih bagian yang mau diubah (1-5): ")

    if pilihUbah == "1":
        obat["nama"] = inputTeks("Masukkkan nama obat: ", "Nama obat")
        print("Nama obat berhasil diperbarui!")
    elif pilihUbah == "2":
        obat["stok"] = inputAngka("Masukkan jumlah stok: ", obat["dikonsumsi"])
        print("Stok obat berhasil diperbarui!")
    elif pilihUbah == "3":
        obat["kadaluarsa"] = inputTanggal("Masukkan tanggal kadaluarsa (YYYY-MM-DD): ")
        print("Tanggal kadaluarsa berhasil diperbarui!")
    elif pilihUbah == "4":
        obat["dikonsumsi"] = inputAngka("Masukkan jumlah yang sudah dikonsumsi: ", 0, obat["stok"])
        print("Jumlah dikonsumsi berhasil diperbarui!")
    elif pilihUbah == "5":
        namaBaru = inputTeks("Masukkan nama obat: ", "Nama obat")
        stokBaru = inputAngka("Masukkan jumlah stok: ")
        kadaluarsaBaru = inputTanggal("Masukkan tanggal kadaluarsa (YYYY-MM-DD): ")
        konsumsiBaru = inputAngka("Masukkan jumlah yang sudah dikonsumsi: ", 0, stokBaru)
        obat.update({
            "nama": namaBaru,
            "stok": stokBaru,
            "kadaluarsa": kadaluarsaBaru,
            "dikonsumsi": konsumsiBaru
        })
        print("Seluruh data obat berhasil diperbarui!")
    else:
        print("Pilihan tidak valid!")
    tekanEnter("\nTekan Enter untuk kembali...")

def hapusObat():
    bersihkanLayar()
    print("\n--- HAPUS DATA OBAT ---")

    if hitungJumlahObat() == 0:
        print("Data obat masih kosong!")
    else:
        for idObat, obat in dataObat.items():
            print(f"{idObat:>2}. {obat['nama']}")

        idPilih = inputIdObat("\nPilih ID obat yang mau dihapus: ")
        if idPilih is not None:
            obatDihapus = dataObat.pop(idPilih)
            print(f"Data obat '{obatDihapus['nama']}' berhasil dihapus!")
    tekanEnter("\nTekan Enter untuk kembali...")

def logout():
    global loginSukses, role
    loginSukses = False
    role = ""
    bersihkanLayar()
    print("Berhasil logout!")
    tekanEnter()

def menuUtama():
    bersihkanLayar()
    print("=== DATA STOK OBAT ===")
    print("1. Login")
    print("2. Buat Akun Baru")
    print("3. Keluar")
    pilihan = input("Masukkan pilihan (1-3) ")

    if pilihan == "1":
        prosesLogin()
    elif pilihan == "2":
        prosesBuatAkun()
    elif pilihan == "3":
        bersihkanLayar()
        print("Terima kasih telah menggunakan program ini.")
        return False
    else:
        print("Pilihan tidak valid!")
        tekanEnter()
    return True

def menuSetelahLogin():
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
        logout()
    else:
        print("\nPilihan menu tidak valid!")
        tekanEnter("\nTekan Enter untuk kembali...")

def main():
    jalan = True
    while jalan:
        try:
            if not loginSukses:
                jalan = menuUtama()
            else:
                menuSetelahLogin()
        except ValueError as error:
            print(f"Terjadi kesalahan: {error}")
            tekanEnter()

main()