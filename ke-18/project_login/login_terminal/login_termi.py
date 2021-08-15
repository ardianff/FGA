import os, time, getpass

granted = False
def grant():
    global granted
    granted = True
def login(username,password):
    success = False
    file = open('D:\Kuliah\FGA\ke-18\project_login\login_terminal\db.txt',"r")
    for i in file:
         a,b = i.split(",")
         b = b.strip()
         if(a==username and b==password):
             success = True
             break
    file.close()
    if(success):
        print("Login Successful")
        grant()
    else:
        print("wrong user name or password")        
def register(username,password):
    file = open('D:\Kuliah\FGA\ke-18\project_login\login_terminal\db.txt',"a")
    file.write("\n"+username+","+password)
    grant()
def access(option):
    global username
    if(option=="login"):
        username = input("Username : ")
        password = getpass.getpass()
        login(username,password)
    else:
        print("*"*20)
        print("Form Registrasi User")
        print("*"*20)
        username = input("Masukkan Username Anda : ")
        password = getpass.getpass()
        register(username,password)

def begin():
    global option
    print("welcome to Victor's programming club")
    option = input("Login or Register (Login,Reg): ")
    if(option!="login" and option!="reg"):
        begin()
        
begin()
access(option)

if(granted):
    print("Selamat Datang Di Sistem")
    print("Halo, ",username)
