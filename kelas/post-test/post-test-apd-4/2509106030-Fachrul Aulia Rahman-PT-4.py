import math

username_benar = "arul"
password_benar = "030"
kesempatan = 5
login_berhasil = False 

for i in range(kesempatan, 0, -1):
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username == username_benar and password == password_benar:
        print("Selamat datang,",username_benar,"!")
        login_berhasil = True 
        break
    else:
        print("Login gagal. Sisa percobaan:", i - 1)
        if i - 1 == 0:
            print("Akun terkunci!")

if login_berhasil:
    print("=== Program Menentukan Jenis Segitiga ===")
    sisi1 = int(input("Masukkan sisi pertama: "))
    sisi2 = int(input("Masukkan sisi kedua: ")) 
    sisi3 = int(input("Masukkan sisi ketiga: "))

    if (sisi1 + sisi2 > sisi3) and (sisi1 + sisi3 > sisi2) and (sisi2 + sisi3 > sisi1):
        if sisi1 == sisi2 == sisi3:
            jenis = "Segitiga Sama Sisi"
        elif sisi1 == sisi2 or sisi2 == sisi3 or sisi1 == sisi3:
            jenis = "Segitiga Sama Kaki"
        else:
            jenis = "Segitiga Sembarang"

        print("Jenis segitiga: ", jenis)

        s = (sisi1 + sisi2 + sisi3) / 2
        luas = math.sqrt(s * (s - sisi1) * (s - sisi2) * (s - sisi3))
        print("Luas segitiga = ", luas)
    else:
        print("Bukan segitiga")

    print("==========================================")
