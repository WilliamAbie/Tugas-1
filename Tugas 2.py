# ======================
# Nama  : William Abie 
# NPM   : 5210411353    
# ======================

# Penambahan string ditengah
exp = "Aku sayang ibu"
exp2 = exp[:11] + "ayah dan" + exp[10:]
# NB : (:x) berarti kalimat dari 0 sampai x akan diprint
# NB : (x:) berarti kalimat dari x sampai akhir akan diprint
print(exp2)


# Menghapus string
exp = "--"
print(exp)


# Uppercase dan Lowercase string menggunakan upper() dan lower()
tes = "Kelas Informatika H"
print(tes)
print(tes.lower())
print(tes.upper())


# Menghapus blank dan spasi diawal menggunakan strip()
abc = "    Halo semuanya    "
print(abc)
print(abc.strip())


# Menghitung jumlah karakter string menggunakan len()
print(len(tes)) # (tes) merujuk kepada variable tes diatas


# Menggabungkan string dari 2 variabel/ lebih
a = "Bagaimana bila aku "
b = "tidak baik-baik saja"
print(a+b)


# Mencari huruf menggunakan index()
print(a.index("n"))


# Mengubah kalimat menggunakan replace()
print(a.replace("Bagaimana","Gimana"))


# Penggunaan %s
x = "Satu"
y = "Dua"
print("Anak Pak Dodi ada %s, dan anak Bu Mira ada %s"%(x,y))


# Memisahkan string menggunakan split()
print(tes.split())


# Meng-input angka
def input():   # Untuk bagian ini saya menggunakan def agar hasilnya tidak perlu diinput dahulu
    p = int(input("Masukkan angka : "))
    q = int(input("Masukkan angka : "))
    hasil = p**q
    print("Hasil dari %s pangkat %s adalah : "%(p,q),hasil)


# list
cnth = [0,1,2,3,4,5,6,7,8,9]
print (cnth)
print (cnth[4])
print (cnth[:4])
print (cnth[4:]) 
print (cnth[2:6]) # Range
print (cnth[-6])  # Dibaca dari belakang


# Menambah list menggunakan append()
r = cnth.append(10)
print(cnth)


# Menambah string kedalam menggunakan method extend()
abcd = "Halo"
cnth.extend("Halo")
print(cnth)


# Menghapus elemen menggunakan del
del cnth[5]
print(cnth)


# Menghapus elemen menggunakan fungsi remove()
cnth.remove(7)
print(cnth)


# Menghapus menggunakan fungsi pop()
cnth.pop()
'o'
print(cnth)


# Ascending menggunakan sort()
no = [60,50,30,90,70]
no.sort()
print(no)


# Ascending menggunakan sorted()
no2 = sorted(no)
print(no2)


# Descending menggunakan sort() dan reverse()
no.reverse()
print(no)


# Menentukan nilai min dan max
print (min(no))
print (max(no))


# Menggunakan dictionary
d = {1:100,2:200,3:300,4:400,5:500}
print(d)


# Mencari dictionary menggunakan key
print(d.keys())
print(d[3])


# Melihat nilai dictionary
print(d.values())


# Menghapus nilai dictionary menggunakan key
del d[2]
print(d)


# Menyalin dictionary d ke e
e = d.copy()
print(e)


# Menghapus seluruh elemen dictionary menggunakan fungsi clear()
d.clear()
print(d)


# Melihat jumlah dictionary yang ada didalam variabel
print(len(d))


# Membaca tuple dengan bracket
t =(100,200,300,400)
print(t[0])


# Mencari indeks dari 100 di tuple
n = t.index(100)
print(n)


# Menghitung berapa banyak jumlah satu elemen dalam tuple
m = t.count(200)
print(m)


# Set
k = [10,20,30,40,10]
l = set(k)
print(l)


# Menambah elemen menggunakan add() dan update()
l.add(50)
print(l)

o = {"a","b"}
l.update(o)
print(l)


# Menghapus elemen di suatu set menggunakan discard() dan clear()
l.discard("a")
print(l)

l.clear()
print(l)


# Mengcopy dari satu variabel ke variabel lain
tess = {10,20,30}
set1 = tess.copy()
print(set1)


# Mencari irisan menggunakan intersection()
abcde = {20,30,40}
print(set1.intersection(abcde))


# Mencari selisih menggunakan difference()
print(set1.difference(abcde))


# Menggabungkan kedua set dengan union()
print(set1.union(abcde))


# Membuat elemen set tidak dapat diubah lagi/menjadi kunci
frozenset(abcde)
print(abcde)