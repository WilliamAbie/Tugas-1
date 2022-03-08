class Segitiga:
    def __init__(self,alas,tinggi):
        self.alas = alas
        self.tinggi = tinggi
        self.luas = 0.5 * tinggi * alas

segitiga_besar = Segitiga(100,30)
print("Alasnya sebesar : {}".format(segitiga_besar.alas))
print("Tingginya sebesar : {}".format(segitiga_besar.tinggi))
print("Luasnya sebesar : {}".format(segitiga_besar.luas))