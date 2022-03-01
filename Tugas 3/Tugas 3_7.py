class Mahasiswa:
    def __init__(self,nama,nim,prodi,thn_masuk):
        self.nama       = nama
        self.nim        = nim
        self.prodi      = prodi
        self.thn_masuk  = thn_masuk

m1   = Mahasiswa("Udin","10120371","Sistem Informasi",2020)
m2   = Mahasiswa("William","5210411353","Informatika",2021)
m3   = Mahasiswa("Anug","10230023","Kedinasan",2021)

mahasiswa = [m1,m2,m3]
for x in mahasiswa:
    teks = "{} adalah mahasiswa {} angkatan {} dengan NIM {}".format(x.nama,x.prodi,x.thn_masuk,x.nim)
    print(teks)