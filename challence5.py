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


############################################################################
# Pozitif Sayıları Filtreleme

def pozitif_Sayilar(lst):
    return [x for x in lst if x > 0]  # Pozitif olanları seçiyoruz.


sayilar = [-10, -3, 0, 3, 7, 5, -2, 8]
sonuc = pozitif_Sayilar(sayilar)

print(sonuc)

# Lambda ve filter() ile Daha Kısa Yazımı

sayilar = [-10, -3, 0, 3, 7, 5, -2, 8]
sonuc = list(filter(lambda x: x > 0, sayilar))
print(sonuc)


############################################################################
# String Uzunluklarını Döndüren Fonksiyon

def kelime_uzunluklari(lst):
    return [len(x) for x in lst]  # Her kelimenin uzunluğunu alır.


kelimeler = ["Python", "Lamda", " Fonksiyon", "Kod"]
sonuc = kelime_uzunluklari(kelimeler)
print(sonuc)  # Çıktı: [6, 6, 9, 3]


############################################################################
# Çift Sayıları Filtreleme

def cift_sayilar(lst):
    return [x for x in lst if x % 2 == 0]  # Çift sayıları seçiyoruz.


sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sonuc = cift_sayilar(sayilar)
print(sonuc)  # Çıktı: [2, 4, 6, 8, 10]


# Lambda ve filter() ile Daha Kısa Yazımı
sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sonuc = list(filter(lambda x: x % 2 == 0, sayilar))
print(sonuc)  # Çıktı: [2, 4, 6, 8, 10]


############################################################################
# Tek Sayıları Filtreleme


def tek_sayilar(lst):
    return [x for x in lst if x % 2 != 0]


sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sonuc = tek_sayilar(sayilar)
print(sonuc)


# Lambda ve filter() ile Daha Kısa Yazımı
sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sonuc = list(filter(lambda x: x % 2 != 0, sayilar))
print(sonuc)


############################################################################
# 5'in Katlarını Filtreleme

def besin_katlari(lst):
    return [x for x in lst if x % 5 == 0]  # 5’e tam bölünenleri seçiyoruz.


sayilar = [1, 5, 10, 14, 15, 20, 22, 25, 30, 33]
sonuc = besin_katlari(sayilar)
print(sonuc)  # Çıktı: [5, 10, 15, 20, 25, 30]


# Lambda ve filter() ile Daha Kısa Yazımı
sayilar = [1, 5, 10, 14, 15, 20, 22, 25, 30, 33]
sonuc = list(filter(lambda x: x % 5 == 0, sayilar))
print(sonuc)
