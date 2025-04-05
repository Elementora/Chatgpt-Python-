# OOP'nin önemli kavramları


# 1. Encapsulation (Kapsülleme)

class Kisi:
    def __init__(self, ad, yas):
        self.__ad = ad
        self.__yas = yas

    def get_ad(self):
        return self.__ad

    def set_ad(self, yeni_ad):
        self.__ad = yeni_ad

    def get_yas(self):
        return self.__yas

    def set_yas(self, yeni_yas):
        if yeni_yas > 0:
            self.__yas = yeni_yas
        else:
            print("Yaş negatif olamaz!")


kisi1 = Kisi("Ahmet", 28)

print(kisi1.get_ad())  # Ahmet
kisi1.set_yas(30)
print(kisi1.get_yas())   # 30


##############################################################################
# 2. Inheritance (Kalıtım)

class Hayvan:
    def __init__(self, ad):
        self.ad = ad

    def ses_cikar(self):
        return "Bir ses Çıkart"


class Kedi(Hayvan):
    def ses_cikar(self):
        return "Miyav"


class Kopek(Hayvan):
    def ses_cikar(self):
        return "Hav Hav"


kedi1 = Kedi("Leo")
kopek1 = Kopek("Comar")

print(kedi1.ses_cikar())  # Miyav
print(kopek1.ses_cikar())  # Hav hav
