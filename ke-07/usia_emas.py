from datetime import date
mulai = True
while mulai :
    thn_skrg = date.today()
    print("Tahun ini  : ", thn_skrg.year)
    nama =input("Masukkan Nama Anda : ")
    input_umur = input("Masukkan Umur Anda Sekarang : ")
    try : 
        umur = int(input_umur)
    except : 
        print("Masukkan Angka Umurmu Dong Jangan Yang Lain")
    else :     
        if umur <=50 : 
            umur_now = 50 - umur
            thn_emas = umur_now + thn_skrg.year
            umur_emas = thn_emas-thn_skrg.year+umur
            print("Nama Anda %s, Anda Berusia %d tahun. Pada tahun %d anda akan berusia %d tahun." %(nama,umur,thn_emas,umur_emas))
        else : 
            umur_now = umur - 50
            thn_emas = thn_skrg.year - umur_now
            umur_emas = thn_emas-thn_skrg.year+umur

            print("Nama Anda %s, Anda Berusia %d tahun. Pada tahun %d anda berusia %d tahun." %(nama,umur,thn_emas,umur_emas))
    break