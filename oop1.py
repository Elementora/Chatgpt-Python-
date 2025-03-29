
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
