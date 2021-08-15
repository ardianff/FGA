# hai = open('D:\Kuliah\FGA\ke-18\\test.txt','r')
# f = hai.read()
# print (f)
with open('D:\Kuliah\FGA\ke-18\\test.txt', 'r') as database :
    data = database.readlines()
    print (data[0])
    print (data[1])