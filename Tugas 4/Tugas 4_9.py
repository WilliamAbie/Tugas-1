class Mahasiswa:
    def __init__(self,nama,nim,prodi,thn_masuk,univ):
        self.nama       = nama
        self.nim        = nim
        self.prodi      = prodi
        self.thn_masuk  = thn_masuk
        self.__univ       = univ

    def Keterangan(self):
        print("{} adalah mahasiswa {} dari {} angkatan {} dengan NIM {}".format(self.nama,self.prodi,self.__univ,self.thn_masuk,self.nim))

m1   = Mahasiswa("Udin","10120371","Sistem Informasi",2020,"Universitas Teknologi Yogyakarta")
m2   = Mahasiswa("\nWilliam","5210411353","Informatika",2021,"Universitas Teknologi Yogyakarta")
m3   = Mahasiswa("\nAnug","10230023","Kedinasan",2021,"Universitas Negeri Semarang")

mahasiswa = [m1,m2,m3]
for x in mahasiswa:
    x.Keterangan()