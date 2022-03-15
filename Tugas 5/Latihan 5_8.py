# Hierarichal Inheritance (Teori)
class Induk:
    def fungsiInduk(self):
        print('Fungsi pada Parent Class')

class Anak1(Induk):
    def fungsiAnak1(self):
        print('Fungsi pada anak 1')

class Anak2(Induk):
    def fungsiAnak2(self):
        print('Fungsi pada anak 2')

a1 = Anak1()
a2 = Anak2()

a1.fungsiInduk()
a1.fungsiAnak1()

a2.fungsiInduk()
a2.fungsiAnak2()

# Penjelasan : Untuk hierarichal inheritance, adalah 2 anakan yang mewarisi 
# sifat dari 1 induk.