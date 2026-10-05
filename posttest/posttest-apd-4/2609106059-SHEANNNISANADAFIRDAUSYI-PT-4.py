userBenar = "shean"
passwordBenar = "2609106059"
kesempatan = 3
loginBerhasil = False

while kesempatan > 0 and not loginBerhasil:
    print(f"\nKesempatan Login: {kesempatan}")
    userInput = input("Masukkan  Username : ").lower()
    passwordInput = input("Masukkan Password : ")
    
    if userInput == userBenar and passwordInput == passwordBenar:
        print("\nLogin berhasil! Selamat datang, shean!")
        loginBerhasil = True
    else:
        if userInput !=userBenar and passwordInput == passwordBenar:
            print("Login gagal! Username salah!")
        elif userInput == userBenar and passwordInput != passwordBenar:
                print("Login gagal! Password salah!")
        else:
            print("Login gagal! Username dan Password salah!")

        kesempatan -= 1

if not loginBerhasil:
    print("\nKesempatan login anda telah habis. Silakan coba lagi nanti.")
else:
    totalPorsi = 0
    penerimaManfaat = 0
    jumlahReguler = 0
    jumlahAnak = 0
    jumlahKeluarga = 0

    while True:
        print("\n===================================")
        print("        MENU DISTRIBUSI PAKET        ")
        print("===================================")
        print("1. Paket Reguler     (1 porsi)")
        print("2. Paket Anak        (1 porsi)")
        print("3. Paket Keluarga    (4 porsi)")
        print("4. Keluar dari program")

        pilihanMenu = input("Masukkan pilihan Anda (1-4): ")

        if pilihanMenu == "" or not pilihanMenu.isdigit():
            print("\nOpsi tidak valid. Silakan masukkan angka 1-4.")
            continue

        pilihan = int(pilihanMenu)

        if pilihan == 4:
            print("Terima kasih!")
            break
        elif pilihan < 1 or pilihan > 4:
            print("\nOpsi tidak valid. Silakan masukkan angka 1-4.")
            continue

        while True:
            jumlahPaket = input("Masukkan jumlah paket yang akan dibagikan: ")

            if jumlahPaket == "" or not jumlahPaket.isdigit():
                print("\nJumlah paket tidak valid. Silakan masukkan angka.")
                continue

            jumlahPorsi = int(jumlahPaket)

            if jumlahPorsi <= 0:
                print("\nJumlah paket minimal 1!")
                continue
            break

        if pilihan == 3:
            porsiPerPaket = 4
        else:
            porsiPerPaket = 1

        for i in range(jumlahPorsi):
            totalPorsi += porsiPerPaket

        if pilihan == 1:
            jumlahReguler += jumlahPorsi
            penerimaManfaat += jumlahPorsi * 1
            print(f"\nMenambahkan {jumlahPorsi} Paket Reguler.")
        elif pilihan == 2:
            jumlahAnak += jumlahPorsi
            penerimaManfaat += jumlahPorsi * 1
            print(f"\nMenambahkan {jumlahPorsi} Paket Anak.")
        elif pilihan == 3:
            jumlahKeluarga += jumlahPorsi
            penerimaManfaat += jumlahPorsi * 4
            print(f"\nMenambahkan {jumlahPorsi} Paket Keluarga.")

    if totalPorsi >= 20:
        bonus = "5 paket buah"
    elif totalPorsi >= 10:
        bonus = "3 botol susu"
    elif totalPorsi >= 5:
        bonus = "1 paket vitamin"
    else:
        bonus = "Tidak ada bonus"

    print("\n-----------------------------------")
    print(f"Paket Reguler: {jumlahReguler} paket")
    print(f"Paket Anak: {jumlahAnak} paket")
    print(f"Paket Keluarga: {jumlahKeluarga} paket")
    print(f"Total Porsi: {totalPorsi} porsi")
    print(f"Penerima Manfaat: {penerimaManfaat} orang")
    print(f"Bonus: {bonus}")
    print("-----------------------------------")
    print("Makanan dibagikan secara gratis sehingga tidak ada harga dan pembayaran.")