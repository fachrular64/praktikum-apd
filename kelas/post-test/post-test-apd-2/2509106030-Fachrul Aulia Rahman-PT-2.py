
data = ["Arul", 19, 4.5, True]
print("=========List data: ==========================")
print("\n")
print(data)
print("\n")

print("=== Data Sebelum Diubah ===")
print("1.", data[0], "->", type(data[0]).__name__)
print("2.", data[1], "->", type(data[1]).__name__)
print("3.", data[2], "->", type(data[2]).__name__)
print("4.", data[3], "->", type(data[3]).__name__)

# Hitung jumlah int dan float
jml_int = (type(data[0]).__name__ == "int") + (type(data[1]).__name__ == "int") + (type(data[2]).__name__ == "int") + (type(data[3]).__name__ == "int")
jml_float = (type(data[0]).__name__ == "float") + (type(data[1]).__name__ == "float") + (type(data[2]).__name__ == "float") + (type(data[3]).__name__ == "float")

print("Jumlah int  :", jml_int)
print("Jumlah float:", jml_float)

# Ubah tipe data
data_baru = [
    bool(data[0]),    # str → bool
    float(data[1]),     # int → float
    int(data[2]),     # float → int
    int(data[3])    # bool → int
]

print("\n=== Data Setelah Diubah ===")
print("1.", data_baru[0], "->", type(data_baru[0]).__name__)
print("2.", data_baru[1], "->", type(data_baru[1]).__name__)
print("3.", data_baru[2], "->", type(data_baru[2]).__name__)
print("4.", data_baru[3], "->", type(data_baru[3]).__name__)

# Hitung jumlah int dan float setelah diubah
jml_int2 = (type(data_baru[0]).__name__ == "int") + (type(data_baru[1]).__name__ == "int") + (type(data_baru[2]).__name__ == "int") + (type(data_baru[3]).__name__ == "int")
jml_float2 = (type(data_baru[0]).__name__ == "float") + (type(data_baru[1]).__name__ == "float") + (type(data_baru[2]).__name__ == "float") + (type(data_baru[3]).__name__ == "float")

print("Jumlah int  :", jml_int2)
print("Jumlah float:", jml_float2)
print("==============================================")

