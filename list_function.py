# Bir listede tüm sayıların karesini alan bir fonksiyon

def kareler(lst):
    return [x ** 2 for x in lst]


print(kareler([1, 2, 3, 4,]))

# Bir listede tüm sayıların küpünü alan bir fonksiyon


def küpler(lst):
    return [x ** 3 for x in lst]


print(küpler([1, 2, 3, 4,]))

######################################################################

# Listeleri Fonksiyonlarla İşlemek

# 1: Listeyi Ters Çevirme


def ters_cevir(lst):
    return lst[::-1]


print(ters_cevir([1, 2, 3, 4]))  # Çıktı: [4, 3, 2, 1]


# 2: Listeyi Filtreleme

def buyuk_10(lst):
    return [x for x in lst if x > 10]


print(buyuk_10([5, 12, 8, 15, 3]))  # Çıktı: [12, 15]
#######################################################################
# Listeyi 2 ile çarpacak bir fonksiyon.


def carpi_2(lst):
    return [x ** 2 for x in lst]


print(carpi_2([1, 2, 3, 4]))  # Çıktı: [2, 4, 6, 8]

####################################################################
# Listeyi 3 ile bölecek bir fonksiyon.


def bölü_3(lst):
    return [x // 3 for x in lst]


print(bölü_3([9, 10, 15, 18]))  # Çıktı: [3, 3, 5, 6]
