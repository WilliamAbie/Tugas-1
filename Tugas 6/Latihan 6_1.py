# Polymorphism : Contoh simple menggunakan fungsi len

print(len('William Abie'))
print(len([0,1,2,6,4,7,9]))

# Hasil run (output) dari tes diatas adalah :
# 12 (William Abie)
# 7 [0,1,2,6,4,7,9]

# Menggunakan kelas
class Indonesia:
    def ibukota(self):
        print('Jakarta adalah ibukota negara Indonesia')

class Britain:
    def ibukota(self):
        print('London adalah ibukota negara Inggris')

negara1 = Indonesia()
negara2 = Britain()

for country in (negara1,negara2):
    country.ibukota()