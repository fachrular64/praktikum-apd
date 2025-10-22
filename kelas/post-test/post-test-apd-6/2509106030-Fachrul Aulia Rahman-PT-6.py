data_pelanggan = {}

# LOGIN
def login():
    print("\n" + "="*40)
    print("LOGIN")
    print("="*40)
    
    username_benar = "Fachrul"
    password_benar = "123"
    percobaan = 0
    max_percobaan = 3
    
    while percobaan < max_percobaan:
        username = input("Username: ")
        password = input("Password: ")
        
        if username == username_benar and password == password_benar:
            print("\n Login berhasil! Selamat datang, Fachrul!")
            print("="*40)
            return True
        else:
            percobaan += 1
            sisa = max_percobaan - percobaan
            if sisa > 0:
                print(f" Login gagal! Sisa percobaan: {sisa}")
            else:
                print("\n Login gagal! Anda telah mencapai batas percobaan.")
                print(" Program dihentikan.")
                return False
    
    return False

# CREATE
def tambah_pelanggan():
    nama = input("Nama pelanggan: ")
    komputer = input("Nomor komputer: ")
    jam_mulai = int(input("Jam mulai (1-24): "))
    jam_selesai = int(input("Jam selesai (1-24): "))
    harga_per_jam = 5000

    durasi = jam_selesai - jam_mulai
    total = durasi * harga_per_jam

    # Menggunakan nomor komputer sebagai key
    data_pelanggan[komputer] = {
        "nama": nama,
        "jam_mulai": jam_mulai,
        "jam_selesai": jam_selesai,
        "total": total
    }

    print(f" Data {nama} ditambahkan! Total bayar: Rp{total}")

# READ
def lihat_data():
    if not data_pelanggan:
        print(" Belum ada pelanggan.")
    else:
        print("\n=== DAFTAR PELANGGAN WARNET ===")
        for i, (komputer, p) in enumerate(data_pelanggan.items(), start=1):
            print(f"{i}. {p['nama']} | Komputer {komputer} | {p['jam_mulai']}-{p['jam_selesai']} | Rp{p['total']}")

# UPDATE
def ubah_data():
    lihat_data()
    if not data_pelanggan:
        return
    
    nomor = int(input("Masukkan nomor pelanggan yang ingin diubah: ")) - 1
    keys = list(data_pelanggan.keys())
    
    if 0 <= nomor < len(keys):
        komputer = keys[nomor]
        jam_selesai = int(input("Ubah jam selesai: "))
        
        # Hitung ulang total
        harga_per_jam = 5000
        durasi = jam_selesai - data_pelanggan[komputer]["jam_mulai"]
        total = durasi * harga_per_jam
        
        data_pelanggan[komputer]["jam_selesai"] = jam_selesai
        data_pelanggan[komputer]["total"] = total
        print(" Data berhasil diubah!")
    else:
        print(" Nomor tidak valid!")

# DELETE
def hapus_data():
    lihat_data()
    if not data_pelanggan:
        return
    
    nomor = int(input("Masukkan nomor pelanggan yang ingin dihapus: ")) - 1
    keys = list(data_pelanggan.keys())
    
    if 0 <= nomor < len(keys):
        komputer = keys[nomor]
        nama = data_pelanggan[komputer]["nama"]
        del data_pelanggan[komputer]
        print(f" Data {nama} berhasil dihapus!")
    else:
        print(" Nomor tidak valid!")

# PROGRAM UTAMA
if __name__ == "__main__":
    # Proses Login
    if not login():
        exit()
    
    # Menu utama setelah login berhasil
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