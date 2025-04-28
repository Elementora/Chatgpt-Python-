
import random


def sayi_tahmin_oyunu():
    gizli_sayi = random.randint(1, 100)
    tahmin_sayisi = 0

    print("1 ile 100 arasıında bir sayı tutum. Bakalım tahmin edebilecekmisin ")

    while True:
        tahmin = int(input("Tahminini gir:"))
        tahmin_sayisi += 1

        if tahmin < gizli_sayi:
            print("Daha büyük bir sayı dene !")
        elif tahmin > gizli_sayi:
            print("Daha kücük bir sayı dene !")
        else:
            print(
                f"Tebrikler! {tahmin_sayisi} denemede doğru tahmin ettin.Sayı:{gizli_sayi}")
        break
    sayi_tahmin_oyunu()
