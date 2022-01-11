"""
Program perulangan membaca buku dengan while

"""
Jumlah_buku = 100
print('Ibu berkata,"Baca semua bukumu"')

Jumlah_buku_yang_sudah_dibaca = 0
print(f"Jumlah buku yang sudah di baca {Jumlah_buku_yang_sudah_dibaca}")

print("Dengan While")
while Jumlah_buku_yang_sudah_dibaca < Jumlah_buku:

    Jumlah_buku_yang_sudah_dibaca = Jumlah_buku_yang_sudah_dibaca + 1
    print(f"Buku ke {Jumlah_buku_yang_sudah_dibaca} sudah di baca")

print(f"Jumlah buku yang sudah di baca {Jumlah_buku_yang_sudah_dibaca}")
print("Program Selesai")