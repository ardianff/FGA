import os

def persegi() :
    print("Anda Akan Menghitung Luas dan Keliling Persegi")
    sisi= float(input('Masukkan Sisinya : '))
    kel_persegi = 4*sisi
    luas_persegi = sisi*sisi
    print("Kelilingnya adalah ",str(kel_persegi), "dan luasnya adalah ",str(luas_persegi))
    pilih=(input("Apakah Anda ingin menghitung keliling dan luas bangun datar yang lain ? (Y/T) "))
    if(pilih=='Y' or pilih=='y') :
        os.system('cls')
        persegi_panjang()  
    elif(pilih=='T' or pilih=='t') :
        os.system('cls')
        print("Anda Keluar Dari Sistem")
        exit()
    return pilih
def persegi_panjang () : 
    print("Anda Akan Menghitung Luas dan Keliling Persegi Panjang")
    p= float(input('Masukkan Panjangnya : '))
    l= float(input('Masukkan Lebarnya : '))
    kel_persegipanjang = 2*(p+l)
    luas_persegipanjang = p*l
    print("Kelilingnya adalah ",str(kel_persegipanjang), "dan luasnya adalah ",str(luas_persegipanjang))
    pilih=(input("Apakah Anda ingin menghitung keliling dan luas bangun datar yang lain ? (Y/T) "))
    if(pilih=='Y' or pilih=='y') :
        os.system('cls')
        persegi()    
    elif(pilih=='T' or pilih=='t') :
        os.system('cls')
        print("Anda Keluar Dari Sistem")
        exit()
    return pilih

choose=3
while choose !=0 : 
    print("Program Menghitung Luas Dan Keliling Bangun Datar")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Keluar")
    x = int(input('Masukkan Pilihan (1-3) : '))
    if (x==1) :
        pilih=persegi()
    elif (x==2) :
        pilih=persegi_panjang()

    elif (x==3) :
        os.system('cls')
        print("Anda Keluar Dari Sistem")
        exit()
    else :
        print("Pilihan tidak diketahui/salah")