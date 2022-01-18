
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