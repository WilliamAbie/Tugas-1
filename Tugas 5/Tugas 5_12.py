#========================
# Nama : William Abie
# NPM  : 5210411353
#========================
# Multiple inheritance
class ComputerPart:
    def __init__(self,pabrikan,nama):
        self.pabrikan = pabrikan
        self.nama     = nama

class ComputerPart2:
    def __init__(self,jenis,harga):
        self.jenis    = jenis
        self.harga    = harga

class Processor(ComputerPart,ComputerPart2):
    def __init__(self,pabrikan,nama,harga,jumlah_core,speed):
        ComputerPart.__init__(self,pabrikan,nama)
        ComputerPart2.__init__(self,"Processor",harga)
        self.jumlah_core = jumlah_core
        self.speed       = speed

class RandomAccessMemory(ComputerPart,ComputerPart2):
    def __init__(self,pabrikan,nama,harga,kapasitas):
        ComputerPart.__init__(self,pabrikan,nama)
        ComputerPart2.__init__(self,"RAM",harga)
        self.kapasitas = kapasitas

class HardDiskSATA(ComputerPart,ComputerPart2):
    def __init__(self,pabrikan,nama,harga,kapasitas,rpm):
        ComputerPart.__init__(self,pabrikan,nama)
        ComputerPart2.__init__(self,"SATA",harga)
        self.kapasitas = kapasitas
        self.rpm       = rpm

p = Processor("AMD","Ryzen 3 3250U",3500000,2,"2.6 GHz")
r = RandomAccessMemory("Corsaire","DDR4 SODIMM PC19200/2400 MHz",990000,"8 GB")
hdd = HardDiskSATA("Toshiba","HDD 2.5 inch",295000,"500 GB",7200)

part = [p,r,hdd]
for x in part:
    print('\n{} {} produksi {} berharga {}'.format(x.jenis,x.nama,x.pabrikan,x.harga))