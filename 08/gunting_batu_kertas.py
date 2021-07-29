from time import sleep
import os
from random import randint

choices =["Kertas","Gunting","Batu"]
p1win= False
p2win= False
while p1win != True and p2win != True:
    # pemain1 = input("Masukkan Nama Pemain Pertama : ")
    # pemain2 = input("Masukkan Nama Pemain Kedua : ")
    pemain1 = "ardian"
    pemain2 = "agung"
    # sleep(1)
    # os.system("cls")
    print("Giliran",pemain1," Memilih\nPilih Angka (1-3)\t\tBatu(1)\t\tGunting(2)\t\tKertas(3)")
    p1choice = int(input(": "))
    # sleep(2)
    # os.system("cls")
    print("Giliran",pemain2," Memilih\nPilih Angka (1-3)\t\tBatu(1)\t\tGunting(2)\t\tKertas(3)")
    p2choice = int(input(": "))
    p1choice_name = choices[p1choice-1]
    p2choice_name = choices[p2choice-1]
    print("\n%s Memilih %s" %(pemain1,p1choice_name))
    sleep(1)
    print("%s Memilih %s\n" %(pemain2,p2choice_name))
    sleep(1)
    if abs(p1choice - p2choice)==1: 
        if p1choice > p2choice: 
            p1win = True
        else: 
            p2win =True
    elif p1choice == p2choice : 
        print("%s Memilih %s Sedangkan %s Memilih %s. Pilihan Kalian Sama!\nAyo Mainkan Lagi!" %(pemain1,p1choice_name,pemain2,p2choice_name))
    else :
        if p1choice < p2choice : 
            p1win = True
        else : 
            p2win = True
if p1win == True : 
    print("%s Memilih %s Sedangkan %s Memilih %s, %s Menang Dan %s Kalah !" %(pemain1,p1choice_name,pemain2,p2choice_name, pemain1,pemain2))
else :
    print("%s Memilih %s Sedangkan %s Memilih %s, %s Menang Dan %s Kalah !" %(pemain2,p2choice_name,pemain1,p1choice_name, pemain2,pemain1))