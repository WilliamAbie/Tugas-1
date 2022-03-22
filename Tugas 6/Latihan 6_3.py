# Polymorphism dengan Inheritance

class Burung:
    def intro(self):
        print('Di dunia ini ada beberapa tipe dari spesies burung')

    def terbang(self):
        print('Hampir semua jenis burung dapat terbang namun ada beberapa yang tidak dapat terbang')

class Elang(Burung):
    def terbang(self):
        print('Elang dapat terbang')

class BurungUnta(Burung):
    def terbang(self):
        print('Burung untu tidak dapat terbang')

obj_burung      = Burung()
obj_elang       = Elang()
obj_burungunta  = BurungUnta()

# Kelas parent
obj_burung.intro()
obj_burung.terbang()
print('\n')

# Kelas anakan
obj_elang.intro()
obj_elang.terbang()
print('\n')

obj_burungunta.intro()
obj_burungunta.terbang()