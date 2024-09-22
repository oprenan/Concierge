import pandas as pd
from datetime import date, timedelta, datetime
import os

def makeCombos(places, dates):
    columnMap = {
        'place_org':'org'
        ,'place_dest':'dest'
        #,'date':'date'
    }

    places['key'] = 0
    dates['key'] = 0

    placesCombos = places.merge(places, on='key', how = 'outer', suffixes = ('_org','_dest'))
    scenariosTemp = placesCombos.merge(dates, on='key', how = 'outer')

    scenariosTemp.rename(columns=columnMap, inplace=True)
    scenariosTemp['lan'] = 'en'
    scenariosTemp['days'] = 10
    scenario = scenariosTemp.drop(columns=['key'])

    return scenario[scenario['org'] != scenario['dest']]

def makeDateRanges(dateRange):
    daysItems = []
    for i, row in dateRange.iterrows():
        sday = datetime.strptime(row.loc['dateInit'],'%Y-%m-%d')
        eday = datetime.strptime(row.loc['dateEnd'],'%Y-%m-%d')
        daysItems.append(pd.date_range(sday,eday))

    daysS = []
    for days in daysItems:
        for day in days:
            daysS.append(day.strftime('%Y-%m-%d'))
    
    return pd.DataFrame(list(set(daysS)),columns=['date'])


places = pd.read_csv('places.csv')
dateRange = pd.read_csv('dates.csv')

dates = makeDateRanges(dateRange)
scenarios = makeCombos(places, dates)

scenarios.to_csv('Concierge/Trip/scenarios.csv', index=False)