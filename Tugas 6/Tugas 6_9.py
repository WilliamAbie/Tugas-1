#========================
# Nama : William Abie
# NPM  : 5210411353
#========================
# Implementasi Overriding pada class ComputerPart

class ComputerPart:
    def __init__(self,pabrikan,nama,jenis,harga):
        self.pabrikan = pabrikan
        self.nama     = nama
        self.jenis    = jenis
        self.harga    = harga

    def harga(self):
        print("Harga dari setiap komponen sangatlah bervariasi")

class Processor(ComputerPart):
    def __init__(self,pabrikan,nama,harga,jumlah_core,speed):
        super().__init__(pabrikan,nama,"Processor",harga)  
        self.jumlah_core = jumlah_core
        self.speed       = speed

    def spek(self): # Metode Overriding
        print("Jumlah core dari Prosessor ini terdapat {}".format(self.jumlah_core))

class RandomAccessMemory(ComputerPart):
    def __init__(self,pabrikan,nama,harga,kapasitas):
        super().__init__(pabrikan,nama,"RAM",harga)
        self.kapasitas = kapasitas

    def spek(self): # Metode Overriding
        print("Kapasitas dari RAM ini {}".format(self.kapasitas))

class HardDiskSATA(ComputerPart):
    def __init__(self,pabrikan,nama,harga,kapasitas,rpm):
        super().__init__(pabrikan,nama,"SATA",harga)
        self.kapasitas = kapasitas
        self.rpm       = rpm

    def spek(self): # Metode Overriding
        print("HardDisk tipe ini memiliki kecepatan rotasi {}/menit".format(self.rpm))

p = Processor("AMD","Ryzen 3 3250U",3500000,2,"2.6 GHz")
r = RandomAccessMemory("Corsaire","DDR4 SODIMM PC19200/2400 MHz",990000,"8 GB")
hdd = HardDiskSATA("Toshiba","HDD 2.5 inch",295000,"500 GB",7200)

part = [p,r,hdd]
for x in part:
    print('\n{} {} produksi {} berharga {}'.format(x.jenis,x.nama,x.pabrikan,x.harga))
    # Pemanggilan Overriding
    x.spek()
