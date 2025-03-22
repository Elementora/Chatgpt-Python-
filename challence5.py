# Bir liste verildiğinde, sadece çift sayıları seçen bir filter() fonksiyonu

from functools import reduce


def cift_Sayi(x):
    return x % 2 == 0


sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sonuc = list(filter(cift_Sayi, sayilar))
print(sonuc)


# Lambda ile Daha Kısa Yazımı

sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sonuc = list(filter(lambda x: x % 2 == 0, sayilar))
print(sonuc)  # Çıktı: [2, 4, 6, 8]


############################################################################
# Tüm Elemanları Birleştiren reduce() Fonksiyonu


def birlestir(x, y):
    return x + y  # İki string'i veya liste elemanını birleştirir.


girdi = ["Merhaba", " ", "Dünya", "!"]
sonuc = reduce(birlestir, girdi)

print(sonuc)  # Çıktı: "Merhaba Dünya!"


############################################################################
# Liste Elemanlarını Karesi Alınmış Haliyle Döndüren Fonksiyon


def kare_al(lst):
    return [x ** 2 for x in lst]  # Listenin her elemanının karesini alır.


sayilar = [1, 2, 3, 4, 5]
sonuc = kare_al(sayilar)

print(sonuc)  # Çıktı: [1, 4, 9, 16, 25]

# Lambda ve map() ile Daha Kısa Yazımı
sayilar = [1, 2, 3, 4, 5]
sonuc = list(map(lambda x: x ** 2, sayilar))
print(sonuc)
