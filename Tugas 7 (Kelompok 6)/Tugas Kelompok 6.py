# Anggota Kelompok 6
# 5210411353_William Abie
# 5170411359_Surya Yuda Tama
# 5210411220_Baroto Samadyo
# 5170411344 Maulana Zuhdi Firmansyah

class Operator:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Penambahan(Operator):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def tambah(self):
        print("Hasil Penjumlahan: ",self.x + self.y)

class Pengurangan(Operator):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def kurang(self):
        print("Hasil Pengurangan: ",self.x - self.y)

class Perkalian(Operator):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def kali(self):
        print("Hasil Perkalian: ",self.x * self.y)

class Pembagian(Operator):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def bagi(self):
        print("Hasil Pembagian: ",self.x / self.y)

x1 = int(input("Masukkan Nilai x: "))
y1 = int(input("Masukkan nilai y: "))

f1 = Penambahan(x1,y1)
f2 = Pengurangan(x1,y1)
f3 = Perkalian(x1,y1)
f4 = Pembagian(x1,y1)

mode = int(input("1. Penambahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian\nMasukkan metode : "))
if mode == 1:
    f1.tambah()
elif mode == 2:
    f2.kurang()
elif mode == 3:
    f3.kali()
elif mode == 4:
    f4.bagi()
else:
    print("Metode tidak ditemukan")