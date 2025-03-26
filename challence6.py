###############################################################
#  Sayıları 3 ile Çarpma


def uc_ile_carp(lst):
    return [x*3 for x in lst]  # Tüm elemanları 3 ile çarpıyoruz.


sayilar = [1, 2, 3, 4, 5]
sonuc = uc_ile_carp(sayilar)
print(sonuc)  # Çıktı: [3, 6, 9, 12, 15]

# Lambda ve map() ile Daha Kısa Yazımı

sayilar = [1, 2, 3, 4, 5]
sonuc = list(map(lambda x: x*3, sayilar))
print(sonuc)

###############################################################
# Uzunluğu 5’ten Büyük Kelimeleri Filtrele


def uzun_kelime_filtrele(lst):
    return [kelime for kelime in lst if len(kelime) > 5]


kelimeler = ["Elma", "Kiraz", "Armut", "Babagannus", "Portakal", "Karpuz"]
sonuc = uzun_kelime_filtrele(kelimeler)
print(sonuc)


# Lambda ve filter() ile Daha Kısa Yazımı

kelimeler = ["Elma", "Kiraz", "Armut", "Babagannus", "Portakal", "Karpuz"]
sonuc = list(filter(lambda kelime: len(kelime) > 5, kelimeler))
print(sonuc)

###############################################################
# Pozitif Sayıları Seçme


def pozitif_sayilari_sec(lst):
    return [sayi for sayi in lst if sayi > 0]


sayilar = [-5, -3, 0, 2, 4, 7, -1, 9]
sonuc = pozitif_sayilari_sec(sayilar)
print(sonuc)  # Çıktı: [2, 4, 7, 9]

# Lambda ve filter() ile Daha Kısa Yazımı
sayilar = [-5, -3, 0, 2, 4, 7, -1, 9]
sonuc = list(filter(lambda sayi: sayi > 0, sayilar))
print(sonuc)


###############################################################
# En Büyük Sayıyı Bulma

def en_buyuk_sayi(lst):
    return max(lst)


sayilar = [1, 5, 8, 10, 3, 6]
sonuc = en_buyuk_sayi(sayilar)
print(sonuc)  # Çıktı: 10

# Lambda ile Daha Kısa Yazımı

sayilar = [1, 5, 8, 10, 3, 6]
sonuc = max(sayilar, key=lambda x: x)  # x, her bir liste elemanıdır.
print(sonuc)


# lamda ile Her sayının karesine göre en büyüğü
sayilar = [1, 5, 8, 10, 3, 6]

# Her sayının karesine göre en büyüğü bulur.
sonuc = max(sayilar, key=lambda x: x ** 2)
print(sonuc)


# lamda ile en kucuk sayı
sayilar = [1, 5, 8, 10, 3, 6]
sonuc = min(sayilar, key=lambda x: x)
print(sonuc)


sayilar = [1, 5, 8, 10, 3, 6]
# Her sayının karesine göre en küçük olanı bulur.
sonuc = min(sayilar, key=lambda x: x**2)
print(sonuc)
