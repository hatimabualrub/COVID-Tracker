import pandas as pd
from tkinter import *

from Components import header, footer
from requestData import requestGlobalData, requestContryData
from figures import generateLinePlot

def countryScreen(master):
    try:
        CountryWindow = Toplevel(master)
        CountryWindow.title("Country Statistics")
        CountryWindow.configure(background='gray90')
        CountryWindow.state('zoomed')
        CountryWindow.iconbitmap('./icon.ico')

        header(CountryWindow)

        title = Label(CountryWindow, text="Country Statistics", font="Helvetica 28 bold", fg='#009933', bg='gray90')
        title.configure(anchor=NW, pady=10)
        title.pack()
        countriesData = requestGlobalData()
        countriesDF = pd.DataFrame(countriesData)
        countries = countriesDF['Country'].tolist()
        tkvar= StringVar(CountryWindow)
        tkvar.set('Select')

        noInput = Label(CountryWindow, text="Please Select A Country", width=200, font="Helvetica 40", fg='#B00000',
                        bg='gray90')
        noInput.configure(anchor="center", pady=150)
        noInput.pack()

        menuLabel = Label(CountryWindow, text="Select Country:", font="Helvetica 18", fg='gray18')
        menuLabel.place(x=1010, y=610, anchor="nw")

        menu = OptionMenu(CountryWindow, tkvar, *countries)
        menu.config( width=15, height=2)
        menu.place(x=1200, y=600, anchor="nw")

        def onClick():
            if not(tkvar.get() == 'Select'):
                noInput.destroy()
                data = requestContryData(tkvar.get())
                df = pd.DataFrame(data)
                df.Date = df.Date.str.split('T')
                df.Date = df.Date.str[0]
                countryName = df['Country'][0]


                def activeBtnHandler():
                    generateLinePlot(df, 'Active', countryName)
                def confirmedBtnHandler():
                    generateLinePlot(df, 'Confirmed', countryName)
                def recoveredBtnHandler():
                    generateLinePlot(df, 'Recovered', countryName)
                def deathsBtnHandler():
                    generateLinePlot(df, 'Deaths', countryName)
                def generalBtnHandler():
                    generateLinePlot(df, ['Confirmed','Deaths', 'Recovered', 'Active'], countryName)

                title['text'] = countryName+ ' Statistics'


                ActiveLabel = Label(CountryWindow, text='Active Cases:', font="Helvetica 14 bold", fg='#009933', bg='gray90')
                ActiveLabel.configure(anchor="center")
                ActiveLabel.place(x=100, y=150)

                ActiveValue = Label(CountryWindow, text=df.Active.iloc[-1], font="Helvetica 14", fg='gray18', bg='gray90', width=9)
                ActiveValue.configure(anchor="center")
                ActiveValue.place(x=250, y=150)

                ConfirmedLabel = Label(CountryWindow, text='Confirmed Cases:', font="Helvetica 14 bold", fg='#009933', bg='gray90')
                ConfirmedLabel.configure(anchor="center")
                ConfirmedLabel.place(x=390, y=150)

                ConfirmedValue = Label(CountryWindow, text=df.Confirmed.iloc[-1], font="Helvetica 14", fg='gray18', bg='gray90', width=9)
                ConfirmedValue.configure(anchor="center")
                ConfirmedValue.place(x=580, y=150)

                RecoveredLabel = Label(CountryWindow, text='Recovered Cases:', font="Helvetica 14 bold", fg='#009933', bg='gray90')
                RecoveredLabel.configure(anchor="center")
                RecoveredLabel.place(x=730, y=150)

                RecoveredValue = Label(CountryWindow, text=df.Recovered.iloc[-1], font="Helvetica 14", fg='gray18', bg='gray90', width=9)
                RecoveredValue.configure(anchor="center")
                RecoveredValue.place(x=920, y=150)

                DeathsLabel = Label(CountryWindow, text='Death Cases:', font="Helvetica 14 bold", fg='#009933', bg='gray90')
                DeathsLabel.configure(anchor="center")
                DeathsLabel.place(x=1060, y=150)

                DeathsValue = Label(CountryWindow, text=df.Deaths.iloc[-1], font="Helvetica 14", fg='gray18', bg='gray90', width=9)
                DeathsValue.configure(anchor="center")
                DeathsValue.place(x=1200, y=150)

                btnActive = Button(CountryWindow,
                                   text="Active Figure",
                                   command= activeBtnHandler,
                                   font="Helvetica 12 bold", bg='#D8D8D8', fg='#009933', width=18)
                btnActive.place(x=120, y=200, anchor="nw")

                btnConfirmed = Button(CountryWindow,
                                   text="Confirmed Figure",
                                   command=confirmedBtnHandler,
                                   font="Helvetica 12 bold", bg='#D8D8D8', fg='#009933', width=18)
                btnConfirmed.place(x=440, y=200, anchor="nw")

                btnRecovered= Button(CountryWindow,
                                   text="Recovered Figure",
                                   command=recoveredBtnHandler,
                                   font="Helvetica 12 bold", bg='#D8D8D8', fg='#009933', width=18)
                btnRecovered.place(x=760, y=200, anchor="nw")

                btnDeaths= Button(CountryWindow,
                                   text="Deaths Figure",
                                   command=deathsBtnHandler,
                                   font="Helvetica 12 bold",  bg='#D8D8D8', fg='#009933', width=18)
                btnDeaths.place(x=1070, y=200, anchor="nw")

                btnGeneral= Button(CountryWindow,
                                   text="General Statistics Figure",
                                   command=generalBtnHandler,
                                   font="Helvetica 16 bold", bg='#009933', fg='white', width=26, height=1)
                btnGeneral.place(x=530, y=320, anchor="nw")



        btnOK = Button(CountryWindow,
                              text="OK",
                              command=onClick,
                              font="Helvetica 9 bold", bg='#009933', fg='white', height=2)
        btnOK.place(x=1330, y=603,anchor="nw")


        footer(CountryWindow)

    except:
        CountryWindow.destroy()
