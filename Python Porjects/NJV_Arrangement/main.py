from tkinter import *
from GJH import create_njv_delivery_GJH
from Ishop import create_njv_delivery_Ishop
from Krisshop import create_njv_delivery_KS
from DA import create_njv_delivery_DA

window = Tk()
window.title("NJV Delivery Arrangement File Generator")
window.config(padx=100,pady=100,bg="grey")

image_GJH = PhotoImage(file=r"C:\Users\Ng ChunPing\.vscode\python\Workspace\NJV_Arrangement\Images\GJH Eshop Icon.PNG")
button_GJH = Button(width=200,height=200,command=create_njv_delivery_GJH, image=image_GJH,highlightthickness=0, bg="white")
button_GJH.grid(row=0,column=0)

image_ishop = PhotoImage(file=r"C:\Users\Ng ChunPing\.vscode\python\Workspace\NJV_Arrangement\Images\Ishop Icon.PNG")
button_ishop = Button(width=200,height=200, command=create_njv_delivery_Ishop, image = image_ishop,highlightthickness=0, bg="white")
button_ishop.grid(row=0,column=1)

image_ks = PhotoImage(file=r"C:\Users\Ng ChunPing\.vscode\python\Workspace\NJV_Arrangement\Images\Krisshop icon.PNG")
button_ks = Button(width=200,height=200, command=create_njv_delivery_KS, image= image_ks,highlightthickness=0, bg="white")
button_ks.grid(row=0,column=2)

image_DA = PhotoImage(file=r"C:\Users\Ng ChunPing\.vscode\python\Workspace\NJV_Arrangement\Images\DA icon.PNG")
button_DA = Button(width=200,height=200, command=create_njv_delivery_DA, image= image_DA,highlightthickness=0, bg="white")
button_DA.grid(row=0,column=3)

window.mainloop()