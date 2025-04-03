class HesapMakinesi:
    def __init__(self, sayi1, sayi2):
        self.sayi1 = sayi1
        self.sayi2 = sayi2

    def toplama(self):
        return self.sayi1 + self.sayi2

    def cikartma(self):
        return self.sayi1-self.sayi2

    def carpma(self):
        return self.sayi1 * self.sayi2

    def bolme(self):
        if self.sayi2 != 0:
            return self.sayi1 / self.sayi2
        else:
            return "Bir sayıyı 0 a bölemezsiniz"


# Nesne oluşturma
hesap = HesapMakinesi(10, 5)

# İşlemleri gerçekleştirme
print("Toplama:", hesap.toplama())    # 10 + 5 = 15
print("Çıkarma:", hesap.cikarma())    # 10 - 5 = 5
print("Çarpma:", hesap.carpma())      # 10 * 5 = 50
print("Bölme:", hesap.bolme())        # 10 / 5 = 2.0
