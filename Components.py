from tkinter import *



def header(parent):
    header1 = Label(parent, text="JUST", width=200, font="Helvetica 16 bold", fg='#009933', bg='gray18')
    header1.configure(anchor=NW)
    header1.place(x=0, y=0, anchor="nw")

    header2 = Label(parent, text="COVID-19 Tracker", font="Helvetica 16", fg='white', bg='gray18')
    header2.configure(anchor=NW)
    header2.pack(side=TOP, anchor=NE)

def footer(parent):
    footer1 = Label(parent, text="Copyright © 2020 by Hatim Abualrub. All rights reserved.", height=2, font="Helvetica 12", fg='white', bg='gray18')
    footer1.pack(side=BOTTOM, fill="x")