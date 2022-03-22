# Polymorphism dengan kelas

class Cat:
    def __init__(self,nama,umur):
        self.nama = nama
        self.umur = umur

    def bersuara(self):
        print('Meong.. meong...')

class Dog:
    def __init__(self,nama,umur):
        self.nama = nama
        self.umur = umur

    def bersuara(self):
        print('Guk... guk..')

hewan1 = Cat('Tom','3 bulan')
hewan2 = Dog('Spike','7 bulan')

for hewan in (hewan1,hewan2):
    hewan.bersuara()