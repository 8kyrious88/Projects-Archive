from tkinter import *
from Shopee import sorting_Shopee_waybills
from Lazada import sorting_Lzd_waybills
from Qoo10 import sorting_Qoo10_waybills

window = Tk()
window.title("Waybills Sorting Tool")
window.config(padx=100,pady=100,bg="grey")

image_shopee = PhotoImage(file=r"C:\Users\Ng ChunPing\.vscode\python\Workspace\Waybills_Sorting\images\Shopee.png")
button_shopee = Button(width=200,height=200,command=sorting_Shopee_waybills, image=image_shopee,highlightthickness=0, )
button_shopee.grid(row=0,column=0)

image_lzd = PhotoImage(file=r"C:\Users\Ng ChunPing\.vscode\python\Workspace\Waybills_Sorting\images\Lzd.png")
button_Lzd = Button(width=200,height=200, command=sorting_Lzd_waybills, image = image_lzd,highlightthickness=0)
button_Lzd.grid(row=0,column=1)

image_qoo10 = PhotoImage(file=r"C:\Users\Ng ChunPing\.vscode\python\Workspace\Waybills_Sorting\images\Qoo10.png")
button_Qoo10 = Button(width=200,height=200, command=sorting_Qoo10_waybills, image= image_qoo10)
button_Qoo10.grid(row=0,column=2)


window.mainloop()