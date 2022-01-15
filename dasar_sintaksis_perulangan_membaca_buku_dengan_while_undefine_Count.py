"""
Program perulangan membaca buku dengan while

"""
book_count = 10
print('Ibu berkata,"Baca dan pahami semua bukumu"')

read_count = 0
understood_count = 0
print(f"Jumlah buku yang sudah di baca dan di pahami adalah {understood_count}")

print("Dengan While Undefine")
while read_count < book_count * 2:
    read_count = read_count + 1
    if understood_count == 10 :
        print(f"Buku ke {understood_count + 1} Belum paham")
    else:
        understood_count = understood_count + 1
        print(f"Buku ke {understood_count} sudah di baca dan di pahami")

print(f"Jumlah buku yang sudah di baca dan di pahami {understood_count}")
if understood_count == book_count:
    print(f'"Buku yang sudah di baca dan di pahami sebanyak {understood_count} Buku')
else:
    print(f'"Tidak Semua buku bisa di pahami, dan yang paham hanya '
          f'{understood_count} buku saja')
print("Program Selesai")