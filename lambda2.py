
##########################################################################
# Lambda Fonksiyonları ile Çift Sayıların Küplerini Hesaplama

def cube(x): return x**3


print(cube(4))  # Çıktı: 64

###############################################################
# filter() ve map() Kullanımı
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Çıktı: [2, 4, 6, 8, 10]


###############################################################
