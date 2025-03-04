# Liste Tanımlama

sayilar = [10, 20, 30, 40, 50]
isimler = ["Janice", "Luna", "Alex"]
karisik = [1, "Merhaba", 3.14, True]

print(sayilar)
print(isimler)
print(karisik)


# Liste Elemenlarına Erişim

sayilar = [10, 20, 30, 40, 50]
print(sayilar[0])  # 10 (İlk eleman)
print(sayilar[2])  # 30 (Üçüncü eleman)
print(sayilar[-1])  # 50 (Son eleman)

# For Döngüsü ile Listeyi Gezinme


meyveler = ["Apple", "Banana", "Orange", "Strawberry"]

for meyve in meyveler:
    print(meyve)


# For Döngüsü ile İndex kullanımı

meyveler = ["Apple", "Banana", "Orange", "Strawberry"]
for index, meyve in enumerate(meyveler):
    print(f"{index}.meyve:{meyve}")
