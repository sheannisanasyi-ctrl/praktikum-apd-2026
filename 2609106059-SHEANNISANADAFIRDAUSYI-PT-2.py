# Deklarasi dan inisialisasi nilai
skincare_1 = 35000
skincare_2 = 42000
skincare_3 = 50000
skincare_4 = 55000
skincare_5 = 68000
skincare_6 = 70000
ongkir = 12000
nim = 59
kurs_jpy = 113

# List harga skincare
harga_skincare = [skincare_1, skincare_2, skincare_3, skincare_4, skincare_5, skincare_6]

# Total pengeluaran
total_pengeluaran = skincare_1 + skincare_2 + skincare_3 + skincare_4 + skincare_5 + skincare_6 + ongkir

# Rata-rata 
rata_rata = total_pengeluaran / len(harga_skincare)

# Perbandingan NIM dengan rata-rata
bolean = nim < rata_rata

# Konversi ke JPY
total_jpy = total_pengeluaran / kurs_jpy

# Output
print("Harga skincare:", skincare_1, skincare_2, skincare_3, skincare_4, skincare_5, skincare_6)
print("Total pengeluaran:", total_pengeluaran)
print(f"Rata-rata: {rata_rata:.2f}")
print("NIM:", nim)
print("Bolean (nim < rata-rata):", bolean)
print(f"Total dalam JPY: {total_jpy:.2f}")
print("Slice skincare_3 s/d skincare_5:", harga_skincare[-4:-1])