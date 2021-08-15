jam_mulai = int(input('Masukkan Jam Mulai : '))
menit_mulai = int(input('Masukkan Menit Mulai : '))
menit_durasi = int(input('Masukkan Menit Durasi : '))

detik_mulai = (jam_mulai*3600)+(menit_mulai*60)
detik_durasi = (menit_durasi*60)

durasi = detik_mulai+detik_durasi
durasijam = int(durasi//3600)
sisa = durasi%3600
durasimenit = int(sisa//60)
print("Outputnya "+str(durasijam)+":"+str(durasimenit))