import datetime

prov = 'PROVINSI JAWA TENGAH'
print(prov.center(50))
kota = 'KOTA SEMARANG'
print(kota.center(50))
print('\n')
NIK = str(3304232201070001)
print('NIK \t\t\t: '+ NIK)
nama = 'ARDIAN FERDY FIRMANSYAH'
print('Nama \t\t\t: '+ nama)
tempat_lahir = 'semarang'
tgl_lahir = datetime.date(1999,2,23)
print('Tempat/Tanggal Lahir \t: '+tempat_lahir.upper()+', '+ tgl_lahir.strftime("%d-%m-%Y"))
print('Jenis Kelamin \t\t: LAKI-LAKI \t\tGol Darah : -')
alamat = 'Jl. Puri Dinar Elok'
print('Alamat \t\t\t: '+alamat.upper())
rt = '005'
rw = '022'
print('\tRT/RW \t\t: '+rt+'/'+rw)
print('\tKel/Desa \t: METESEH')
print('\tKecamatan \t: TEMBALANG')
print('Status Perkawinan \t: BELUM KAWIN')
print('Perkerjaan  \t\t: PELAJAR/MAHASISWA')
kewarnegaraan = 'WNI'
print('Kewarnegaraan \t\t: '+kewarnegaraan)
print('Berlaku Hingga \t\t: SEUMUR HIDUP')
print('\t\t\t'+kota.rjust(50))
tanggal_cetak = (datetime.date(2020,7,13))
print('\t\t\t'+tanggal_cetak.strftime("%d-%m-%Y").rjust(50))