import math
print("=== Program Menentukan Jenis Segitiga ===")


sisi1 = int(input("Masukkan sisi pertama: "))
sisi2 = int(input("Masukkan sisi ketiga: "))
sisi3 = int(input("Masukkan sisi ketiga: "))


if (sisi1 + sisi2 > sisi3) and (sisi1 + sisi3 > sisi2) and (sisi2 + sisi3 > sisi1):
    if sisi1 == sisi2 == sisi3:
        jenis = "Segitiga Sama Sisi"
    elif sisi1 == sisi2 or sisi2 == sisi3 or sisi1 == sisi3:
        jenis = "Segitiga Sama Kaki"
    else:
        jenis = "Segitiga Sembarang"
    
    print("Jenis segitiga: ", jenis)

    # Hitung luas segitiga dengan rumus Heron
    s = (sisi1 + sisi2 + sisi3) / 2  
    luas = math.sqrt(s * (s - sisi1) * (s - sisi2) * (s - sisi3))
    print("Luas segitiga = ", luas)
else:
    print("Bukan segitiga")

print("==========================================")

