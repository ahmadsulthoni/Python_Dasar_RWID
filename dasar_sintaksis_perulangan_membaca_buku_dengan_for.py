"""
Program perulangan membaca buku dengan for
"""

Jumlah_buku = 100
print('Ibu berkata,"Baca semua bukumu"')

Jumlah_buku_yang_sudah_dibaca = 0
print(f"Jumlah buku yang sudah di baca {Jumlah_buku_yang_sudah_dibaca}")

print("Dengan For")
for Jumlah_buku_yang_sudah_dibaca in range(1,Jumlah_buku+1):

    print(f"Buku ke {Jumlah_buku_yang_sudah_dibaca} sudah di baca")

print(f"Jumlah buku yang sudah di baca {Jumlah_buku_yang_sudah_dibaca}")
