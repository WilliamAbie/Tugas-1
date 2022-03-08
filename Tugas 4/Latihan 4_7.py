#=======================
# Nama  : William Abie
# NPM   : 5210411353
#=======================

# Fungsi Private dan Public

class Pegawai:
    __nama = ""
    __alamat = ""
    __gaji = 0

    def __init__(self,nama,alamat):
        self.__nama = nama
        self.__alamat = alamat

    def __hitungGaji(self):
        upahLembur = 20000
        gajiPokok = 2000000
        jumLembur = int(input("Total Jam Lembur yang sudah anda lakukan: "))
        self.__gaji = (upahLembur*jumLembur)+gajiPokok

    def tampilDetail(self):
        print("\n===== Menghitung dan Tampilkan detail Gaji Pegawai =====")
        print("Nama      : ",self.__nama)
        print("Alamat    : ",self.__alamat)
        self.__hitungGaji()
        print("Total Gaji: ",self.__gaji)

pgw1 = Pegawai("William Abie","Jambi")
pgw1.tampilDetail()

pgw2 = Pegawai("Nurhan Udin","Bengkulu")
pgw2.tampilDetail()
