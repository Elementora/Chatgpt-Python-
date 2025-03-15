

# Liste Elemanlarını Belirli Bir Sayıyla Çarpan Fonksiyon

def multiply_list(numbers, factor):
    multiplied_numbers = []
    for num in numbers:
        multiplied_numbers.append(num*factor)
        return multiplied_numbers
    my_list = [2, 4, 6, 8, 10]
    factor = 0
    print("Çarpışmış Liste : ", multiply_list(my_list, factor))
