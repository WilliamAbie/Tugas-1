class MenuMinuman:
    def __init__(self,nama,deskripsi,harga,stok):
        self.nama       = nama
        self.deskripsi  = deskripsi
        self.harga      = harga
        self.__stok     = stok

    def Keterangan(self):
        print("{} harga Rp. {}, {}. Stok Tersedia : {}".format(self.nama,self.harga,self.deskripsi,self.__stok))

mnm1 = MenuMinuman("Jus Jambu","Jus Jambu Merah tanpa gula",8500,10)
mnm2 = MenuMinuman("\nJus Alpukat Ori","Jus Alpukat dengan tambahan air gula merah",15000,20)
mnm3 = MenuMinuman("\nJus Alpukat Xtra Milk","Jus Alpukat dengan campuran susu coklat dan taburan kepingan choco",15000,15)
mnm4 = MenuMinuman("\nRed & Smooth","Smoothie pisang susu dengan stroberi",17500,17)
mnm5 = MenuMinuman("\nGilus Mix","Kopi Hitam New Zealand dengan tambahan Gula Aren",12000,"Habis")
mnm6 = MenuMinuman("\nMilk Tea Boba's","Minuman penyegar gerah yang mengandung campuran teh,susu, dan boba",15000,7)

pilihan_minuman = [mnm1,mnm2,mnm3,mnm4,mnm5,mnm6]
print("Daftar Menu Healthy & Fruits")

for mn in pilihan_minuman:
    mn.Keterangan()