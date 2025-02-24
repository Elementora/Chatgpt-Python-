# Kullanıcıdan iki sayı al

sayi1 = float(input("Birinci sayıyı giriniz: "))
sayi2 = float(input("İkinci sayıyı giriniz: "))

# İşlem türünü al

print("İşlem seçin +, -, *, /")
islem = input("İşlem: ")

# İşlemi kontrol et ve sonucu hesapla
if islem == "+":
    print("Sonuç:", sayi1 + sayi2)
elif islem == "-":
    print("Sonuç:", sayi1 - sayi2)
elif islem == "*":
    print("Sonuç:", sayi1 * sayi2)
elif islem == "/":
    if sayi2 != 0:   # Sıfıra bölmeyi engellemek için kontrol ekledik
        print("Sonuç:", sayi1 / sayi2)
    else:
        print("hata bir sayı 0 a bölünemez !!!!!")

else:
    print("Geçersiz İşlem")
