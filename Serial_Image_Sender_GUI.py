from tkinter import *
from GUI import *

window = Tk()

window.title("Serial Image Sender")
window.iconbitmap("asset/Pao_cA1_icon.ico")

gui = GUI(window)
gui.UI_init()

window.geometry('720x470')
window.mainloop()
