
# OOP'ye Başlangıç

class Araba:
    def __init__(self, marka, model, yil):
        self.marka = marka
        self.model = model
        self.yil = yil

    def bilgi_goster(self):
        return f"{self.yil} model {self.marka} {self.model}"


# Sınıftan bir nesne oluşturalım
araba1 = Araba("Toyota", "Coralla", 2020)
print(araba1.bilgi_goster())  # Çıktı: 2020 model Toyota Corolla

########################################################################

# ÖRNEK


class Telefon:
    def __init__(self, marka, model, yil):
        self.marka = marka
        self.model = model
        self.yil = yil

    def tel_bilgi_goster(self):
        return f"{self.yil} model {self.marka} {self.model}"


# Sınıftan bir nesne oluşturalım
telephone = Telefon("İphone", "16 Pro Max Blue", 2025)
print(telephone.tel_bilgi_goster())


########################################################################

# Araba Sınıfı

class Araba:
    def __init__(self, marka, model, yil, renk):
        self.marka = marka
        self.model = model
        self.yil = yil
        self.renk = renk
        self.hiz = 0

    def araba_bilgileri(self):
        return f"{self.yil} model {self.marka} {self.model} - Renk : {self.renk}"

    def hizlan(self, kmh):
        self.hiz += kmh
        return f"Hız:{self.hiz} km/s"

    def yavasla(self, kmh):
        self.hiz -= kmh
        if self.hiz < 0:
            self.hiz = 0
        return f"Hiz : {self.hiz}km/x"


# Sınıftan bir nesne oluşturalım
araba1 = Araba("BMW", "M4 COMPETİİON", 2025, "Colorful")
# Araba bilgilerini göster
print(araba1.araba_bilgileri())
# Hızlanma
print(araba1.hizlan(50))
# Yavaşlama
print(araba1.yavasla(30))
