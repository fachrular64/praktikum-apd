# VARIABEL GLOBAL   
data_pelanggan = {}
total_pendapatan_keseluruhan = 0
HARGA_PER_JAM = 5000
MAX_PERCOBAAN_LOGIN = 3

# ========== FUNGSI DENGAN PARAMETER ==========

# Fungsi 1: Menghitung total biaya (dengan parameter)
def hitung_total(jam_mulai, jam_selesai, tarif):
    """Menghitung total biaya berdasarkan durasi dan tarif"""
    try:
        durasi = jam_selesai - jam_mulai
        if durasi <= 0:
            return None
        total = durasi * tarif
        return total
    except Exception as e:
        print(f"Error saat menghitung total: {e}")
        return None

# Fungsi 2: Validasi jam (dengan parameter)
def validasi_jam(jam, tipe="mulai"):
    """Validasi input jam (1-24)"""
    try:
        jam_int = int(jam)
        if 1 <= jam_int <= 24:
            return jam_int
        else:
            print(f"Jam {tipe} harus antara 1-24!")
            return None
    except ValueError:
        print(f"Input jam {tipe} harus berupa angka!")
        return None

# ========== FUNGSI TANPA PARAMETER ==========

# Fungsi 3: Cek apakah data kosong (tanpa parameter)
def cek_data_kosong():
    """Mengecek apakah data pelanggan kosong"""
    return len(data_pelanggan) == 0

# Fungsi 4: Hitung total pendapatan aktif (tanpa parameter)
def hitung_total_pendapatan_aktif():
    """Menghitung total pendapatan dari pelanggan yang masih aktif"""
    try:
        total_pendapatan = sum(p['total'] for p in data_pelanggan.values())
        return total_pendapatan
    except Exception as e:
        print(f"Error menghitung pendapatan: {e}")
        return 0

# ========== PROSEDUR ==========

# Prosedur 1: Tampilkan header
def tampilkan_header():
    """Prosedur untuk menampilkan header aplikasi"""
    print("\n" + "="*50)
    print("     SISTEM MANAJEMEN WARNET - FACHRUL")
    print("="*50)

# Prosedur 2: Tampilkan statistik
def tampilkan_statistik():
    """Prosedur untuk menampilkan statistik warnet"""
    print("\n" + "="*50)
    print("           STATISTIK WARNET")
    print("="*50)
    jumlah_pelanggan = len(data_pelanggan)
    total_pendapatan_aktif = hitung_total_pendapatan_aktif()
    
    print(f"Jumlah Pelanggan Aktif : {jumlah_pelanggan}")
    print(f"Pendapatan Aktif       : Rp{total_pendapatan_aktif:,}")
    print(f"Total Pendapatan       : Rp{total_pendapatan_keseluruhan:,}")
    
    if jumlah_pelanggan > 0:
        rata_rata = total_pendapatan_aktif / jumlah_pelanggan
        print(f"Rata-rata per Pelanggan: Rp{rata_rata:,.2f}")
    print("="*50)

# ========== LOGIN ==========
def login():
    tampilkan_header()
    print("           LOGIN")
    print("="*50)
    
    # Variabel lokal
    username_benar = "Fachrul"
    password_benar = "123"
    percobaan = 0
    
    while percobaan < MAX_PERCOBAAN_LOGIN:
        try:
            username = input("Username: ")
            password = input("Password: ")
            
            if username == username_benar and password == password_benar:
                print("\n Login berhasil! Selamat datang, Fachrul!")
                print("="*50)
                return True
            else:
                percobaan += 1
                sisa = MAX_PERCOBAAN_LOGIN - percobaan
                if sisa > 0:
                    print(f" Login gagal! Sisa percobaan: {sisa}")
                else:
                    print("\n Login gagal! Anda telah mencapai batas percobaan.")
                    print("  Program dihentikan.")
                    return False
        except Exception as e:
            print(f"Error saat login: {e}")
            percobaan += 1
    
    return False

# ========== CREATE ==========
def tambah_pelanggan():
    global total_pendapatan_keseluruhan
    print("\n=== TAMBAH PELANGGAN ===")
    try:
        # Variabel lokal
        nama = input("Nama pelanggan: ")
        if not nama.strip():
            print(" Nama tidak boleh kosong!")
            return
        
        komputer = input("Nomor komputer: ")
        if not komputer.strip():
            print(" Nomor komputer tidak boleh kosong!")
            return
        
        if komputer in data_pelanggan:
            print(f" Komputer {komputer} sudah digunakan!")
            return
        
        jam_mulai_input = input("Jam mulai (1-24): ")
        jam_mulai = validasi_jam(jam_mulai_input, "mulai")
        if jam_mulai is None:
            return
        
        jam_selesai_input = input("Jam selesai (1-24): ")
        jam_selesai = validasi_jam(jam_selesai_input, "selesai")
        if jam_selesai is None:
            return
        
        total = hitung_total(jam_mulai, jam_selesai, HARGA_PER_JAM)
        if total is None:
            print(" Jam selesai harus lebih besar dari jam mulai!")
            return
        
        data_pelanggan[komputer] = {
            "nama": nama,
            "jam_mulai": jam_mulai,
            "jam_selesai": jam_selesai,
            "total": total
        }
        
        total_pendapatan_keseluruhan += total
        
        print(f" Data {nama} ditambahkan! Total bayar: Rp{total:,}")
        
    except Exception as e:
        print(f" Error saat menambah pelanggan: {e}")

