
#  1 Kullanıcıdan alınan sayılardan yalnızca çift olanları bir listeye ekleyen program

cift_sayilar = []   # Boş bir liste oluştur

# Kullanıcıdan kaç sayı gireceğini sor
adet = int(input("Kaç sayı girmek istiyorsunuz : "))


# Kullanıcıdan sayı al ve sadece çift olanları listeye ekle
for _ in range(adet):
    sayi = int(input("Bir seyı girin: "))
    # Eğer sayı çiftse listeye ekle ( sayı 2 ye TAM BÖLÜNÜYORSA çift sayıdır .)
    if sayi % 2 == 0:
        cift_sayilar.append(sayi)

print("Çift sayılar: ", cift_sayilar)


# 2 Kullanıcının girdiği kelimenin harflerini listeye ekleyip alfabetik sıralayan bir program


kelime = input("Bir kelime girin : ")  # Kullanıcıdan kelime al
harf_listesi = sorted(list(kelime))  # Harfleri bir listeye çevirip sıralayalım

print("Sıralanmış harfler :", harf_listesi)


# 3 Bir liste içinde kaç tane tekrar eden eleman olduğunu hesaplayan program


# Kullanıcıdan liste elemanlarını al
elemanlar = input("Liste elemanlarını bpşlukla ayırarak girin").split()
tekrar_sayisi = {}  # Tekrar eden elemanları saymak için sözlük (dict) kullan

for eleman in elemanlar:
    if eleman in tekrar_sayisi:
        tekrar_sayisi[eleman] += 1
    else:
        tekrar_sayisi[eleman] = 1
print("Elemen tekrar sayıları : ")
for eleman, tekrar in tekrar_sayisi.items():
    print(f"{eleman}: {tekrar} kez")
