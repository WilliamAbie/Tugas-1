# Single Inheritance (Teori)
class Hewan:
    def bersuara(self):
        print('Kucing Bersuara')

class Kucing(Hewan):
    def suara(self):
        print('Ngeong.... ngeong...')

k = Kucing()
k.bersuara()
k.suara()

# Penjelasan : Class hewan sebagai parent class mewariskan 
# atribut kepada class Kucing, sehingga fungsi bersuara(self)
# yang terdapat di class Parent (Hewan) dapat dipanggil 
# melalui class Anakannya (Kucing).