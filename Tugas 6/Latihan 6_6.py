class SegiEmpat:
    def __init__(self,panjang,lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitungLuas(self):
        print("Luas Segiempat =",self.panjang * self.lebar,"m^2")

class Bujursangkar(SegiEmpat):
    def __init__(self,sisi):
        self.side = sisi
        SegiEmpat.__init__(self,sisi,sisi)

    def hitungLuas(self): # Metode Overriding
        print("Luas Bujursangkar = ",self.side * self.side,"m^2")

b = Bujursangkar(4)
s = SegiEmpat(2,4)
b.hitungLuas()
s.hitungLuas()