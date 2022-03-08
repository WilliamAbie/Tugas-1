#=======================
# Nama  : William Abie
# NPM   : 5210411353
#=======================

# Variabel bersifat publik
class Mobil():
    def __init__(self,jendela,pintu,mesin):
        self.jendela = jendela
        self.pintu = pintu
        self.mesin = mesin

audi = Mobil(4,4,"Diesel")
print("Jumlah jendela mobil : ",audi.jendela)
print("Jumlah pintu mobil : ",audi.pintu)
print("Jenis mesin mobil : ",audi.mesin)