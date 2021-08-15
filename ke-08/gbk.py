from time import sleep
import os

while True:
    pemain1 = input('Masukkan Nama Pemain 1 : ')
    pilihan_pemain1 = input('Giliran %s Memilih\nMasukkan Pilihan ---->\tGunting\t\tBatu\t\tKertas\n : '%(pemain1))
    sleep(1)
    os.system("cls")
    pemain2 = input('Masukkan Nama Pemain 2 : ')
    pilihan_pemain2 = input('Giliran %s Memilih\nMasukkan Pilihan ---->\tGunting\t\tBatu\t\tKertas\n : '%(pemain2))
    sleep(1)
    os.system("cls")

    if pilihan_pemain1.lower() == pilihan_pemain2.lower(): 
        print(f'Pilihan {pemain1} adalah {pilihan_pemain1.capitalize()}')
        print(f'Pilihan {pemain2} adalah {pilihan_pemain2.capitalize()}')
        print('\nWaduh Hasilnya Seri\n\n')
    #bagian pemain1 menang
    elif pilihan_pemain1.lower() == 'batu' and pilihan_pemain2.lower() == 'gunting' : 
        print(f'Pilihan {pemain1} adalah {pilihan_pemain1.capitalize()}')
        print(f'Pilihan {pemain2} adalah {pilihan_pemain2.capitalize()}')
        print('\nHoree %s Menang dan %s Kalah\n\n'%(pemain1, pemain2))
    elif pilihan_pemain1.lower() == 'kertas' and pilihan_pemain2.lower() == 'batu' : 
        print(f'Pilihan {pemain1} adalah {pilihan_pemain1.capitalize()}')
        print(f'Pilihan {pemain2} adalah {pilihan_pemain2.capitalize()}')
        print('\nHoree %s Menang dan %s Kalah\n\n'%(pemain1, pemain2))
    elif pilihan_pemain1.lower() == 'gunting' and pilihan_pemain2.lower() == 'kertas' : 
        print(f'Pilihan {pemain1} adalah {pilihan_pemain1.capitalize()}')
        print(f'Pilihan {pemain2} adalah {pilihan_pemain2.capitalize()}')
        print('\nHoree %s Menang dan %s Kalah\n\n'%(pemain1, pemain2))
    #bagian pemain2 menang
    elif pilihan_pemain1.lower() == 'gunting' and pilihan_pemain2.lower() == 'batu' : 
        print(f'Pilihan {pemain1} adalah {pilihan_pemain1.capitalize()}')
        print(f'Pilihan {pemain2} adalah {pilihan_pemain2.capitalize()}')
        print('\nHoree %s Menang dan %s Kalah\n\n'%(pemain2, pemain1))
    elif pilihan_pemain1.lower() == 'batu' and pilihan_pemain2.lower() == 'kertas' : 
        print(f'Pilihan {pemain1} adalah {pilihan_pemain1.capitalize()}')
        print(f'Pilihan {pemain2} adalah {pilihan_pemain2.capitalize()}')
        print('\nHoree %s Menang dan %s Kalah\n\n'%(pemain2, pemain1))
    elif pilihan_pemain1.lower() == 'kertas' and pilihan_pemain2 == 'batu' : 
        print(f'Pilihan {pemain1} adalah {pilihan_pemain1.capitalize()}')
        print(f'Pilihan {pemain2} adalah {pilihan_pemain2.capitalize()}')
        print('\nHoree %s Menang dan %s Kalah\n\n'%(pemain2, pemain1))
    else :
        print('Data yang dimasukkan salah \n\n')
    break