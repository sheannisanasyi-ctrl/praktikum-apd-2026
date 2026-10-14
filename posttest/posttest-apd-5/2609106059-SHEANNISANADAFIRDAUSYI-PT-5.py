import os

dataPengguna = [
    ["shean", "3005", "admin"],
    ["user", "0508", "user"]
]

dataObat = [
    ["Paracetamol", 50, "2027-01-31", 5],
    ["Amoxicillin", 30, "2027-02-28", 2],
    ["Ibuprofen", 20, "2027-03-31", 0],
    ["Cetirizine", 40, "2027-04-30", 3],
    ["Antasida Doen", 100, "2027-05-31", 15],
    ["Ambroxol", 25, "2027-06-30", 8],
    ["Lansoprazole", 15, "2027-07-31", 12],
    ["Demacolin", 60, "2027-08-31", 4],
    ["Diapet", 80, "2027-09-30", 6],
    ["Mefenamic Acid", 35, "2027-10-31", 9]
]

statusLogin = False
role = ""

while True:
    if os.name == "nt":
        os.system("cls")    
    else:
        os.system("clear")

    if not statusLogin:
        print("===  DATA STOK OBAT ===")
        print("1. Login")
        print("2. Buat Akun Baru")
        print("3. Keluar")
        pilihan = input("Masukkan pilihan (1-3): ")

        if pilihan == "1":
            print("\n--- LOGIN ---")
            username = input("Username: ")
            password = input("Password: ")

            loginBerhasil = False
            for akun in dataPengguna:
                if akun[0] == username and akun[1] == password:
                    loginBerhasil = True
                    role = akun[2]
                    break

            if loginBerhasil:
                statusLogin = True
                print("Login berhasil!")
            else:
                print("Login gagal. Username atau password salah.")

            input("\nTekan Enter untuk melanjutkan...")

        elif pilihan == "2":
            print("\n--- BUAT AKUN BARU ---")
            usernameBaru = input("Username: ")
            passwordBaru = input("Password: ")

            if usernameBaru != "":
                if passwordBaru != "":
                    dataPengguna.append([usernameBaru, passwordBaru, "user"])
                    print("Akun baru berhasil dibuat! Silakan login")
                else:
                    print("Password tidak boleh kosong!")
            else:
                print("Username tidak boleh kosong!")
        
            input("\nTekan Enter untuk melanjutkan...")

        elif pilihan == "3":
            print("Terima kasih telah menggunakan program ini.")
            break   
        else:
            print("Pilihan tidak valid!")
            input("\nTekan Enter untuk melanjutkan...")

    else:
        print(f"\n===  DATA STOK OBAT (Login sebagai {role}) ===")
        print("1. Lihat Data Obat")
        print("2. Tambah Data Obat")
        print("3. Ubah Data Obat")
        print("4. Hapus Data Obat")
        print("5. Logout")
        pilihanMenu = input("Masukkan pilihan (1-5): ")

        if pilihanMenu == "1":
            print("\n--- DATA OBAT ---")
            print(f"{'No':<4} | {'Nama Obat':<15} | {'Stok Awal':<9} | {'Tanggal Kadaluarsa':<10} | {'Jumlah Dikonsumsi':<9} | {'Sisa Stok'}")
            print("-" * 87)

            i = 0
            while i < len(dataObat):
                nama = dataObat[i][0]
                stokAwal = dataObat[i][1]
                tanggalKadaluarsa = dataObat[i][2]
                dikonsumsi = dataObat[i][3]

                stokAkhir = stokAwal - dikonsumsi

                print(f"{i+1:<3}. | {nama:<15} | {str(stokAwal):<9} | {str(tanggalKadaluarsa):<18} | {str(dikonsumsi):<17} | {stokAkhir}")
                i = i + 1
            input("\nTekan Enter untuk kembali...")

        elif pilihanMenu == "2":
            if role == "admin":
                print("\n--- TAMBAH DATA OBAT ---")
                namaObat = input("Nama Obat: ")
                stokAwal = int(input("Stok Awal: "))
                TanggalKadaluarsa = input ("Tanggal Kadaluarsa: ")
                konsumsi = int(input("Jumlah yang sudah dikonsumsi: "))

                dataObat.append([namaObat, stokAwal, TanggalKadaluarsa, konsumsi])
                print("Data obat berhasil ditambahkan!")
            else:
                print("\nAkses ditolak! Menu ini khusus admin.")
            input("\nTekan Enter untuk kembali...")

        elif pilihanMenu == "3":
            if role == "admin":
                print("\n--- UBAH DATA OBAT ---")
                print(f"{'No':<4} | {'Nama Obat':<15} | {'Stok Awal':<9} | {'Tanggal Kadaluarsa':<10} | {'Jumlah Dikonsumsi':<9} | {'Sisa Stok'}")
                print("-" * 87)

                i = 0
                while i < len(dataObat):
                    nama = dataObat[i][0]
                    stokAwal = dataObat[i][1]
                    tanggalKadaluarsa = dataObat[i][2]
                    dikonsumsi = dataObat[i][3]
                    stokAkhir = stokAwal - dikonsumsi
                    
                    print(f"{i+1:<3} | {nama:<16} | {str(stokAwal):<9} | {str(tanggalKadaluarsa):<18} | {str(dikonsumsi):<17} | {stokAkhir}")
                    i = i + 1

                indeks = int(input("Pilih nomor obat yang mau diubah: ")) - 1

                if indeks >= 0:
                    if indeks < len(dataObat):
                        print(f"Mengubah data untuk: {dataObat[indeks][0]}")
                        print("1. Ubah Nama Obat")
                        print("2. Ubah Stok Awal")
                        print("3. Ubah Tanggal Kadaluarsa")
                        print("4. Ubah Jumlah Dikonsumsi")
                        print("5. Ubah Seluruh Data")
                        pilihUbah = input("Pilih bagian yang mau diubah (1-5)")

                        if pilihUbah == "1":
                            namaBaru = input("Masukkan nama obat: ")
                            dataObat[indeks][0] = namaBaru
                            print("Nama obat berhasil diperbarui!")
                        elif pilihUbah == "2":
                            stokBaru = int(input("Masukkan jumlah stok: "))
                            dataObat[indeks][1] = stokBaru
                            print("Stok obat berhasil diperbarui!")
                        elif pilihUbah == "3":
                            kadaluarsaBaru = input("Masukkan tanggal kadaluarsa: ")
                            dataObat[indeks][2] = kadaluarsaBaru
                            print("Tanggal kadaluarsa berhasil diperbarui!")
                        elif pilihUbah == "4":
                            konsumsiBaru = int(input("Masukkan  jumlah obat yang sudah dikonsumsi: "))
                            dataObat[indeks][3]
                            print("Jumlah dikonsumsi berhasil diperbarui!")
                        elif pilihUbah == "5":
                            namaBaru = input("Masukkan nama obat: ")
                            stokBaru = int(input("Masukkan jumlah stok: "))
                            kadaluarsaBaru = int(input("Masukkan tanggal kadaluarsa: "))
                            konsumsiBaru = int(input("Masukkan jumlah obat yang sudah dikonsumsi: "))
                            
                            dataObat[indeks][0] = namaBaru
                            dataObat[indeks][1] = stokBaru
                            dataObat[indeks][2] = kadaluarsaBaru
                            dataObat[indeks][3] = konsumsiBaru
                            print("Seluruh Data obat berhasil diperbarui!")
                        else:
                            print("Pilihan tidak valid!")
                    else:
                        print("Nomor obat tidak valid!")
                else:
                    print("Nomor obat tidak valid!")
            else:
                print("\nAkses ditolak! Menu ini khusus admin.")    
            input("\nTekan Enter untuk kembali...")

        elif pilihanMenu == "4":
            if role == "admin":
                print("\n--- HAPUS DATA OBAT ---")
                i = 0
                while i < len(dataObat):
                    print(f"{i+1:>2}). {dataObat[i][0]}")
                    i = i +1

                indeks = int(input("Pilih nomor obat yang mau dihapus: ")) - 1

                if indeks >= 0:
                    if indeks < len(dataObat):
                        obatDihapus = dataObat.pop(indeks)
                        print(f"Data obat '{obatDihapus[0]}' berhasil dihapus!")
                    else:
                        print("Nomor obat tidak valid!")
                else:
                    print("Nomor obat tidak valid!") 
            else:
                print("\nAkses ditolak! Menu ini khusus admin.")
            input("\nTekan Enter untuk kembali...")

        elif pilihanMenu == "5":
            statusLogin = False
            role = ""
            print("Berhasil Logout!")
            input("\nTekan Enter untuk lanjut...")
        else:
            print("Pilihan menu tidak valid!")
            input("\nTekan Enter untuk kembali...")                       