# Multilevel Inheritence (Teori)
class Hewan:
    def bersuara(self):
        print('Kucing Bersuara')

class Kucing(Hewan):
    def suara(self):
        print('Ngeong.... ngeong...')

class AnakKucing(Kucing):
    def minum(self):
        print('Minum susu')

ak = AnakKucing()
ak.bersuara()
ak.suara()
ak.minum()

# Penjelasan : Class hewan sebagai parent class mewariskan 
# atribut kepada class Kucing lalu diwariskan lagi ke class 
# AnakKucing, sehingga fungsi bersuara(self) dan suara(self) 
# yang terdapat di class Parent (Hewan) dan class Anakannya 
# (Kucing) dapat diwariskan ke class yang lebih jauh lagi.