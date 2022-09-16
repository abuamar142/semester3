# kode ini lebih susah untuk dipahami
# print("Nilai:", float(input("Masukkan suhu dalam Celcius: "))+ 273.15, "K")

# # memsisahkan kode menjadi input, proses, dan output
# # input
# celcius = input("Masukkan suhu dalam Celcius: ")
# # celcius = float(celcius)

# # proses
# kelvin = celcius + 273.15

# # output
# print("Nilai Kelvin adalah", kelvin, "K")

# program penghitung rata-rata
# cacah = total = 0
# while True:
#     nilai = input("Masukkan data: ")
#     try:
#         if not nilai:
#             break
#         cacah += 1
#         total += float(nilai)
#     except:
#         cacah -= 1
#         print("Masukkan angka..!")
# print("Total: ", total, "Cacah: ", cacah)
# print("Rata-rata data adalah:", total/cacah)

# program penghitung rata-rata dengan pemisahan bagian
# # input
# data = []
# while True:
#     nilai = float(input("Masukkan data: "))
#     if not nilai:
#         break
#     data.append(nilai)

# # proses
# cacah = len(data)
# total = 0
# for nilai in data:
#     total += nilai
# hasil = total/cacah

# # output
# print("Rata-rata data adalah: ", hasil)

# # input
data = []
while True:
    nilai = input("Masukkan data: ")
    if not nilai:
        break
    try:
        nilai = float(nilai)
        data.append(nilai)
    except:
        print("Masukkan angka..!")     

# # proses
cacah = len(data)
total = 0
for nilai in data:
    total += nilai
hasil = total/cacah

# # output
print("Rata-rata data adalah: ", hasil)