
data_pelanggan = []

# CREATE
def tambah_pelanggan():
    nama = input("Nama pelanggan: ")
    komputer = input("Nomor komputer: ")
    jam_mulai = int(input("Jam mulai (1-24): "))
    jam_selesai = int(input("Jam selesai (1-24): "))
    harga_per_jam = 5000

    durasi = jam_selesai - jam_mulai
    total = durasi * harga_per_jam

    pelanggan = {
        "nama": nama,
        "komputer": komputer,
        "jam_mulai": jam_mulai,
        "jam_selesai": jam_selesai,
        "total": total
    }

    data_pelanggan.append(pelanggan)
    print(f" Data {nama} ditambahkan! Total bayar: Rp{total}")

# READ
def lihat_data():
    if not data_pelanggan:
        print(" Belum ada pelanggan.")
    else:
        print("\n=== DAFTAR PELANGGAN WARNET ===")
        for i, p in enumerate(data_pelanggan, start=1):
            print(f"{i}. {p['nama']} | {p['komputer']} | {p['jam_mulai']}-{p['jam_selesai']} | Rp{p['total']}")

# UPDATE
def ubah_data():
    lihat_data()
    index = int(input("Masukkan nomor pelanggan yang ingin diubah: ")) - 1
    if 0 <= index < len(data_pelanggan):
        jam_selesai = input("Ubah jam: ")
        data_pelanggan[index]["jam_selesai"] = jam_selesai
        print(" Data berhasil diubah!")
    else:
        print(" Nomor tidak valid!")

# DELETE
def hapus_data():
    lihat_data()
    index = int(input("Masukkan nomor pelanggan yang ingin dihapus: ")) - 1
    if 0 <= index < len(data_pelanggan):
        nama = data_pelanggan[index]["nama"]
        del data_pelanggan[index]
        print(f" Data {nama} berhasil dihapus!")
    else:
        print(" Nomor tidak valid!")

# PROGRAM UTAMA
while True:
    print("\n=== SISTEM CRUD WARNET ===")
    print("1. Tambah Pelanggan ")
    print("2. Lihat Data ")
    print("3. Ubah Data ")
    print("4. Hapus Data ")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        tambah_pelanggan()
    elif pilihan == "2":
        lihat_data()
    elif pilihan == "3":
        ubah_data()
    elif pilihan == "4":
        hapus_data()
    elif pilihan == "5":
        print(" Keluar dari program. Terima kasih!")
        break
    else:
        print(" Pilihan tidak valid!")
