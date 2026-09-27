NamaBenar = "Shean"
NIMBenar = "59"
RewardDasar = 1000

InputNama = input("Masukkan nama: ")
InputNIM = input("Masukkan NIM: ")

if InputNama == NamaBenar:
    if InputNIM == NIMBenar:
        print("=== GREEN LANTERN CORPS MISSION ===")
        print("1. Misi Standar (Bonus 2%)")
        print("2. Misi Sulit (Bonus 5%)")
        print("3. Misi Kritis (Bonus 8%)")
        print("4. Misi Penyelamatan Bumi (Bonus 12%)")
        print("-----------------------------------")
    else:
        print("Login gagal! NIM Anda salah.")
        exit()
else:
    print("Login gagal! Nama Anda salah.")
    exit()

PilihanMisi = input("Masukkan Pilihan Misi (1-4): ")

if PilihanMisi == "1":
    PersentaseBonus = 0.02
    print("Pilihan Misi 1 dipilih.")
elif PilihanMisi == "2":
    PersentaseBonus = 0.05
    print("Pilihan Misi 2 dipilih.")
elif PilihanMisi == "3":
    PersentaseBonus = 0.08
    print("Pilihan Misi 3 dipilih.")
elif PilihanMisi == "4":
    PersentaseBonus = 0.12
    print("Pilihan Misi 4 dipilih.")
else:
    print("Pilihan Misi Tidak Valid!")
    exit()
    
JumlahBonus = RewardDasar * PersentaseBonus
RewardAkhir = RewardDasar + JumlahBonus

print("-----------------------------------")
print("Reward Dasar: ", RewardDasar)
print("Jumlah Bonus: ", JumlahBonus)
print("Total Reward Akhir: ", RewardAkhir)


