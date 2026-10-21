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

while True:
    if os.name == "nt":
        os.system("cls")    
    else:
        os.system("clear")

    if not loginSukses:
        print("===  DATA STOK OBAT ===")
        print("1. Login")
        print("2. Buat Akun Baru")
        print("3. Keluar")
        pilihan = input("Masukkan pilihan (1-3): ")

        if pilihan == "1":
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
                    
            print("\n--- LOGIN ---")
            username = input("Username: ")
            password = input("Password: ")

            dataAkun = dataPengguna.get(username)

            if dataAkun is not None and dataAkun["password"] == password:
                loginSukses = True
                role = dataAkun["role"]
                print("Login berhasil!")
            else:
                print("Login gagal! Username atau password salah.")

            input("\nTekan Enter untuk melanjutkan...")

        elif pilihan == "2":
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
                    
            print("\n--- BUAT AKUN BARU ---")
            usernameBaru = input("Username: ")
            passwordBaru = input("Password: ")

            if usernameBaru == "":
                print("Username tidak boleh kosong!")
            elif passwordBaru == "":
                print("Password tidak boleh kosong!")
            elif dataPengguna.get(usernameBaru) is not None:
                print("Username sudah digunakan!")
            else:
                dataPengguna.update ({usernameBaru: {"password": passwordBaru, "role": "user"}})
                print("Akun baru berhasil dibuat! Silakan login.")
        
            input("\nTekan Enter untuk melanjutkan...")

        elif pilihan == "3":
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
                    
            print("Terima kasih telah menggunakan program ini.")
            break   
        else:
            print("Pilihan tidak valid!")
            input("\nTekan Enter untuk melanjutkan...")

    else:
        if role == "admin":
            print(f"\n===  DATA STOK OBAT (Login sebagai {role}) ===")
            print("1. Lihat Data Obat")
            print("2. Tambah Data Obat")
            print("3. Ubah Data Obat")
            print("4. Hapus Data Obat")
            print("5. Logout")
            pilihanMenu = input("Masukkan pilihan (1-5): ")
        else:
            print(f"\n===  DATA STOK OBAT (Login sebagai {role}) ===")
            print("1. Lihat Data Obat")
            print("2. Logout")
            pilihanMenu = input("Masukkan pilihan (1-2): ")
             
        if pilihanMenu == "1":
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")

            print("\n--- DATA OBAT ---")

            if len(dataObat) == 0:
                print("Data obat masih kosong!")
            else:
                print(f"{'ID':<4} | {'Nama Obat':<15} | {'Stok Awal':<9} | " 
                    f"{'Tanggal Kadaluarsa':<18} | {'Jumlah Dikonsumsi':<17} | {'Sisa Stok'}")
                print("-" * 87)

                for idObat, obat in dataObat.items():
                    stokAkhir = obat["stok"] - obat["dikonsumsi"] 
                    print(f"{idObat:<4} | {obat['nama']:<15} | {obat['stok']:<9} | "
                        f"{obat['kadaluarsa']:<18} | {obat['dikonsumsi']:<17} | {stokAkhir}")

            input("\nTekan Enter untuk kembali...")

        elif pilihanMenu == "2" and role == "admin":
                if os.name == "nt":
                    os.system("cls")
                else:
                    os.system("clear")

                print("\n--- TAMBAH DATA OBAT ---")

                namaObat = input("Nama Obat: ")
                while namaObat == "":
                        print("Nama obat tidak boleh kosong!")
                        namaObat = input("Nama Obat: ")
                    
                stokInput = input("Stok Awal: ")
                while not stokInput.isdigit():
                    print("Stok harus berupa angka!")
                    stokInput = input("Stok Awal: ")
                stokAwal = int(stokInput)

                tanggalValid = False
                while not tanggalValid:
                    tanggalKadaluarsa = input("Tanggal Kadaluarsa (YYYY-MM-DD): ")
                    if (len(tanggalKadaluarsa) == 10
                            and tanggalKadaluarsa[4] == "-"
                            and tanggalKadaluarsa[7] == "-"
                            and tanggalKadaluarsa[:4].isdigit()
                            and tanggalKadaluarsa[5:7].isdigit()
                            and tanggalKadaluarsa[8:].isdigit()):
                        bulan = int(tanggalKadaluarsa[5:7])
                        hari = int(tanggalKadaluarsa[8:])
                        if bulan >= 1 and bulan <= 12 and hari >= 1 and hari <= 31:
                            tanggalValid = True
                    if not tanggalValid:
                        print("Format tanggal tidak valid! Contoh: 2000-01-31")

                konsumsiInput = input("Jumlah yang sudah dikonsumsi: ")
                while not konsumsiInput.isdigit() or int(konsumsiInput) > stokAwal:
                    print("Harus berupa angka dan tidak boleh melebihi stok awal!")
                    konsumsiInput = input("Jumlah yang sudah dikonsumsi: ")
                konsumsi = int(konsumsiInput)

                idTerbesar = 0
                for idObat in dataObat.keys():
                    if idObat > idTerbesar:
                        idTerbesar = idObat
                idBaru = idTerbesar + 1

                dataObat[idBaru] = {
                    "nama": namaObat,
                    "stok": stokAwal,
                    "kadaluarsa": tanggalKadaluarsa,
                    "dikonsumsi": konsumsi
                }
                print(f"Data obat berhasil ditambahkan dengan ID {idBaru}!")

                input("\nTekan Enter untuk kembali...")

        elif pilihanMenu == "3" and role == "admin":
                if os.name == "nt":
                    os.system("cls")
                else:
                    os.system("clear")
                    
                print("\n--- UBAH DATA OBAT ---")

                if len(dataObat) == 0:
                    print("Data obat masih kosong!")
                else:
                    print(f"{'ID':<4} | {'Nama Obat':<15} | {'Stok Awal':<9} | " 
                        f"{'Tanggal Kadaluarsa':<18} | {'Jumlah Dikonsumsi':<17} | {'Sisa Stok'}")
                    print("-" * 87)

                    for idObat, obat in dataObat.items():
                        stokAkhir = obat["stok"] - obat["dikonsumsi"]
                        print(f"{idObat:<4} | {obat['nama']:<15} | {obat['stok']:<9} | "
                            f"{obat['kadaluarsa']:<18} | {obat['dikonsumsi']:<17} | {stokAkhir}")

                    idInput = input("Pilih ID obat yang mau diubah: ")

                    if not idInput.isdigit():
                        print("Input harus berupa angka!")
                    elif dataObat.get(int(idInput)) is None:
                        print("ID obat tidak ditemukan!")
                    else:
                        idPilih = int(idInput)

                        if os.name == "nt":
                            os.system("cls")
                        else:
                            os.system("clear")

                        print(f"\nMengubah data untuk: {dataObat[idPilih]['nama']}")
                        print("1. Ubah Nama Obat")
                        print("2. Ubah Stok Awal")
                        print("3. Ubah Tanggal Kadaluarsa")
                        print("4. Ubah Jumlah Dikonsumsi")
                        print("5. Ubah Seluruh Data")
                        pilihUbah = input("Pilih bagian yang mau diubah (1-5): ")

                        if pilihUbah == "1":
                            if os.name == "nt":
                                os.system("cls")
                            else:
                                os.system("clear")
                    
                            namaBaru = input("Masukkan nama obat: ")
                            while namaBaru == "":
                                print("Nama obat tidak boleh kosong!")
                                namabaru = input("Masukkan nama obat: ")

                            dataObat[idPilih]["nama"] = namaBaru
                            print("Nama obat berhasil diperbarui!")

                        elif pilihUbah == "2":
                            if os.name == "nt":
                                os.system("cls")
                            else:
                                os.system("clear")

                            stokInput = input("Masukkan jumlah stok: ")
                            while not stokInput.isdigit() or int(stokInput) < dataObat[idPilih]["dikonsumsi"]:
                                print("Harus berupa angka dan tidak boleh kurang dari jumlah dikonsumsi!")
                                stokInput = input("Masukkan jumlah stok: ")
                            stokBaru = int(stokInput)

                            dataObat[idPilih]["stok"] = stokBaru
                            print("Stok obat berhasil diperbarui!")

                        elif pilihUbah == "3":
                            if os.name == "nt":
                                os.system("cls")
                            else:
                                os.system("clear")

                            tanggalValid = False
                            while not tanggalValid:
                                kadaluarsaBaru = input("Masukkan tanggal kadaluarsa (YYYY-MM-DD): ")
                                if (len(kadaluarsaBaru) == 10
                                        and kadaluarsaBaru[4] == "-"
                                        and kadaluarsaBaru[7] == "-"
                                        and kadaluarsaBaru[:4].isdigit()
                                        and kadaluarsaBaru[5:7].isdigit()
                                        and kadaluarsaBaru[8:].isdigit()):
                                    bulan = int(kadaluarsaBaru[5:7])
                                    hari = int(kadaluarsaBaru[8:])
                                    if bulan >= 1 and bulan <= 12 and hari >= 1 and hari <= 31:
                                        tanggalValid = True
                                if not tanggalValid:
                                    print("Format tanggal tidak valid! Contoh: 2000-01-31")
                                    
                            dataObat[idPilih]["kadaluarsa"] = kadaluarsaBaru
                            print("Tanggal kadaluarsa berhasil diperbarui!")

                        elif pilihUbah == "4":
                            if os.name == "nt":
                                os.system("cls")
                            else:
                                os.system("clear")

                            konsumsiInput = input("Masukkan jumlah obat yang sudah dikonsumsi: ")
                            while not konsumsiInput.isdigit() or int(konsumsiInput) > dataObat[idPilih]["stok"]:
                                print("Harus berupa angka dan tidak boleh melebihi stok awal!")
                                konsumsiInput = input("Masukkan jumlah obat yang sudah dikonsumsi: ")
                            konsumsiBaru = int(konsumsiInput)

                            dataObat[idPilih]["dikonsumsi"] = konsumsiBaru
                            print("Jumlah dikonsumsi berhasil diperbarui!")

                        elif pilihUbah == "5":
                            if os.name == "nt":
                                os.system("cls")
                            else:
                                os.system("clear")

                            namaBaru = input("Masukkan nama obat: ")
                            while namaBaru == "":
                                print("Nama obat tidak boleh kosong!")
                                namaBaru = input("Masukkan nama obat: ")

                            stokInput = input("Masukkan jumlah stok: ")
                            while not stokInput.isdigit():
                                print("Stok harus berupa angka!")
                                stokInput = input("Masukkan jumlah stok: ")
                            stokBaru = int(stokInput)

                            tanggalValid = False
                            while not tanggalValid:
                                kadaluarsaBaru = input("Masukkan tanggal kadaluarsa (YYYY-MM-DD): ")
                                if (len(kadaluarsaBaru) == 10
                                        and kadaluarsaBaru[4] == "-"
                                        and kadaluarsaBaru[7] == "-"
                                        and kadaluarsaBaru[:4].isdigit()
                                        and kadaluarsaBaru[5:7].isdigit()
                                        and kadaluarsaBaru[8:].isdigit()):
                                    bulan = int(kadaluarsaBaru[5:7])
                                    hari = int(kadaluarsaBaru[8:])
                                    if bulan >= 1 and bulan <= 12 and hari >= 1 and hari <= 31:
                                        tanggalValid = True
                                if not tanggalValid:
                                    print("Format tanggal tidak valid! Contoh: 2000-01-31")

                            konsumsiInput = input("Masukkan jumlah obat yang sudah dikonsumsi: ")
                            while not konsumsiInput.isdigit() or int(konsumsiInput) > stokBaru:
                                print("Harus berupa angka dan tidak boleh melebihi stok awal!")
                                konsumsiInput = input("Masukkan jumlah obat yang sudah dikonsumsi")
                            konsumsiBaru = int(konsumsiInput)

                            dataObat[idPilih].update({
                                "nama": namaBaru,
                                "stok": stokBaru,
                                "kadaluarsa": kadaluarsaBaru,
                                "dikonsumsi": konsumsiBaru,
                            })
                            print("Seluruh data obat berhasil diperbarui!")

                        else:
                            print("Pilihan tidak valid!")

                input("Tekan Enter untuk kembali...")

        elif pilihanMenu == "4" and role == "admin":
                if os.name == "nt":
                    os.system("cls")
                else:
                    os.system("clear")
                    
                print("\n--- HAPUS DATA OBAT ---")

                if len(dataObat) == 0:
                    print("Data obat masih kosong!")
                else:
                    for idObat, obat in dataObat.items():
                        print(f"{idObat:>2}). {obat['nama']}")

                    idInput = input("Pilih ID obat yang mau dihapus: ")

                    if not idInput.isdigit():
                        print("Input harus berupa angka!")
                    elif dataObat.get(int(idInput)) is None:
                        print("ID obat tidak ditemukan!")
                    else:
                        obatDihapus = dataObat.pop(int(idInput))
                        print(f"Data obat '{obatDihapus['nama']}' berhasil dihapus!")

                input("\nTekan Enter untuk kembali...")

        elif (role == "user" and pilihanMenu == "2") or (role == "admin" and pilihanMenu == "5"):
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")

            loginSukses = False
            role = ""
            print("Berhasil Logout!")
            input("\nTekan Enter untuk lanjut...")
        else:
            print("Pilihan menu tidak valid!")
            input("\nTekan Enter untuk kembali...")                       