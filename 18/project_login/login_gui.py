from tkinter import Tk, Label, Entry, messagebox, Button
name = "Ardian"
username = "ardian"
password = "12345"
def login_user() :
    get_name = input_name.get()
    get_pass = input_pass.get()
    if username == get_name and password == get_pass :
        messagebox.showinfo("Berhasil", "Selamat %s berhasil login"%(name))
    elif username == get_name and password != get_pass :
        messagebox.showerror("Gagal", "Mohon Maaf Password Yang Anda Masukkan Salah Periksa Kembali")
    elif username != get_name and password == get_pass :
        messagebox.showerror("Gagal", "Mohon Maaf Username Yang Anda Masukkan Salah Periksa Kembali")
    else :
        messagebox.showerror("Gagal", "Mohon Maaf Username dan Password Yang Anda Masukkan Salah Periksa Kembali")
gui = Tk()
gui.title("Login User")
gui.geometry("400x300")

username_label = Label(gui, text="Username").pack()
input_name = Entry(gui,width=20)
input_name.pack(padx=15,pady=5)
input_name.insert(0,"Masukkan Username...")

username_label = Label(gui, text="Password").pack()
input_pass = Entry(gui,width=20)
input_pass.pack(padx=15,pady=5)
input_pass.insert(0,"Masukkan Password...")

btn = Button(gui, text="Login", command=login_user)
btn.pack(padx=10,pady=10)

gui.mainloop()

