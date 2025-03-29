#######################################################
# Çift sayıların küplerini hesaplayan bir fonksiyon
def cube_even_numbers(numbers):
    #  Bir liste alacak.
    #  Çift sayıları seçecek.
    #  Küplerini hesaplayıp yeni bir listeye ekleyecek.
    # Seçtiğimiz çift sayıların küplerini saklamak için bir liste oluşturacağız
    cube_numbers = []

# Şimdi listeyi for döngüsü ile gezelim ve çift sayıları bulup küplerini alalım
    for num in numbers:
        if num % 2 == 0:  # Eğer sayı çiftse
            cube_numbers.append(num ** 3)  # Küpünü al ve ekle

            # Artık yeni listeyi döndürebiliriz
            return cube_numbers


# Şimdi fonksiyonumuzu test edelim
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Çift sayıların küpleri : ", cube_even_numbers(my_list))


############################################################################################

# List Comprehension ile Daha Kısa Yazalım

def cube_even_numbers(numbers):
    return [num ** 3 for num in numbers if num % 2 == 0]


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Çift sayıların küpleri : ", cube_even_numbers(my_list))
