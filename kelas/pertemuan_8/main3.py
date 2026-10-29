import inquirer
from prettytable import PrettyTable

# Deklarasi struktur dictionary untuk menampung data mahasiswa
data_mahasiswa = {
"nim": [],
"nama": [],
"kelas": []
}

def tambah_data():
    pertanyaan = [
    inquirer.Text("nim", message="Input NIM kamu"),
    inquirer.Text("nama", message="Input nama lengkapmu"),
    inquirer.List("kelas", message="Pilih kelas", choices=["A", "B", "C"]),
    ]

# Hasil input disimpan ke variabel jawaban dalam bentuk dictionary:
# {'nim': '...', 'nama': '...', 'kelas': '...'}

jawaban = inquirer.prompt(pertanyaan)

# Menambahkan masing-masing nilai ke dalam list pada dictionary
data_mahasiswa
data_mahasiswa["nim"].append(jawaban["nim"])
data_mahasiswa["nama"].append(jawaban["nama"])
data_mahasiswa["kelas"].append(jawaban["kelas"])

def tampil_data():
tabel = PrettyTable()
tabel.field_names = ["No", "NIM", "Nama", "Kelas"]
for i in range(len(data_mahasiswa["nim"])):
tabel.add_row([
i + 1,
data_mahasiswa["nim"][i],
data_mahasiswa["nama"][i],
data_mahasiswa["kelas"][i]
])
print(tabel)

# Memanggil fungsi
tambah_data()