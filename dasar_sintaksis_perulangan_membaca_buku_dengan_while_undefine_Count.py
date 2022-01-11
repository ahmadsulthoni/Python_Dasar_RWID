"""
Program perulangan membaca buku dengan while

"""
Jumlah_buku = 10
print('Ibu berkata,"Baca dan pahami semua bukumu"')

Total_jumlah_baca = 0
Jumlah_buku_yang_sudah_dibaca_dan_di_pahami = 0
print(f"Jumlah buku yang sudah di baca dan di pahami adalah {Jumlah_buku_yang_sudah_dibaca_dan_di_pahami}")

print("Dengan While Undefine")
while Jumlah_buku_yang_sudah_dibaca_dan_di_pahami < Jumlah_buku * 2:
    Total_jumlah_baca = Total_jumlah_baca + 1
    if Jumlah_buku_yang_sudah_dibaca_dan_di_pahami == 9:
        print(f"Buku ke {Jumlah_buku_yang_sudah_dibaca_dan_di_pahami + 1} Belum paham")
    else:
        Jumlah_buku_yang_sudah_dibaca_dan_di_pahami = Jumlah_buku_yang_sudah_dibaca_dan_di_pahami + 1
        print(f"Buku ke {Jumlah_buku_yang_sudah_dibaca_dan_di_pahami} sudah di baca dan di pahami")

print(f"Jumlah buku yang sudah di baca dan di pahami {Jumlah_buku_yang_sudah_dibaca_dan_di_pahami}")
print("Program Selesai")