import matplotlib.pyplot as plt


def generateBarPlot(dataf, x, y, title):
    dataf.nlargest(20, y[0])\
        .plot.bar(
        title=title,
        x=x,
        y=y,
        sharey=True, rot=0,
        figsize=(100, 32),
        logy=True,
        fontsize=10)
    plt.show()

def generateLinePlot(dataf, type, countryName):
    dataf.plot.line(
        x='Date',
        y=type,
        figsize=(16,8),
        fontsize=12,
        ylabel = 'Cases',
        title= countryName,
        linewidth=3
    )
    plt.show()
