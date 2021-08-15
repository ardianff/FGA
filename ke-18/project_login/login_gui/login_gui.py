from tkinter import *
import tkinter.messagebox as msg
nama = "Ardian"
user_name = 'ardian'
user_pass = '12345'
 
class LoginUser:
    def __init__(self, gui, header):
        self.gui = gui
        self.gui.geometry("300x150")
        self.gui.title(header)
        self.gui.resizable(True, True)
        self.set_gui()
         
    def set_gui(self):
        mainFrame = Frame(self.gui, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        dataFrame = Frame(mainFrame, bd=5)
        dataFrame.pack(fill=BOTH, expand=YES)
        Label(dataFrame, text='Username ').grid(row=0, column=0)
        self.entryUser = Entry(dataFrame, width=30)
        self.entryUser.grid(row=0, column=1)
        Label(dataFrame, text='Password').grid(row=1, column=0)
        self.entryPass = Entry(dataFrame, show='*',width=30)
        self.entryPass.grid(row=1, column=1)
        self.check = IntVar() 
        self.showPass = Checkbutton(dataFrame, text='Lihat Password', 
            variable=self.check, command=self.open_password)
        self.showPass.grid(row=2, column=1)
        frTombol = Frame(mainFrame, bd=5)
        frTombol.pack(fill=BOTH, expand=YES)
        self.btnLogin = Button(frTombol, text='Login', command=self.do_login)
        self.btnLogin.pack(side=LEFT, fill=BOTH, expand=YES, padx=5)
        self.btnCancel = Button(frTombol, text='Cancel', command=self.close_gui)
        self.btnCancel.pack(side=LEFT, fill=BOTH, expand=YES, padx=5)
         
    def do_login(self):
        get_username = self.entryUser.get()
        get_password = self.entryPass.get()
        if get_username==user_name and get_password==user_pass:
            msg.showinfo("Berhasil Login", "Selamat Datang %s"%(nama), parent=self.gui)
            self.close_gui()
        elif get_username=='' or get_password=='':
            msg.showwarning('Gagal', 'Username atau Password Anda Tidak Boleh Kosong', parent=self.gui)
            self.entryUser.focus_set()     
        else:
            msg.showerror('Gagal', 'Username atau Password Yang Anda Masukkan Salah Silahkan Periksa Kembali', parent=self.gui)
            self.delete_data()     
    def delete_data(self):
        self.entryUser.delete(0, END)
        self.entryPass.delete(0, END)
        self.entryUser.focus_set() 
    def open_password(self):
        Show = self.check.get()
        if Show== 1:
            self.entryPass['show'] = ''
        else:
            self.entryPass['show'] = '*'
         
    def close_gui(self):
        self.gui.destroy()              
         
if __name__ == '__main__':
    app = Tk()
    start = LoginUser(app, "** LOGIN SISTEM **")
    app.mainloop()