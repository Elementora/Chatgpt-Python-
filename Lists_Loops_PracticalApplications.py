
# Kullanıcıdan 5 tane isim alıp bir listeye ekleyen program

isimler = []

for i in range(5):
    isim = input(f"{i+1}. isim giriniz : ")
    isimler.append(isim)

    print("Girdiğiniz İsimler :", isimler)


# Listedeki Sayıların Toplamını Bulma

sayilar = [10, 20, 30, 40, 50]
toplam = 0

for sayi in sayilar:
    toplam += sayi

print("Listedeki sayıların toplamı ", toplam)


# Listedeki En Büyük ve En Küçük Sayıyı Bulma

sayilar = [5, 12, 3, 90, 45, 7]

print("En büyük sayi : ", max(sayilar))
print("En kücük sayı", min(sayilar))

# Kullanıcıdan Sayılar Alıp Sıralayan Program

sayilar = []

for i in range(5):
    sayi = int(input(f"{i+1}. sayi giriniz : "))
    sayilar.append(sayi)

    sayilar.sort()
print("Sıralanmış liste: ", sayilar)


# Girilen Kelimenin Tersini Liste Kullanarak Yazdırma

kelime = input("Bir kelime giriniz : ")
ters_kelime = list(kelime)  # Kelimeyi listeye çevir
ters_kelime.reverse()   # Ters çevir

print("Ters kelime:", "".join(ters_kelime))


# Mini Proje: Liste Kullanarak Not Ortalaması Hesaplama

notlar = []
ders_sayisi = int(input("Kaç dersiniz var ?  "))

for i in range(ders_sayisi):
    notlar.append(float(input(f"{i+1}.dersin notunu giriniz: ")))

    ortalama = sum(notlar) / len(notlar)
    print(f"Derslerinizin Ortalaması: {ortalama}")
