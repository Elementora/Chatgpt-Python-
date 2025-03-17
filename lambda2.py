
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


# Challenge!

# 1. Yöntem: For Döngüsü ile
def replace_negatives(lst):
    new_list = []
    for num in lst:
        if num < 0:
            new_list.append(0)
        else:
            new_list.append(num)
            return new_list

    my_list = [-3, 5, -1, 7, 0, -8, 4]
    print(replace_negatives(my_list))  # Çıktı: [0, 5, 0, 7, 0, 0, 4]
