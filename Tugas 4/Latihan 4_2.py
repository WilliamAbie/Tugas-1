#=======================
# Nama  : William Abie
# NPM   : 5210411353
#=======================
class Utama:
    def __init__(self):
        self._a = 2

class Turunan(Utama):
    def __init__(self):
        Utama.__init__(self)
        print("Memanggil variabel protected di Class Utama: ",self._a)

        self._a = 3
        print("Memanggil variabel protected yang dimodifikasi diluar Class Utama : ",self._a)

objek1 = Turunan()
objek2 = Utama()

print("Mengakses variabel protected dari objek1 : ",objek1._a)
print("Mengakses variabel protected dari objek2 : ",objek2._a)