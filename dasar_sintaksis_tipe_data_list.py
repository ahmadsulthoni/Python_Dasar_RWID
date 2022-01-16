daftar_buku = ['Seven Habits', 'How to influence people', 'first thing first','4DX']
print('Tampilkan variable daftar buku')
print(daftar_buku)

print('\nProses semua dengan for in')
for buku in daftar_buku:
    print(buku)

print('\nTampilkan isi daftar_buku pada indeks tertentu')
print(daftar_buku[0])
print(daftar_buku[2])

#len di gunakan untuk menampilkan banyaknya data dan dapat menyesuaikan data tersebut
print('\nTampilkan dengan For in Range')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nTampilkan dengan For in len dimana type data tiap elemen berbeda-beda')
daftar_buku = [1, 'Kenji Volume 2', -313, 3.14]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nKembalikan nilai awal daftar_buku')
daftar_buku = ['Seven Habits', 'How to influence people', 'first thing first','4DX']
print('\nTambahkan 1 Buku Baru')
daftar_buku.append('Dunia Matematika Kelas 5')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
