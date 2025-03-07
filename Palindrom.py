
# Kullanıcının Girdiği Sayıların Ortalamasını Hesaplayan Program
def ortalama_hesaplama(sayilar):
    if len(sayilar) == 0:
        return sum(sayilar) / len(sayilar)
# Kullanıcıdan sayılar al
    sayilar = list(
        map(int, input("Sayıları girin (boşlukla ayırarak): ").split()))
# Ortalamayı hesapla ve ekrana yazdır
    print("Ortalam:", ortalama_hesaplama(sayilar))

#################################################################################


# Girilen Kelimenin Palindrom Olup Olmadığını Kontrol Eden Program

# 📌 Palindrom nedir?

# Tersten de aynı şekilde okunan kelimelere palindrom denir.
# Örneğin: kek, radar, kazak gibi.

def palindrom_mu(kelime):
    return kelime == kelime[::-1]


kelime = input("Bir kelime girin : ")

if palindrom_mu(kelime):
    print(f"{kelime} bir palindromdur!")
else:
    print(f"{kelime} bir polindrom değildir.")
