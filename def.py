def selamlama(isim):
    print(f"merhaba, {isim}!")


selamlama("olcay")
selamlama("KurtKobein")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


def kare_al(sayi):
    return sayi**2


sonuc = kare_al(5)
print(sonuc)  # 25

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


def küp_al(sayi):
    return sayi**3


sonuc = küp_al(7)
print(sonuc)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


def küp_al(sayi):
    return sayi**3


sayi = int(input("Bir sayı giriniz"))  # Kullanıcıdan sayı al
sonuc = küp_al(sayi)  # Fonksiyonu çağır
print("Sonuç", sonuc)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


def küp_al(sayi):
    return sayi**3


try:
    sayi = int(input("Bir sayı giriniz"))  # Kullanıcıdan sayı al
    sonuc = küp_al(sayi)  # Fonksiyonu çağır
    print("Sonuç", sonuc)

except ValueError:
    print("Sadece sayı giriniz ")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


def küp_al(sayi):
    return sayi**3


while True:
    try:
        sayi = int(input("Bir sayı giriniz"))  # Kullanıcıdan sayı al
        sonuc = küp_al(sayi)  # Fonksiyonu çağır
        print("Sonuç", sonuc)
        break
    except ValueError:
        print("Sadece sayı giriniz ")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