# ========== READ ==========
def lihat_data():
    print("\n=== DAFTAR PELANGGAN WARNET ===")
    try:
        if cek_data_kosong():
            print(" Belum ada pelanggan.")
        else:
            print(f"{'No':<5} {'Nama':<20} {'Komputer':<10} {'Jam':<15} {'Total':<15}")
            print("-" * 65)
            for i, (komputer, p) in enumerate(data_pelanggan.items(), start=1):
                jam = f"{p['jam_mulai']}-{p['jam_selesai']}"
                print(f"{i:<5} {p['nama']:<20} {komputer:<10} {jam:<15} Rp{p['total']:,}")
    except Exception as e:
        print(f" Error saat menampilkan data: {e}")

# ========== UPDATE ==========
def ubah_data():
    print("\n=== UBAH DATA PELANGGAN ===")
    try:
        lihat_data()
        if cek_data_kosong():
            return
        
        # Variabel lokal
        nomor_input = input("\nMasukkan nomor pelanggan yang ingin diubah: ")
        nomor = int(nomor_input) - 1
        keys = list(data_pelanggan.keys())
        
        if 0 <= nomor < len(keys):
            komputer = keys[nomor]
            print(f"\nMengubah data pelanggan: {data_pelanggan[komputer]['nama']}")
            
            jam_selesai_input = input("Ubah jam selesai: ")
            jam_selesai = validasi_jam(jam_selesai_input, "selesai")
            if jam_selesai is None:
                return
            
            jam_mulai = data_pelanggan[komputer]["jam_mulai"]
            total = hitung_total(jam_mulai, jam_selesai, HARGA_PER_JAM)
            
            if total is None:
                print(" Jam selesai harus lebih besar dari jam mulai!")
                return
            
            data_pelanggan[komputer]["jam_selesai"] = jam_selesai
            data_pelanggan[komputer]["total"] = total
            print(f" Data berhasil diubah! Total baru: Rp{total:,}")
        else:
            print(" Nomor tidak valid!")
            
    except ValueError:
        print(" Input harus berupa angka!")
    except Exception as e:
        print(f" Error saat mengubah data: {e}")

# ========== DELETE ==========
def hapus_data():
    print("\n=== HAPUS DATA PELANGGAN ===")
    try:
        lihat_data()
        if cek_data_kosong():
            return
        
        # Variabel lokal
        nomor_input = input("\nMasukkan nomor pelanggan yang ingin dihapus: ")
        nomor = int(nomor_input) - 1
        keys = list(data_pelanggan.keys())
        
        if 0 <= nomor < len(keys):
            komputer = keys[nomor]
            nama = data_pelanggan[komputer]["nama"]
            
            konfirmasi = input(f"Yakin ingin menghapus data {nama}? (y/n): ").lower()
            if konfirmasi == 'y':
                del data_pelanggan[komputer]
                print(f" Data {nama} berhasil dihapus!")
            else:
                print(" Penghapusan dibatalkan.")
        else:
            print(" Nomor tidak valid!")
            
    except ValueError:
        print(" Input harus berupa angka!")
    except Exception as e:
        print(f" Error saat menghapus data: {e}")

# ========== MENU UTAMA ==========
def menu_utama():
    while True:
        try:
            print("\n" + "="*50)
            print("         MENU UTAMA")
            print("="*50)
            print("1. Tambah Pelanggan")
            print("2. Lihat Data Pelanggan")
            print("3. Ubah Data Pelanggan")
            print("4. Hapus Data Pelanggan")
            print("5. Tampilkan Statistik")
            print("6. Keluar")
            print("="*50)

            pilihan = input("Pilih menu (1-6): ")

            if pilihan == "1":
                tambah_pelanggan()
            elif pilihan == "2":
                lihat_data()
            elif pilihan == "3":
                ubah_data()
            elif pilihan == "4":
                hapus_data()
            elif pilihan == "5":
                tampilkan_statistik()
            elif pilihan == "6":
                print("\n Keluar dari program. Terima kasih, Fachrul!")
                print("="*50)
                break
            else:
                print(" Pilihan tidak valid! Pilih 1-6.")
                
        except KeyboardInterrupt:
            print("\n\n Program dihentikan oleh user.")
            break
        except Exception as e:
            print(f" Error pada menu utama: {e}")

# ========== PROGRAM UTAMA ==========
if __name__ == "__main__":
    try:
        if not login():
            exit()
        menu_utama()
        
    except Exception as e:
        print(f" Error fatal: {e}")
        exit(1)