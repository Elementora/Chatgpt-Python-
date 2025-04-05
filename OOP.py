# OOP'nin önemli kavramları


# 1. Encapsulation (Kapsülleme)

class Kisi:
    def __init__(self, ad, yas):
        self.__ad = ad
        self.__yas = yas

    def get_ad(self):
        self.__ad

    def set_ad(self, yeni_ad):
        self.__ad = yeni_ad

    def get_yas(self, yeni_yas):
        self.__yas

    def set_yas(self, yeni_yas):
        if yeni_yas > 0:
            self.__yas = yeni_yas
        else:
            print("Yaş negatif olamaz!")


kisi1 = Kisi("Ahmet", 28)

print(kisi1.get_ad())  # Ahmet
kisi1.set_yas(30)
print(kisi1.get_yas())   # 30
