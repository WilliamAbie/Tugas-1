# Hierarichal inheritance
class Mahasiswa:
    def __init__(self,nama,nim):
        self.nama = nama
        self.nim  = nim

class Siswa1(Mahasiswa):
    def __init__(self,nama,nim):
        self.nama = nama
        self.nim  = nim

    def detSiswa1(self):
        x = input("Masukkan alamat anda : ")
        print(self.nama,'alamat',x)

class Siswa2(Mahasiswa):
    def __init__(self,nama,nim):
        self.nama = nama
        self.nim  = nim

    def detSiswa2(self):
        x = input("Masukkan jurusan anda : ")
        print(self.nama,'jurusan',x)

mhs1 = Siswa1('William','5210411353')
mhs2 = Siswa2('Udin','10242121')

print(mhs1.nim)
mhs1.detSiswa1()
print(mhs2.nim)
mhs2.detSiswa2()