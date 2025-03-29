
# Kullanıcının Girdiği Sayıların Ortalamasını Hesaplayan Program
import random


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


###########################################################################

#  Rastgele Sayı Üreten ve Kullanıcıdan Tahmin Alan Oyun


def sayi_tahmin_oyunu():
    rastgele_sayi = random.random(1, 100)
    tahmin = -1

    while tahmin != rastgele_sayi:
        tahmin = int(input("Tahmini bir sayı girin (1-100): "))

        if tahmin < rastgele_sayi:
            print("Daha büyük bir sayı girin !")
        elif tahmin > rastgele_sayi:
            print("Daha küük bir sayı girin !")
    print("Tebrikler ! Doğru tahmin ettiniz .")

    sayi_tahmin_oyunu()

############################################################################

# Kullanıcının girdiği bir metindeki sesli harfleri bulan bir program


sesliharfler = ["a", "e", "ı", "i", "o", "ö", "u", "ü"]

cumle = input(" Bir cümle girin : ")

sesli_harf_sayisi = 0

for harf in cumle:
    if harf.lower() in sesliharfler:
        print(harf, end=" ,")
        sesli_harf_sayisi += 1

print(f"\nToplam  {sesli_harf_sayisi}, sesli harf var")
