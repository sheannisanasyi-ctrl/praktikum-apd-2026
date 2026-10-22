game = ["Genshin", 7.0, True]
for i in game:
    print(i)

for i in range(1, 3):# Mengontrol baris dalam tabel perkalian
    for j in range(1, 4):# Mengontrol kolom dalam tabel perkalian
          print(f'{i} x {j} = {i * j}')
    print('') #biar ada jarak tiap iterasi

jawab = "ya"
hitung = 0
while(jawab == "ya"):
    hitung += 1
    jawab = input("Ulang lagi tidak? ")
    
print(f"Total Perulangan : {hitung}")

for i in range(10): 
    if i == 5:
        break
    print(i)

angka_benar = 7

while True:
    print("=== Game Tebak Angka ===")

    angka_input = int(input("Masukkan angka (1-10): "))

    if angka_benar == angka_input:
        print("Angka yang kamu masukkan benar")
        break
    else:
        print("Angka masih salah")
        
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

