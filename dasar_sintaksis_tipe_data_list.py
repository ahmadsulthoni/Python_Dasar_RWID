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

print('\nClear List')
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nGanti Elemen Pertama')
daftar_buku = ['Seven Habits', 'How to influence people', 'first thing first','4DX']
daftar_buku[0] = 'Eight Habbit'
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nAmbil elemen ke-2')
buku = daftar_buku.pop(1) #perintah pop menghapus element daftar buku ke 2
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nBuku yang di ambil')
print(buku)

print('\nPop')
daftar_buku.pop() #perintah pop menghapus element daftar buku terakhir
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])

print('\nPop -1')
daftar_buku = ['Seven Habits', 'How to influence people', 'first thing first','4DX']
daftar_buku.pop(-1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah Menghapus dengan del')
daftar_buku = ['Seven Habits', 'How to influence people', 'first thing first','4DX']
del daftar_buku[0]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nperintah del dengan list comprehension')
daftar_buku = ['Seven Habits', 'How to influence people', 'first thing first','4DX']
del daftar_buku[:] #del dengan : adalah menghapus semua element yang ada dalam list
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nperintah del dengan list comprehension start')
daftar_buku = ['Seven Habits', 'How to influence people', 'first thing first','4DX']
del daftar_buku[0:1] #del dengan star 0 dan akhiran element 1 yang di hapus
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
