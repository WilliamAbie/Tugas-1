# Implementasi Overloading

class Mahasiswa:
    def __init__(self,nama,nim):
        self.nama = nama
        self.nim = nim

    def tampilMahasiswa(self):
        print("Nama: {}\nNIM: {}".format(self.nama,self.nim))

    # Metode Overloading
    def hitungSKS(self,jmlsks = None,sks = None):
        if jmlsks != None and sks != None:
            total = jmlsks + sks
            print("Total SKS: ",total)
        else:
            total = jmlsks
            print("Total SKS: ", total)

mhs1 = Mahasiswa("William",5210411353)
mhs2 = Mahasiswa("Udin",5200320320)
mhs1.tampilMahasiswa()
mhs2.tampilMahasiswa()
mhs1.hitungSKS(80,34)
mhs2.hitungSKS(80)