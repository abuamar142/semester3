# menghitung luas bangunan
# disitu terdapat beberapa ruangan yang memiliki luas yang sama diantaranya
# ada 5 ruangan berukuran 4 x 3,
# ada 3 ruangan berukuran 4 x 4, dan
# ada 1 ruangan berukuran 8 x 5

# buat fungsi untuk mengukur, dengan memasukkan jumlah ruangan dan ukuran berturut-turut

def calculate(sisi1, sisi2, jumlah):
    hasil = sisi1 * sisi2 * jumlah
    return hasil

building = []

jenis_bangunan = int(input("Masukkan jumlah jenis bangunan: "))
print("\n")

for a in range(jenis_bangunan):
    sisi_1 = int(input(f"Bangunan {a + 1} sisi 1: "))
    sisi_2 = int(input(f"Bangunan {a + 1} sisi 2: "))
    jumlah = int(input(f"Bangunan {a + 1} jumlah: "))
    print("\n")

    building.append(calculate(sisi_1, sisi_2, jumlah))

hasil = 0

for a in building:
    hasil += a

print(f"Total luas bangunan adalah: {hasil} m^2")