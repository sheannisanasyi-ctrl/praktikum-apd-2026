from prettytable import PrettyTable
from helper import bersihkanLayar, tekanEnter
from data import dataObat

def hitungSisaStok(obat):
    return obat["stok"] - obat["dikonsumsi"]

def hitungJumlahObat():
    return len(dataObat)

def buatIdBaru():
    if not dataObat:
        return 1
    return max(dataObat.keys()) + 1

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

    return 1 <= hari <= jumlahHari[bulan - 1]

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
        if idPilih in dataObat:
            return idPilih
        print("ID obat tidak ditemukan!")
    except ValueError:
        print("Input harus berupa angka!")
    return None

def hitungObatMenipis(listId, batas=10):
    if not listId:
        return 0
    sisa = hitungSisaStok(dataObat[listId[0]])
    return (1 if sisa < batas else 0) + hitungObatMenipis(listId[1:], batas)

def tampilTabelObat():
    if hitungJumlahObat() == 0:
        print("Data obat masih kosong!")
        return

    tabel = PrettyTable()
    tabel.field_names = ["ID", "Nama Obat", "Stok Awal", "Tanggal Kadaluarsa", "Jumlah Dikonsumsi", "Sisa Stok"]
    tabel.align = "c"
    tabel.hrules = 1

    for idObat, obat in dataObat.items():
        tabel.add_row([
            idObat,
            obat["nama"],
            obat["stok"],
            obat["kadaluarsa"],
            obat["dikonsumsi"],
            hitungSisaStok(obat)
        ])

    print(tabel)
    obatMenipis = hitungObatMenipis(list(dataObat.keys()), 10)
    print(f"Jumlah obat yang menipis: {obatMenipis}")

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
        print("Jumlah obat yang sudah dikonsumsi berhasil diperbarui!")
    elif pilihUbah == "5":
        namaBaru = inputTeks("Masukkan nama obat: ", "Nama obat")
        stokBaru = inputAngka("Masukkan jumlah stok: ")
        kadaluarsaBaru = inputTanggal("Masukkan tanggal kadaluarsa (YYYY-MM-DD): ")
        konsumsiBaru = inputAngka("Masukkan jumlah obat yang sudah dikonsumsi: ", 0, stokBaru)
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