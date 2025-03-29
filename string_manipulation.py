
#############################################
# Kullanıcının girdiği kelimenin harflerini listeye ekleyip alfabetik sıralayan bir program


kelime = input("Bir kelime girin : ")  # Kullanıcıdan kelime al
harfler = list(kelime)  # Kelimenin harflerini listeye ekle
harfler.sort()  # Alfabetik sırala

print("Sıralanmış harfler", harfler)

#############################################
# Bir liste içinde kaç tane tekrar eden eleman olduğunu hesaplayan bir program

elemanlar = input("Bir cümle girin")
tekrar_eden_eleman = {}

# Elemanları say
for eleman in elemanlar:
    if eleman in tekrar_eden_eleman:
        tekrar_eden_eleman[eleman] += 1
    else:
        tekrar_eden_eleman[eleman] = 1
print("Eleman tekrar sayıları : ")
for eleman, tekrar in tekrar_eden_eleman.items():
    print(f"{eleman}: {tekrar} kez")

#######################

# Liste kullanılmış hali

elemanlar = input("Bir cümle giriniz : ")
benzersiz_harfler = list(set(elemanlar))
tekrar_sayilari = []

for harf in benzersiz_harfler:
    tekrar_sayilari.append((harf, elemanlar.count(harf)))

    print("Eleman tekrar sayıları: ")

    for harf, tekrar in tekrar_sayilari:
        print(f"{harf},{tekrar} kez ")



#############################################
# Kullanıcının girdiği kelimenin harflerini listeye ekleyip alfabetik sıralayan bir program


kelime = input("Bir kelime girin : ")  # Kullanıcıdan kelime al
harfler = list(kelime)  # Kelimenin harflerini listeye ekle
harfler.sort()  # Alfabetik sırala

print("Sıralanmış harfler", harfler)

#############################################
# Bir liste içinde kaç tane tekrar eden eleman olduğunu hesaplayan bir program

elemanlar = input("Bir cümle girin")
tekrar_eden_eleman = {}

# Elemanları say
for eleman in elemanlar:
    if eleman in tekrar_eden_eleman:
        tekrar_eden_eleman[eleman] += 1
    else:
        tekrar_eden_eleman[eleman] = 1
print("Eleman tekrar sayıları : ")
for eleman, tekrar in tekrar_eden_eleman.items():
    print(f"{eleman}: {tekrar} kez")

#######################

# Liste kullanılmış hali

elemanlar = input("Bir cümle giriniz : ")
benzersiz_harfler = list(set(elemanlar))
tekrar_sayilari = []

for harf in benzersiz_harfler:
    tekrar_sayilari.append((harf, elemanlar.count(harf)))

    print("Eleman tekrar sayıları: ")

    for harf, tekrar in tekrar_sayilari:
        print(f"{harf},{tekrar} kez ")
