class Buku:
    def __init__(self,judul,pengarang,tahun_terbit):
        self.judul        = judul
        self.pengarang    = pengarang
        self.tahun_terbit = tahun_terbit

buku1 = Buku("Tenggelamnya Kapal Van der Widjk","HAMKA",1938)
buku2 = Buku("El Ingenioso Hidalgo Don Quixote de la Mancha","Miguel de Cervantes",1605)
buku3 = Buku("Birds of America","John James Audubon",1827)

buku = [buku1,buku2,buku3]
for x in buku:
    t    = "Buku {} karangan {} pertama kali diterbitkan tahun {}".format(x.judul,x.pengarang,x.tahun_terbit)
    print (t)