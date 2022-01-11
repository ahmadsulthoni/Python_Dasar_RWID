"""
Semua sintaksis dasar bahasa pemrograman terdiri dari:
1. Sekuensial : langkah berurutan
2. Percabangan : langkah melompat jika kondisi terpenuhi
3. Perulangan : mengulang langkah yang sama berkali kali selama/sampai kondisi terpenuhi
"""
# Sekuensial
print('Ibu berkata. "Pergi ke toko"')
print('Budi Menjawab, "Baik, apa yang harus saya lakukan di toko?"')
print('Ibu menjawab,"Beli satu botol susu, dan jika ada telur beli 6"')
print("Maka Budi berangkat ke toko")
print("Dan mulai berbelanja")

# Percabangan
jumlah_botol_susu = 210
jumlah_telur = 300
print(f"jumlah botol susu {jumlah_botol_susu} botol")
print(f"jumlah telur {jumlah_telur} butir")
if jumlah_botol_susu > 0:
    print("Budi mengecheck harganya dan ternyata uangnya cukup")
    if jumlah_telur == 0:
        print("Budi membeli 1 botol susu")
    else:
        print("Budi membeli 1 botol susu dan 6 butir telur")
else:
    print("Budi tidak jadi membeli susu")

print("Budi pulang ke rumah")
print("Menyampaikan hasilnya kepada Ibu")