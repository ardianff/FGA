import random
angkaAcak = random.randint(1, 50)
nama_pemain = input("Masukkan Namamu : ")
print('\n'*2)
print('^' * 60)
print('Halo %s, Kami telah menyimpan satu angka, silakan tebak!'%(nama_pemain))
print('^' * 60)
batas = 10
print(f'\n{nama_pemain}, Kamu Memiliki {batas} Percobaan')
for percobaan in range(batas):
  jawaban = int(input(f'\n[Percobaan Ke-{percobaan + 1}] Silahkan Masukkan Angka Tebakan: '))
  if jawaban == angkaAcak:
    print('Selamat %s Tebakanmu, angka %d benar !!!'%(nama_pemain,jawaban))
    break
  else:
    if jawaban > angkaAcak: 
      print('%s Tebakanmu, angka %d terlalu besar !!!'%(nama_pemain,jawaban))
    else: 
      print('%s Tebakanmu, angka %d terlalu kecil !!!'%(nama_pemain,jawaban))
else:
  print(f'\nSayang sekali, {nama_pemain} kamu sudah salah menebak sebanyak {batas}x!\nJawaban yang benar adalah angka {angkaAcak}')