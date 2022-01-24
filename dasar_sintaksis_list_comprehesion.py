
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

print('\nperintah del dengan list comprehension step')
daftar_buku = ['Seven Habits', 'How to influence people', 'first thing first','4DX']
del daftar_buku[0::2] #START:END:STEP
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat List Baru')
daftar_buku = ['Seven Habits', 'How to influence people', 'first thing first','4DX']
daftar_buku_baru = daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat List Baru2')
del daftar_buku[:]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat List Baru dengan comprehension : ganjil')
daftar_buku = ['1 Seven Habits', '2 How to influence people', '3 first thing first','4 4DX']
daftar_buku_baru = daftar_buku[0::2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat List Baru dengan comprehension : genap')
daftar_buku = ['1 Seven Habits', '2 How to influence people', '3 first thing first','4 4DX']
daftar_buku_baru = daftar_buku[1::2] #start stop end
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat List Baru dengan comprehension : buang di ujung')
daftar_buku = ['1 Seven Habits', '2 How to influence people', '3 first thing first','4 4DX']
daftar_buku_baru = daftar_buku[0:-1:2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat List Baru dengan comprehension : ganjil')
daftar_buku = ['1 Seven Habits', '2 How to influence people', '3 first thing first','4 4DX']
print(daftar_buku[0::2])