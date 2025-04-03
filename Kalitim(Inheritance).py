# Üst Sınıf (Parent Class)

class Arac:
    def __init__(self, marka, model, yil):
        self.marka = marka
        self.model = model
        self.yil = yil

    def arac_bilgisi(self):
        return f"{self.yil} model {self.marka} {self.model}"

# Alt sınıf (Child Class) - Arac sınıfından miras alıyor


class Araba(Arac):
    def __init__(self, marka, model, yil, renk):
        super().__init__(marka, model, yil)
        self.renk = renk

    def araba_bilgisi(self):
        return f"{self.yil} model {self.marka} {self.model} - Renk : {self.renk}"

# Araba nesnesi oluşturalım


araba1 = Araba("Toyota", "Corolla", 2025, "Grey")


# Üst sınıf metodunu kullanabiliyor!

print(araba1.arac_bilgisi())  # Çıktı: 2025 model Toyota Corolla

# Alt sınıfın yeni metodunu kullanabiliyor!

print(araba1.araba_bilgisi())  # Çıktı: 2025 model Toyota Corolla - Renk: Grey
