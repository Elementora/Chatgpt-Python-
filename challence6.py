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

###############################################################
# Lambda ve filter() ile Daha Kısa Yazımı

kelimeler = ["Elma", "Kiraz", "Armut", "Babagannus", "Portakal", "Karpuz"]
sonuc = list(filter(lambda kelime: len(kelime) > 5, kelimeler))
print(sonuc)
