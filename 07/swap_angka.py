x = input('Masukkan Angka Pertama : ')
y = input('Masukkan Angka Kedua : ')
print('')
print('Angka Pertama Sebelum di Swap : {}'.format(x))
print('Angka Kedua Sebelum di Swap : {}'.format(y))

if x >= y :
    temp = x
    x = y
    y = temp
    print('')
    print('Terjadi Swap Angka')
    print('Angka Pertama Setelah di Swap : {}'.format(x))
    print('Angka Kedua Setelah di Swap : {}'.format(y))
else :
    print('')
    print('Tidak Terjadi Swap Angka')
    print('Angka Pertama Setelah di Swap : {}'.format(x))
    print('Angka Kedua Setelah di Swap : {}'.format(y))