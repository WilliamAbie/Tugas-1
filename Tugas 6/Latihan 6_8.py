# Implementasi Overriding pada class Mahasiswa

class Mahasiswa:
    def __init__(self,nama,nim):
        self.nama = nama
        self.nim = nim

    # Metode yang akan di overriding
    def tampilMahasiswa(self):
        print("Nama: {}\nNIM: {}".format(self.nama,self.nim))

    def hitungSKS(self,jmlsks = None,sks = None):
        if jmlsks != None and sks != None:
            total = jmlsks + sks
            print("Total SKS: ",total)
        else:
            total = jmlsks
            print("Total SKS: ", total)

class Mahasiswa2(Mahasiswa):
    def __init__(self,alamat,email):
        self.alamat = alamat
        self.email = email

    # Metode Overriding
    def tampilMahasiswa(self):
        print("Alamat: {}\nNIM: {}".format(self.alamat,self.email))

mhs1 = Mahasiswa("William",5210411353)
mhs2 = Mahasiswa2("Jln. Merangin","williamabie63@gmail.com")
mhs1.tampilMahasiswa()
mhs2.tampilMahasiswa()