
# Fonksiyon Parametreleri
def greet(name):
    print(f"Merhaba,{name}!")

    greet("Nadia")  # Merhaba, Naida !


###############################################################

# Fonksiyonlar: Varsayılan Parametreler ile Fonksiyon
# Varsayılan Parametreler


def greet(name="Misafir "):
    print(f"Merhaba,{name}!")

    greet("Olga")  # Merhaba, Olga!
    greet()  # Merhaba ,Misafir!


# Liste Üzerinde Döngü

fruits = ["apple,banana,avacado"]
for fruit in fruits:
    print(fruit)


# Liste Elemanlarını Değiştirme

fruits[0] = "Çilek"
print(fruits)  # ['çilek', 'armut', 'muz']

#############################################################

# Fonksiyonlar: Birden Fazla Parametre


def calculate_area(length, width):
    area = length*width
    return area


# Fonksiyonu çağırarak alan hesaplayalım
result = calculate_area(5, 10)
print(f"Alan: {result}")


###############################################################

# Listeler ve Döngüler: Listeyi Döngü ile Gezmek

fruits = ["banana,muz,orange,strawberry"]

for fruit in fruits:
    print(f"{fruit} meyvesi")

##############################################################

# Listeler ve Döngüler: Liste Elemanını Değiştirmek

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Listeyi döngü ile gezip her sayıyı 2 ile çarpalım
for i in range(len(numbers)):
    numbers[i] = numbers[i]*2

    print(numbers)  # [2, 4, 6, 8, 10]
