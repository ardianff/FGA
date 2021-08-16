import tkinter
import random

root = tkinter.Tk()
root.geometry('600x400')
root.title('Melempar Dadu')

label = tkinter.Label(root, text='', font=('Helvetica', 150))
def roll_dice():
    # unicode dadu
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    label.configure(text=f'{random.choice(dice)} {random.choice(dice)}')
    label.pack()
button = tkinter.Button(root, text='roll dice', foreground='green', command=roll_dice)
button.pack()
root.mainloop()