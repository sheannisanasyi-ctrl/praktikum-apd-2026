kartu = {"merah", "merah", "biru", "hijau"}

kartu.discard("red")

print(kartu)

matkul = ("apd", "orsikom", "apd", "kalkulus")
sks = tuple(matkul)
print(sks)

angka_ganjil = {1, 3, 5, 7, 9}
for angka in angka_ganjil:
    print (angka)

aslab1 = {"fina", "shasha", "risma", "attar"}
aslab2 = {"larry", "attar", "haekal"}
irisan = aslab2.difference(aslab1)
print(irisan)


Matkul = {
    "Matkul_ganjil" : "kalkulus",
    "Matkul_genap" : "statistik"
}
print(Matkul["Matkul_ganjil"])

print(Matkul.get("Matkul_genp" "key tidak ada"))

game = {
"pou" : "chill",
"genshin impact" : "action",
"valorant" : "fps",
"minecraft" : "sandbox",
"mobile legend" : "moba"
}

for i, j in game.items():
    print(f"{i} adalah jenis game {j}")

game = {
    "pou" : "chill",
    "genshin impact" : "action",
    "valorant" : "fps",
    "minecraft" : "sandbox",
    "mobile legend" : "moba"
}

game["resident evil"] = "horror"
print(game)

game = {
    "pou" : "chill",
    "genshin impact" : "action",
    "valorant" : "fps",
    "minecraft" : "sandbox",
    "mobile legend" : "moba"
}

tambah = game.setdefault("resident evil", "horror")
print(game)
print("Tipe game", game.setdefault("grow a garden", "gardening"))

menu = {
"ayam" : ["ayam geprek", "ayam goreng", "ayam bakar"],
"nasi" : ["nasi goreng", "nasi uduk"],
"mie" : ["mie goreng rendang", "mie goreng aceh"],
"kuah" : ["soto", "rawon", "sop iga"]
}