# append()

sayilar = [1, 2, 3]
sayilar.append(4)  # 4'ü ekler
print(sayilar)  # [1, 2, 3, 4]


# insert()

sayilar = [1, 2, 3]
sayilar.insert(2, 30)  # 2. indekse 30 ekler
print(sayilar)  # [10, 20, 30, 40]

# remove()

sayilar = [1, 2, 3]
sayilar.remove(30)  # 30'u listeden çıkarır
print(sayilar)  # [10, 20, 40]


# pop()

sayilar = [10, 20, 30, 40]
sayilar.pop()  # Son elemanı siler
print(sayilar)   # [10, 20, 30]


sayilar.pop(1)  # 1. indeks (20) silinir
print(sayilar)  # [10, 30]


# sort()

sayilar = [5, 1, 8, 3]
sayilar.sort()  # Küçükten büyüğe sıralar
print(sayilar)  # [1, 3, 5, 8]

# reverse() tersten sıralar

sayilar = [1, 2, 3, 4]
sayilar.reverse()
print(sayilar)  # [4, 3, 2, 1]
