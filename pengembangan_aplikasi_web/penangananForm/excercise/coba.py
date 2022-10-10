# program kalkulator sederhana
print(f"""

Program kalkulator sederhana
{'-' * 10}
Pilihan Perhitungan:

1. Tambah
2. Pengurangan
3. Perkalian
4. Pembagian
{'-' * 10}

""")

angka_1 = float(input("Masukkan angka ke-1 = "))
angka_2 = float(input("Masukkan angka ke-2 = "))
pilihan = input("Masukkan pilihan perhitungan anda = ")

if pilihan == '1':
    hasil = angka_1 + angka_2
    print("Hasil Pertambahan = ",hasil)
elif pilihan == '2':
    hasil = angka_1 - angka_2
    print("Hasil Pengurangan = ",hasil)
elif pilihan == '3':
    hasil = angka_1 * angka_2
    print("Hasil Perkalian = ",hasil)
elif pilihan == '4':
    hasil = angka_1 / angka_2
    print("Hasil Pembagian = ",hasil)
else:
    print("Angka anda salah")