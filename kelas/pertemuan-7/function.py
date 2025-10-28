# # # def perkenalan():
# # #   print("halo, aku Nabil")

# # # def kali():
# # #   x = 5*5
# # #   print(x)

# # def kali(s):
# #   x = s*s
# #   return x
  
# # def luasPersegiPanjang(panjang, lebar):
# #   luas = panjang * lebar
# #   return luas

# # print(luasPersegiPanjang(10,5))
# # print(type(kali(5)))

# # def luassegitiga(alas, tinggi):
# #   luas = 0.5 * alas * tinggi
# #   return luas

# # print (luassegitiga(5,7))

# # nama = "ridho"

# # def biodata():
# #   username = "ridho"
# #   print(username)
# # biodata()

# # def faktorial(n):
# #   if n==1 or n==0:
# #     return 1
# #   else:
# #     return n * faktorial(n-1)
# # print(faktorial(5))

# film = []


# def show_data():
#     if len(film) <= 0:
#         print("Belum Ada data")
#     else:
#         print("ID | Judul Film")
#         for indeks in range(len(film)):
#             print(indeks+1, "|", film[indeks])

# # Fungsi untuk menambah data
# def insert_data():
#     film_baru = input("Judul Film: ")
#     film.append(film_baru)
#     print("Film berhasil ditambahkan!")


# # Fungsi untuk mengedit data
# def edit_data():
#     show_data()
#     indeks = int(input("Inputkan ID film: "))
#     if indeks >= len(film) or indeks < 0:
#         print("ID salah")
#     else:
#         judul_baru = input("Judul baru: ")
#         film[indeks] = judul_baru
#         print("Film berhasil diupdate!")


# # Fungsi untuk menghapus data
# def delete_data():
#     show_data()
#     indeks = int(input("Inputkan ID film: "))
#     if indeks >= len(film) or indeks < 0:
#         print("ID salah")
#     else:
#         film.remove(film[indeks])
#         print("Film berhasil dihapus!")


# # fungsi untuk menampilkan menu
# def show_menu():
#     print ("\n")
#     print ("----------- MENU---------- ")
#     print ("[1] Show Data")
#     print ("[2] Insert Data")
#     print ("[3] Edit Data")
#     print ("[4] Delete Data")
#     print ("[5] Exit")
#     menu = input("PILIH MENU> ")
#     print ("\n")

#     if menu == "1":
#         show_data()
#     elif menu == "2":
#         insert_data()
#     elif menu == "3":
#         edit_data()
#     elif menu == "4":
#         delete_data()
#     elif menu == "5":
#         exit()
#     else:
#         print ("Salah pilih!")

# if __name__ == "__main__" :
#     while (True):
#       show_menu()

while True:
  try:
    angka = int(input("masukkan angka: "))
  except ValueError:
    print("angka tidak boleh string")
  else :
    print("angka kamu adalah: ", angka)
  finally:
    print("selesai")