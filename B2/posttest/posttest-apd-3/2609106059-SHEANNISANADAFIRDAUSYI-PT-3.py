NamaBenar = "Shean"
NIMBenar = 59
RewardDasar = 1000

InputNama = input("Masukkan nama: ")

while InputNama != NamaBenar:
    print("Login gagal! Nama Anda salah. Silakan masukkan ulang.")
    InputNama = input("Masukkan nama: ")

InputNIM = int(input("Masukkan NIM: "))

while InputNIM != NIMBenar:
    print("Login gagal! NIM Anda salah. Silakan masukkan ulang.")
    InputNIM = int(input("Masukkan NIM: "))

print("=== GREEN LANTERN CORPS MISSION ===")
print("1. Misi Standar (Bonus 2%)")
print("2. Misi Sulit (Bonus 5%)")
print("3. Misi Kritis (Bonus 8%)")
print("4. Misi Penyelamatan Bumi (Bonus 12%)")
print("-----------------------------------")
print("Masukkan Pilihan Misi (1-4): ")

PilihanMisi = int(input("Masukkan Pilihan Misi (1-4): "))

while PilihanMisi < 1 or PilihanMisi > 4:
    print("Pilihan Misi Tidak Valid!")
    PilihanMisi = int(input("Masukkan Pilihan Misi (1-4): "))

if PilihanMisi == 1:
    PersentaseBonus = 0.02
elif PilihanMisi == 2:
        PersentaseBonus = 0.05
elif PilihanMisi == 3:
            PersentaseBonus = 0.08
elif PilihanMisi == 4:
                PersentaseBonus = 0.12

JumlahBonus = RewardDasar * PersentaseBonus
RewardAkhir = RewardDasar + JumlahBonus

print("-----------------------------------")
print("Reward Dasar: ", RewardDasar)
print("Jumlah Bonus: ", JumlahBonus)
print("Total Reward Akhir: ", RewardAkhir) 
