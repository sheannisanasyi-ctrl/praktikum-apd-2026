skincare_1 = 35000
skincare_2 = 42000
skincare_3 = 50000
skincare_4 = 55000
skincare_5 = 68000
skincare_6 = 70000
ongkir = 12000

harga_skincare = [35000, 42000, 50000, 55000, 68000, 70000]

total_pengeluaran = 35000 + 42000 + 50000 + 55000 + 68000 + 70000 + 12000

rata_rata = total_pengeluaran / len(harga_skincare)

nim = 59

bolean = nim < rata_rata

total_jpy = total_pengeluaran / 113

slice_skincare = harga_skincare[-4:-1]

print("Total Pengeluaran:", total_pengeluaran)
print("Rata-rata Pengeluaran:", rata_rata)
print("Bolean:", bolean)
print("Total JPY:", total_jpy)
print("Slice Skincare:", slice_skincare)