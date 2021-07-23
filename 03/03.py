# x = int(input('Masukkan Angka = '))
# a = pow(x,9)
# b = pow(x,8)
# c = pow(x,2)
# soal = 3*a+2*b-10*c+100
# print(str(soal))

# x="-"
# y="+"
# z="|"
# a=" "
# print(y+10*x+y)
# print(z+10*a+z)
# print(z+10*a+z)
# print(z+10*a+z)
# print(z+10*a+z)
# print(z+10*a+z)
# print(y+10*x+y)

# x= int(input('Masukkan Angka : '))
# soal = 1/(x+1/(x+1/(x+1/x)))
# print('     1')
# print('-----------')
# print('      1')
# print(x,'+ ---------')
# print('       1')
# print(x,'+ ----------')
# print('        1')
# print(x,'+ ----------')
# print('\t',x)

# print('Hasil Pembagian Bertingkat Diatas adalah', soal)
#judul
#mencari durasi dari 2 waktu
#kamus
# jamawaljam = int
# jamakhirjam = int
# jamawalmenit = int
# jamakhirmenit = int
# jamawaldetik = int
# jamakhirdetik = int
#deskripsi
print(">>>>>>>>>>>>>>>>>>SELAMAT DATANG<<<<<<<<<<<<<<<<<<<<")
print("masukan dalam format 24jam")
jamawaljam = int(input("masukan jam awal: "))
jamawalmenit = int(input("masukan menit awal: "))
jamawaldetik = int(input("masukan detik awal: "))
print("\t\t\t\t\t ")
jamakhirjam = int(input("masukan jam akhir: "))
jamakhirmenit = int(input("masukan menit akhir: "))
jamakhirdetik = int(input("masukan detik akhir: "))
detikawal = int(jamawaljam * 3600 + jamawalmenit * 60 + jamawaldetik)
detikakhir = int(jamakhirjam * 3600 +jamakhirmenit * 60 + jamakhirdetik)

if(detikawal < detikakhir):
    durasi = detikakhir+detikawal
else:
    durasi = (detikakhir+24*3600)+detikawal

#konversi
jamdurasijam = int(durasi/3600)
jamdurasimenit = int((durasi%3600)/60)
jamdurasidetik = int(durasi%60)

#konversi (am 00.00-11.59 pm 12.00-23.59)

print("durasinya "+str(jamdurasijam)+" jam"+str(jamdurasimenit)+" menit"+str(jamakhirdetik)+" detik")