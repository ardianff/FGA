import bangunruang
print("----- Menghitung Keliling, Luas, Volume Kubus -----")
x = float(input('Masukkan Sisi Kubusnya : '))
kel_kubus = bangunruang.keliling_kubus(x)
print ("Keliling Bangun Kubus adalah" ,kel_kubus)
ls_kubus = bangunruang.luas_kubus(x)
print("Luas Permukaan Bangun Kubus Adalah ",ls_kubus)
vol_kubus = bangunruang.volume_kubus(x)
print("Volume Bangun Kubus Adalah ",vol_kubus)
print("")
print("----- Menghitung Keliling, Luas, Volume Balok -----")
p = float(input('Masukkan Panjang Baloknya : '))
l = float(input('Masukkan Lebar Baloknya : '))
t = float(input('Masukkan Tinggi Baloknya : '))
kel_balok = bangunruang.keliling_balok(p,l,t)
print ("Keliling Bangun Balok adalah" ,kel_balok)
ls_balok = bangunruang.luas_balok(p,l,t)
print ("Luas Bangun Balok adalah" ,ls_balok)
vol_balok = bangunruang.volume_balok(p,l,t)
print ("Volume Bangun Balok adalah" ,vol_balok)
print ("")
print("----- Menghitung Keliling, Luas, Volume Bola -----")
r = float(input('Masukkan Jari-Jari Bolanya : '))
kel_bola = bangunruang.keliling_bola(r)
print ("Keliling Bangun Bola adalah" ,round(kel_bola,3))
ls_bola = bangunruang.luas_bola(r)
print ("Luas Permukaan Bangun Bola adalah" ,round(ls_bola,3))
vol_bola = bangunruang.volume_bola(r)
print ("Volume Bangun Bola adalah" ,round(vol_bola,3))


