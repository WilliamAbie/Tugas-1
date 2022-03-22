# Implementasi Overloading

class Pegawai:
    jumlah = 0

    def __init__(self,nama,gaji):
        self.nama = nama
        self.gaji = gaji
        Pegawai.jumlah += 1

    def tampilJumlah(self):
        print("Total Pegawai:", Pegawai.jumlah)

    def tampilPegawai(self):
        print("Nama: {}\nGaji: {} juta".format(self.nama,self.gaji))

    # Metode Overloading
    def tunjangan(self,istri=None,anak=None):
        if istri != None and anak != None:
            total = anak + istri
            print("Tunjangan anak dan Istri: {} juta".format(total))

        else:
            total = istri
            print("Tunjangan Istri: {} juta".format(total))

pgw1 = Pegawai("William",10)
pgw2 = Pegawai("Udin",7)

pgw1.tampilPegawai()
pgw1.tunjangan(6.5,3)
pgw2.tampilPegawai()
pgw2.tunjangan(6.5)

print("Total Pegawai %d" % Pegawai.jumlah)
rataGaji = (pgw1.gaji + pgw2.gaji)/Pegawai.jumlah
print("Rata-rata gaji: {} juta".format(rataGaji))