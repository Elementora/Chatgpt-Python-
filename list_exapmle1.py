
# Liste Elemanlarını Toplayan Fonksiyon
def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
        return total
    my_list = [10, 20, 30, 40, 50]
    print("Toplam", sum_list(my_list))  # Çıktı: 150

# Bu fonksiyon bir liste alıyor, döngü ile tüm elemanlarını topluyor ve sonucu döndürüyor.

    #####################################################

# Liste Filtreleme Fonksiyonu
# Çift Sayıları Filtreleme


def filter_even_numbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.appent(num)
            return even_numbers

        my_list = [3, 6, 9, 12, 15, 18]
        print("Çift sayılar", filter_even_numbers(my_list))
        # Çıktı: [6, 12, 18]

 #####################################################

# Fonksiyon ile Liste Üzerinde İşlem Yapma
# istenin Elemanlarını İkiye Katlayan Fonksiyon


def double_numbers(numbers):
    for i in range(len(numbers)):
        numbers[i] = numbers[i]*2
        return numbers

    my_list = [2, 4, 6, 8, 10]
    print("İkiye katlanmış liste:", double_numbers(my_list))

# Çıktı: [4, 8, 12, 16, 20]
