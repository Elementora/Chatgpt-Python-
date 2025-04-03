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
