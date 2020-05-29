from tkinter import *
from GUI import *

window = Tk()

window.title("Serial Image Sender")
window.iconbitmap("asset/eth_icon.ico")

gui = GUI(window)
gui.UI_init()

window.geometry('900x670')
window.mainloop()
