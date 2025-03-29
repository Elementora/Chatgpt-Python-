# Cümlenin Kelimelerini Alfabetik Sıralama

cumle = input("Bir cünle girin : ")  # Kullanıcıdan cümle al

kelimeler = cumle.split()  # Cümleyi boşluklardan ayırıp listeye çevir

kelimeler.sort()  # Listeyi alfabetik olarak sırala

print("Alfabetik sıralanmış kelimeler : ", kelimeler)  # Sonucu yazdır


# Listenin En Büyük ve En Küçük Elemanını Bulma

# Kullanıcıdan sayı listesi al (boşlukla ayırarak)
sayilar = list(map(int, input("Sayıları girin (boşlukla ayırarak): ").split()))

en_kucuk = min(sayilar)  # En büyük ve en küçük sayıyı bul
en_buyuk = max(sayilar)

print("En küçük satı :", en_kucuk)  # Sonucu yazdır
print("En büyük sayı : ", en_buyuk)


# Bir Liste İçinde Kaç Tane Tekrar Eden Eleman Olduğunu Bulma


# Kullanıcıdan sayı listesi al (boşlukla ayırarak)
sayilar = list(map(int, input("Sayıları girin(boşlukla ayırarak): ").split()))

# Sayıları ve tekrar sayılarını saklamak için bir sözlük (dictionary) oluştur
tekrar_sayilari = {}

for sayi in sayilar:
    if sayi in tekrar_sayilari:
        tekrar_sayilari[sayi] += 1
    else:
        tekrar_sayilari[sayi] = 1

# Sadece tekrar edenleri ekrana yazdır
print("Tekrar eden sayılar ve tekrar sayıları:")
for sayi, tekrar in tekrar_sayilari.items():
    if tekrar > 1:
        print(f"{sayi}: {tekrar} kez tekrar etti")


# Bir Cümlenin İçindeki Her Harfin Kaç Kez Geçtiğini Bulma

cumle = input("Bir cümle girin : ")  # Kullanıcıdan bir cümle al
harf_Sayilari = {}  # Harf tekrarlarını saklamak için sözlük oluştur

for harf in cumle:  # Cümledeki her harfi kontrol et
    if harf != " ":
        if harf in harf_Sayilari:  # Boşlukları sayma
            harf_Sayilari[harf] += 1
        else:
            harf_Sayilari[harf] = 1

print("Harflerin tekrar sayıları : ")  # Sonucu ekrana yazdır
for harf, tekrar in harf_Sayilari.items():
    print(f"{harf}: {tekrar} kez")
