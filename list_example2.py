

# Liste Elemanlarını Belirli Bir Sayıyla Çarpan Fonksiyon

def multiply_list(numbers, factor):
    multiplied_numbers = []
    for num in numbers:
        multiplied_numbers.append(num*factor)
        return multiplied_numbers
    my_list = [2, 4, 6, 8, 10]
    factor = 0
    print("Çarpışmış Liste : ", multiply_list(my_list, factor))


# Proje  Tek Sayıların Karesini Hesaplayan Fonksiyon


def square_odd_numbers(numbers):
    squared_numbers = []

    for num in numbers:
        if num % 2 == 1:  # Eğer sayı tekse
            squared_numbers.append(num ** 2)  # Karesini alıp ekle
            return squared_numbers

        my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        print("Tek sayıların kareleri : ", square_odd_numbers(my_list))
