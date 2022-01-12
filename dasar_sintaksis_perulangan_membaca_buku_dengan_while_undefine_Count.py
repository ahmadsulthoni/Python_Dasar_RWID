"""
Program perulangan membaca buku dengan while

"""
Jumlah_buku = 10
print('Ibu berkata,"Baca dan pahami semua bukumu"')

Total_jumlah_baca = 0
Jumlah_buku_yang_sudah_dibaca_dan_di_pahami = 0
print(f"Jumlah buku yang sudah di baca dan di pahami adalah {Jumlah_buku_yang_sudah_dibaca_dan_di_pahami}")

print("Dengan While Undefine")
while Total_jumlah_baca < Jumlah_buku * 2:
    Total_jumlah_baca = Total_jumlah_baca + 1
    if Jumlah_buku_yang_sudah_dibaca_dan_di_pahami == 9:
        print(f"Buku ke {Jumlah_buku_yang_sudah_dibaca_dan_di_pahami + 1} Belum paham")
    else:
        Jumlah_buku_yang_sudah_dibaca_dan_di_pahami = Jumlah_buku_yang_sudah_dibaca_dan_di_pahami + 1
        print(f"Buku ke {Jumlah_buku_yang_sudah_dibaca_dan_di_pahami} sudah di baca dan di pahami")

print(f"Jumlah buku yang sudah di baca dan di pahami {Jumlah_buku_yang_sudah_dibaca_dan_di_pahami}")
if Jumlah_buku_yang_sudah_dibaca_dan_di_pahami == Jumlah_buku:
    print(f'"Buku yang sudah di baca dan di pahami sebanyak {Jumlah_buku_yang_sudah_dibaca_dan_di_pahami} Buku')
else:
    print(f'"Tidak Semua buku bisa di pahami, dan yang paham hanya '
          f'{Jumlah_buku_yang_sudah_dibaca_dan_di_pahami} buku saja')
print("Program Selesai")