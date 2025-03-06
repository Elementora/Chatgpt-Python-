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
