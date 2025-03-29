yas = int(input("Yasınızı GİRİNİZ : "))

if yas >= 18:
    print("Ehliyet alabilirsiniz ")

else:
    print("Ehliyet alamazsınız .")


sayi = int(input("Bir sayı girin"))
if sayi > 0:
    print("Pozitif sayı girdiniz ,")
elif sayi < 0:
    print("Negatif bir sayı girdiniz , ")
else:
    print("Sayı sıfırdır.")


notu = int(input("Notuzu girin:"))
if notu >= 75:
    print("Geçtiniz! Tebriks,🎉")
else:
    print("Maalesef Kaldınız , 😞")


notu = int(input("Notuzu girin:"))
if notu >= 80:
    print("Geçtiniz! Tebriks,🎉")
elif 50 <= notu <= 79:
    print("Getin ama Daha iyi olabilirdi. 🙂")
else:
    print("Maalesef Kaldınız , 😞")


yas = 25
if yas >= 18 and yas <= 33:  # 18 ile 33 arasını kontrol ediyoruz
    print("Genç yetişkinisiz.")


notu = int(input("Notunuzu girin : "))

if notu >= 80:
    print("Çok iyi")
elif notu >= 50:  # Burada ayrıca "and" kullanmaya gerek yok
    print("Geçtin ama dah aiyi olabilirdi.")
else:
    print("kaldın maalesef.")
