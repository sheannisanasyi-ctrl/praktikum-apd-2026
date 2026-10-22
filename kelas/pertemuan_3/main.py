cuaca = "hujan"

if cuaca == "hujan":
    print("bawa payung/jas hujan")
    print("telat dikit")

    print("otw ke kampus")

budget = 20000
cuaca = ("Hujan")

if budget > 30000 and cuaca == "cerah":
    print("beli yoshinoya")
else:
    print("masak indomie aja")

kendaraan = input("masukkan jenis kendaraan: ")
if kendaraan == "mobil":
    tarif_parkir = 10_000 
elif kendaraan == "motor":
    tarif_parkir = 5_000
else: 
    tarif_parkir = 15_000

    print(f"tarif parkir yang harus dibayar: {tarif_parkir}")


kendaraan = input("Masukkan jenis kendaraan anda: ").lower().strip()
## mobil
if kendaraan == "mobil":
tarif_parkir = 10000
elif kendaraan == "motor":
tarif_parkir = 5000
elif kendaraan = "sepeda":
    tarif_parkir = 6_700
else:
tarif_parkir = 15000
# Menampilkan tarif parkir yang harus dibayar
print("Tarif parkir yang harus dibayar:", tarif_parkir)




bilangan = -5

status = "bilangan negatif" if bilangan < 0 else "bilangan positif"

print("bilangan adalah", status)

username = input("masuk username: ").lower().strip()
password = input("masuk password: ").strip()

if username == "sheannisa":
    if password == "059":
        print("login berhasil")
        else:
            print("password salah")
else:
    print("username salah")
