# Multilevel Inheritance
class Mahasiswa:
    def __init__(self,nama,nim):
        self.nama = nama
        self.nim  = nim

class Siswa1(Mahasiswa):
    def __init__(self,nama,nim,kelas):
        self.nama  = nama
        self.nim   = nim
        self.kelas = kelas

class Siswa2(Siswa1):
    def __init__(self,nama,nim,kelas):
        self.nama = nama
        self.nim  = nim
        self.kelas= kelas

mhs1 = Mahasiswa('William',10001)
mhs2 = Siswa1('Udin',10002,'H')
mhs3 = Siswa2('Manjur',10003,'I')

print(mhs1.nama,mhs1.nim)
print(mhs2.nim,mhs2.kelas)
print(mhs3.nama,mhs3.kelas)