#fungsi mencari luas persegi panjang 
def luaspersegipanjang (panjang, lebar):
    return panjang*lebar

panjang=int(input("masukan panjang :"))
lebar=int(input("masukan lebar :"))
 
hasil_luas=luaspersegipanjang(panjang,lebar)

#nilai luas jika panjang =10, dan lebar =5
hasil_luas = luaspersegipanjang(panjang, lebar)
print ("hasil luas adalah",hasil_luas)

# fungsi mencari luas lingkaran
def luaslingkaran(panjang,lebar):
    return (panjang+lebar)
jari_jari = float(input("masukan jari-jari lingkaran: "))
luas = (jari_jari ** 2)

print("luas lingkaran adalah:", luas)

def fungsiku (x) :
    return (2*x**2 + 3*x - 10) - x
x = int(input("masukkan nilai x:"))
hasil_fx = fungsiku(x)
print(hasil_fx)
