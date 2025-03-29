######################################################################
# Lambda Fonksiyonları (Anonim Fonksiyonlar)


def square(num):
    return num ** 2


print(square(5))  # Çıktı: 25

# Aynı İşlem Lambda ile:


def square_lambda(num): return num ** 2


print(square_lambda(5))  # Çıktı: 25

######################################################################
# List Comprehension (Kısa Liste Oluşturma)

numbers = [1, 2, 3, 4, 5]
squares = []
for num in numbers:
    square.append(num ** 2)
    print(squares)  # Çıktı: [1, 4, 9, 16, 25]

# Aynı İşlem List Comprehension ile:

numbers = [1, 2, 3, 4, 5]
squares = [num ** 2 for num in numbers]
print(squares)  # Çıktı: [1, 4, 9, 16, 25]


######################################################################
# Fonksiyonları Parametre Olarak Kullanma

def apply_function_to_list(func, numbers):
    return [func(num) for num in numbers]
# Kullanım:


numbers = [1, 2, 3, 4, 5]
result = apply_function_to_list(lambda x: x * 2, numbers)
print(result)
