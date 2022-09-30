kelas = [
    {
        'npm': '2121001',
        'nama': 'Naruto Saifudin',
        'hasil_studi': [
            {
                'kode': 'INF001',
                'nama': 'Konsep Pemrograman',
                'sks': 4,
                'nilai': 'A'
            },
            {
                'kode': 'INF002',
                'nama': 'Pengantar Teknologi Informasi',
                'sks': 2,
                'nilai': 'A-',
            },
        ],
    },
    {
        'npm': '2121002',
        'nama': 'Saitama Gundul',
        'hasil_studi': [
            {
                'kode': 'INF001',
                'nama': 'Konsep Pemrograman',
                'sks': 4,
                'nilai': 'B',
            },
            {
                'kode': 'INF002',
                'nama': 'Pengantar Teknologi Informasi',
                'sks': 2,
                'nilai': 'B+',
            }
        ],
    },
]

def hitung_ipk(mahasiswa):
    skor = {
        'A': 4, 'A-': 3.75, 'AB': 3.5, 'B+': 3.25,
        'B': 3, 'B-': 2.75, 'BC': 2.5, 'C+': 2.25,
        'C': 2,
        'D': 1,
    }
    total_sks = 0
    total_skor = 0
    for hasil_studi in mahasiswa['hasil_studi']:
        sks = hasil_studi['sks']
        nilai = hasil_studi['nilai']
        total_sks += sks
        total_skor += sks * skor.get(nilai, 0,)
        # jika nilai tidak ditemukan maka defaultnya 0, tidak error
    ipk = total_skor / total_sks
    return ipk

total_ipk = 0
for mahasiswa in kelas:
    total_ipk += hitung_ipk(mahasiswa)
    print(total_ipk)
rata2_ipk = total_ipk / len(kelas)

print(rata2_ipk)