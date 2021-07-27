jml = 0
x = int(input('Masukkan Angka : '))
for a in range(1,x+1) :
    kuadrat= pow(a,2)
    print(kuadrat, end=' ')
    if a == x :
        print('=', end=' ')
    else :
        print('+', end=' ')
    jml = jml + kuadrat
print(jml)