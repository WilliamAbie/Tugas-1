# Variable bersifat private
class Mobil():
    def __init__(self,jendela,pintu,mesin):
        self.__jendela = jendela
        self.__pintu = pintu
        self.__mesin = mesin

    def Tampil(self) :
        print("Jendela :", self.__jendela)
        print("Pintu :", self.__pintu)
        print("Mesin :", self.__mesin)

toyota = Mobil(6,2,"Elektrik")
toyota.Tampil()
