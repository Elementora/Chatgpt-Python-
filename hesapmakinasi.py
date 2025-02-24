
import math
import sys

while True:
    print("\n===== HESAP MAKİNESİ =====")
    print("İşlemler: +  -  *  /  ** (üs)  % (mod)  √ veya sqrts (karekök)")
    print("Çıkmak için 'q' yazın.")
# İşlem türünü al

    islem = input("İşlem seçiniz.").strip().lower()

    if islem == "q":
        print("Çıkış yapılıyor. Hoşça kal! 👋")
        sys.exit()  # ✅ Doğru

    # Karekök işlemi için tek sayı al

    if islem == "√" or islem == "sqrt":  # ✅ Hem "√" hem de "sqrt" kabul edilsin
        try:
            sayi = float(input("Karekökü alınacak sayıyı girin: "))
            if sayi < 0:  # ✅ Negatif sayı kontrolü eklendi
                print("Hata: Negatif sayıların karekökü alınamaz!")
            else:
                print(f"Sonuç: √{sayi} = {math.sqrt(sayi)}")
        except ValueError:
            print("Hata: Geçerli bir sayı girin!")

        continue  # ✅ Hata olsun veya olmasın, döngü başa dönsün

    # İşlemin geçerli olup olmadığını kontrol et
    if islem not in ["+", "-", "*", "/", "**", "%"]:
        print("Geçersiz işlem!")
        continue  # Başa dön ve tekrar işlem iste

    # Kullanıcıdan iki sayı al
    try:
        sayi1 = float(input("Birinci sayıyı giriniz: "))
        sayi2 = float(input("İkinci sayıyı giriniz: "))

        # İşlemi kontrol et ve sonucu hesapla
        if islem == "+":  # Toplama işlemi
            print(f"Sonuç: {sayi1} + {sayi2} = {sayi1 + sayi2}")
        elif islem == "-":  # Çıkartma işlemi
            print(f"Sonuç: {sayi1} - {sayi2} = {sayi1 - sayi2}")
        elif islem == "*":  # Çarpma işlemi
            print(f"Sonuç: {sayi1} * {sayi2} = {sayi1 * sayi2}")

        elif islem == "/":  # Bölme işlemi
            if sayi2 != 0:   # Sıfıra bölmeyi engellemek için kontrol ekledik
                print(f"Sonuç: {sayi1} / {sayi2} = {sayi1 / sayi2}")
            else:
                print("hata bir sayı 0 a bölünemez !!!!!")

        elif islem == "**":  # Üs alma işlemi
            print(f"Sonuç: {sayi1} ** {sayi2} = {sayi1 ** sayi2}")

        elif islem == "%":
            print(f"Sonuç: {sayi1} % {sayi2} = {sayi1 % sayi2}")
        else:
            print("Geçersiz İşlem")

    except ValueError:
        print("Hata: Geçerli bir sayı girin!")

        # Kullanıcıya tekrar çalıştırmak isteyip istemediğini soralım
    tekrar = input(
        "Başka bir işlem yapmak ister misiniz? ( Evet / Hayır ):").strip().lower()
    if tekrar == "Hayır":  # Kullanıcı "evet" yazmadıysa çık
        print("Çıkış yapılıyor. Hoşça kal  👋")
        break  # Döngüyü kır ve programı bitir
