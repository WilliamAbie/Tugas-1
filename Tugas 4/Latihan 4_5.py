#=======================
# Nama  : William Abie
# NPM   : 5210411353
#=======================

# Variabel bersifat protected
class Mobil():
    def __init__(self,jendela,pintu,mesin):
        self._jendela = jendela
        self._pintu = pintu
        self._mesin = mesin

class Truk(Mobil):
    def __init__(self,jendela,pintu,mesin,tipe):
        super().__init__(jendela,pintu,mesin)
        self.tipebak = tipe

truk = Truk(4,4,'Diesel','Bak tertutup')
print(truk._mesin)
print(truk.tipebak)