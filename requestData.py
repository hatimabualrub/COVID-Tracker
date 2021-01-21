import requests as req


def requestGlobalData():
    data = req.get('https://api.covid19api.com/summary',verify=False).json()['Countries']
    return data

def requestContryData(country):
    conutryName = country.replace(" ", "-")
    data = req.get('https://api.covid19api.com/country/'+conutryName, verify=False).json()
    return data