import pandas as pd
from pandastable import Table
from tkinter import *

from Components import header
from requestData import requestGlobalData
from figures import generateBarPlot

def globalScreen(master):
    try:
        def currentBtnHandler():
            generateBarPlot(dataFrame,'CountryCode', ['TotalConfirmed','NewConfirmed'], 'Global Confirmed Cases')
        def recoveredBtnHandler():
            generateBarPlot(dataFrame,'CountryCode', ['TotalRecovered', 'NewRecovered'], 'Global Recovered Cases')
        def deathsBtnHandler():
            generateBarPlot(dataFrame,'CountryCode', ['TotalDeaths', 'NewDeaths'],'Global Death Cases')
        def totalBtnHandler():
            generateBarPlot(dataFrame,'CountryCode', ['TotalConfirmed','TotalRecovered', 'TotalDeaths'], 'Global Total Cases')
        def newBtnHandler():
            generateBarPlot(dataFrame,'CountryCode', ['NewConfirmed','NewRecovered', 'NewDeaths'], 'Global New Cases')


        GlobalWindow = Toplevel(master)
        GlobalWindow.title("Global Statestics")
        GlobalWindow.configure(background='gray90')
        GlobalWindow.state('zoomed')
        GlobalWindow.iconbitmap('./icon.ico')

        header(GlobalWindow)

        data = requestGlobalData()
        df = pd.DataFrame(data)
        dataFrame = pd.DataFrame(data)
        del df['CountryCode']
        del df['Slug']
        del df['Premium']
        del df['Date']
        f = Frame(GlobalWindow)
        f.place(x=0, y=30, width=900, height=1000)
        table = Table(f, dataframe=df, showtoolbar=False, showstatusbar=False, cellwidth=83)
        table.show()

        TitleLabel = Label(GlobalWindow, text='Global Statistics:', font="Helvetica 20 bold", fg='#009933', bg='gray90')
        TitleLabel.place(x=920, y=90, anchor="nw")


        TotalCurrentTitleLabel = Label(GlobalWindow, text='Total Confirmed:', font="Helvetica 16 bold", fg='gray25', bg='gray90')
        TotalCurrentTitleLabel.place(x=940, y=150, anchor="nw")

        TotalCurrentLabel = Label(GlobalWindow, text=str(df.TotalConfirmed.sum()), font="Helvetica 16", fg='gray25', bg='gray90')
        TotalCurrentLabel.place(x=1140, y=150, anchor="nw")

        NewCurrentTitleLabel = Label(GlobalWindow, text='New Confirmed:', font="Helvetica 16", fg='gray25', bg='gray90')
        NewCurrentTitleLabel.place(x=940, y=180, anchor="nw")

        NewCurrentLabel = Label(GlobalWindow, text=str(df.NewConfirmed.sum()), font="Helvetica 16", fg='gray25', bg='gray90')
        NewCurrentLabel.place(x=1140, y=180, anchor="nw")

        btnCurrent = Button(GlobalWindow,
                      text="Figure",
                      command= currentBtnHandler,
                      font="Helvetica 9 bold", bg='#009933', fg='white', height=2)
        btnCurrent.place(x=1280, y=160, anchor="nw")

        line = Frame(GlobalWindow,width=380,bg="#A9A9A9")
        line.place(x=940, y=230, anchor="nw")

        TotalRecoveredTitleLabel = Label(GlobalWindow, text='Total Recovered:', font="Helvetica 16 bold", fg='gray25', bg='gray90')
        TotalRecoveredTitleLabel.place(x=940, y=240, anchor="nw")

        TotalRecoveredLabel = Label(GlobalWindow, text=str(df.TotalRecovered.sum()), font="Helvetica 16", fg='#009933', bg='gray90')
        TotalRecoveredLabel.place(x=1140, y=240, anchor="nw")

        NewRecoveredTitleLabel = Label(GlobalWindow, text='New Recovered:', font="Helvetica 16", fg='gray25', bg='gray90')
        NewRecoveredTitleLabel.place(x=940, y=270, anchor="nw")

        NewRecoveredLabel = Label(GlobalWindow, text=str(df.NewRecovered.sum()), font="Helvetica 16", fg='gray25', bg='gray90')
        NewRecoveredLabel.place(x=1140, y=270, anchor="nw")

        btnRecovered = Button(GlobalWindow,
                      text="Figure",
                      command= recoveredBtnHandler,
                      font="Helvetica 9 bold", bg='#009933', fg='white', height=2)
        btnRecovered.place(x=1280, y=250, anchor="nw")

        line = Frame(GlobalWindow,width=380,bg="#A9A9A9")
        line.place(x=940, y=320, anchor="nw")

        TotalDeathsTitleLabel = Label(GlobalWindow, text='Total Deaths:', font="Helvetica 16 bold", fg='gray25', bg='gray90')
        TotalDeathsTitleLabel.place(x=940, y=340, anchor="nw")

        TotalDeathsLabel = Label(GlobalWindow, text=str(df.TotalDeaths.sum()), font="Helvetica 16", fg='#B00000', bg='gray90')
        TotalDeathsLabel.place(x=1140, y=340, anchor="nw")

        NewDeathsTitleLabel = Label(GlobalWindow, text='New Deaths:', font="Helvetica 16", fg='gray25', bg='gray90')
        NewDeathsTitleLabel.place(x=940, y=370, anchor="nw")

        NewDeathsLabel = Label(GlobalWindow, text=str(df.NewDeaths.sum()), font="Helvetica 16", fg='gray25', bg='gray90')
        NewDeathsLabel.place(x=1140, y=370, anchor="nw")

        btnDeaths = Button(GlobalWindow,
                      text="Figure",
                      command= deathsBtnHandler,
                      font="Helvetica 9 bold", bg='#009933', fg='white', height=2)
        btnDeaths.place(x=1280, y=350, anchor="nw")

        line = Frame(GlobalWindow,width=380,bg="#A9A9A9")
        line.place(x=940, y=430, anchor="nw")

        btnTotals = Button(GlobalWindow,
                      text="Total Statistics Figure",
                      command= totalBtnHandler,
                      font="Helvetica 18", bg='#009933', fg='white', width=18)
        btnTotals.place(x=1000, y=480, anchor="nw")

        btnNew = Button(GlobalWindow,
                      text="New Statistics Figure",
                      command= newBtnHandler,
                      font="Helvetica 18", bg='#D8D8D8', fg='#009933', width=18)
        btnNew.place(x=1000, y=540, anchor="nw")
    except:
        GlobalWindow.destroy()