#=======================
# Nama  : William Abie
# NPM   : 5210411353
#=======================
class Buku:
    def __init__(self,judul,pengarang,tahun_terbit,penerbit):
        self.judul        = judul
        self.pengarang    = pengarang
        self.tahun_terbit = tahun_terbit
        self.__penerbit   = penerbit

    def Keterangan(self):
        print("Buku {} karangan {} pertama kali diterbitkan tahun {} oleh {}".format(self.judul,self.pengarang,self.tahun_terbit,self.__penerbit))

buku1 = Buku("Tenggelamnya Kapal Van der Widjk","HAMKA",1938,"PT. Gramedia")
buku2 = Buku("\nEl Ingenioso Hidalgo Don Quixote de la Mancha","Miguel de Cervantes",1605,"Fransisco de Robles")
buku3 = Buku("\nBirds of America","John James Audubon",1827,"John James Audubon")

buku = [buku1,buku2,buku3]
for x in buku:
    x.Keterangan()