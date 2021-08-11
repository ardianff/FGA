import getpass

nama="Ardian"
user_name = "ardian"
pass_user = "123456"

get_user = input("Masukkan Username Anda : ")
get_pass = getpass.getpass()

if get_user.lower() == user_name and get_pass == pass_user :
    print ("Anda Berhasil Login, Selamat Datang %s"%(nama))
elif get_user.lower() != user_name and get_pass == pass_user :
    print ("Mohon Maaf Username Yang Anda Masukkan Salah\nSilahkan Periksa Kembali")
elif get_user.lower() == user_name and get_pass != pass_user :
    print ("Mohon Maaf Password Yang Anda Masukkan Salah\nSilahkan Periksa Kembali")
else :
    print ("Mohon Maaf Username dan Password Yang Anda Masukkan Salah\nSilahkan Periksa Kembali")