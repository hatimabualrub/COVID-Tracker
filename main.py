from tkinter import *

from GlobalScreen import globalScreen
from ContryScreen import countryScreen
from Components import header, footer

master = Tk()
master.configure(background='gray90')
master.state('zoomed')
master.title('JUST Tracker')
master.iconbitmap('./icon.ico')

def GlobalWindow():
    globalScreen(master)

def countryWindow():
    countryScreen(master)


header(master)

LOGO = Label(master, text="JUST", width=200, font="Helvetica 85 bold", fg='#009933', bg='gray90')
LOGO.configure(anchor="center")
LOGO.pack(pady=30)

label = Label(master, text="COVID-19 Tracker", width=200, font="Helvetica 50 bold", fg='gray18', bg='gray90')
label.configure(anchor="center")
label.pack()

btn = Button(master,
             text="Global Statistics",
             command=GlobalWindow,
             font="Helvetica 22 bold",  bg='#D8D8D8', fg='#009933', width=18)
btn.pack(pady=20)

btn2 = Button(master,
             text="Country Statistics",
             command=countryWindow,
             font="Helvetica 22 bold",  bg='#D8D8D8', fg='gray18', width=18)
btn2.pack()

footer(master)


mainloop()