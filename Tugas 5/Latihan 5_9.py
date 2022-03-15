# Multiple Inheritance (Teori)
class Perhitungan1:
    def penjumlahan(self,a,b):
        return a+b

class Perhitungan2:
    def perkalian(self,a,b):
        return a*b

class Hitung(Perhitungan1,Perhitungan2):
    def pembagian(self,a,b):
        return a/b

h = Hitung()
print(h.penjumlahan(100,40))
print(h.perkalian(20,35))
print(h.pembagian(100,3))

# Penjelasan : Untuk Multiple Inheritance ini, terdapat 2 induk dengan 1 anakannya
# yang mewarisi atribut dari kedua induknya.