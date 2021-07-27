start = True
while start : 
    input_umur = input("Masukkan Umur Anda : ")
    try:
        umur = int(input_umur)
    except : 
        print("Masukkan Angka Umurmu Dong Jangan Yang Lain")
    else :
        if umur < 6 : 
            print("Anda Masuk Kategori Balita")
        elif umur >=6 and umur <=12 : 
            print("Anda Masuk Kategori Anak-Anak")
        elif umur >12 and umur <=20 : 
            print("Anda Masuk Kategori Remaja")
        elif umur >20 and umur <=35 : 
            print("Anda Masuk Kategori Dewasa")
        else :
            print("Anda Masuk Kategori Orang Tua")
    start = False
 