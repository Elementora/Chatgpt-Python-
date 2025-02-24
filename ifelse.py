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
