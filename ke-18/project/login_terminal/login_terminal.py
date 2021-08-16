import getpass, os, time,sys
def login():
    batas = 3
    for a in range(batas):
        print("*"*25)
        print("\tLogin User")
        print("*"*25)
        get_user = input("Masukkan Username Anda : ")
        get_pass = getpass.getpass()
        sukses = False
        file = open('D:\Kuliah\FGA\ke-18\project_login\login_terminal\database.txt',"r")
        for i in file:
            nama,username,password = i.split(",")
            password = password.strip()
            proses()
            if (get_user == username) and (get_pass == password) :
                sukses = True
                break
        if (sukses) :
            print ("\nAnda Berhasil Login, Selamat Datang %s"%(nama))
            time.sleep(5)
            opsi = input("Apakah Anda Ingin Kembali Ke Menu Utama ? (Y/N) ")
            if opsi.lower() == 'y' :
                print ("\nAnda Akan Dialihkan Ke Menu Utama Tunggu Sebentar")
                time.sleep(2)
                os.system("cls")
                pilih()
            elif opsi.lower() == "n" :
                time.sleep(2)
                print ("\nAnda Akan Tetap Berada Di Halaman Ini")
                time.sleep(120)
                exit()
            else :
                print ("\nMohon Pilihan Tidak Tersedia")
            break
        else :
            print ("\nMohon Maaf Username dan Password Yang Anda Masukkan Salah\nSilahkan Periksa Kembali")
            a -=1
            time.sleep(2)
            os.system("cls")
    else :
        print ("Maaf Anda Sudah Salah Memasukkan Username/Password Sebanyak %s kali"%(batas))   
def register():
    print ("")
    print("*"*35)
    print("\tForm Registrasi User")
    print("*"*35)
    nama = input("Masukkan Nama Anda : ")
    username = input("Masukkan Username Anda : ")
    password = getpass.getpass()
    simpan(nama,username,password)
    print("Data Berhasil Disimpan")
    time.sleep(2)
    opsi = input("Apakah Anda Ingin Kembali Ke Menu Utama ? (Y/N) ")
    if opsi.lower() == 'y' :
        print ("\nAnda Akan Dialihkan Ke Menu Utama Tunggu Sebentar")
        time.sleep(2)
        os.system("cls")
        pilih()
    elif opsi.lower() == "n" :
        time.sleep(2)
        print ("\nProgram Akan Kami Hentikan, Terima Kasih Telah Melakukan Registrasi Pada Sistem Ini")
    else :
        print ("\nMohon Pilihan Tidak Tersedia, Anda Akan Kami ALihkan Ke Menu Utama")
        time.sleep(2)
        os.system("cls")
        mulai()
def simpan(nama,username,password):
    file = open('D:\Kuliah\FGA\ke-18\project_login\login_terminal\database.txt',"a")
    file.write("\n"+nama+","+username+","+password)

def mulai () :
    print("\nSelamat Datang Di Sistem\nSilahkan Masukkan Kata (Reg) Untuk Register User Baru | (Login) Untuk Login User Ke Sistem | (Exit) Untuk Keluar Dari Program")
    pilih()
def pilih ():
    opsi = input("Masukkan Kata (Reg) atau (Login) atau (Exit) : ")
    if opsi.lower() == "reg":
        print ("Anda Memilih Form Registrasi User\nSilahkan Tunggu Sebentar Anda Akan Di Alihkan Ke Form Registrasi User")
        time.sleep(2)
        os.system("cls")
        register()
    elif opsi.lower() == "login":
        print ("Anda Memilih Form login User\nSilahkan Tunggu Sebentar Anda Akan Di Alihkan Ke Form Login User")
        time.sleep(2)
        os.system("cls")
        login()
    elif opsi.lower() == "exit" :
        print ("Anda Telah Memilih Exit Program")
        time.sleep(2)
        os.system("cls")
        print("Terima Kasih Telah Menggunakan Program Ini Sampai Jumpa")
        time.sleep(2)
        exit()
    else :
        print("Mohon Maaf Pilihan Tidak Tersedia")
        time.sleep(2)
        os.system("cls")
        mulai()
import sys,time
def proses():
    try:
        L="/-\\|"
        for q in range(20):
            time.sleep(0.1)
            sys.stdout.write("\rMemeriksa Data User " +L[q % len(L)]+"")
            sys.stdout.flush()
    except:
        os.system("cls")
        exit()
mulai()
