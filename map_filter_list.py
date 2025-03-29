
#####################################################
# Liste Elemanlarını Dönüştürme


from functools import reduce


def iki_katı(x):
    return x * 2


sayilar = [1, 2, 3, 4, 5]
sonuc = list(map(iki_katı, sayilar))
print(sonuc)  # Çıktı: [2, 4, 6, 8, 10]


# lambda olarak

sayilar = [1, 2, 3, 4, 5]
sonuc = list(map(lambda x: x * 2, sayilar))
print(sonuc)  # Çıktı: [2, 4, 6, 8, 10]


#############################################################################
# Listeyi Şartlara Göre Filtreleme


def tek_Sayi(x):
    return x % 2 != 0


sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sonuc = list(filter(tek_Sayi, sayilar))


# lamvda olarak
sayilar = [1, 2, 3, 4, 5]
sonuc = list(filter(lambda x: x % 2 != 0, sayilar))  # Çıktı: [1, 3, 5, 7, 9]


#############################################################################
# Liste Elemanlarını Tek Bir Sonuca İndirgeme


def carp(x, y):
    return x*y


sayilar = [1, 2, 3, 4, 5]
sonuc = reduce(carp, sayilar)
print(sonuc)  # Çıktı: 120  (1*2*3*4*5)

# Lamda olarak

sayilar = [1, 2, 3, 4, 5]
sonuc = reduce(lambda x, y: x*y, sayilar)
print(sonuc)  # Çıktı: 120
