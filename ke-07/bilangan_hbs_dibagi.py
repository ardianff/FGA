def hbs_dibagi (bil) :
    print('Bilangan habis pembagi dari', bil,"adalah : ")
    for i in range(1,bil+1) : 
        if bil % i == 0 : 
            print(i)
hbs_dibagi()

